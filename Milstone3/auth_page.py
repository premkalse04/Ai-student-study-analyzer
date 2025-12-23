import streamlit as st
from auth.auth_utils import authenticate_user, create_user
from auth_styles import auth_css   # or wherever auth_css() is defined

def auth_page():
    # Inject page-specific CSS
    auth_css()

    # Outer shell to center content
    st.markdown('<div class="auth-page"><div class="auth-wrapper">', unsafe_allow_html=True)

    left, right = st.columns([1.15, 1])

    # ---------- LEFT PANEL ----------
    with left:
        st.markdown(
            """
            <div class="auth-left">
                <div class="logo-badge">🎓</div>
                <h1>StudyTrack</h1>
                <p class="eyebrow">AI Study Habit Analyzer</p>
                <p class="lede">
                    Understand study patterns, predict performance, and surface
                    tailored actions that keep learners on track.
                </p>
                <div class="pill-group">
                    <span class="pill">Progress dashboards</span>
                    <span class="pill">Smart reminders</span>
                    <span class="pill">Personalized tips</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------- RIGHT PANEL ----------
    with right:
        st.markdown('<div class="auth-right">', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="auth-header">
                <h2>Welcome back</h2>
                <p>Log in or create your StudyTrack account to continue.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        tab_login, tab_signup = st.tabs(["🔐 Login", "📝 Sign Up"])

        # LOGIN
        with tab_login:
            email = st.text_input("Email", key="login_email", placeholder="name@email.com")
            password = st.text_input("Password", type="password", key="login_password", placeholder="••••••••")

            if st.button("Login", use_container_width=True, key="login_btn"):
                if authenticate_user(email, password):
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.rerun()
                else:
                    st.error("Invalid email or password")

        # SIGN UP
        with tab_signup:
            email = st.text_input("Email", key="signup_email", placeholder="name@email.com")
            password = st.text_input("Password", type="password", key="signup_password", placeholder="Min. 8 characters")
            confirm = st.text_input("Confirm Password", type="password", key="signup_confirm", placeholder="Re-enter password")

            if st.button("Create Account", use_container_width=True, key="signup_btn"):
                if password != confirm:
                    st.error("Passwords do not match")
                elif create_user(email, password):
                    st.success("Account created. Please login.")
                else:
                    st.error("User already exists")

        st.markdown('</div>', unsafe_allow_html=True)

    # Close wrapper
    st.markdown('</div></div>', unsafe_allow_html=True)
