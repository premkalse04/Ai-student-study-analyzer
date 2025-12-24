import streamlit as st

def show_homepage():
    # Hero section
    st.markdown(
        """
        <div class="hero">
          <div class="hero-grid">
            <div class="hero-text">
              <div class="pill pill-glow">AI Study Habit Recommender</div>
              <h1>Study smarter with <span class="gradient-text">StudyTrack</span></h1>
              <p class="hero-subtitle">Outcome-focused analytics for educators and learners</p>
              <p class="hero-desc">
                Analyze study behaviors, predict performance, and deliver
                tailored actions that keep every learner on track — powered by
                machine learning insights.
              </p>
              <div class="hero-actions">
                <a class="btn primary">📊 Start analyzing</a>
                <a class="btn ghost">📄 View sample report</a>
              </div>
              <div class="hero-microcopy">
                Secure by design • Works with spreadsheets • Built for educators
              </div>
            </div>
            <div class="hero-card">
              <div class="card-title">Live snapshot</div>
              <div class="stat-row">
                <div>
                  <div class="stat-label">Forecast accuracy</div>
                  <div class="stat-value">95%</div>
                </div>
                <div>
                  <div class="stat-label">Students profiled</div>
                  <div class="stat-value">10K+</div>
                </div>
              </div>
              <div class="divider"></div>
              <div class="stacked">
                <div class="stacked-item">
                  <span class="dot green"></span>
                  Early-risk detection active
                </div>
                <div class="stacked-item">
                  <span class="dot blue"></span>
                  Personalized recommendations ready
                </div>
                <div class="stacked-item">
                  <span class="dot purple"></span>
                  Clustering calibrated (K=3)
                </div>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Metrics row
    m1, m2, m3 = st.columns(3)
    m1.metric("On-time completion", "93%", "↑ 4%")
    m2.metric("Students supported", "10,482", "↑ 612")
    m3.metric("Recommendation CTR", "47%", "↑ 6%")

    st.markdown("<div class='section-heading'>What you get</div>", unsafe_allow_html=True)

    # Features grid
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown(
            """
            <div class="card feature">
              <div class="icon-badge">📊</div>
              <h3>Data-driven insights</h3>
              <p>Track study hours, sleep, attendance, and outcomes in one place.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f2:
        st.markdown(
            """
            <div class="card feature">
              <div class="icon-badge">🤖</div>
              <h3>ML-powered predictions</h3>
              <p>Blend regression, clustering, and risk models to forecast performance.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with f3:
        st.markdown(
            """
            <div class="card feature">
              <div class="icon-badge">⚡</div>
              <h3>Actionable next steps</h3>
              <p>Serve personalized recommendations and downloadable reports instantly.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Secondary row
    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown(
            """
            <div class="card mini">
              <h4>Performance prediction</h4>
              <p>Forecast grade trajectories early to intervene faster.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with g2:
        st.markdown(
            """
            <div class="card mini">
              <h4>Student segmentation</h4>
              <p>Cluster learners to tailor feedback and support at scale.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with g3:
        st.markdown(
            """
            <div class="card mini">
              <h4>Real-time dashboards</h4>
              <p>Monitor engagement and outcomes as data arrives.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Workflow
    st.markdown("<div class='section-heading'>Workflow</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="timeline">
          <div class="step"><span>1</span> Upload data</div>
          <div class="step"><span>2</span> Clean & preprocess</div>
          <div class="step"><span>3</span> Model & cluster</div>
          <div class="step"><span>4</span> Generate insights</div>
          <div class="step"><span>5</span> Share reports</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="cta-panel">
          <div>
            <div class="pill muted">Ready to explore?</div>
            <h3>Run your first analysis in minutes.</h3>
            <p>Upload an Excel file or enter data manually to see instant recommendations.</p>
          </div>
          <div class="cta-actions">
            <a class="btn primary">📁 Upload Excel</a>
            <a class="btn ghost">✍️ Manual entry</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("Final Year Project · StudyTrack AI Study Habit Recommender")
