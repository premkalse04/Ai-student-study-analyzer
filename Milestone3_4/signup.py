import streamlit as st
from auth.auth_utils import create_user
from auth_styles import auth_css

def signup_page():
    auth_css()

    st.markdown("""
    <div class="auth-container">
        <div class="auth-left">
            <h1>🎓 StudyTrack</h1>
            <h3>Create Account</h3>
            <p>
                Join StudyTrack to unlock AI-powered academic
                insights and personalized learning recommendations.
            </p>
        </div>
        <div class="auth-right">
            <h2>📝 Sign Up</h2>
    """, unsafe_allow_html=True)



    email = st.text_input("Email").strip().lower()
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):
        if password != confirm:
            st.error("Passwords do not match")
        elif create_user(email, password):
            st.success("Account created! Please login.")
        else:
            st.error("User already exists")

    st.markdown("</div></div>", unsafe_allow_html=True)
