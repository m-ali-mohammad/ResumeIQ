"""
ResumeIQ — AI-Powered Resume Analyzer and Career Enhancement Assistant
Main Application Entry Point

Domain: Artificial Intelligence (AI)
Academy: SITER Academy, Norge — Summer Internship 2026
"""

import streamlit as st
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Page imports
from pages import home, about, analyzer, career_guidance, contact

# ─── PAGE CONFIGURATION ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResumeIQ — AI Resume Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/resumeiq",
        "Report a bug": "https://github.com/resumeiq/issues",
        "About": "ResumeIQ — AI-Powered Resume Analyzer | SITER Academy 2026"
    }
)

# ─── GLOBAL CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Import Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

/* ── Root Variables ── */
:root {
    --bg-deep:    #0f172a;
    --bg-card:    #1e293b;
    --bg-hover:   #273549;
    --border:     #334155;
    --purple:     #7c3aed;
    --purple-lt:  #a78bfa;
    --blue:       #3b82f6;
    --green:      #22c55e;
    --red:        #ef4444;
    --amber:      #f59e0b;
    --text-1:     #e2e8f0;
    --text-2:     #94a3b8;
    --text-3:     #64748b;
}

/* ── Base Reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, sans-serif;
    background-color: var(--bg-deep);
    color: var(--text-1);
}

/* ── Hide Streamlit Branding ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2rem 3rem; max-width: 1200px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #111827 !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] .stMarkdown p { color: var(--text-2); }

/* ── Sidebar Logo ── */
.sidebar-logo {
    text-align: center;
    padding: 1.25rem 0.5rem 0.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.5rem;
}
.sidebar-logo-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7c3aed, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.sidebar-tagline {
    color: var(--text-3);
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.2rem;
}

/* ── Navigation Radio ── */
div[data-testid="stRadio"] label {
    color: var(--text-2) !important;
    font-size: 0.95rem;
    padding: 0.5rem 0.75rem;
    border-radius: 8px;
    transition: all 0.2s;
    cursor: pointer;
    display: block;
    margin: 2px 0;
}
div[data-testid="stRadio"] label:hover { background: var(--bg-hover); color: var(--text-1) !important; }
div[data-testid="stRadio"] [aria-checked="true"] + label,
div[data-testid="stRadio"] input:checked + label {
    background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(59,130,246,0.15));
    color: var(--purple-lt) !important;
    border-left: 3px solid var(--purple);
}

/* ── Buttons ── */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 1.5rem !important;
    transition: all 0.25s ease !important;
    border: none !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed, #3b82f6) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(124,58,237,0.35) !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(124,58,237,0.5) !important;
}
.stButton > button[kind="secondary"] {
    background: var(--bg-card) !important;
    color: var(--purple-lt) !important;
    border: 1px solid var(--purple) !important;
}
.stButton > button[kind="secondary"]:hover {
    background: rgba(124,58,237,0.15) !important;
}
.stButton > button:disabled {
    opacity: 0.5 !important;
    cursor: not-allowed !important;
    transform: none !important;
}

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea, .stSelectbox select {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-1) !important;
    font-size: 0.92rem !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--purple) !important;
    box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label { color: var(--text-2) !important; }

/* ── File Uploader ── */
[data-testid="stFileUploader"] {
    background: var(--bg-card) !important;
    border: 2px dashed var(--border) !important;
    border-radius: 12px !important;
    transition: all 0.25s !important;
}
[data-testid="stFileUploader"]:hover { border-color: var(--purple) !important; }

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border-radius: 8px !important;
    color: var(--text-1) !important;
    border: 1px solid var(--border) !important;
}
.streamlit-expanderContent { background: var(--bg-card) !important; border: 1px solid var(--border) !important; }

/* ── ═══════════ CUSTOM COMPONENTS ═══════════ ── */

