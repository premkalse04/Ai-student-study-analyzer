import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');

    * { font-family: 'Inter', sans-serif; }

    body {
      background: radial-gradient(circle at top, #0f172a, #020617);
      color: #e5e7eb;
    }

    /* FIX STREAMLIT WIDTH */
    .block-container {
      max-width: 1400px !important;
      padding-left: 3rem !important;
      padding-right: 3rem !important;
    }

    .main {
      background:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
      background-size: 60px 60px;
    }

    /* HERO */
    .hero {
      padding: 5rem 1rem;
    }

    .hero-grid {
      max-width: 1200px;
      margin: auto;
      display: grid;
      grid-template-columns: 1.3fr 1fr;
      gap: 2.5rem;
    }

    .hero-text h1 {
      font-size: 56px;
      font-weight: 800;
      color: white;
    }

    .gradient-text {
      background: linear-gradient(135deg, #38bdf8, #0ea5e9);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
      font-size: 20px;
      color: #94a3b8;
      margin-top: .5rem;
    }

    .hero-desc {
      color: #64748b;
      max-width: 520px;
      margin: 1rem 0 2rem;
    }

    .pill {
      display: inline-block;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 14px;
      margin-bottom: 1rem;
    }

    .pill-glow {
      background: rgba(56,189,248,.15);
      color: #38bdf8;
      box-shadow: 0 0 20px rgba(56,189,248,.35);
    }

    /* BUTTONS */
    .btn {
      display: inline-block;
      padding: 12px 22px;
      border-radius: 12px;
      font-weight: 600;
      margin-right: 12px;
    }

    .btn.primary {
      background: linear-gradient(135deg, #38bdf8, #0ea5e9);
      color: black;
    }

    .btn.ghost {
      border: 1px solid #1e293b;
      color: #e5e7eb;
    }

    /* HERO CARD */
    .hero-card {
      background: rgba(15,23,42,.85);
      border: 1px solid #1e293b;
      border-radius: 20px;
      padding: 24px;
      backdrop-filter: blur(10px);
    }

    .card-title {
      color: #94a3b8;
      margin-bottom: 1rem;
    }

    .stat-row {
      display: flex;
      justify-content: space-between;
    }

    .stat-label {
      font-size: 13px;
      color: #64748b;
    }

    .stat-value {
      font-size: 32px;
      font-weight: 700;
      color: #38bdf8;
    }

    .divider {
      height: 1px;
      background: #1e293b;
      margin: 1.2rem 0;
    }

    .stacked-item {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #94a3b8;
      margin-bottom: 8px;
    }

    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }

    .dot.green { background: #22c55e; }
    .dot.blue { background: #38bdf8; }
    .dot.purple { background: #a855f7; }

    /* FEATURES */
    .section-heading {
      font-size: 36px;
      font-weight: 700;
      color: white;
      margin: 4rem 0 2rem;
      text-align: center;
    }

    .features-grid {
      max-width: 1200px;
      margin: auto;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }

    .card {
      background: rgba(15,23,42,.85);
      border: 1px solid #1e293b;
      border-radius: 18px;
      padding: 22px;
    }

    .icon-badge {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, #38bdf8, #8b5cf6);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)
