"""
=================================================================
 Contextual Predictive Maintenance (IoT Edge AI) — Dashboard
 Infotact Technical Internship Program 2026
 Repo: predictive-maintance-iot  (Tarun Saxena · Vaibhav Gautam)
=================================================================

This dashboard is wired directly to your real project files:

    data/ai4i2020.csv        -> raw AI4I 2020 sensor dataset
    src/retrain.py           -> the feature-engineering + SMOTE +
                                 LightGBM logic this dashboard mirrors
    models/lgbm_retrained.pkl -> the model retrain.py saves
    models/lgbm_pipeline.pkl  -> the model src/model.py saves

WHERE TO PUT THIS FILE
-----------------------
Save as `app.py` in the ROOT of the repo (same level as README.md):

    predictive-maintance-iot/
    ├── app.py              <-- HERE
    ├── data/ai4i2020.csv
    ├── models/
    ├── notebooks/
    ├── src/
    ├── README.md
    └── requirements.txt

HOW TO RUN THE FULL PROJECT
-----------------------------
1) Create/activate a virtual environment and install dependencies:

       cd predictive-maintance-iot
       python -m venv venv
       source venv/bin/activate          # Windows: venv\\Scripts\\activate
       pip install -r requirements.txt
       pip install streamlit plotly       # dashboard-only extras

   NOTE: this repo's requirements.txt was exported as UTF-16 by pip
   freeze on Windows. If `pip install -r requirements.txt` errors
   with a decode error, re-save that file as UTF-8 (open it in
   VS Code -> bottom-right encoding -> "Save with Encoding" -> UTF-8),
   or just run:
       pip install pandas numpy lightgbm imbalanced-learn shap
                   scikit-learn matplotlib seaborn joblib streamlit plotly

2) (Recommended) Train the real model once so the dashboard loads
   your actual trained pipeline instead of training on the fly:

       python src/retrain.py

   This reads data/ai4i2020.csv, engineers features, trains the
   SMOTE + LightGBM pipeline, and saves it to
   models/lgbm_retrained.pkl (models/ and data/ are gitignored,
   which is why they aren't already in the repo).

3) Launch the dashboard:

       streamlit run app.py

   Open the URL Streamlit prints (usually http://localhost:8501).

If you skip step 2, the dashboard still works — it trains an
in-memory copy of the same pipeline on first load (cached), and
shows a banner telling you it's running in that mode.
"""

import os
import re
import glob
import warnings
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix, precision_recall_curve, roc_curve, auc,
    f1_score, precision_score, recall_score,
)

warnings.filterwarnings("ignore")

try:
    import joblib
except Exception:
    joblib = None

try:
    import shap
except Exception:
    shap = None

from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE
from lightgbm import LGBMClassifier


# =================================================================
# PROJECT-SPECIFIC CONSTANTS — mirrors src/retrain.py exactly
# =================================================================
DATA_PATH = "data/ai4i2020.csv"
FALLBACK_DATA_GLOBS = ["data/ai4i2020.csv", "**/ai4i2020.csv"]

MODEL_CANDIDATES = [
    "models/lgbm_retrained.pkl",   # saved by src/retrain.py
    "models/lgbm_pipeline.pkl",    # saved by src/model.py
]

RAW_FEATURES = [
    "Air temperature [K]", "Process temperature [K]",
    "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]",
]
EXTERNAL_CONTEXT_FEATURES = ["ambient_temp_C", "factory_load_pct", "humidity_pct"]
TARGET_COL = "Machine failure"
FAILURE_SUBTYPES = ["TWF", "HDF", "PWF", "OSF", "RNF"]

NOISE_TARGET_F1 = 0.85


def clean_col(c):
    """Same regex src/retrain.py & src/evaluate.py use to clean LightGBM feature names."""
    return re.sub(r"[^A-Za-z0-9_]+", "_", c)


