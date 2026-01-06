# =========================================================
# StudyTrack – AI Study Habit Recommender
# Clean & Refactored app.py
# =========================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

from homepage import show_homepage
from styles import load_css
from auth_page import auth_page
from recommendation import generate_recommendation
from excel_utils import normalize_columns, COLUMN_ALIASES
from analysis_charts import (
    plot_actual_vs_predicted,
    plot_clusters,
    cluster_summary
)
from pdf_utils import export_analytics_pdf
ADMIN_EMAILS = ["premkalse108@gmail.com"]
    
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

if "model_trained" not in st.session_state:
    st.session_state.model_trained = False

# =========================================================
# Session State Initialization (REQUIRED)
# =========================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = None

if "_open_admin" not in st.session_state:
    st.session_state._open_admin = False

if not st.session_state.logged_in:
    auth_page()
    st.stop()

# =========================================================
# Page Config (ONCE)
# =========================================================
st.set_page_config(
    page_title="StudyTrack – AI Study Habit Recommender",
    page_icon="🎓",
    layout="wide"
)

load_css()

# =========================================================
# Session State Defaults
# =========================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================================
# Authentication Guard
# =========================================================
if not st.session_state.logged_in:
    auth_page()
    st.stop()

# =========================================================
# Sidebar Navigation
# =========================================================
with st.sidebar:
    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:20px;">
            <div style="font-size:28px;">🎓</div>
            <div>
                <div style="font-size:18px; font-weight:600;">StudyTrack</div>
                <div style="font-size:12px; color:#9ca3af;">
                    AI Study Habit Recommender
                </div>
            </div>
        </div>
        <hr>
        """,
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        ["🏠 Home", "👤 Individual Prediction", "📁 Train Model",
         "📦 Predict & Recommendation", "📊 Analytics"],
        label_visibility="collapsed"
    )

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# =========================================================
# Helpers
# =========================================================
def read_file(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    return pd.read_excel(file)

# =========================================================
# Pages
# =========================================================

# -------------------- HOME --------------------
if page == "🏠 Home":
    show_homepage()

# -------------------- INDIVIDUAL --------------------
elif page == "👤 Individual Prediction":
    st.header("👤 Individual Prediction")

    mode = st.radio(
        "Prediction mode",
        ["Single Student", "Bulk Dataset"],
        horizontal=True
    )

    # =========================================================
    # 🔹 SINGLE STUDENT (EXISTING)
    # =========================================================
    if mode == "Single Student":
        with st.form("manual_form"):
            c1, c2 = st.columns(2)

            with c1:
                study = st.number_input("Study Hours / Day", 0.0, 16.0, 3.0)
                sleep = st.number_input("Sleep Hours", 0.0, 16.0, 7.0)
                attendance = st.slider("Attendance (%)", 0, 100, 80)

            with c2:
                assignment = st.slider("Assignment Completion (%)", 0, 100, 75)
                score = st.slider("Test Score", 0, 100, 65)

            submit = st.form_submit_button("💡 Get Recommendation")

        if submit:
            rec = generate_recommendation(
                study, sleep, attendance, assignment, score
            )

            st.subheader("📌 Recommendation")
            for k, v in rec.items():
                st.markdown(f"**{k}:** {v}")

    # =========================================================
    # 🔹 BULK DATASET (NEW)
    # =========================================================
    else:
        st.subheader("📦 Bulk Dataset Prediction")

        if "trained_model" not in st.session_state:
            st.error("❌ Train the model first.")
            st.stop()

        file = st.file_uploader(
            "Upload dataset (NO Test_Score)",
            type=["xlsx", "csv"]
        )

        if file is None:
            st.info("Upload a dataset to continue.")
            st.stop()

        df = normalize_columns(
            pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
        )

        required = st.session_state["trained_features"]
        missing = [c for c in required if c not in df.columns]

        if missing:
            st.error(f"Missing columns: {', '.join(missing)}")
            st.stop()

        # =========================================================
        # Prediction
        # =========================================================
        X = df[required]
        preds = st.session_state["trained_model"].predict(X)
        df["Predicted_Test_Score"] = preds.round(2)

        # =========================================================
        # Performance Category
        # =========================================================
        def perf_bucket(score):
            if score < 60:
                return "At Risk"
            elif score < 80:
                return "Average"
            return "Excellent"

        df["Performance_Category"] = df["Predicted_Test_Score"].apply(perf_bucket)

        # =========================================================
        # Recommendations
        # =========================================================
        recs = []
        for _, r in df.iterrows():
            recs.append(generate_recommendation(
                r["study_hours_per_day"],
                r["sleep_hours"],
                r["attendance_percentage"],
                r.get("assignment_completion", 75),
                r["Predicted_Test_Score"]
            ))

        rec_df = pd.DataFrame(recs)
        final_df = pd.concat([df, rec_df], axis=1)

        # =========================================================
        # Visual Insights
        # =========================================================
        st.markdown("### 📊 Performance distribution")

        dist = final_df["Performance_Category"].value_counts()
        labels = ["At Risk", "Average", "Excellent"]
        values = [dist.get(l, 0) for l in labels]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(labels, values, color=["#ef4444", "#facc15", "#22c55e"])
        ax.set_ylabel("Number of Students")
        ax.set_title("Prediction Performance Distribution")
        ax.grid(axis="y", linestyle="--", alpha=0.6)

        st.pyplot(fig)

        # =========================================================
        # Output
        # =========================================================
        st.subheader("📄 Prediction Results")
        st.dataframe(final_df.head(), use_container_width=True)

        buf = BytesIO()
        final_df.to_excel(buf, index=False)
        buf.seek(0)

        st.download_button(
            "⬇️ Download Bulk Predictions",
            buf,
            "bulk_individual_predictions.xlsx",
            use_container_width=True
        )


# -------------------- TRAIN MODEL --------------------
elif page == "📁 Train Model":
    st.header("📁 Train Model")

    file = st.file_uploader(
        "Upload training dataset (XLSX / CSV)",
        type=["xlsx", "csv"]
    )

    if file is None:
        st.info("Please upload a dataset to train the model.")
        st.session_state.model_trained = False

    else:
        # ===============================
        # Read file SAFELY
        # ===============================
        raw_df = read_file(file)

        required_cols = [
            "Student_ID", "Student_Name",
            "Study_Hours_Per_Day", "Sleep_Hours",
            "Attendance_Percentage", "Assignment_Completion",
            "Social_Media_Hours", "Exercise_Hours",
            "Test_Score"
        ]

        # Validate columns
        missing_cols = [c for c in required_cols if c not in raw_df.columns]
        if missing_cols:
            st.error(f"Missing required columns: {', '.join(missing_cols)}")
            st.session_state.model_trained = False
            st.stop()

        df = raw_df[required_cols].copy()

        # Convert numeric columns
        for col in required_cols[2:]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # Clean data
        cleaned_df = df.dropna().reset_index(drop=True)

        # ===============================
        # Store cleaned data for Analytics
        # ===============================
        st.session_state.uploaded_df = cleaned_df

        st.success("✅ Data cleaned successfully")
        st.dataframe(cleaned_df.head(), use_container_width=True)

        # ===============================
        # Normalize for ML
        # ===============================
        df_norm = normalize_columns(cleaned_df)

        feature_cols = [
            "study_hours_per_day",
            "sleep_hours",
            "attendance_percentage",
            "assignment_completion",
            "social_media_hours",
            "exercise_hours"
        ]

        X = df_norm[feature_cols]
        y = cleaned_df["Test_Score"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        r2 = r2_score(y_test, model.predict(X_test))
        
        # =========================================================
# 📊 Visual Insights – Training Data
# =========================================================
        st.markdown("## 📊 Visual insights")
        st.markdown("Performance distribution derived from training dataset")

        def performance_bucket(score):
            
            if score < 60:
                 return "At Risk"
            elif score < 80:
                return "Average"
            else:
                return "Excellent"

        cleaned_df["Performance_Category"] = cleaned_df["Test_Score"].apply(performance_bucket)

        dist = cleaned_df["Performance_Category"].value_counts()
        labels = ["At Risk", "Average", "Excellent"]
        values = [dist.get(l, 0) for l in labels]

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.bar(labels, values, color=["#ef4444", "#facc15", "#22c55e"])
        ax.set_title("Performance Distribution")
        ax.set_xlabel("Performance Category")
        ax.set_ylabel("Number of Students")
        ax.grid(axis="y", linestyle="--", alpha=0.6)
        st.pyplot(fig)


        # ===============================
        # Store trained model & STATE
        # ===============================
        st.session_state.trained_model = model
        st.session_state.trained_features = feature_cols
        st.session_state.model_r2 = r2
        st.session_state.model_trained = True   # ✅ SET ONLY HERE

        st.markdown("### 📊 Model Performance")
        st.markdown(f"**R² Score:** {r2 * 100:.2f}%")

        # ===============================
        # Download prediction-ready file
        # ===============================
        pred_file = cleaned_df.drop(columns=["Test_Score"])
        buf = BytesIO()
        pred_file.to_excel(buf, index=False)
        buf.seek(0)

        st.download_button(
            "⬇️ Download Cleaned Dataset (For Prediction)",
            buf,
            "prediction_input.xlsx",
            use_container_width=True
        )


# -------------------- PREDICT --------------------
elif page == "📦 Predict & Recommendation":
    st.header("📦 Predict & Recommendation")

    if "trained_model" not in st.session_state:
        st.error("Train the model first.")
        st.stop()

    file = st.file_uploader("Upload prediction dataset (NO Test_Score)", type=["xlsx", "csv"])
    if file is None:
        st.warning("⚠️ Please upload a dataset to predict scores.")
        st.stop()

    df = normalize_columns(read_file(file))

    missing = [
        col for col in st.session_state["trained_features"]
        if col not in df.columns
    ]
    if missing:
        st.error(f"Missing columns: {', '.join(missing)}")
        st.stop()

    X_pred = df[st.session_state["trained_features"]]
    preds = st.session_state["trained_model"].predict(X_pred)
    df["Predicted_Test_Score"] = preds.round(2)

    st.subheader("📊 Predicted Scores")
    fig, ax = plt.subplots()
    ax.bar(range(len(df)), df["Predicted_Test_Score"])
    st.pyplot(fig)

    # Recommendations
    recs = []
    for _, r in df.iterrows():
        recs.append(generate_recommendation(
            r["study_hours_per_day"],
            r["sleep_hours"],
            r["attendance_percentage"],
            r["assignment_completion"],
            r["Predicted_Test_Score"]
        ))

    rec_df = pd.DataFrame(recs)
    out = pd.concat([df, rec_df], axis=1)

    st.dataframe(out.head(), use_container_width=True)

    buf = BytesIO()
    out.to_excel(buf, index=False)
    buf.seek(0)

    st.download_button(
        "⬇️ Download Predictions",
        buf,
        "predictions.xlsx",
        use_container_width=True
    )

# -------------------- ANALYTICS --------------------
elif page == "📊 Analytics":
    # =========================================================
    # Professional Header (Option 1)
    # =========================================================
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #0f172a, #020617);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 25px;
    ">
        <div style="color:#38bdf8; font-size:13px; margin-bottom:6px;">
            📊 Analytics Dashboard
        </div>
        <h1 style="margin:0; font-size:30px;">Analytics & Insights</h1>
        <p style="margin-top:12px; color:#cbd5f5; line-height:1.6; max-width:900px;">
            This dashboard provides a data-driven understanding of how student study habits
            influence academic performance using statistical analysis, machine learning,
            and clustering techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # State Validation
    # =========================================================
    if not st.session_state.get("model_trained", False):
        st.warning("⚠️ Please train the model to view analytics.")
        st.stop()

    df = st.session_state.get("uploaded_df")
    if df is None or df.empty:
        st.error("❌ Training data not available.")
        st.stop()

    # =========================================================
    # Dataset Statistics
    # =========================================================
    with st.expander("📄 View dataset statistics"):
        st.dataframe(df.describe(), use_container_width=True)

    # =========================================================
    # Key Performance Snapshot
    # =========================================================
    st.markdown("## Key performance snapshot")

    avg_score = round(df["Test_Score"].mean(), 2)
    max_score = df["Test_Score"].max()
    min_score = df["Test_Score"].min()

    c1, c2, c3 = st.columns(3)
    c1.metric("Average score", avg_score)
    c2.metric("Highest score", max_score)
    c3.metric("Lowest score", min_score)

    # =========================================================
    # Regression Analysis
    # =========================================================
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score

    features = [
        "Study_Hours_Per_Day",
        "Sleep_Hours",
        "Attendance_Percentage"
    ]

    X = df[features]
    y = df["Test_Score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # =========================================================
    # Visual Analytics
    # =========================================================
    st.markdown("## Visual analytics")

    left, right = st.columns(2)

    with left:
        st.markdown("### 📉 Actual vs Predicted Scores")
        st.pyplot(plot_actual_vs_predicted(y_test, y_pred))

    with right:
        st.markdown("### 🧩 Habit-Based Student Clusters")

        from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(df[features])

        df["Cluster_Number"] = KMeans(
            n_clusters=3,
            random_state=42
        ).fit_predict(X_scaled)

        st.pyplot(plot_clusters(df))

    # =========================================================
    # 📊 Study Hours vs Marks (NEW – BEFORE CLUSTER SUMMARY)
    # =========================================================
    st.markdown("## 📊 Study Hours vs Test Score")

    fig_sh, ax_sh = plt.subplots(figsize=(8, 4))
    ax_sh.scatter(
        df["Study_Hours_Per_Day"],
        df["Test_Score"],
        alpha=0.7
    )
    ax_sh.set_xlabel("Study Hours / Day")
    ax_sh.set_ylabel("Test Score")
    ax_sh.set_title("Relationship between Study Hours and Academic Performance")
    ax_sh.grid(True)
    st.pyplot(fig_sh)

    # =========================================================
    # Cluster Summary
    # =========================================================
    st.markdown("## Cluster summary")
    summary = cluster_summary(df)
    st.dataframe(summary, use_container_width=True)

    # Cluster sizes
    cluster_counts = df["Cluster_Number"].value_counts().sort_index()
    c0 = cluster_counts.get(0, 0)
    c1 = cluster_counts.get(1, 0)
    c2 = cluster_counts.get(2, 0)

    # =========================================================
    # Key Insights
    # =========================================================
    st.markdown("## Key insights")

    insights = [
        f"📘 Average study hours per day: {df['Study_Hours_Per_Day'].mean():.2f}",
        f"🎯 Average test score: {df['Test_Score'].mean():.2f}",
        f"📉 Model Mean Squared Error (MSE): {mse:.2f}",
        f"📈 Model R² score: {r2:.2f}",
        f"🧩 Cluster sizes → C0: {c0}, C1: {c1}, C2: {c2}"
    ]

    for insight in insights:
        st.markdown(f"- {insight}")

    # =========================================================
    # 📄 Export Analytics PDF
    # =========================================================
    st.markdown("## 📄 Export Analytics Report")

    if st.button("📄 Download Analytics PDF"):
        pdf_buffer = export_analytics_pdf(
            df=df,
            mse=mse,
            r2=r2,
            cluster_summary_df=summary
        )

        st.download_button(
            "⬇️ Download PDF",
            pdf_buffer,
            "StudyTrack_Analytics_Report.pdf",
            mime="application/pdf"
        )

        # =========================================================
# Global Footer (Streamlit-safe)
# =========================================================
        st.markdown("""            
                    <style>
                    /* Add space at bottom so footer is visible */
                    .main {
                        padding-bottom: 80px;
                    }

                    /* Footer styling */

                    .app-footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    background: linear-gradient(90deg, #020617, #0f172a);
                    color: #94a3b8;
                    text-align: center;
                    padding: 12px 0;
                    font-size: 13px;
                    border-top: 1px solid rgba(255,255,255,0.08);
                    z-index: 9999;
                    }
                    </style>

                    <div class="app-footer">
                    <strong style="color:#e5e7eb;">StudyTrack – AI Study Habit Recommender</strong><br>
                    Designed by <strong>Prem Kalse</strong> under the guidance of <strong>Mr. Anil Kumar Sir</strong>
                    
                    </div>
                    """, unsafe_allow_html=True)
