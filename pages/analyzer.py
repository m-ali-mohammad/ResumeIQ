"""
Resume Analyzer Page - ResumeIQ
Core AI analysis page with PDF upload, JD input, and results dashboard.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills, analyze_skill_gaps, get_skill_categories
from utils.similarity import calculate_similarity, get_match_percentage, get_match_level, keyword_overlap_analysis


def render_gauge(percentage: int, color: str) -> go.Figure:
    """Render a gauge chart for match percentage."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        number={"suffix": "%", "font": {"size": 48, "color": "#e2e8f0"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#475569", "tickfont": {"color": "#94a3b8"}},
            "bar": {"color": color, "thickness": 0.3},
            "bgcolor": "#1e293b",
            "bordercolor": "#334155",
            "steps": [
                {"range": [0, 40], "color": "#1e1b2e"},
                {"range": [40, 60], "color": "#1e2a1b"},
                {"range": [60, 80], "color": "#1b2233"},
                {"range": [80, 100], "color": "#1b2a1b"},
            ],
            "threshold": {
                "line": {"color": color, "width": 4},
                "thickness": 0.8,
                "value": percentage
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font={"color": "#e2e8f0"},
        margin=dict(l=20, r=20, t=30, b=20),
        height=280,
    )
    return fig


def render_skills_bar(categories_data: dict, color: str, title: str) -> go.Figure:
    """Render a horizontal bar chart of skills by category."""
    if not categories_data:
        return None

    labels = list(categories_data.keys())
    values = [len(v) for v in categories_data.values()]

    fig = go.Figure(go.Bar(
        x=values,
        y=labels,
        orientation='h',
        marker_color=color,
        marker_line_color='rgba(0,0,0,0)',
        text=values,
        textposition='outside',
        textfont={"color": "#e2e8f0"}
    ))
    fig.update_layout(
        title={"text": title, "font": {"color": "#e2e8f0", "size": 14}},
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font={"color": "#94a3b8"},
        xaxis={"gridcolor": "#334155", "color": "#94a3b8"},
        yaxis={"gridcolor": "#334155", "color": "#94a3b8"},
        margin=dict(l=10, r=40, t=40, b=10),
        height=250,
    )
    return fig


def render_donut(matching: int, missing: int) -> go.Figure:
    """Render a donut chart showing matched vs missing skills."""
    labels = ["Matching Skills", "Missing Skills"]
    values = [matching, missing]
    colors = ["#22c55e", "#ef4444"]

    fig = go.Figure(go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        marker_colors=colors,
        textinfo="label+percent",
        textfont={"color": "#e2e8f0", "size": 12},
        hovertemplate="%{label}: %{value}<extra></extra>"
    ))
    fig.update_layout(
        paper_bgcolor="#1e293b",
        plot_bgcolor="#1e293b",
        font={"color": "#e2e8f0"},
        legend={"font": {"color": "#94a3b8"}},
        margin=dict(l=10, r=10, t=30, b=10),
        height=250,
    )
    return fig


