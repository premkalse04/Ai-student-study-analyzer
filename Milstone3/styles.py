import streamlit as st

def load_css():
    st.markdown("""
    <style>
    :root {
        --bg: #0b1220;
        --card: #111827;
        --border: #1f2937;
        --muted: #9ca3af;
        --text: #e5e7eb;
        --accent: #60a5fa;
        --accent-2: #a78bfa;
        --shadow: 0 22px 60px rgba(0,0,0,0.45);
    }

    .block-container {
        padding: 2.5rem 2.2rem 3rem;
        max-width: 1200px;
    }

    .stApp {
        background: radial-gradient(circle at 14% 18%, rgba(96,165,250,0.08), transparent 32%),
                    radial-gradient(circle at 84% 8%, rgba(167,139,250,0.12), transparent 36%),
                    var(--bg);
        color: var(--text);
    }

    /* Hero */
    .hero {
        width: 100%;
        padding: 2.6rem;
        border-radius: 22px;
        background: linear-gradient(135deg, rgba(17,24,39,0.92), rgba(30,41,59,0.94));
        border: 1px solid rgba(96,165,250,0.18);
        box-shadow: var(--shadow);
        margin-bottom: 2rem;
    }

    .hero-grid {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 1.8rem;
        align-items: center;
    }

    .hero-text {
        text-align: center;
    }

    .hero-text h1 {
        margin: 0.35rem 0 0.55rem;
        font-size: 2.35rem;
        line-height: 1.2;
        color: #f8fafc;
    }

    .gradient-text {
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-desc {
        color: #cbd5e1;
        margin: 0 0 1.15rem;
        font-size: 1.02rem;
        line-height: 1.65;
    }

    .hero-actions {
        display: flex;
        justify-content: center;
        gap: 0.7rem;
        margin-bottom: 0.9rem;
        flex-wrap: wrap;
    }

    .hero-microcopy {
        color: #94a3b8;
        font-size: 0.92rem;
    }

    .pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        font-size: 0.84rem;
        color: #e2e8f0;
        background: rgba(96,165,250,0.12);
        border: 1px solid rgba(96,165,250,0.35);
    }

    .pill-glow {
        box-shadow: 0 8px 26px rgba(96,165,250,0.28);
    }

    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.72rem 1.05rem;
        border-radius: 12px;
        font-weight: 700;
        text-decoration: none;
        border: 1px solid transparent;
        color: #0b1220;
        cursor: pointer;
        box-shadow: 0 16px 32px rgba(96,165,250,0.32);
        transition: transform 120ms ease, box-shadow 120ms ease, opacity 120ms ease;
    }

    .btn:hover { transform: translateY(-1px); opacity: 0.98; }

    .btn.primary {
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        color: #0b1220;
    }

    .btn.ghost {
        background: transparent;
        border: 1px solid rgba(255,255,255,0.12);
        color: #e2e8f0;
        box-shadow: none;
    }

    /* Hero card */
    .hero-card {
        background: #0f172a;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 1.35rem;
        box-shadow: var(--shadow);
        color: #e2e8f0;
    }

    .card-title {
        font-weight: 700;
        margin-bottom: 0.9rem;
        color: #e5e7eb;
        text-align: center;
    }

    .stat-row {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.75rem;
    }

    .stat-label {
        color: #94a3b8;
        font-size: 0.92rem;
    }

    .stat-value {
        font-size: 1.55rem;
        font-weight: 700;
        color: #f8fafc;
    }

    .divider {
        height: 1px;
        background: rgba(255,255,255,0.08);
        margin: 0.9rem 0;
    }

    .stacked {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        color: #cbd5e1;
    }

    .stacked-item {
        display: flex;
        align-items: center;
        gap: 0.45rem;
    }

    .dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: inline-block;
    }
    .dot.green { background: #22c55e; }
    .dot.blue { background: #60a5fa; }
    .dot.purple { background: #a78bfa; }

    /* Cards */
    .card {
        background: var(--card);
        border-radius: 16px;
        padding: 1.25rem 1.3rem;
        border: 1px solid var(--border);
        box-shadow: var(--shadow);
        color: var(--text);
    }

    .card.feature {
        min-height: 170px;
    }

    .card.mini {
        min-height: 140px;
    }

    .card h3, .card h4 {
        margin: 0.15rem 0 0.35rem;
    }

    .card p {
        margin: 0;
        color: #cbd5e1;
        line-height: 1.55;
    }

    .icon-badge {
        display: inline-flex;
        width: 44px;
        height: 44px;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: rgba(96,165,250,0.12);
        border: 1px solid rgba(96,165,250,0.28);
        font-size: 1.15rem;
    }

    .section-heading {
        margin: 1.8rem 0 1rem;
        font-weight: 700;
        font-size: 1.25rem;
        color: #e5e7eb;
        text-align: center;
    }

    .timeline {
        display: flex;
        gap: 0.65rem;
        flex-wrap: wrap;
    }

    .step {
        padding: 0.8rem 0.95rem;
        border-radius: 12px;
        background: #111827;
        border: 1px solid var(--border);
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        box-shadow: 0 10px 24px rgba(0, 0, 0, 0.25);
    }

    .step span {
        width: 26px;
        height: 26px;
        border-radius: 8px;
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        color: #0b1220;
        display: grid;
        place-items: center;
        font-weight: 700;
        font-size: 0.9rem;
    }

    .cta-panel {
        margin-top: 1.3rem;
        padding: 1.35rem;
        border-radius: 16px;
        background: #0f172a;
        border: 1px solid var(--border);
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        align-items: center;
        flex-wrap: wrap;
        box-shadow: var(--shadow);
    }

    .cta-panel h3 {
        margin: 0.15rem 0 0.35rem;
        color: #e5e7eb;
    }

    .cta-panel p {
        margin: 0;
        color: #cbd5e1;
    }

    .cta-actions {
        display: flex;
        gap: 0.6rem;
        flex-wrap: wrap;
    }

    .pill.muted {
        background: rgba(96,165,250,0.12);
        border: 1px solid rgba(96,165,250,0.28);
        color: #e2e8f0;
    }

    @media (max-width: 992px) {
        .hero-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)
