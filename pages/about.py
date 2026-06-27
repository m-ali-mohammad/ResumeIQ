"""
About Page - ResumeIQ
"""

import streamlit as st


def show():
    st.markdown('<h1 class="page-title">About ResumeIQ</h1>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Built to solve a real problem — resume-job mismatch</p>', unsafe_allow_html=True)

    # Problem Statement
    st.markdown("---")
    st.markdown('<h2 class="section-title">The Problem</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        <div class="about-text-card">
            <p>Every year, millions of qualified candidates get filtered out by Applicant Tracking Systems (ATS) 
            and recruiters — not because they're unqualified, but because their resume doesn't <em>speak the same language</em> 
            as the job description.</p>
            <p>Students and job seekers often submit resumes without understanding how well they match a specific 
            job description. This leads to lower shortlisting rates, wasted applications, and missed opportunities.</p>
            <p>Traditional resume review is slow, subjective, and expensive. ResumeIQ makes it instant, objective, and free.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="problem-stats">
            <div class="p-stat"><span class="p-num">75%</span><span class="p-label">of resumes are rejected by ATS before human review</span></div>
            <div class="p-stat"><span class="p-num">3s</span><span class="p-label">Average recruiter time spent reading a resume</span></div>
            <div class="p-stat"><span class="p-num">250+</span><span class="p-label">Applications per corporate job opening on average</span></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Objectives
    st.markdown('<h2 class="section-title">Project Objectives</h2>', unsafe_allow_html=True)

    objectives = [
        ("🎯", "Primary Objective", "Develop an AI-powered platform that evaluates resumes against job descriptions using NLP and machine learning techniques."),
        ("📊", "Match Score", "Calculate a precise resume-job match percentage using TF-IDF vectorization and Cosine Similarity algorithms."),
        ("🔍", "Skill Gap Analysis", "Identify matching skills and detect missing skills that recruiters are specifically looking for."),
        ("🗺️", "Career Guidance", "Provide actionable learning recommendations and prioritized career enhancement pathways."),
        ("📈", "Visual Analytics", "Deliver clear data visualizations to help candidates understand their positioning."),
    ]

    for icon, title, desc in objectives:
        st.markdown(f"""
        <div class="objective-item">
            <span class="obj-icon">{icon}</span>
            <div>
                <strong style="color:#e2e8f0">{title}</strong>
                <p style="color:#94a3b8;margin:0.2rem 0 0;font-size:0.9rem">{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Technology Stack
    st.markdown('<h2 class="section-title">Technology Stack</h2>', unsafe_allow_html=True)

    tech_cols = st.columns(3)
    tech_groups = [
        ("🐍 Core Backend", [
            ("Python 3.10+", "Primary programming language"),
            ("Streamlit", "Web application framework"),
            ("Pandas / NumPy", "Data manipulation & analysis"),
        ]),
        ("🤖 AI / NLP", [
            ("Scikit-learn", "TF-IDF Vectorization & Cosine Similarity"),
            ("PyPDF2", "PDF text extraction"),
            ("NLTK", "Natural Language Processing"),
        ]),
        ("📊 Visualization", [
            ("Plotly", "Interactive charts & graphs"),
            ("Streamlit Charts", "Native data visualizations"),
            ("Custom CSS", "Responsive UI design"),
        ]),
    ]

    for col, (group_title, items) in zip(tech_cols, tech_groups):
        with col:
            items_html = "".join([
                f'<div class="tech-item"><strong style="color:#e2e8f0">{name}</strong><br><small style="color:#64748b">{desc}</small></div>'
                for name, desc in items
            ])
            st.markdown(f"""
            <div class="tech-card">
                <h4 style="color:#7c3aed;margin:0 0 0.75rem">{group_title}</h4>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How the AI Works
    st.markdown('<h2 class="section-title">How the AI Works</h2>', unsafe_allow_html=True)

    ai_steps = [
        ("1", "Text Extraction", "PyPDF2 extracts raw text from the uploaded PDF resume, preserving all content across pages."),
        ("2", "Text Preprocessing", "Both texts are lowercased, cleaned of special characters, and normalized for consistent comparison."),
        ("3", "TF-IDF Vectorization", "Term Frequency-Inverse Document Frequency converts text into numerical vectors capturing word importance."),
        ("4", "Cosine Similarity", "The angle between the two vectors is computed — the closer to 1.0, the higher the match."),
        ("5", "Skill Extraction", "A curated database of 80+ tech skills is cross-referenced against both documents using regex matching."),
        ("6", "Gap Analysis & Recommendations", "Missing skills are identified, categorized, and sorted by learning priority with resource links."),
    ]

    for step, title, desc in ai_steps:
        st.markdown(f"""
        <div class="ai-step">
            <div class="ai-step-num">{step}</div>
            <div>
                <strong style="color:#e2e8f0">{title}</strong>
                <p style="color:#94a3b8;margin:0.1rem 0 0;font-size:0.88rem">{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Project Info
    st.markdown('<h2 class="section-title">Project Information</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
            <table class="info-table">
                <tr><td class="info-key">Project Title</td><td class="info-val">ResumeIQ</td></tr>
                <tr><td class="info-key">Domain</td><td class="info-val">Artificial Intelligence (AI)</td></tr>
                <tr><td class="info-key">Project Type</td><td class="info-val">Web Application</td></tr>
                <tr><td class="info-key">Framework</td><td class="info-val">Streamlit</td></tr>
                <tr><td class="info-key">Version</td><td class="info-val">1.0.0</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="info-card">
            <table class="info-table">
                <tr><td class="info-key">Language</td><td class="info-val">Python 3.10+</td></tr>
                <tr><td class="info-key">Deployment</td><td class="info-val">Streamlit Community Cloud</td></tr>
                <tr><td class="info-key">License</td><td class="info-val">MIT</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
