import streamlit as st
from pathlib import Path

ASSETS = Path(__file__).parent / "assets"

def _hero_section():
    return """
    <div style="text-align:center; padding:48px 0 24px 0;">
      <div style="display:inline-block; background:linear-gradient(90deg,#06b6d4,#3b82f6); color:white; padding:6px 14px; border-radius:20px; font-weight:700; margin-bottom:14px;">
      🎓  AI Study Habit Recommender
      </div>
      <h1 style="font-size:48px; margin:6px 0 8px 0; color:#ffffff;"> 🎓 StudyTrack</h1>
      <p style="color:#9ca3af; max-width:900px; margin:0 auto 18px auto; line-height:1.6;">
        An intelligent analytics platform that analyzes student study habits, predicts academic performance,
        and generates personalized recommendations using machine learning.
      </p>
      <div style="margin-top:12px;">
        <a href="#" style="background:linear-gradient(90deg,#06b6d4,#3b82f6); color:white; padding:10px 18px; border-radius:10px; text-decoration:none; margin-right:8px;">Get Started</a>
        <a href="#" style="background:#0b1220; color:#cbd5e1; padding:10px 18px; border-radius:10px; text-decoration:none;">View sample report</a>
      </div>
    </div>
    """

def _workflow_section():
    return """
    <div style="border-top:2px dashed rgba(148,163,184,0.12); margin:28px 0; padding:20px 10px; border-radius:8px;">
      <h3 style="text-align:center; color:#e6eef8; margin-bottom:12px;">System Workflow</h3>
      <div style="display:flex; gap:14px; justify-content:space-between; flex-wrap:wrap;">
        <div style="flex:1; min-width:160px; text-align:center; padding:12px; background:#071018; border-radius:10px;">
          <div style="width:52px; height:52px; margin:0 auto 8px; border-radius:12px; background:linear-gradient(135deg,#06b6d4,#3b82f6); display:flex; align-items:center; justify-content:center; color:white; font-weight:700;">01</div>
          <div style="font-weight:700; color:#e6eef8;">Upload Data</div>
          <div style="color:#9ca3af; font-size:13px;">Excel or manual entry</div>
        </div>
        <div style="flex:1; min-width:160px; text-align:center; padding:12px; background:#071018; border-radius:10px;">
          <div style="width:52px; height:52px; margin:0 auto 8px; border-radius:12px; background:linear-gradient(135deg,#7c3aed,#06b6d4); display:flex; align-items:center; justify-content:center; color:white; font-weight:700;">02</div>
          <div style="font-weight:700; color:#e6eef8;">Preprocess</div>
          <div style="color:#9ca3af; font-size:13px;">Normalize & clean</div>
        </div>
        <div style="flex:1; min-width:160px; text-align:center; padding:12px; background:#071018; border-radius:10px;">
          <div style="width:52px; height:52px; margin:0 auto 8px; border-radius:12px; background:linear-gradient(135deg,#06b6d4,#9333ea); display:flex; align-items:center; justify-content:center; color:white; font-weight:700;">03</div>
          <div style="font-weight:700; color:#e6eef8;">ML Analysis</div>
          <div style="color:#9ca3af; font-size:13px;">Regression & Clustering</div>
        </div>
        <div style="flex:1; min-width:160px; text-align:center; padding:12px; background:#071018; border-radius:10px;">
          <div style="width:52px; height:52px; margin:0 auto 8px; border-radius:12px; background:linear-gradient(135deg,#10b981,#06b6d4); display:flex; align-items:center; justify-content:center; color:white; font-weight:700;">04</div>
          <div style="font-weight:700; color:#e6eef8;">Generate Insights</div>
          <div style="color:#9ca3af; font-size:13px;">Personalized actions</div>
        </div>
        <div style="flex:1; min-width:160px; text-align:center; padding:12px; background:#071018; border-radius:10px;">
          <div style="width:52px; height:52px; margin:0 auto 8px; border-radius:12px; background:linear-gradient(135deg,#3b82f6,#06b6d4); display:flex; align-items:center; justify-content:center; color:white; font-weight:700;">05</div>
          <div style="font-weight:700; color:#e6eef8;">Visualize</div>
          <div style="color:#9ca3af; font-size:13px;">Interactive dashboards</div>
        </div>
      </div>
    </div>
    """

