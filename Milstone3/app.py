from homepage import show_homepage
from styles import load_css
import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from homepage import show_homepage
from pdf_utils import export_analytics_pdf
from login import login_page
from signup import signup_page


st.set_page_config(page_title="StudyTrack", layout="wide")


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
        ["🏠 Home", "👤 Individual prediction", "📁 Train Model", "📊 Analytics"],
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

elif page == "👤 Individual prediction":
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


elif page == "📁 Train Model":
    st.header("📁 Upload File")
    st.markdown(
        """
        Upload your dataset to generate tailored recommendations.
        We'll adapt to your column names automatically (common aliases supported).
        """,
        unsafe_allow_html=True,
    )

    file = st.file_uploader("Upload .xlsx file", type=["xlsx"])

    if file:
        df = pd.read_excel(file)
        # Attempt to map and process; show friendly errors
        try:
            result_df = process_excel(df)
            st.session_state["uploaded_df"] = df

            st.success("Data uploaded and mapped successfully. Model ready to recommend.")

            st.markdown("#### Preview (first 5 rows)")
            st.dataframe(df.head(), use_container_width=True)

            if st.button("🚀 Train Model", use_container_width=True):
                    st.markdown("#### Full results (all columns)")
                    cols_to_show = [
                        "Performance_Level",
                        "Rec_Study",
                        "Rec_Sleep",
                        "Rec_Attendance",
                        "Rec_Assignments",
                        "Rec_Advice",
                    ]
                    available = [c for c in cols_to_show if c in result_df.columns]
                    exclude = [
                        "Study_Hours_Per_Day",
                        "Sleep_Hours",
                        "Attendance_Percentage",
                        "Assignment_Completion",
                        "Test_Score",
                        "Social_Media_Hours",
                        "Exercise_Hours",
                    ]
                    display_cols = [c for c in result_df.columns if c not in exclude]
                    st.dataframe(result_df[display_cols], use_container_width=True)

                    with st.expander("Personalized recommendations"):
                        st.dataframe(result_df[available], use_container_width=True)

                    st.markdown("#### Visual insights")
                    numeric_cols = [
                        "Study_Hours_Per_Day",
                        "Sleep_Hours",
                        "Attendance_Percentage",
                        "Assignment_Completion",
                        "Test_Score",
                    ]
                    missing_numeric = [c for c in numeric_cols if c not in result_df.columns]

                    # Prediction test marks distribution
                    if "Test_Score" in result_df.columns:
                        hist = result_df["Test_Score"].value_counts(
                            bins=10, sort=False
                        ).sort_index()
                        st.markdown("**Prediction test marks distribution**")
                        st.bar_chart(hist)

                    # Recommendation distribution (Performance levels)
                    if "Performance_Level" in result_df.columns:
                        perf_counts = result_df["Performance_Level"].value_counts()
                        st.markdown("**Recommendation / performance distribution**")
                        st.bar_chart(perf_counts)

                    # Simple clustering visualization
                    if not missing_numeric:
                        try:
                            from sklearn.preprocessing import StandardScaler
                            from sklearn.cluster import KMeans

                            X = result_df[numeric_cols]
                            scaler = StandardScaler()
                            X_scaled = scaler.fit_transform(X)

                            kmeans = KMeans(n_clusters=3, random_state=42)
                            clusters = kmeans.fit_predict(X_scaled)
                            result_df["Cluster"] = clusters

                            fig, ax = plt.subplots(figsize=(6, 4))
                            scatter = ax.scatter(
                                result_df["Study_Hours_Per_Day"],
                                result_df["Test_Score"],
                                c=clusters,
                                cmap="viridis",
                                alpha=0.8,
                            )
                            ax.set_xlabel("Study Hours/Day")
                            ax.set_ylabel("Test Score")
                            ax.set_title("Clustering by study hours vs test score")
                            st.markdown("**Clustering (Study hours vs Test score)**")
                            st.pyplot(fig)
                        except Exception as e:
                            st.info(f"Clustering not shown: {e}")

                    buffer = BytesIO()
                    result_df.to_excel(buffer, index=False)
                    buffer.seek(0)

                    st.download_button(
                        "⬇️ Download Results",
                        buffer,
                        "studytrack_results.xlsx",
                        use_container_width=True,
                    )
        except Exception as e:
            st.error(f"Could not process file: {e}")
            st.info(
                "Ensure your sheet includes study hours, sleep hours, attendance %, "
                "assignment completion %, and test score columns (common aliases accepted)."
            )


