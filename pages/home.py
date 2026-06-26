"""
Home Page - ResumeIQ
"""

import streamlit as st


def show():
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">🤖 AI-Powered Career Tool</div>
        <h1 class="hero-title">Land Your Dream Job<br><span class="hero-accent">Faster with AI</span></h1>
        <p class="hero-subtitle">
            ResumeIQ analyzes your resume against any job description using advanced NLP, 
            identifies skill gaps, and gives you a personalized roadmap to get hired.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("98%", "Accuracy Rate"),
        ("<5s", "Analysis Time"),
        ("80+", "Skills Tracked"),
        ("Free", "Always Free"),
    ]
    for col, (val, label) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-value">{val}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # CTA Button
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("🚀 Analyze My Resume Now", use_container_width=True, type="primary"):
            st.session_state.page = "Resume Analyzer"
            st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # How it works
    st.markdown('<h2 class="section-title">How It Works</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Three simple steps to career clarity</p>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    steps = [
        ("1", "📄", "Upload Resume", "Upload your PDF resume and paste the target job description into the analyzer."),
        ("2", "🧠", "AI Analysis", "Our NLP engine extracts skills, computes TF-IDF vectors, and calculates your match score."),
        ("3", "🎯", "Get Insights", "Receive your match percentage, skill gaps, and a personalized learning roadmap."),
    ]
    for col, (num, icon, title, desc) in zip([c1, c2, c3], steps):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <div class="feature-step">Step {num}</div>
                <h3 class="feature-title">{title}</h3>
                <p class="feature-desc">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Features
    st.markdown('<h2 class="section-title">Key Features</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Everything you need to optimize your job search</p>', unsafe_allow_html=True)

    features = [
        ("📊", "Match Score Dashboard", "Get an instant percentage match between your resume and any job description using cosine similarity."),
        ("🔍", "Skill Gap Analysis", "See exactly which skills the employer wants that your resume is missing — no guessing."),
        ("🗺️", "Learning Roadmap", "Get a prioritized, category-sorted list of resources to close your skill gaps fast."),
        ("📈", "Visual Analytics", "Interactive charts show your skill coverage, category distribution, and more."),
        ("💡", "Career Recommendations", "AI-powered tips tailored to your specific profile and target role."),
        ("⚡ Fast", "5-Second Analysis", "Advanced NLP processes your documents in under 5 seconds."),
    ]

    r1c1, r1c2, r1c3 = st.columns(3)
    r2c1, r2c2, r2c3 = st.columns(3)
    cols = [r1c1, r1c2, r1c3, r2c1, r2c2, r2c3]

    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="mini-card">
                <span class="mini-icon">{icon}</span>
                <strong>{title}</strong>
                <p style="font-size:0.82rem;color:#94a3b8;margin:0.3rem 0 0">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Supported job boards
    st.markdown('<h2 class="section-title">Works With Any Job Board</h2>', unsafe_allow_html=True)
    boards = ["LinkedIn", "Indeed", "Naukri", "Glassdoor", "Monster", "AngelList", "Company Careers Pages"]
    board_html = " ".join([f'<span class="board-tag">{b}</span>' for b in boards])
    st.markdown(f'<div class="board-row">{board_html}</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Footer CTA
    st.markdown("""
    <div class="cta-banner">
        <h3>Ready to stand out from the crowd?</h3>
        <p>Join thousands of job seekers who've improved their resume match rates with ResumeIQ.</p>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if st.button("✨ Start Free Analysis", use_container_width=True, type="primary", key="cta2"):
            st.session_state.page = "Resume Analyzer"
            st.rerun()