# =================================================================
# PAGE CONFIG + STYLE
# =================================================================
st.set_page_config(
    page_title="Predictive Maintenance IoT | Dashboard",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    .block-container {padding-top: 1.6rem; padding-bottom: 2rem;}
    .kpi-card {background: linear-gradient(135deg, #101826 0%, #1b2536 100%);
        border: 1px solid #26324a; border-radius: 14px; padding: 18px 20px;}
    .kpi-label {font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em;
        color: #8fa2c7; margin-bottom: 6px;}
    .kpi-value {font-size: 1.9rem; font-weight: 700; color: #f2f5fb;}
    .kpi-sub {font-size: 0.78rem; color: #6fdc9a; margin-top: 4px;}
    .section-title {font-size: 1.25rem; font-weight: 700; margin-top: 0.4rem;
        margin-bottom: 0.6rem; color: #f2f5fb;}
    .badge {display: inline-block; padding: 3px 10px; border-radius: 999px;
        font-size: 0.72rem; font-weight: 600; letter-spacing: 0.03em;}
    .badge-live {background: #123d2a; color: #6fdc9a; border: 1px solid #1f6b46;}
    .badge-demo {background: #3d2e12; color: #f0c674; border: 1px solid #6b511f;}
</style>
""", unsafe_allow_html=True)


# =================================================================
# DATA LOADING + FEATURE ENGINEERING (mirrors src/retrain.py)
# =================================================================
def find_data_path():
    for p in FALLBACK_DATA_GLOBS:
        matches = glob.glob(p, recursive=True)
        if matches:
            return matches[0]
    return None


@st.cache_data(show_spinner=False)
def load_raw_data():
    path = find_data_path()
    if path is None:
        raise FileNotFoundError(
            "Couldn't find data/ai4i2020.csv. Place app.py in the repo root, "
            "next to the data/ folder."
        )
    df = pd.read_csv(path)
    return df, path


@st.cache_data(show_spinner=False)
def engineer_features(df):
    """Exact logic from src/retrain.py::apply_feature_engineering()."""
    df = df.copy()
    le = LabelEncoder()
    df["Type_enc"] = le.fit_transform(df["Type"])

    np.random.seed(42)
    df["ambient_temp_C"] = np.random.normal(loc=28, scale=5, size=len(df))
    df["factory_load_pct"] = np.random.uniform(50, 100, size=len(df))
    df["humidity_pct"] = np.random.normal(loc=60, scale=10, size=len(df))

    ext_features = RAW_FEATURES + ["Type_enc"] + EXTERNAL_CONTEXT_FEATURES
    X = df[ext_features].copy()
    y = df[TARGET_COL]
    X.columns = [clean_col(c) for c in X.columns]
    return df, X, y, le


@st.cache_resource(show_spinner=False)
def load_or_train_pipeline(_X, _y):
    """Try the real saved model first; otherwise train one live (same recipe as retrain.py)."""
    if joblib is not None:
        for path in MODEL_CANDIDATES:
            if os.path.exists(path):
                try:
                    pipeline = joblib.load(path)
                    return pipeline, path, True
                except Exception:
                    continue

    X_train, X_test, y_train, y_test = train_test_split(
        _X, _y, test_size=0.2, random_state=42, stratify=_y
    )
    pipeline = ImbPipeline([
        ("smote", SMOTE(random_state=42)),
        ("lgbm", LGBMClassifier(
            random_state=42, n_jobs=-1, verbose=-1,
            n_estimators=500, learning_rate=0.05,
            num_leaves=31, scale_pos_weight=20,
        )),
    ])
    pipeline.fit(X_train, y_train)
    return pipeline, None, False


# =================================================================
# LOAD EVERYTHING
# =================================================================
load_error = None
try:
    raw_df, data_path = load_raw_data()
    full_df, X, y, type_encoder = engineer_features(raw_df)
    pipeline, model_path, model_is_real = load_or_train_pipeline(X, y)
    y_proba = pipeline.predict_proba(X)[:, 1]
except Exception as e:
    load_error = str(e)

if load_error:
    st.error(
        f"**Couldn't load the project data/model.**\n\n{load_error}\n\n"
        "Make sure `app.py` sits in the repo root, next to the `data/` folder, "
        "and that `data/ai4i2020.csv` exists."
    )
    st.stop()


# =================================================================
# SIDEBAR
# =================================================================
st.sidebar.markdown("## 🛠️ Predictive Maintenance")
st.sidebar.caption("Contextual IoT Edge AI · Infotact Internship 2026")

page = st.sidebar.radio(
    "Navigate",
    [
        "📊 Overview", "🔍 Dataset Explorer", "🎯 Model Performance",
        "🧠 Explainability (SHAP)", "🌊 Noise Robustness",
        "⚡ Live Prediction", "ℹ️ About the Project",
    ],
)

st.sidebar.markdown("---")
badge_cls = "badge-live" if model_is_real else "badge-demo"
badge_txt = "TRAINED MODEL LOADED" if model_is_real else "TRAINED LIVE THIS SESSION"
st.sidebar.markdown(f'<span class="badge {badge_cls}">{badge_txt}</span>', unsafe_allow_html=True)
st.sidebar.caption(f"Data: `{data_path}`\n\nModel: `{model_path or 'in-memory (run src/retrain.py to persist)'}`")
if not model_is_real:
    st.sidebar.info("Run `python src/retrain.py` once to save a real model to `models/` "
                     "so the dashboard loads instantly next time.", icon="💡")


# =================================================================
# PAGE: OVERVIEW
# =================================================================
if page == "📊 Overview":
    st.title("Contextual Predictive Maintenance — Dashboard")
    st.caption("AI-Powered Predictive Maintenance using Contextual Data Fusion & Explainable Machine Learning")

    y_pred_default = (y_proba >= 0.5).astype(int)
    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        (c1, "Macro F1 Score", f"{f1_score(y, y_pred_default, average='macro'):.4f}", "Target ≥ 0.85"),
        (c2, "Precision", f"{precision_score(y, y_pred_default, zero_division=0):.4f}", "Positive-class"),
        (c3, "Recall", f"{recall_score(y, y_pred_default, zero_division=0):.4f}", "Positive-class"),
        (c4, "Records", f"{len(full_df):,}", f"Failure rate {y.mean()*100:.2f}%"),
    ]
    for col, label, value, sub in kpis:
        with col:
            st.markdown(f"""<div class="kpi-card"><div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div><div class="kpi-sub">{sub}</div></div>""",
                unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    left, right = st.columns([1.3, 1])
    with left:
        st.markdown('<div class="section-title">Pipeline</div>', unsafe_allow_html=True)
        stages = ["Raw IoT Data", "Type Encoding", "External Context Fusion",
                   "SMOTE", "LightGBM", "SHAP", "Threshold Tuning", "Prediction"]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=list(range(len(stages))), y=[0]*len(stages), mode="lines",
                                  line=dict(color="#2c3a55", width=3), showlegend=False))
        fig.add_trace(go.Scatter(x=list(range(len(stages))), y=[0]*len(stages), mode="markers+text",
                                  text=stages, textposition="top center",
                                  marker=dict(size=20, color="#4c8bf5"), showlegend=False))
        fig.update_layout(height=220, margin=dict(l=10, r=10, t=40, b=10),
                           xaxis=dict(visible=False), yaxis=dict(visible=False, range=[-1, 1]),
                           plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
    with right:
        st.markdown('<div class="section-title">Class Balance</div>', unsafe_allow_html=True)
        counts = y.value_counts().rename({0: "Healthy", 1: "Failure"})
        fig = px.pie(values=counts.values, names=counts.index, hole=0.55,
                     color=counts.index, color_discrete_map={"Healthy": "#2ecc71", "Failure": "#e74c3c"})
        fig.update_layout(height=220, margin=dict(l=10, r=10, t=10, b=10), paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Failure Subtypes (raw dataset flags)</div>', unsafe_allow_html=True)
    present_subtypes = [c for c in FAILURE_SUBTYPES if c in full_df.columns]
    if present_subtypes:
        sub_counts = full_df[present_subtypes].sum().sort_values(ascending=True)
        fig = px.bar(sub_counts, orientation="h", labels={"value": "Count", "index": "Failure type"})
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=280, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)
    st.write("`Python` · `Pandas`/`NumPy` · `LightGBM` · `Scikit-Learn` · "
             "`Imbalanced-Learn (SMOTE)` · `SHAP` · `Streamlit` · `Plotly`")


# =================================================================
# PAGE: DATASET EXPLORER
# =================================================================
elif page == "🔍 Dataset Explorer":
    st.title("Dataset Explorer")
    st.caption(f"Source: `{data_path}` · Raw shape: {raw_df.shape[0]:,} rows × {raw_df.shape[1]} cols "
               f"· Engineered features: {X.shape[1]}")

    tab1, tab2, tab3, tab4 = st.tabs(["Raw Data", "Engineered Features", "Sensor Distributions", "Correlation"])

    with tab1:
        st.dataframe(raw_df.head(200), use_container_width=True)
        st.download_button("Download raw CSV", raw_df.to_csv(index=False).encode(), "ai4i2020_preview.csv")

    with tab2:
        st.dataframe(pd.concat([X, y], axis=1).head(200), use_container_width=True)
        st.caption("Type_enc + external context columns simulated with `np.random.seed(42)`, "
                   "exactly as in `src/retrain.py`.")

    with tab3:
        chosen = st.selectbox("Feature", RAW_FEATURES + EXTERNAL_CONTEXT_FEATURES, index=0)
        fig = px.histogram(full_df, x=chosen, color=full_df[TARGET_COL].map({0: "Healthy", 1: "Failure"}),
                            barmode="overlay", opacity=0.7, nbins=40,
                            color_discrete_map={"Healthy": "#2ecc71", "Failure": "#e74c3c"})
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", legend_title="Status")
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        corr_df = pd.concat([X, y.rename(TARGET_COL)], axis=1)
        corr = corr_df.corr()
        fig = px.imshow(corr, color_continuous_scale="RdBu_r", zmin=-1, zmax=1, aspect="auto")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=550)
        st.plotly_chart(fig, use_container_width=True)


# =================================================================
# PAGE: MODEL PERFORMANCE
# =================================================================
elif page == "🎯 Model Performance":
    st.title("Model Performance")
    st.caption("SMOTE + LightGBM pipeline, evaluated on the full engineered dataset.")

    threshold = st.slider("Decision threshold", 0.05, 0.95, 0.50, 0.01)
    y_pred = (y_proba >= threshold).astype(int)

    c1, c2, c3 = st.columns(3)
    c1.metric("Macro F1", f"{f1_score(y, y_pred, average='macro'):.4f}")
    c2.metric("Precision", f"{precision_score(y, y_pred, zero_division=0):.4f}")
    c3.metric("Recall", f"{recall_score(y, y_pred, zero_division=0):.4f}")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown('<div class="section-title">Confusion Matrix</div>', unsafe_allow_html=True)
        cm = confusion_matrix(y, y_pred)
        fig = px.imshow(cm, text_auto=True, color_continuous_scale="Blues",
                         labels=dict(x="Predicted", y="Actual"),
                         x=["Healthy", "Failure"], y=["Healthy", "Failure"])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380)
        st.plotly_chart(fig, use_container_width=True)
    with col_b:
        st.markdown('<div class="section-title">Precision–Recall Curve</div>', unsafe_allow_html=True)
        prec, rec, _ = precision_recall_curve(y, y_proba)
        fig = px.area(x=rec, y=prec, labels={"x": "Recall", "y": "Precision"})
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">ROC Curve</div>', unsafe_allow_html=True)
    fpr, tpr, _ = roc_curve(y, y_proba)
    fig = px.area(x=fpr, y=tpr, labels={"x": "False Positive Rate", "y": "True Positive Rate"},
                  title=f"AUC = {auc(fpr, tpr):.4f}")
    fig.add_shape(type="line", x0=0, y0=0, x1=1, y1=1, line=dict(dash="dash", color="gray"))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=400)
    st.plotly_chart(fig, use_container_width=True)

    lgbm_model = pipeline.named_steps.get("lgbm", None)
    if lgbm_model is not None and hasattr(lgbm_model, "feature_importances_"):
        st.markdown('<div class="section-title">Feature Importance</div>', unsafe_allow_html=True)
        imp = pd.Series(lgbm_model.feature_importances_, index=X.columns).sort_values(ascending=True)
        fig = px.bar(imp, orientation="h")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=420, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)


# =================================================================
# PAGE: SHAP EXPLAINABILITY
# =================================================================
elif page == "🧠 Explainability (SHAP)":
    st.title("Explainability — SHAP")
    st.caption("Which sensors and contextual features drive the model's failure predictions.")

    lgbm_model = pipeline.named_steps.get("lgbm", pipeline)
    if shap is None:
        st.warning("Install `shap` (`pip install shap`) to see live SHAP plots here.")
    else:
        with st.spinner("Computing SHAP values (sampled for speed)..."):
            sample = X.sample(min(800, len(X)), random_state=42)
            try:
                explainer = shap.TreeExplainer(lgbm_model)
                sv = explainer.shap_values(sample)
                sv = sv[1] if isinstance(sv, list) else sv
                imp = pd.Series(np.abs(sv).mean(axis=0), index=X.columns).sort_values(ascending=True)

                st.markdown('<div class="section-title">Global Feature Importance (mean |SHAP|)</div>', unsafe_allow_html=True)
                fig = px.bar(imp, orientation="h")
                fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=450, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)

                st.markdown('<div class="section-title">Dependence Plot</div>', unsafe_allow_html=True)
                feat = st.selectbox("Feature", list(X.columns), index=list(X.columns).index(imp.index[-1]))
                fidx = list(X.columns).index(feat)
                fig2 = px.scatter(x=sample[feat], y=sv[:, fidx], labels={"x": feat, "y": "SHAP value"},
                                   color=sample[feat], color_continuous_scale="RdBu_r")
                fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380)
                st.plotly_chart(fig2, use_container_width=True)
            except Exception as e:
                st.error(f"Couldn't compute SHAP values: {e}")


# =================================================================
# PAGE: NOISE ROBUSTNESS
# =================================================================
elif page == "🌊 Noise Robustness":
    st.title("Noise Sensitivity Analysis")
    st.caption("Gaussian noise (mean 0, std = noise level × feature std) injected into sensor "
               "readings to simulate real-world signal drift — same idea as the Week 4 robustness study.")

    noise_levels = [0.0, 0.05, 0.15, 0.30]
    rows = []
    rng = np.random.default_rng(0)
    stds = X.std()
    for nl in noise_levels:
        Xn = X.copy()
        if nl > 0:
            Xn = Xn + rng.normal(0, nl, Xn.shape) * stds.values
        proba_n = pipeline.predict_proba(Xn)[:, 1]
        f1_n = f1_score(y, (proba_n >= 0.5).astype(int), average="macro")
        rows.append({"Noise Level (σ)": nl, "Macro F1": f1_n})
    noise_df = pd.DataFrame(rows)
    noise_df["% Drop vs Clean"] = (noise_df["Macro F1"].iloc[0] - noise_df["Macro F1"]) / noise_df["Macro F1"].iloc[0] * 100

    fig = go.Figure()
    fig.add_trace(go.Bar(x=noise_df["Noise Level (σ)"].astype(str), y=noise_df["Macro F1"], marker_color="#4c8bf5"))
    fig.add_hline(y=NOISE_TARGET_F1, line_dash="dash", line_color="#e74c3c", annotation_text="Target F1 = 0.85")
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=420,
                       xaxis_title="Noise Level (σ)", yaxis_title="Macro F1 Score")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(noise_df.style.format({"Macro F1": "{:.4f}", "% Drop vs Clean": "{:.2f}%"}), use_container_width=True)

    st.markdown('<div class="section-title">Threshold Sweep (0.10 – 0.90)</div>', unsafe_allow_html=True)
    thresholds = np.arange(0.10, 0.95, 0.05)
    sweep = [{
        "Threshold": t,
        "Precision": precision_score(y, (y_proba >= t).astype(int), zero_division=0),
        "Recall": recall_score(y, (y_proba >= t).astype(int), zero_division=0),
        "F1": f1_score(y, (y_proba >= t).astype(int), average="macro"),
    } for t in thresholds]
    sweep_df = pd.DataFrame(sweep)
    fig2 = px.line(sweep_df, x="Threshold", y=["Precision", "Recall", "F1"])
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=380)
    st.plotly_chart(fig2, use_container_width=True)
    best_row = sweep_df.loc[sweep_df["F1"].idxmax()]
    st.success(f"Best F1 at threshold ≈ **{best_row['Threshold']:.2f}** (F1 = {best_row['F1']:.4f})")


# =================================================================
# PAGE: LIVE PREDICTION
# =================================================================
elif page == "⚡ Live Prediction":
    st.title("Live Failure Prediction")
    st.caption("Enter current sensor + contextual readings to get a failure-risk estimate from the real pipeline.")

    with st.form("predict_form"):
        c1, c2, c3 = st.columns(3)
        with c1:
            machine_type = st.selectbox("Machine Type", sorted(raw_df["Type"].unique().tolist()))
            air_temp = st.slider("Air temperature [K]", float(raw_df["Air temperature [K]"].min()),
                                  float(raw_df["Air temperature [K]"].max()), float(raw_df["Air temperature [K]"].median()))
            process_temp = st.slider("Process temperature [K]", float(raw_df["Process temperature [K]"].min()),
                                      float(raw_df["Process temperature [K]"].max()), float(raw_df["Process temperature [K]"].median()))
        with c2:
            rot_speed = st.slider("Rotational speed [rpm]", float(raw_df["Rotational speed [rpm]"].min()),
                                   float(raw_df["Rotational speed [rpm]"].max()), float(raw_df["Rotational speed [rpm]"].median()))
            torque = st.slider("Torque [Nm]", float(raw_df["Torque [Nm]"].min()),
                                float(raw_df["Torque [Nm]"].max()), float(raw_df["Torque [Nm]"].median()))
            tool_wear = st.slider("Tool wear [min]", float(raw_df["Tool wear [min]"].min()),
                                   float(raw_df["Tool wear [min]"].max()), float(raw_df["Tool wear [min]"].median()))
        with c3:
            ambient_temp = st.slider("Ambient temperature [°C]", 10.0, 45.0, 28.0)
            factory_load = st.slider("Factory load [%]", 50.0, 100.0, 75.0)
            humidity = st.slider("Humidity [%]", 20.0, 90.0, 60.0)

        submitted = st.form_submit_button("Predict Failure Risk", use_container_width=True)

    if submitted:
        type_enc_val = int(type_encoder.transform([machine_type])[0])
        row = {
            "Air temperature [K]": air_temp, "Process temperature [K]": process_temp,
            "Rotational speed [rpm]": rot_speed, "Torque [Nm]": torque,
            "Tool wear [min]": tool_wear, "Type_enc": type_enc_val,
            "ambient_temp_C": ambient_temp, "factory_load_pct": factory_load,
            "humidity_pct": humidity,
        }
        x_new = pd.DataFrame([row])
        x_new.columns = [clean_col(c) for c in x_new.columns]
        x_new = x_new[X.columns]  # enforce training column order

        proba = float(pipeline.predict_proba(x_new)[0, 1])

        c1, c2 = st.columns([1, 1.4])
        with c1:
            fig = go.Figure(go.Indicator(
                mode="gauge+number", value=proba * 100, number={"suffix": "%"},
                title={"text": "Failure Probability"},
                gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#e74c3c" if proba > 0.5 else "#2ecc71"},
                       "steps": [{"range": [0, 50], "color": "#123d2a"}, {"range": [50, 100], "color": "#3d1212"}]},
            ))
            fig.update_layout(height=320, paper_bgcolor="rgba(0,0,0,0)", font_color="#f2f5fb")
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            verdict = "⚠️ High Risk — schedule maintenance" if proba > 0.5 else "✅ Healthy — no action needed"
            st.subheader(verdict)
            if shap is not None:
                try:
                    lgbm_model = pipeline.named_steps.get("lgbm", pipeline)
                    explainer = shap.TreeExplainer(lgbm_model)
                    sv = explainer.shap_values(x_new)
                    sv = sv[1] if isinstance(sv, list) else sv
                    contrib = pd.Series(sv[0], index=X.columns).sort_values()
                    fig2 = px.bar(contrib, orientation="h", title="Feature contribution to this prediction")
                    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", height=350, showlegend=False)
                    st.plotly_chart(fig2, use_container_width=True)
                except Exception:
                    st.caption("SHAP explanation unavailable for this input.")


# =================================================================
# PAGE: ABOUT
# =================================================================
else:
    st.title("About This Project")
    st.markdown(f"""
**Contextual Predictive Maintenance (IoT Edge AI)**
*Infotact Technical Internship Program — Advanced Data Science & Machine Learning (2026)*

This system predicts industrial equipment failures before they occur by fusing
internal IoT sensor telemetry (air/process temperature, rotational speed, torque,
tool wear) with simulated external contextual signals (ambient temperature,
factory load, humidity).

**Pipeline (`src/retrain.py`):** Load `data/ai4i2020.csv` → encode `Type` →
simulate external context → SMOTE (train fold only) → LightGBM classifier →
evaluate on a held-out test split → save to `models/`.

**This session**
| | |
|---|---|
| Dataset | `{data_path}` ({len(full_df):,} rows) |
| Model source | {"Loaded from `" + model_path + "`" if model_is_real else "Trained live this session"} |
| Failure rate | {y.mean()*100:.2f}% |

**Team**
- **Tarun Saxena** — Data Engineer & Evaluation/Deployment Lead
- **Vaibhav Gautam** — ML Engineer & Context Integration Lead

**Tech Stack:** Python · Pandas · NumPy · LightGBM · Scikit-Learn ·
Imbalanced-Learn (SMOTE) · SHAP · Streamlit · Plotly

**Repository:** github.com/tarunsaxena2/predictive-maintance-iot
""")
    st.caption(f"Dashboard rendered {datetime.now().strftime('%Y-%m-%d %H:%M')}")
