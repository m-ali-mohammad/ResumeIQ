# 🎯 ResumeIQ — AI-Powered Resume Analyzer and Career Enhancement Assistant

> **SITER Academy, Norway — Summer Internship 2026**  
> **Domain:** Artificial Intelligence (AI)  
> **Type:** Web Application

---

## 📌 Project Overview

ResumeIQ is an AI-powered web application that helps job seekers optimize their resumes by comparing them against job descriptions using NLP techniques — TF-IDF vectorization and Cosine Similarity. The system identifies skill gaps, calculates match percentages, and provides actionable career enhancement recommendations.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📄 **Resume Upload** | Upload PDF resumes (multi-page supported) |
| 💼 **JD Input** | Paste any job description from LinkedIn, Naukri, Indeed, etc. |
| 📊 **Match Score** | AI-calculated percentage match using TF-IDF + Cosine Similarity |
| 🔍 **Skill Gap Analysis** | Matching skills, missing skills, and additional skills |
| 🗺️ **Learning Roadmap** | Prioritized learning path with official resource links |
| 📈 **Visual Dashboard** | Interactive Plotly charts (gauge, donut, bar charts) |
| 💡 **Career Tips** | Personalized career enhancement recommendations |
| ❓ **FAQ & Contact** | Full contact form and FAQ section |

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **Web Framework** | Streamlit |
| **NLP / AI** | Scikit-learn (TF-IDF, Cosine Similarity) |
| **PDF Processing** | PyPDF2 |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Plotly |
| **Styling** | Custom CSS (Dark Theme) |
| **Version Control** | Git / GitHub |
| **Deployment** | Streamlit Community Cloud |

---

## 🤖 AI Implementation

### TF-IDF Vectorization
```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 2),   # unigrams + bigrams
    max_features=5000,
    sublinear_tf=True     # log normalization
)
tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
```

### Cosine Similarity
```python
from sklearn.metrics.pairwise import cosine_similarity

score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
match_percentage = round(score * 100)
```

---

## 📁 Project Structure

```
ResumeIQ/
│
├── app.py                    # Main application entry point
│
├── pages/
│   ├── __init__.py
│   ├── home.py               # Landing page
│   ├── about.py              # About & tech info
│   ├── analyzer.py           # Core AI analysis page
│   ├── career_guidance.py    # Roadmap & recommendations
│   └── contact.py            # Contact form & FAQ
│
├── utils/
│   ├── __init__.py
│   ├── pdf_reader.py         # PDF text extraction
│   ├── skill_extractor.py    # Skill detection & gap analysis
│   └── similarity.py         # TF-IDF & cosine similarity
│
├── data/
│   └── skills.csv            # Skills database (80+ skills)
│
├── docs/
│   └── ResumeIQ_Client_Guide.pdf   #User Guide
├── assets/
│   └── (images/icons)
│
├── .streamlit/
│   └── config.toml           # Dark theme configuration
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/ResumeIQ.git
cd ResumeIQ

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🌐 Deployment — Streamlit Community Cloud (Free)

1. Push your project to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **New app** → Select repo → Set `app.py` as main file
5. Click **Deploy** — live in ~2 minutes!

---

## 📊 System Architecture

```
User
 │
 ▼
Streamlit Interface (app.py)
 │
 ├── Home Page
 ├── Resume Analyzer ──── PDF Upload ──► PDF Text Extraction (PyPDF2)
 │                  ──── JD Input   ──┐
 │                                    ▼
 │                             Text Preprocessing
 │                                    │
 │                             TF-IDF Vectorization (Scikit-learn)
 │                                    │
 │                             Cosine Similarity
 │                                    │
 │                         ┌──────────┼──────────┐
 │                         ▼          ▼          ▼
 │                    Match Score  Skill Gap  Keyword
 │                                Analysis   Analysis
 │
 ├── Career Guidance ──── Learning Roadmap + Resources
 ├── About Page
 └── Contact Page
```

---

## 🧪 Sample Workflow

**Input:**
- Resume: *Python, Flask, Machine Learning, Pandas*
- Job Description: *Python, SQL, Docker, Machine Learning, AWS*

**Output:**
```
Match Score: 72%

✅ Matching Skills: Python, Machine Learning

❌ Missing Skills: SQL, Docker, AWS

📚 Learning Path:
  1. SQL (Database) → w3schools.com/sql
  2. Docker (DevOps) → docs.docker.com
  3. AWS (Cloud) → aws.amazon.com/getting-started
```

---

## 🔮 Future Enhancements

- [ ] ATS Compatibility Checker
- [ ] AI Chat Career Coach (ChatGPT-style)
- [ ] Multi-Resume Comparison
- [ ] Job Recommendation Engine
- [ ] LinkedIn Profile Analyzer
- [ ] Resume Formatting Analysis
- [ ] DOCX / TXT support
- [ ] Email report export

---

## 📋 SRS Summary

| Requirement | Status |
|---|---|
| FR1: PDF Upload | ✅ |
| FR2: Text Extraction | ✅ |
| FR3: JD Input | ✅ |
| FR4: Resume-JD Comparison | ✅ |
| FR5: Similarity Score | ✅ |
| FR6: Recommendations | ✅ |
| FR7: Analytics Dashboard | ✅ |
| NFR: Analysis < 5 seconds | ✅ |
| NFR: Mobile Responsive | ✅ |
| NFR: Public Deployment | ✅ (Streamlit Cloud) |

---

## 👨‍💻 Author

- **Academy:** SITER Academy, Norway  
- **Program:** Summer Internship 2026  
- **Domain:** Artificial Intelligence (AI)

---

## 📄 License

MIT License — Free to use, modify, and distribute.