def _features_section():
    return """
    <div style="margin:18px 0 6px 0;">
      <h3 style="text-align:center; color:#e6eef8; margin-bottom:12px;">Key Features</h3>
      <div style="display:flex; gap:18px; justify-content:center; flex-wrap:wrap;">
        <div style="width:320px; background:#071018; padding:18px; border-radius:10px; text-align:left;">
          <div style="font-size:26px;">📊</div>
          <h4 style="margin:8px 0 6px 0; color:#e6eef8;">Data-Driven Analysis</h4>
          <div style="color:#9ca3af; font-size:13px;">Study & sleep pattern analysis, attendance impact, and performance tracking.</div>
        </div>
        <div style="width:320px; background:#071018; padding:18px; border-radius:10px; text-align:left;">
          <div style="font-size:26px;">🤖</div>
          <h4 style="margin:8px 0 6px 0; color:#e6eef8;">AI & ML Models</h4>
          <div style="color:#9ca3af; font-size:13px;">Regression for prediction, K-Means for segmentation, and risk classification.</div>
        </div>
        <div style="width:320px; background:#071018; padding:18px; border-radius:10px; text-align:left;">
          <div style="font-size:26px;">⚡</div>
          <h4 style="margin:8px 0 6px 0; color:#e6eef8;">Smart Recommendations</h4>
          <div style="color:#9ca3af; font-size:13px;">Personalized study tips, downloadable reports, and tailored advice.</div>
        </div>
      </div>
    </div>
    """

def _brand_card():
    return """
    <div style="margin-top:22px; padding:22px; background:linear-gradient(90deg, rgba(7,11,18,0.85), rgba(14,20,28,0.75)); border-radius:12px; display:flex; align-items:center; gap:18px; flex-wrap:wrap;">
      <div style="flex:1; min-width:280px;">
        <div style="display:inline-block; background:linear-gradient(90deg,#06b6d4,#3b82f6); color:white; padding:8px 12px; border-radius:12px; font-weight:700;">AI-Powered Academic Analytics</div>
        <h2 style="color:#fff; margin-top:12px;">StudyTrack</h2>
        <p style="color:#9ca3af; max-width:700px;">AI-based student study habit recommender — analyze habits, forecast outcomes, and deliver tailored recommendations to keep learners on track.</p>
        <div style="margin-top:12px;">
          <a href="#" style="background:linear-gradient(90deg,#06b6d4,#3b82f6); color:white; padding:10px 14px; border-radius:8px; text-decoration:none; margin-right:8px;">Get Started</a>
          <a href="#" style="background:#0b1220; color:#9ca3af; padding:10px 14px; border-radius:8px; text-decoration:none;">View sample report</a>
        </div>
      </div>
      <div style="width:220px; min-width:180px; text-align:center;">
        <div style="background:#08121a; border-radius:10px; padding:14px;">
          <div style="font-weight:800; color:#06b6d4; font-size:28px;">95%</div>
          <div style="color:#9ca3af; font-size:13px;">Forecast accuracy</div>
          <hr style="opacity:0.06; margin:12px 0;">
          <div style="font-weight:700; color:#7dd3fc; font-size:20px;">10K+</div>
          <div style="color:#9ca3af; font-size:13px;">Students</div>
        </div>
      </div>
    </div>
    """

def _what_you_get():
    return """
    <div style="margin-top:18px;">
      <h3 style="text-align:center; color:#e6eef8;">What you get</h3>
      <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin-top:10px;">
        <div style="width:300px; background:#071018; padding:16px; border-radius:10px; text-align:left;">
          <div style="font-size:22px;">📊</div>
          <h4 style="margin:8px 0 6px 0; color:#e6eef8;">Data-driven insights</h4>
          <div style="color:#9ca3af; font-size:13px;">Track study hours, sleep, attendance and outcomes.</div>
        </div>
        <div style="width:300px; background:#071018; padding:16px; border-radius:10px; text-align:left;">
          <div style="font-size:22px;">🔮</div>
          <h4 style="margin:8px 0 6px 0; color:#e6eef8;">ML-powered predictions</h4>
          <div style="color:#9ca3af; font-size:13px;">Regression, clustering and risk identification.</div>
        </div>
        <div style="width:300px; background:#071018; padding:16px; border-radius:10px; text-align:left;">
          <div style="font-size:22px;">⚡</div>
          <h4 style="margin:8px 0 6px 0; color:#e6eef8;">Actionable steps</h4>
          <div style="color:#9ca3af; font-size:13px;">Personalized recommendations and reports.</div>
        </div>
      </div>
    </div>
    """

def show_homepage():
    st.markdown(_hero_section(), unsafe_allow_html=True)
    st.markdown(_workflow_section(), unsafe_allow_html=True)
    st.markdown(_features_section(), unsafe_allow_html=True)
    st.markdown(_brand_card(), unsafe_allow_html=True)
    st.markdown(_what_you_get(), unsafe_allow_html=True)
    st.markdown("<hr style='opacity:0.06'>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_homepage()
