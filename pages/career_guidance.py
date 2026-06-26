"""
Career Guidance Page - ResumeIQ
Shows personalized learning path, missing skills, and career enhancement tips.
"""

import streamlit as st
import plotly.graph_objects as go
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.skill_extractor import generate_learning_path, get_skill_details, get_skill_categories


CATEGORY_ICONS = {
    "Programming": "💻",
    "Database": "🗄️",
    "Data Science": "📊",
    "Data Engineering": "⚙️",
    "AI/ML": "🤖",
    "Web Development": "🌐",
    "DevOps": "🔧",
    "Cloud": "☁️",
    "Security": "🔐",
    "Data Visualization": "📈",
    "Architecture": "🏗️",
    "Methodology": "📋",
    "Tools": "🛠️",
    "Design": "🎨",
    "Emerging Tech": "🚀",
    "System": "🖥️",
    "Productivity": "📂",
    "General": "📌",
}


def show():
    st.markdown('<h1 class="page-title">Career Guidance</h1>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Your personalized roadmap to close skill gaps and accelerate your career</p>', unsafe_allow_html=True)

    st.markdown("---")

    if "analysis_results" not in st.session_state:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size:3rem">🗺️</div>
            <h3 style="color:#e2e8f0;margin:1rem 0 0.5rem">No Analysis Yet</h3>
            <p style="color:#94a3b8">Run a resume analysis first to get your personalized career guidance.</p>
        </div>
        """, unsafe_allow_html=True)
        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            if st.button("🔍 Go to Resume Analyzer", use_container_width=True, type="primary"):
                st.session_state.page = "Resume Analyzer"
                st.rerun()
        return

    results = st.session_state["analysis_results"]
    gap = results["gap_analysis"]
    match_pct = results["match_pct"]
    match_info = results["match_info"]
    missing_skills = gap["missing"]
    matching_skills = gap["matching"]

    # Summary banner
    st.markdown(f"""
    <div class="guidance-banner" style="border-left: 4px solid {match_info['color']}">
        <div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap">
            <span style="font-size:2rem">{match_info['emoji']}</span>
            <div>
                <strong style="color:#e2e8f0;font-size:1.1rem">{match_info['level']} — {match_pct}%</strong>
                <p style="color:#94a3b8;margin:0.2rem 0 0;font-size:0.9rem">{match_info['description']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ─── STRENGTHS ───────────────────────────────────────────────────
    if matching_skills:
        st.markdown('<h2 class="section-title">💪 Your Strengths</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#94a3b8;margin-bottom:0.75rem">These skills from your resume match what the employer is looking for:</p>', unsafe_allow_html=True)
        strength_cats = get_skill_categories(matching_skills)
        for category, skills in strength_cats.items():
            icon = CATEGORY_ICONS.get(category, "📌")
            skills_html = "".join([f'<span class="skill-tag skill-match">{s}</span>' for s in skills])
            st.markdown(f"""
            <div class="cat-section">
                <div class="cat-title">{icon} {category}</div>
                <div>{skills_html}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

    # ─── LEARNING ROADMAP ────────────────────────────────────────────
    if missing_skills:
        st.markdown('<h2 class="section-title">🗺️ Your Learning Roadmap</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#94a3b8;margin-bottom:1rem">Skills sorted by priority — start from the top for maximum impact:</p>', unsafe_allow_html=True)

        learning_path = generate_learning_path(missing_skills)

        # Group by category
        by_category = {}
        for item in learning_path:
            cat = item["category"]
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(item)

        step_num = 1
        for category, items in by_category.items():
            icon = CATEGORY_ICONS.get(category, "📌")

            st.markdown(f"""
            <div class="roadmap-category">
                <div class="roadmap-cat-header">{icon} {category}</div>
            </div>
            """, unsafe_allow_html=True)

            for item in items:
                resource_html = ""
                if item["resource"]:
                    resource_html = f'<a href="{item["resource"]}" target="_blank" class="learn-link">📖 Learn {item["skill"]}</a>'

                st.markdown(f"""
                <div class="roadmap-step">
                    <div class="step-badge">{step_num}</div>
                    <div class="step-content">
                        <strong style="color:#e2e8f0">{item["skill"]}</strong>
                        <span style="color:#64748b;font-size:0.82rem;margin-left:0.5rem">({category})</span>
                        <div style="margin-top:0.3rem">{resource_html}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                step_num += 1

        st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="success-box">
            🎉 <strong>Outstanding!</strong> Your resume covers all the required skills for this role. 
            Focus on highlighting your experience depth and preparing for technical interviews.
        </div>
        """, unsafe_allow_html=True)

    # ─── CAREER TIPS ─────────────────────────────────────────────────
    st.markdown('<h2 class="section-title">🎯 Career Enhancement Tips</h2>', unsafe_allow_html=True)

    general_tips = [
        ("📄", "Tailor Your Resume", "Customize your resume summary/objective for every application. Mirror the language and keywords from the job description to pass ATS filters."),
        ("🔗", "LinkedIn Optimization", "Ensure your LinkedIn profile matches your resume and includes all skills. Use the 'Skills' section and get endorsements from colleagues."),
        ("📁", "Build a Portfolio", "Create GitHub repos, Kaggle notebooks, or a personal website showcasing real projects that demonstrate the required skills."),
        ("🏆", "Certifications", "Consider getting certifications (AWS, Google Cloud, TensorFlow Developer, etc.) to formally validate skills you're learning."),
        ("🤝", "Network Actively", "Join communities, attend meetups, and connect with professionals in your target field. Many jobs are filled through referrals."),
        ("💬", "Practice Interviews", "Use platforms like LeetCode, HackerRank, and Pramp to practice technical and behavioral interviews before applying."),
    ]

    for icon, title, tip in general_tips:
        st.markdown(f"""
        <div class="tip-card">
            <span style="font-size:1.5rem">{icon}</span>
            <div style="margin-left:0.75rem">
                <strong style="color:#e2e8f0">{title}</strong>
                <p style="color:#94a3b8;font-size:0.88rem;margin:0.2rem 0 0">{tip}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ─── FUTURE ENHANCEMENTS ─────────────────────────────────────────
    st.markdown('<h2 class="section-title">🚀 What\'s Coming to ResumeIQ</h2>', unsafe_allow_html=True)
    future = [
        ("🤖", "AI Chat Career Coach", "Interactive AI assistant for personalized career advice"),
        ("📋", "ATS Compatibility Check", "Detailed ATS formatting and keyword analysis"),
        ("📑", "Multi-Resume Comparison", "Compare multiple resume versions side-by-side"),
        ("💼", "Job Recommendation Engine", "AI-powered job matching from live listings"),
        ("🔗", "LinkedIn Profile Analyzer", "Analyze and optimize your LinkedIn presence"),
        ("📐", "Resume Formatting Analysis", "Check structure, length, and visual hierarchy"),
    ]

    future_cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(future):
        with future_cols[i % 3]:
            st.markdown(f"""
            <div class="future-card">
                <span style="font-size:1.5rem">{icon}</span>
                <strong style="color:#7c3aed;display:block;margin:0.4rem 0 0.2rem">{title}</strong>
                <p style="color:#64748b;font-size:0.82rem;margin:0">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
