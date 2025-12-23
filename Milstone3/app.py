from homepage import show_homepage
import streamlit as st
import pandas as pd
from io import BytesIO
from pdf_utils import export_analytics_pdf
from login import login_page
from signup import signup_page


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


from excel_utils import process_excel
from recommendation import generate_recommendation
from analysis_charts import (
    plot_actual_vs_predicted,
    plot_clusters,
    cluster_summary
)
from styles import load_css

# =========================================================
# Page Configuration
# =========================================================
st.set_page_config(
    page_title="StudyTrack – AI Study Habit Recommender",
    page_icon="🎓",
    layout="wide"
)

load_css()

from auth_page import auth_page

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

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
        <hr style="margin-top:10px; margin-bottom:10px;">
        """,
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        ["🏠 Home", "✍️ Individual prediction", "📁 Upload Excel", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
with st.sidebar:
    st.markdown("### 👤 Account")

    if st.button("🚪 Logout", use_container_width=True):
        # Clear session
        st.session_state.logged_in = False
        st.session_state.pop("user_email", None)
        st.session_state.pop("auth_mode", None)

        st.success("Logged out successfully")
        st.rerun()
     

# =========================================================
# Page Routing
# =========================================================
if page == "🏠 Home":
    show_homepage()
    st.markdown("""    
              <div class="hero">
     <h1>🎓 StudyTrack</h1>
     <p class="hero-subtitle">
         AI-Based Student Study Habit Recommender System
     </p>
     <p class="hero-desc">
        Analyze student study habits, predict academic performance,
        and generate intelligent recommendations using Machine Learning.
     </p>
</div>
""", unsafe_allow_html=True)
   

# ---------------- Landing ----------------
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("## Welcome to StudyTrack")
        st.markdown(
            "Analyze student study habits, identify risks early, "
            "and generate AI-based recommendations."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Snapshot")
        st.markdown("""
        - 🎓 Student-focused  
        - 📊 Excel-based analysis  
        - 🤖 AI-style recommendations  
        - 🚀 Easy to extend with ML  
        """)
        st.markdown("</div>", unsafe_allow_html=True)



elif page == "✍️ Individual prediction":
    st.header(" Manual Student Data Entry")

    with st.form("manual_form"):
        c1, c2 = st.columns(2)

        with c1:
            study = st.number_input("Study Hours / Day", 0.0, 16.0, 2.5)
            sleep = st.number_input("Sleep Hours", 0.0, 16.0, 7.0)
            attendance = st.slider("Attendance (%)", 0, 100, 80)

        with c2:
            assignment = st.slider("Assignment Completion (%)", 0, 100, 75)
            score = st.slider("Test Score", 0, 100, 65)

        submit = st.form_submit_button("💡 Get Recommendation")

    if submit:
        result = generate_recommendation(
            study, sleep, attendance, assignment, score
        )

        st.subheader("📌 Recommendation")
        for k, v in result.items():
            st.markdown(f"**{k}:** {v}")


elif page == "📁 Upload Excel":
    st.header("📁 Upload Excel File")

    file = st.file_uploader("Upload .xlsx file", type=["xlsx"])

    if file:
        df = pd.read_excel(file)
        st.session_state["uploaded_df"] = df

        st.success("Data uploaded successfully")
        st.dataframe(df.head(), use_container_width=True)

        if st.button("📊 Analyze & Recommend"):
            result_df = process_excel(df)
            st.dataframe(result_df)

            buffer = BytesIO()
            result_df.to_excel(buffer, index=False)
            buffer.seek(0)

            st.download_button(
                "⬇️ Download Results",
                buffer,
                "studytrack_results.xlsx"
            )


elif page == "📊 Analytics":
    st.header("📊 Analysis & Insights")

    if "uploaded_df" not in st.session_state:
        st.info("Please upload an Excel file first.")
        st.stop()

    df = st.session_state["uploaded_df"]

    # ===============================
    # 📄 Dataset Overview
    # ===============================
    st.subheader("📄 Dataset Overview")
    st.dataframe(df.describe(), use_container_width=True)

    # ===============================
    # 📈 Regression Analysis (COMPUTE FIRST)
    # ===============================
    X = df[['Study_Hours_Per_Day', 'Sleep_Hours', 'Attendance_Percentage']]
    y = df['Test_Score']

    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # ===============================
    # 📊 Key Metrics (ROW 1)
    # ===============================
    st.markdown("## 📊 Key Metrics")
    k1, k2, k3 = st.columns(3)

    k1.metric("Average Score", round(df["Test_Score"].mean(), 2))
    k2.metric("Highest Score", df["Test_Score"].max())
    k3.metric("Lowest Score", df["Test_Score"].min())

    # ===============================
    # 📈 Visual Analytics (ROW 2)
    # ===============================
    st.markdown("## 📈 Visual Analytics")

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 📉 Actual vs Predicted Scores")
        fig1 = plot_actual_vs_predicted(y_test, y_pred)
        fig1.set_size_inches(6, 4)
        st.pyplot(fig1)

    with col_right:
        st.markdown("### 🧩 Student Clusters")

        from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        df["Cluster_Number"] = KMeans(
            n_clusters=3,
            random_state=42
        ).fit_predict(X_scaled)

        fig2 = plot_clusters(df)
        fig2.set_size_inches(6, 4)
        st.pyplot(fig2)   

    # ===============================
    # 📊 Extra Insights (ROW 3)
    # ===============================
    st.markdown("## 📌 Cluster Summary & Model Quality")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 📋 Cluster Summary")
        st.dataframe(cluster_summary(df), use_container_width=True)

    with col4:
        st.markdown("### 🎯 Model Performance")
        st.metric("Mean Squared Error", round(mean_squared_error(y_test, y_pred), 2))
        st.metric("R² Score", round(r2_score(y_test, y_pred), 2))

