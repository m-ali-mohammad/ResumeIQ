"""
Similarity Calculation Utility
Uses TF-IDF and Cosine Similarity to compare resume and job description.
"""

import re
from typing import Tuple, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def preprocess_text(text: str) -> str:
    """
    Preprocess text for TF-IDF vectorization.
    
    Args:
        text: Raw input text
        
    Returns:
        Cleaned and normalized text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def calculate_similarity(resume_text: str, jd_text: str) -> float:
    """
    Calculate cosine similarity between resume and job description
    using TF-IDF vectorization.
    
    Args:
        resume_text: Extracted resume text
        jd_text: Job description text
        
    Returns:
        float: Similarity score between 0 and 1
    """
    if not resume_text or not jd_text:
        return 0.0
    
    # Preprocess texts
    cleaned_resume = preprocess_text(resume_text)
    cleaned_jd = preprocess_text(jd_text)
    
    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer(
        stop_words='english',
        ngram_range=(1, 2),      # Unigrams and bigrams
        max_features=5000,        # Limit vocabulary size
        sublinear_tf=True         # Apply log normalization
    )
    
    try:
        tfidf_matrix = vectorizer.fit_transform([cleaned_resume, cleaned_jd])
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return round(float(score), 4)
    except Exception:
        return 0.0


def get_match_percentage(similarity_score: float) -> int:
    """
    Convert similarity score (0-1) to a percentage (0-100).
    
    Args:
        similarity_score: Raw cosine similarity score
        
    Returns:
        int: Percentage score
    """
    return round(similarity_score * 100)


def get_match_level(percentage: int) -> Dict:
    """
    Categorize the match percentage into a descriptive level.
    
    Args:
        percentage: Match percentage (0-100)
        
    Returns:
        Dict with level name, color, emoji, and description
    """
    if percentage >= 80:
        return {
            "level": "Excellent Match",
            "color": "#22c55e",
            "emoji": "🌟",
            "description": "Your resume is an excellent match! You have strong alignment with this role.",
            "badge": "excellent"
        }
    elif percentage >= 60:
        return {
            "level": "Good Match",
            "color": "#3b82f6",
            "emoji": "✅",
            "description": "Good match. A few skill additions could make you an even stronger candidate.",
            "badge": "good"
        }
    elif percentage >= 40:
        return {
            "level": "Moderate Match",
            "color": "#f59e0b",
            "emoji": "⚡",
            "description": "Moderate match. Consider developing some key missing skills to improve your chances.",
            "badge": "moderate"
        }
    else:
        return {
            "level": "Low Match",
            "color": "#ef4444",
            "emoji": "📚",
            "description": "Low match. Significant skill development is recommended for this role.",
            "badge": "low"
        }


def keyword_overlap_analysis(resume_text: str, jd_text: str) -> Dict:
    """
    Analyze keyword overlap between resume and job description.
    
    Args:
        resume_text: Resume text
        jd_text: Job description text
        
    Returns:
        Dict with overlap statistics
    """
    resume_words = set(preprocess_text(resume_text).split())
    jd_words = set(preprocess_text(jd_text).split())
    
    # Remove common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to',
        'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were',
        'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
        'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can',
        'that', 'this', 'these', 'those', 'it', 'its', 'we', 'you', 'he',
        'she', 'they', 'i', 'me', 'my', 'your', 'our', 'their'
    }
    
    resume_words -= stop_words
    jd_words -= stop_words
    
    # Filter short words
    resume_words = {w for w in resume_words if len(w) > 2}
    jd_words = {w for w in jd_words if len(w) > 2}
    
    common = resume_words.intersection(jd_words)
    
    return {
        "resume_unique_words": len(resume_words),
        "jd_unique_words": len(jd_words),
        "common_words": len(common),
        "coverage_rate": round(len(common) / len(jd_words) * 100, 1) if jd_words else 0
    }
