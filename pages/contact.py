"""
Contact Page - ResumeIQ
"""

import streamlit as st
import re


def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def show():
    st.markdown('<h1 class="page-title">Contact Us</h1>', unsafe_allow_html=True)
    st.markdown('<p class="page-subtitle">Have questions or feedback? We\'d love to hear from you.</p>', unsafe_allow_html=True)

    st.markdown("---")

    col_form, col_info = st.columns([3, 2], gap="large")

    with col_form:
        st.markdown('<h3 style="color:#e2e8f0;margin-bottom:1rem">📬 Send a Message</h3>', unsafe_allow_html=True)

        name = st.text_input("Full Name *", placeholder="Your full name")
        email = st.text_input("Email Address *", placeholder="your.email@example.com")
        subject = st.selectbox("Subject *", [
            "General Inquiry",
            "Bug Report",
            "Feature Request",
            "Collaboration",
            "Academic / Research",
            "Other",
        ])
        message = st.text_area("Message *", placeholder="Type your message here...", height=140)

        st.markdown("<br>", unsafe_allow_html=True)

        submit = st.button("📤 Send Message", type="primary", use_container_width=True)

        if submit:
            errors = []
            if not name.strip():
                errors.append("Please enter your name.")
            if not email.strip() or not is_valid_email(email):
                errors.append("Please enter a valid email address.")
            if not message.strip() or len(message.strip()) < 20:
                errors.append("Message must be at least 20 characters.")

            if errors:
                for err in errors:
                    st.markdown(f'<div class="form-error">⚠️ {err}</div>', unsafe_allow_html=True)
            else:
                st.success(f"✅ Thanks {name.split()[0]}! Your message has been received. We'll reply to {email} within 24–48 hours.")
                st.balloons()

    with col_info:
        st.markdown('<h3 style="color:#e2e8f0;margin-bottom:1rem">📌 Contact Info</h3>', unsafe_allow_html=True)

        contact_items = [
            ("🏫", "Academy", "SITER Academy, Norge"),
            ("📧", "Email", "support@resumeiq.ai"),
            ("💻", "GitHub", "github.com/resumeiq"),
            ("🌐", "Website", "resumeiq.streamlit.app"),
            ("⏰", "Response Time", "Within 24–48 hours"),
        ]

        for icon, label, value in contact_items:
            st.markdown(f"""
            <div class="contact-item">
                <span class="contact-icon">{icon}</span>
                <div>
                    <div style="color:#64748b;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.05em">{label}</div>
                    <div style="color:#e2e8f0;font-size:0.95rem">{value}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<h3 style="color:#e2e8f0;margin-bottom:0.75rem">🐛 Report a Bug</h3>', unsafe_allow_html=True)
        st.markdown("""
        <p style="color:#94a3b8;font-size:0.9rem">
            Found something broken? Open a GitHub issue with:
        </p>
        <ul style="color:#94a3b8;font-size:0.88rem;padding-left:1.2rem">
            <li>Steps to reproduce</li>
            <li>Expected behavior</li>
            <li>Actual behavior</li>
            <li>Browser / OS info</li>
        </ul>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # FAQ
    st.markdown('<h2 class="section-title">❓ Frequently Asked Questions</h2>', unsafe_allow_html=True)

    faqs = [
        ("Is ResumeIQ free to use?", "Yes! ResumeIQ is completely free. No sign-up, no payment, no data stored — just upload and analyze."),
        ("Is my resume data safe?", "Your resume is processed in memory only and is never stored on any server. It is discarded immediately after analysis."),
        ("What resume formats are supported?", "Currently only PDF format is supported. Word (.docx) support is planned for a future release."),
        ("How accurate is the match score?", "The score is based on TF-IDF cosine similarity, which is highly accurate for text comparison. Results are best used as a guide alongside human judgment."),
        ("Can I analyze multiple job descriptions?", "Yes! Just re-upload your resume or use the existing one and paste a new job description, then click Analyze again."),
        ("Why are some skills not detected?", "Our skill database covers 80+ common tech skills. Niche or domain-specific skills may not be detected yet — we're continuously expanding the database."),
    ]

    for question, answer in faqs:
        with st.expander(f"🔹 {question}"):
            st.markdown(f'<p style="color:#94a3b8">{answer}</p>', unsafe_allow_html=True)
