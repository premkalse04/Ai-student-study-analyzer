import streamlit as st

def show_homepage():
    st.markdown("""
    <div style="padding: 2.5rem 1rem;">
        <h1 style="font-size:2.6rem;">🎓 StudyTrack</h1>
        <h4 style="color:#9ca3af;">
            AI-Based Student Study Habit Recommender System
        </h4>
        <p style="max-width:850px; font-size:1.05rem; margin-top:1rem;">
            StudyTrack is an intelligent analytics platform designed to analyze
            student study habits, predict academic performance, and generate
            personalized recommendations using Machine Learning techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # ---------- Features ----------
    st.markdown("## 🚀 Key Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.markdown("""
        ### 📊 Data-Driven Analysis
        - Study & sleep pattern analysis  
        - Attendance impact evaluation  
        - Performance tracking  
        """)

    with f2:
        st.markdown("""
        ### 🤖 AI & ML Models
        - Linear Regression (Score Prediction)  
        - K-Means Clustering (Student Groups)  
        - Risk classification  
        """)

    with f3:
        st.markdown("""
        ### 📄 Smart Recommendations
        - Personalized study tips  
        - Excel-based batch analysis  
        - Downloadable results  
        """)

    st.markdown("---")

    # ---------- Workflow ----------
    st.markdown("## 🧭 System Workflow")

    st.markdown("""
    1️⃣ Upload student data or enter manually  
    2️⃣ System preprocesses & normalizes data  
    3️⃣ ML models analyze patterns  
    4️⃣ Recommendations & insights generated  
    5️⃣ Visual analytics for decision-making  
    """)

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center; color:#9ca3af; font-size:0.9rem;">
        Final Year Project · AI-Based Academic Analytics System
    </div>
    """, unsafe_allow_html=True)