def show():
    st.markdown('<h1 class="page-title">Resume Analyzer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Upload your resume and paste a job description to get your AI-powered match analysis</p>', unsafe_allow_html=True)

    st.markdown("---")

    # ─── INPUT SECTION ───────────────────────────────────────────────
    col_left, col_right = st.columns(2, gap="large")

    with col_left:
        st.markdown('<h3 class="input-label">📄 Upload Your Resume (PDF)</h3>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            label="Drop your PDF resume here",
            type=["pdf"],
            help="Only PDF format is supported",
            label_visibility="collapsed"
        )
        if uploaded_file:
            st.markdown(f"""
            <div class="file-success">
                ✅ <strong>{uploaded_file.name}</strong> uploaded successfully
                <span style="color:#64748b;font-size:0.8rem;margin-left:0.5rem">({round(uploaded_file.size/1024, 1)} KB)</span>
            </div>
            """, unsafe_allow_html=True)

    with col_right:
        st.markdown('<h3 class="input-label">💼 Paste Job Description</h3>', unsafe_allow_html=True)
        jd_text = st.text_area(
            label="Job Description",
            placeholder="Paste the full job description here...\n\nExample:\nWe are looking for a Python developer with experience in Machine Learning, SQL, Docker, AWS...",
            height=160,
            label_visibility="collapsed"
        )
        if jd_text:
            word_count = len(jd_text.split())
            st.markdown(f'<span style="color:#64748b;font-size:0.8rem">{word_count} words entered</span>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ─── ANALYZE BUTTON ──────────────────────────────────────────────
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        analyze_clicked = st.button(
            "🔍 Analyze Resume",
            use_container_width=True,
            type="primary",
            disabled=(not uploaded_file or not jd_text)
        )

    if not uploaded_file or not jd_text:
        st.markdown("""
        <div class="hint-box">
            💡 Please upload a PDF resume and paste a job description to enable analysis.
        </div>
        """, unsafe_allow_html=True)

    # ─── ANALYSIS ────────────────────────────────────────────────────
    if analyze_clicked and uploaded_file and jd_text:
        with st.spinner("🧠 Analyzing your resume with AI..."):
            # Extract text
            resume_text = extract_text_from_pdf(uploaded_file)

            if not resume_text or len(resume_text.strip()) < 50:
                st.error("⚠️ Could not extract sufficient text from the PDF. Please ensure your PDF contains selectable text (not a scanned image).")
                return

            # Calculate similarity
            similarity = calculate_similarity(resume_text, jd_text)
            match_pct = get_match_percentage(similarity)
            match_info = get_match_level(match_pct)

            # Extract skills
            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(jd_text)
            gap_analysis = analyze_skill_gaps(resume_skills, jd_skills)
            keyword_stats = keyword_overlap_analysis(resume_text, jd_text)

            # Store in session state
            st.session_state["analysis_results"] = {
                "match_pct": match_pct,
                "match_info": match_info,
                "resume_skills": resume_skills,
                "jd_skills": jd_skills,
                "gap_analysis": gap_analysis,
                "keyword_stats": keyword_stats,
                "resume_text": resume_text,
            }

        # ─── RESULTS ─────────────────────────────────────────────────
        results = st.session_state["analysis_results"]
        match_pct = results["match_pct"]
        match_info = results["match_info"]
        gap = results["gap_analysis"]
        kw = results["keyword_stats"]

        st.markdown("---")
        st.markdown('<h2 class="section-title">📊 Analysis Results</h2>', unsafe_allow_html=True)

        # ─── MATCH SCORE + OVERVIEW CARDS ────────────────────────────
        score_col, cards_col = st.columns([1, 2], gap="large")

        with score_col:
            fig = render_gauge(match_pct, match_info["color"])
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
            st.markdown(f"""
            <div class="match-badge badge-{match_info['badge']}">
                {match_info['emoji']} {match_info['level']}
            </div>
            <p style="text-align:center;color:#94a3b8;font-size:0.85rem;margin-top:0.5rem">
                {match_info['description']}
            </p>
            """, unsafe_allow_html=True)

        with cards_col:
            st.markdown("<br>", unsafe_allow_html=True)
            m1, m2 = st.columns(2)
            m3, m4 = st.columns(2)

            metrics = [
                (m1, "✅ Matching Skills", str(gap["match_count"]), "#22c55e"),
                (m2, "❌ Missing Skills", str(gap["missing_count"]), "#ef4444"),
                (m3, "📄 Resume Skills", str(len(results["resume_skills"])), "#3b82f6"),
                (m4, "💼 JD Skills Required", str(len(results["jd_skills"])), "#f59e0b"),
            ]

            for col, label, value, color in metrics:
                with col:
                    st.markdown(f"""
                    <div class="metric-card" style="border-left:3px solid {color}">
                        <div class="metric-label">{label}</div>
                        <div class="metric-value" style="color:{color}">{value}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="keyword-stats">
                <span>🔤 Keyword Coverage: <strong style="color:#7c3aed">{kw['coverage_rate']}%</strong></span>
                <span style="margin-left:1.5rem">📝 Resume Words: <strong>{kw['resume_unique_words']}</strong></span>
                <span style="margin-left:1.5rem">📋 JD Words: <strong>{kw['jd_unique_words']}</strong></span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ─── SKILL CHARTS ────────────────────────────────────────────
        if results["jd_skills"]:
            chart1, chart2 = st.columns(2)

            with chart1:
                donut = render_donut(gap["match_count"], gap["missing_count"])
                if donut:
                    st.plotly_chart(donut, use_container_width=True, config={"displayModeBar": False})

            with chart2:
                resume_cats = get_skill_categories(results["resume_skills"])
                if resume_cats:
                    bar = render_skills_bar(resume_cats, "#3b82f6", "Your Skills by Category")
                    if bar:
                        st.plotly_chart(bar, use_container_width=True, config={"displayModeBar": False})

        st.markdown("<br>", unsafe_allow_html=True)

        # ─── SKILLS BREAKDOWN ────────────────────────────────────────
        sk_col1, sk_col2, sk_col3 = st.columns(3)

        with sk_col1:
            st.markdown('<h4 class="skills-header match-header">✅ Matching Skills</h4>', unsafe_allow_html=True)
            if gap["matching"]:
                for skill in gap["matching"]:
                    st.markdown(f'<span class="skill-tag skill-match">{skill}</span>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="no-skills">No matching skills found</p>', unsafe_allow_html=True)

        with sk_col2:
            st.markdown('<h4 class="skills-header missing-header">❌ Missing Skills</h4>', unsafe_allow_html=True)
            if gap["missing"]:
                for skill in gap["missing"]:
                    st.markdown(f'<span class="skill-tag skill-missing">{skill}</span>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:#22c55e;font-style:italic">No missing skills — great job!</p>', unsafe_allow_html=True)

        with sk_col3:
            st.markdown('<h4 class="skills-header extra-header">➕ Additional Skills</h4>', unsafe_allow_html=True)
            if gap["extra"]:
                for skill in gap["extra"][:12]:
                    st.markdown(f'<span class="skill-tag skill-extra">{skill}</span>', unsafe_allow_html=True)
                if len(gap["extra"]) > 12:
                    st.markdown(f'<p style="color:#64748b;font-size:0.8rem">+{len(gap["extra"])-12} more</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="no-skills">None identified</p>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ─── QUICK TIPS ──────────────────────────────────────────────
        st.markdown('<h3 class="section-title">💡 Quick Improvement Tips</h3>', unsafe_allow_html=True)

        tips = []
        if match_pct < 60:
            tips.append("🔴 Your match score is below 60%. Focus on adding the missing skills to your resume or resume summary section.")
        if gap["missing_count"] > 3:
            tips.append(f"📚 You're missing {gap['missing_count']} required skills. Visit the **Career Guidance** page for a learning roadmap.")
        if gap["match_count"] > 0:
            tips.append(f"✅ You already match {gap['match_count']} required skills — make sure they're clearly visible in your resume.")
        if kw["coverage_rate"] < 50:
            tips.append("🔤 Low keyword coverage detected. Mirror more of the JD's language in your resume to pass ATS filters.")
        tips.append("📝 Tailor your resume summary/objective section to echo the JD's requirements directly.")
        tips.append("🎯 Use the Career Guidance page for a full personalized learning roadmap with resources.")

        for tip in tips:
            st.markdown(f'<div class="tip-item">{tip}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            if st.button("🗺️ View Full Career Guidance →", use_container_width=True, type="secondary"):
                st.session_state.page = "Career Guidance"
                st.rerun()

    # Show previous results if they exist
    elif "analysis_results" in st.session_state and not analyze_clicked:
        st.markdown("""
        <div class="hint-box">
            📋 Previous analysis results are stored. Upload a new file or paste a new JD and click <strong>Analyze Resume</strong> to refresh.
        </div>
        """, unsafe_allow_html=True)
