import streamlit as st

def show_homepage():
    st.markdown("### ✨ AI-Powered Academic Analytics")

    st.markdown(
        "# 🎓 **StudyTrack**\n"
        "### AI-Based Student Study Habit Recommender System"
    )

    st.write(
        "An intelligent analytics platform that analyzes student study habits, "
        "predicts academic performance, and generates personalized recommendations "
        "using advanced Machine Learning techniques."
    )

    st.markdown("")


    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Accuracy", "95%")
    m2.metric("Students", "10K+")
    m3.metric("ML Models", "3")

    st.markdown("---")

    # Key Features
    st.subheader("🚀 Key Features")

    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown("### 📊 Data-Driven Analysis")
        st.write("- Study & sleep analysis")
        st.write("- Attendance impact")
        st.write("- Performance tracking")

    with f2:
        st.markdown("### 🤖 AI & ML Models")
        st.write("- Linear Regression")
        st.write("- K-Means Clustering")
        st.write("- Risk classification")

    with f3:
        st.markdown("### 📄 Smart Recommendations")
        st.write("- Personalized tips")
        st.write("- Excel batch analysis")
        st.write("- Downloadable reports")

    st.markdown("")

    f4, f5, f6 = st.columns(3)
    with f4:
        st.markdown("### 📈 Performance Prediction")
        st.write("Forecast academic outcomes")

    with f5:
        st.markdown("### 🧩 Student Segmentation")
        st.write("Identify at-risk students")

    with f6:
        st.markdown("### ⚡ Real-Time Insights")
        st.write("Instant analytics & dashboards")

    st.markdown("---")

    # Workflow
    st.subheader("🧭 System Workflow")
    st.write(
        "Upload Data → Preprocess → ML Analysis → Generate Insights → Visualize"
    )

    st.markdown("---")
    st.caption("Final Year Project · AI-Based Academic Analytics System")
