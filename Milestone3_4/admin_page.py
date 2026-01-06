import streamlit as st
import pandas as pd
from auth.auth_utils import get_all_users, get_all_auth_history


# 🔐 Change this to your admin email(s)
ADMIN_EMAILS = ["premkalse108.com"]


def admin_page():
    st.header("🛡️ Admin Dashboard")

    user_email = st.session_state.get("user_email")

    if user_email not in ADMIN_EMAILS:
        st.error("🚫 You are not authorized to access this page.")
        st.stop()

    # =========================
    # 👤 USERS TABLE
    # =========================
    st.subheader("👤 Registered Users")

    users = get_all_users()
    users_df = pd.DataFrame(
        users,
        columns=["Email", "Created At"]
    )

    st.dataframe(users_df, use_container_width=True)

    # =========================
    # 🕒 AUTH HISTORY
    # =========================
    st.subheader("🕒 Login / Signup History")

    history = get_all_auth_history()
    history_df = pd.DataFrame(
        history,
        columns=["Email", "Action", "Timestamp", "Status"]
    )

    st.dataframe(history_df, use_container_width=True)