/* Hero */
.hero-section {
    text-align: center;
    padding: 3.5rem 1rem 2.5rem;
}
.hero-badge {
    display: inline-block;
    background: rgba(124,58,237,0.15);
    border: 1px solid rgba(124,58,237,0.4);
    color: var(--purple-lt);
    padding: 0.35rem 1rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    margin-bottom: 1.25rem;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    color: var(--text-1);
    line-height: 1.2;
    margin: 0 0 1rem;
}
.hero-accent {
    background: linear-gradient(135deg, #7c3aed, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-subtitle {
    color: var(--text-2);
    font-size: 1.1rem;
    max-width: 620px;
    margin: 0 auto 2rem;
    line-height: 1.7;
}

/* Stat Cards */
.stat-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1rem;
    text-align: center;
    transition: transform 0.2s;
}
.stat-card:hover { transform: translateY(-3px); }
.stat-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7c3aed, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-label { color: var(--text-3); font-size: 0.82rem; margin-top: 0.25rem; }

/* Feature Cards */
.feature-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.75rem 1.25rem;
    text-align: center;
    height: 100%;
    transition: all 0.25s;
}
.feature-card:hover { border-color: var(--purple); transform: translateY(-3px); }
.feature-icon { font-size: 2.2rem; margin-bottom: 0.75rem; }
.feature-step {
    color: var(--purple-lt);
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
}
.feature-title { color: var(--text-1); font-size: 1.05rem; font-weight: 600; margin: 0 0 0.5rem; }
.feature-desc { color: var(--text-2); font-size: 0.88rem; line-height: 1.6; margin: 0; }

/* Mini Cards */
.mini-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 0.75rem;
    transition: all 0.2s;
}
.mini-card:hover { border-color: var(--purple); }
.mini-icon { font-size: 1.2rem; margin-right: 0.4rem; }

/* Board Tags */
.board-row { text-align: center; margin: 1rem 0; }
.board-tag {
    display: inline-block;
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-2);
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    font-size: 0.85rem;
    margin: 0.25rem;
    transition: all 0.2s;
}
.board-tag:hover { border-color: var(--purple); color: var(--purple-lt); }

/* CTA Banner */
.cta-banner {
    background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(59,130,246,0.1));
    border: 1px solid rgba(124,58,237,0.3);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin: 1rem 0;
}
.cta-banner h3 { color: var(--text-1); font-size: 1.4rem; margin: 0 0 0.5rem; }
.cta-banner p { color: var(--text-2); margin: 0; }

/* Page Titles */
.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--text-1);
    margin: 0 0 0.4rem;
}
.page-subtitle { color: var(--text-2); font-size: 1rem; margin: 0 0 1.5rem; }
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--text-1);
    margin: 0 0 0.3rem;
}
.section-sub { color: var(--text-3); font-size: 0.9rem; margin: 0 0 1.25rem; }

/* Input Labels */
.input-label { color: var(--text-1); font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; }

/* File Success */
.file-success {
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.3);
    color: #86efac;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    font-size: 0.88rem;
    margin-top: 0.5rem;
}

/* Hint Box */
.hint-box {
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.25);
    color: var(--text-2);
    padding: 0.85rem 1.1rem;
    border-radius: 10px;
    font-size: 0.9rem;
    margin: 0.75rem 0;
}

