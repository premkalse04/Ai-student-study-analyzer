import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .block-container {
        padding-top: 4.5rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    .navbar {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 3.5rem;
        background: linear-gradient(90deg, #0f172a, #1e293b);
        display: flex;
        align-items: center;
        padding: 0 1.5rem;
        z-index: 1000;
        color: white;
    }

    .navbar-title {
        font-weight: 600;
        font-size: 1rem;
    }

    .hero {
        width: 100%;
        padding: 4rem 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #111827, #1f2937);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        margin-bottom: 2.5rem;
    }

    

    .card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 0.8rem;
        padding: 1rem;
    }
    

    </style>
    """, unsafe_allow_html=True)

