import streamlit as st
from auth.auth_utils import authenticate_user, create_user
from auth_styles import auth_css

def auth_page():
    auth_css()

    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "Login"

    st.markdown('<div class="auth-wrapper">', unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    # ---------- LEFT PANEL ----------
    with left:
        st.markdown("""
        <div class="auth-left">
            <h1>🎓 StudyTrack</h1>
            <h3>AI Study Habit Analyzer</h3>
            <p>
                Analyze student study habits, predict academic performance,
                and receive intelligent AI-based recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ---------- RIGHT PANEL ----------
    with right:
        st.markdown('<div class="auth-right">', unsafe_allow_html=True)

        # Toggle buttons INSIDE box
        t1, t2 = st.columns(2)
        with t1:
            if st.button("🔐 Login", use_container_width=True):
                st.session_state.auth_mode = "Login"
        with t2:
            if st.button("📝 Sign Up", use_container_width=True):
                st.session_state.auth_mode = "Signup"

        st.markdown("---")

        # -------- LOGIN --------
        if st.session_state.auth_mode == "Login":
            st.subheader("🔐 Login")

            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            if st.button("Login", use_container_width=True):
                if authenticate_user(email, password):
                    st.session_state.logged_in = True
                    st.success("Login successful")
                    st.rerun()
                else:
                    st.error("Invalid email or password")

        # -------- SIGNUP --------
        else:
            st.subheader("📝 Sign Up")

            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            confirm = st.text_input("Confirm Password", type="password")

            if st.button("Create Account", use_container_width=True):
                if password != confirm:
                    st.error("Passwords do not match")
                elif create_user(email, password):
                    st.success("Account created! Please login.")
                    st.session_state.auth_mode = "Login"
                else:
                    st.error("User already exists")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