elif page == "📊 Analytics":
    st.header("📊 Analysis & Insights")

    # Hero-style intro for analytics
    st.markdown(
        """
        <div class="analytics-hero card">
          <div>
            <div class="pill pill-glow">Analytics workspace</div>
            <h2>Understand how habits drive outcomes</h2>
            <p>
              Explore how study hours, sleep, and attendance combine to shape performance.
              Use the visuals and clusters below to spot patterns and at‑risk groups quickly.
            </p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "uploaded_df" not in st.session_state:
        st.info("Please upload an Excel file first.")
        st.stop()

    df = st.session_state["uploaded_df"]

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
    # 📄 Dataset Overview (EXPANDER)
    # ===============================
    with st.expander("📄 View dataset statistics"):
        st.dataframe(df.describe(), use_container_width=True)

    # ===============================
    # 📊 Key Metrics (ROW 1)
    # ===============================
    st.markdown("<div class='section-heading'>Key performance snapshot</div>", unsafe_allow_html=True)

    m_col1, m_col2, m_col3 = st.columns(3)
    avg_score = round(df["Test_Score"].mean(), 2)
    max_score = df["Test_Score"].max()
    min_score = df["Test_Score"].min()

    with m_col1:
        st.markdown(
            f"""
            <div class="card mini analytics-metric">
              <div class="stat-label">Average score</div>
              <div class="stat-value">{avg_score}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m_col2:
        st.markdown(
            f"""
            <div class="card mini analytics-metric">
              <div class="stat-label">Highest score</div>
              <div class="stat-value">{max_score}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with m_col3:
        st.markdown(
            f"""
            <div class="card mini analytics-metric">
              <div class="stat-label">Lowest score</div>
              <div class="stat-value">{min_score}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ===============================
    # 📈 Visual Analytics (ROW 2)
    # ===============================
    st.markdown("<div class='section-heading'>Visual analytics</div>", unsafe_allow_html=True)

    col_left, col_right = st.columns(2)
    # ====== INSERTED: standalone dashed separator + Study Hours vs Marks plot ======
    st.markdown(
        """
        <div style="border-top:2px dashed #bbb; margin:20px 0; padding-top:10px;">
          <h3 style="margin:0;">Study Hours vs Marks</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    try:
        import numpy as np

        x = df["Study_Hours_Per_Day"].astype(float)
        y_vals = df["Test_Score"].astype(float)

        fig_sh, ax_sh = plt.subplots(figsize=(8, 4))
        attendance = df.get("Attendance_Percentage", None)

        if attendance is not None:
            sc = ax_sh.scatter(x, y_vals, c=attendance, cmap="viridis", s=60, alpha=0.8)
            plt.colorbar(sc, ax=ax_sh, label="Attendance (%)")
        else:
            ax_sh.scatter(x, y_vals, color="#4c78a8", s=60, alpha=0.8)

        # dashed regression line
        if len(x.dropna()) >= 2:
            m, b = np.polyfit(x.dropna(), y_vals.loc[x.dropna().index], 1)
            xs = np.linspace(x.min(), x.max(), 100)
            ax_sh.plot(xs, m * xs + b, color="red", linestyle="--", linewidth=2)

        ax_sh.set_xlabel("Study Hours / Day")
        ax_sh.set_ylabel("Test Score")
        ax_sh.set_title("Study Hours vs Marks")
        st.pyplot(fig_sh)
    except Exception as e:
        st.info(f"Could not draw Study Hours vs Marks plot: {e}")

    with col_left:
        st.markdown(
            """
            <div class="card analytics-card">
              <h3>📉 Actual vs predicted scores</h3>
              <p class="analytics-caption">
                Compare true test scores against model predictions to inspect fit quality and outliers.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        fig1 = plot_actual_vs_predicted(y_test, y_pred)
        fig1.set_size_inches(6, 4)
        st.pyplot(fig1)

    with col_right:
        st.markdown(
            """
            <div class="card analytics-card">
              <h3>🧩 Habit-based clusters</h3>
              <p class="analytics-caption">
                Students grouped by study hours, sleep, and attendance to reveal distinct learning patterns.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        df["Cluster_Number"] = KMeans(
            n_clusters=3,
            random_state=42
        ).fit_predict(X_scaled)

        fig2 = plot_clusters(df)
        fig2.set_size_inches(3, 2)
        st.pyplot(fig2)

    # ====== INSERTED: Correlation heatmap (standalone, after clusters) ======
    try:
        import seaborn as sns
        # choose numeric columns that exist
        corr_cols = [
            "Study_Hours_Per_Day",
            "Sleep_Hours",
            "Attendance_Percentage",
            "Assignment_Completion",
            "Test_Score",
        ]
        corr_cols = [c for c in corr_cols if c in df.columns]
        if len(corr_cols) >= 2:
            corr = df[corr_cols].corr()

            st.markdown(
                """
                <div style="border-top:1px dashed #bbb; margin:10px 0; padding-top:5px;">
                  <h3 style="margin:0;">Correlation heatmap</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )

            fig_h, ax_h = plt.subplots(figsize=(5, 2))
            sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=ax_h)
            ax_h.set_title("Correlation between study habits and scores")
            st.pyplot(fig_h)
    except Exception as e:
        st.info(f"Could not draw correlation heatmap: {e}")

    # ====== INSERTED: Key insights summary (standalone) ======
    try:
        import numpy as np

        insights = []

        if "Study_Hours_Per_Day" in df.columns:
            insights.append(f"Average study hours / day: {df['Study_Hours_Per_Day'].mean():.2f}")

        if "Test_Score" in df.columns:
            insights.append(f"Average test score: {df['Test_Score'].mean():.1f}")

        # Correlation between study hours and score (if available)
        if "corr" in locals() and "Study_Hours_Per_Day" in corr.index and "Test_Score" in corr.columns:
            insights.append(f"Study hours ↔ Test score correlation: {corr.loc['Study_Hours_Per_Day','Test_Score']:.2f}")

        # Top correlated pairs
        if "corr" in locals() and not corr.empty:
            abs_corr = corr.abs().where(~np.eye(len(corr), dtype=bool)).stack()
            if not abs_corr.empty:
                top = abs_corr.sort_values(ascending=False).head(3)
                top_list = []
                for (a, b), val in top.items():
                    top_list.append(f"{a} vs {b}: {corr.loc[a,b]:+.2f}")
                insights.append("Top correlated pairs: " + "; ".join(top_list))

        # Regression coefficients and performance
        if "model" in locals():
            features = list(X.columns)
            coef_pairs = []
            for feat, coef in zip(features, model.coef_):
                coef_pairs.append(f"{feat}: {coef:.2f}")
            insights.append("Regression coefficients: " + "; ".join(coef_pairs))

            try:
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)
                insights.append(f"Model MSE: {mse:.2f}, R²: {r2:.2f}")
            except Exception:
                pass

        # Cluster summary if present
        if "Cluster_Number" in df.columns:
            counts = df["Cluster_Number"].value_counts().sort_index()
            counts_str = ", ".join([f"C{int(idx)}={int(v)}" for idx, v in counts.items()])
            insights.append("Cluster sizes: " + counts_str)

        # Render insights
        st.markdown(
            "<div style='border-top:1px solid #eee; margin:15px 0; padding-top:10px;'><h3 style='margin:0;'>Key insights</h3></div>",
            unsafe_allow_html=True,
        )
        if insights:
            for item in insights:
                st.markdown(f"- {item}")
        else:
            st.markdown("_No key insights could be derived from the current data._")
    except Exception as e:
        st.info(f"Could not compute key insights: {e}")




