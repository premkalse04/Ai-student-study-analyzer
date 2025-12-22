import streamlit as st

def auth_css():
    st.markdown("""
    <style>

    /* Center everything */
    .main > div {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    .auth-wrapper {
        width: 900px;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 30px 80px rgba(0,0,0,0.35);
        background: white;
    }

    .auth-left {
        padding: 3rem;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
        height: 100%;
    }

    .auth-left h1 {
        font-size: 2.3rem;
        margin-bottom: 0.5rem;
    }

    .auth-left p {
        color: #cbd5f5;
        margin-top: 1rem;
        line-height: 1.6;
    }

    .auth-right {
        padding: 3rem;
    }

    .auth-toggle {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }

    </style>
    """, unsafe_allow_html=True)
