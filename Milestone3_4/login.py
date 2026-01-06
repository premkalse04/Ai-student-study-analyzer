import streamlit as st
from auth.auth_utils import authenticate_user
from auth_styles import auth_css

def login_page():
    auth_css()

    # Center container
    st.markdown('<div class="auth-wrapper">', unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1])

    # -------- LEFT PANEL --------
    with col_left:
        st.markdown("""
        <div class="auth-left-panel">
            <h1>🎓 StudyTrack</h1>
            <h3>AI Study Habit Analyzer</h3>
            <p>
                Analyze student study habits, predict academic performance,
                and receive intelligent AI-based recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # -------- RIGHT PANEL --------
    st.session_state.logged_in = True
    st.session_state.user_email = email
    st.rerun()

    
    with col_right:
        st.markdown("""
        <div class="auth-right-panel">
            <h2>🔐 Login</h2>
        """, unsafe_allow_html=True)

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            if authenticate_user(email, password):
                st.session_state["logged_in"] = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid email or password")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