/* Match Badges */
.match-badge {
    text-align: center;
    padding: 0.55rem 1rem;
    border-radius: 999px;
    font-weight: 700;
    font-size: 1rem;
    margin: 0 auto;
    width: fit-content;
}
.badge-excellent { background: rgba(34,197,94,0.15); color: #86efac; border: 1px solid rgba(34,197,94,0.4); }
.badge-good      { background: rgba(59,130,246,0.15); color: #93c5fd; border: 1px solid rgba(59,130,246,0.4); }
.badge-moderate  { background: rgba(245,158,11,0.15); color: #fcd34d; border: 1px solid rgba(245,158,11,0.4); }
.badge-low       { background: rgba(239,68,68,0.15);  color: #fca5a5; border: 1px solid rgba(239,68,68,0.4); }

/* Metric Cards */
.metric-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.75rem;
}
.metric-label { color: var(--text-3); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; }
.metric-value { font-family: 'Space Grotesk', sans-serif; font-size: 1.75rem; font-weight: 700; margin-top: 0.2rem; }

/* Keyword Stats Bar */
.keyword-stats {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    font-size: 0.88rem;
    color: var(--text-2);
    margin-top: 0.25rem;
}

/* Skill Tags */
.skill-tag {
    display: inline-block;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 500;
    margin: 0.2rem 0.15rem;
}
.skill-match   { background: rgba(34,197,94,0.12);  color: #86efac; border: 1px solid rgba(34,197,94,0.3); }
.skill-missing { background: rgba(239,68,68,0.12);  color: #fca5a5; border: 1px solid rgba(239,68,68,0.3); }
.skill-extra   { background: rgba(59,130,246,0.12); color: #93c5fd; border: 1px solid rgba(59,130,246,0.3); }

.skills-header { color: var(--text-1); font-size: 0.95rem; font-weight: 600; margin: 0 0 0.75rem; }
.match-header   { color: #86efac; }
.missing-header { color: #fca5a5; }
.extra-header   { color: #93c5fd; }
.no-skills { color: var(--text-3); font-style: italic; font-size: 0.88rem; }

/* Tip Item */
.tip-item {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--purple);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    color: var(--text-2);
    font-size: 0.9rem;
    margin-bottom: 0.6rem;
}

/* About Page */
.about-text-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    color: var(--text-2);
    line-height: 1.8;
    font-size: 0.95rem;
}
.about-text-card p { margin: 0 0 1rem; }
.about-text-card p:last-child { margin: 0; }

.problem-stats {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
}
.p-stat { margin-bottom: 1.2rem; border-bottom: 1px solid var(--border); padding-bottom: 1rem; }
.p-stat:last-child { margin: 0; border: 0; padding: 0; }
.p-num {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #7c3aed, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block;
}
.p-label { color: var(--text-2); font-size: 0.85rem; line-height: 1.4; }

.objective-item {
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.6rem;
}
.obj-icon { font-size: 1.4rem; flex-shrink: 0; }

.tech-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
    height: 100%;
}
.tech-item {
    padding: 0.55rem 0;
    border-bottom: 1px solid var(--border);
    font-size: 0.9rem;
}
.tech-item:last-child { border: 0; }

.ai-step {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 0.85rem 1rem;
    border-bottom: 1px solid var(--border);
}
.ai-step:last-child { border: 0; }
.ai-step-num {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7c3aed, #3b82f6);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    font-weight: 700;
    flex-shrink: 0;
}

.info-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem;
}
.info-table { width: 100%; border-collapse: collapse; }
.info-table tr { border-bottom: 1px solid var(--border); }
.info-table tr:last-child { border: 0; }
.info-key { color: var(--text-3); font-size: 0.82rem; padding: 0.65rem 0.5rem; width: 40%; }
.info-val { color: var(--text-1); font-size: 0.88rem; font-weight: 500; padding: 0.65rem 0.5rem; }

/* Career Guidance */
.guidance-banner {
    background: var(--bg-card);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    border: 1px solid var(--border);
}

.cat-section {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
}
.cat-title { color: var(--text-1); font-weight: 600; font-size: 0.95rem; margin-bottom: 0.6rem; }

.roadmap-category { margin: 1.25rem 0 0.5rem; }
.roadmap-cat-header {
    color: var(--purple-lt);
    font-weight: 700;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding-bottom: 0.3rem;
    border-bottom: 2px solid var(--purple);
    display: inline-block;
}
.roadmap-step {
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
    padding: 0.85rem 1rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin: 0.4rem 0;
    transition: border-color 0.2s;
}
.roadmap-step:hover { border-color: var(--purple); }
.step-badge {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7c3aed, #3b82f6);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.78rem;
    font-weight: 700;
    flex-shrink: 0;
}
.step-content { flex: 1; }
.learn-link {
    color: var(--purple-lt);
    font-size: 0.82rem;
    text-decoration: none;
    border-bottom: 1px solid rgba(124,58,237,0.4);
    transition: all 0.2s;
}
.learn-link:hover { color: white; border-color: white; }

.success-box {
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    color: #86efac;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

.tip-card {
    display: flex;
    align-items: flex-start;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.6rem;
    transition: border-color 0.2s;
}
.tip-card:hover { border-color: var(--purple); }

.future-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 0.75rem;
    height: 100%;
    transition: all 0.2s;
}
.future-card:hover { border-color: var(--purple); transform: translateY(-2px); }

.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    background: var(--bg-card);
    border: 1px dashed var(--border);
    border-radius: 16px;
    margin: 2rem 0;
}

/* Contact Page */
.contact-item {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    padding: 0.85rem 1rem;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 0.5rem;
}
.contact-icon { font-size: 1.4rem; flex-shrink: 0; }
.form-error {
    background: rgba(239,68,68,0.1);
    border: 1px solid rgba(239,68,68,0.3);
    color: #fca5a5;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    font-size: 0.88rem;
    margin: 0.3rem 0;
}

/* Divider */
hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }

/* Spinner */
.stSpinner > div > div { border-top-color: var(--purple) !important; }

/* Plotly overrides */
.js-plotly-plot .plotly .modebar { display: none !important; }

/* Responsive */
@media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .block-container { padding: 1rem; }
}
</style>
""", unsafe_allow_html=True)


# ─── SESSION STATE INIT ───────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-text">🎯 ResumeIQ</div>
        <div class="sidebar-tagline">AI-Powered Career Tool</div>
    </div>
    """, unsafe_allow_html=True)

    pages = ["🏠 Home", "🔍 Resume Analyzer", "🗺️ Career Guidance", "ℹ️ About", "📬 Contact"]
    page_labels = {
        "🏠 Home": "Home",
        "🔍 Resume Analyzer": "Resume Analyzer",
        "🗺️ Career Guidance": "Career Guidance",
        "ℹ️ About": "About",
        "📬 Contact": "Contact"
    }

    # Find current index
    current_page_icon = next((k for k, v in page_labels.items() if v == st.session_state.page), "🏠 Home")

    selected = st.radio(
        "Navigation",
        pages,
        index=pages.index(current_page_icon),
        label_visibility="collapsed"
    )

    st.session_state.page = page_labels[selected]

    # Analysis status in sidebar
    st.markdown("<br>", unsafe_allow_html=True)
    if "analysis_results" in st.session_state:
        res = st.session_state["analysis_results"]
        match_pct = res["match_pct"]
        color = res["match_info"]["color"]
        st.markdown(f"""
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:0.9rem;text-align:center">
            <div style="color:var(--text-3);font-size:0.72rem;text-transform:uppercase;letter-spacing:0.05em">Last Analysis</div>
            <div style="font-family:'Space Grotesk';font-size:2rem;font-weight:700;color:{color}">{match_pct}%</div>
            <div style="color:var(--text-3);font-size:0.78rem">Match Score</div>
            <div style="margin-top:0.4rem;color:var(--text-2);font-size:0.8rem">
                ✅ {res['gap_analysis']['match_count']} matched &nbsp;|&nbsp; ❌ {res['gap_analysis']['missing_count']} missing
            </div>
        </div>
        """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="color:var(--text-3);font-size:0.75rem;text-align:center;padding:0.5rem">
    ResumeIQ © 2026<br>
    Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)


# ─── PAGE ROUTING ─────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "Home":
    home.show()
elif page == "Resume Analyzer":
    analyzer.show()
elif page == "Career Guidance":
    career_guidance.show()
elif page == "About":
    about.show()
elif page == "Contact":
    contact.show()
