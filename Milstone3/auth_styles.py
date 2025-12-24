import streamlit as st

def auth_css():
    st.markdown("""
    <style>

    :root {
        --bg: #0b1220;
        --panel: rgba(19, 28, 49, 0.8);
        --muted: #cbd5f5;
        --accent: #5b8cff;
        --accent-strong: #7cf0ff;
        --border: #1e293b;
    }

    /* Overall page */
    .block-container {
        padding: 2.5rem 1rem 3rem;
        max-width: 1150px;
    }

    /* Hide legacy wrappers if still rendered */
    .auth-page,
    .auth-wrapper {
        display: none !important;
    }

    .stApp {
        background: radial-gradient(circle at 10% 20%, #132347 0, rgba(11,18,32,0) 30%),
                    radial-gradient(circle at 80% 0%, #1b3a6c 0, rgba(11,18,32,0) 35%),
                    var(--bg);
    }

    /* Columns container */
    div[data-testid="stHorizontalBlock"] {
        background: linear-gradient(150deg, rgba(16,24,40,0.95), rgba(12,19,35,0.95));
        border: 1px solid var(--border);
        border-radius: 26px;
        overflow: hidden;
        box-shadow: 0 40px 120px rgba(0, 0, 0, 0.55);
        position: relative;
        isolation: isolate;
    }

    div[data-testid="stHorizontalBlock"]::after {
        content: "";
        position: absolute;
        inset: -40%;
        background: radial-gradient(circle at 25% 25%, rgba(124, 240, 255, 0.12), transparent 40%),
                    radial-gradient(circle at 80% 20%, rgba(91, 140, 255, 0.18), transparent 35%);
        filter: blur(18px);
        z-index: -1;
    }

    /* LEFT PANEL */
    .auth-left {
        padding: 3.75rem;
        background: linear-gradient(165deg, #111a2f 0%, #182544 40%, #0f182d 100%);
        color: white;
        display: flex;
        flex-direction: column;
        gap: 1.1rem;
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    .logo-badge {
        height: 64px;
        width: 64px;
        display: grid;
        place-items: center;
        border-radius: 18px;
        background: linear-gradient(135deg, #5b8cff, #7cf0ff);
        color: #0b1220;
        font-size: 2rem;
        font-weight: 700;
        box-shadow: 0 20px 40px rgba(124, 240, 255, 0.25);
    }

    .auth-left h1 {
        font-size: 2.5rem;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .eyebrow {
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-size: 0.8rem;
        color: rgba(255,255,255,0.7);
        margin: 0;
    }

    .lede {
        color: var(--muted);
        margin: 0;
        line-height: 1.7;
        font-size: 1rem;
    }

    .pill-group {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 0.2rem;
    }

    .pill {
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        background: rgba(124, 240, 255, 0.12);
        color: #e2f5ff;
        border: 1px solid rgba(124, 240, 255, 0.35);
        font-size: 0.85rem;
    }

    /* RIGHT PANEL */
    .auth-right {
        padding: 3.4rem;
        background: linear-gradient(155deg, rgba(15, 23, 42, 0.82), rgba(12, 17, 30, 0.9));
        backdrop-filter: blur(12px);
        color: white;
    }

    .auth-header h2 {
        margin: 0 0 0.35rem;
        font-size: 1.9rem;
    }

    .auth-header p {
        margin: 0;
        color: var(--muted);
    }

    /* Tabs styling */
    .stTabs [role="tablist"] {
        gap: 0.4rem;
        padding: 1.25rem 0 0.75rem;
    }

    .stTabs [role="tab"] {
        background: rgba(255,255,255,0.04);
        color: white;
        padding: 0.45rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.06);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #5b8cff, #7cf0ff);
        color: #0b1220 !important;
        border-color: transparent;
        font-weight: 700;
        box-shadow: 0 10px 30px rgba(91, 140, 255, 0.35);
    }

    /* Inputs */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.12);
        color: white;
        border-radius: 12px;
        padding: 0.75rem 0.9rem;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--accent);
        box-shadow: 0 0 0 1px var(--accent);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #5b8cff, #7cf0ff);
        color: #0b1220;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-weight: 700;
        box-shadow: 0 18px 40px rgba(91, 140, 255, 0.35);
    }

    .stButton > button:hover {
        filter: brightness(1.05);
    }

    @media (max-width: 1024px) {
        div[data-testid="stHorizontalBlock"] {
            border-radius: 22px;
        }
    }
    </style>
    """, unsafe_allow_html=True)
