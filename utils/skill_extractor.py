"""
Skill Extractor Utility
Extracts and matches skills from resume and job description text.
"""

import re
import os
import pandas as pd
from typing import List, Dict, Tuple


# Load skills from CSV
def load_skills_database() -> pd.DataFrame:
    """Load the skills database from CSV file."""
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        skills_path = os.path.join(base_dir, "data", "skills.csv")
        return pd.read_csv(skills_path)
    except Exception:
        # Fallback skill list if CSV not found
        fallback = [
            "Python", "JavaScript", "Java", "SQL", "React", "Node.js",
            "Machine Learning", "Deep Learning", "TensorFlow", "Docker",
            "AWS", "Azure", "Git", "MongoDB", "PostgreSQL", "Flask",
            "Django", "Kubernetes", "Linux", "REST API"
        ]
        return pd.DataFrame({"skill": fallback, "category": ["General"] * len(fallback), "learning_resource": [""] * len(fallback)})


SKILLS_DB = load_skills_database()
ALL_SKILLS = SKILLS_DB["skill"].tolist()


def extract_skills(text: str) -> List[str]:
    """
    Extract skills from text by matching against the skills database.
    
    Args:
        text: Input text (resume or job description)
        
    Returns:
        List of found skills
    """
    text_lower = text.lower()
    found_skills = []
    
    for skill in ALL_SKILLS:
        # Create regex pattern for whole-word matching
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
    
    return list(set(found_skills))


def analyze_skill_gaps(
    resume_skills: List[str],
    jd_skills: List[str]
) -> Dict:
    """
    Analyze skill gaps between resume and job description.
    
    Args:
        resume_skills: Skills found in resume
        jd_skills: Skills required in job description
        
    Returns:
        Dict with matching, missing, and extra skills
    """
    resume_set = set(s.lower() for s in resume_skills)
    jd_set = set(s.lower() for s in jd_skills)
    
    # Map back to original case
    skill_map = {s.lower(): s for s in resume_skills + jd_skills}
    
    matching_lower = resume_set.intersection(jd_set)
    missing_lower = jd_set - resume_set
    extra_lower = resume_set - jd_set
    
    matching = [skill_map.get(s, s) for s in matching_lower]
    missing = [skill_map.get(s, s) for s in missing_lower]
    extra = [skill_map.get(s, s) for s in extra_lower]
    
    return {
        "matching": sorted(matching),
        "missing": sorted(missing),
        "extra": sorted(extra),
        "match_count": len(matching),
        "missing_count": len(missing),
        "total_required": len(jd_skills)
    }


def get_skill_details(skill_name: str) -> Dict:
    """
    Get details for a specific skill from the database.
    
    Args:
        skill_name: Name of the skill
        
    Returns:
        Dict with skill details (category, learning_resource)
    """
    row = SKILLS_DB[SKILLS_DB["skill"].str.lower() == skill_name.lower()]
    if not row.empty:
        return {
            "category": row.iloc[0]["category"],
            "learning_resource": row.iloc[0]["learning_resource"]
        }
    return {"category": "General", "learning_resource": ""}


def generate_learning_path(missing_skills: List[str]) -> List[Dict]:
    """
    Generate a prioritized learning path for missing skills.
    
    Args:
        missing_skills: List of skills to learn
        
    Returns:
        List of dicts with skill, category, and resource
    """
    path = []
    for skill in missing_skills:
        details = get_skill_details(skill)
        path.append({
            "skill": skill,
            "category": details["category"],
            "resource": details["learning_resource"]
        })
    
    # Sort by category priority
    category_priority = {
        "Programming": 1,
        "Database": 2,
        "Data Science": 3,
        "Data Engineering": 3,
        "AI/ML": 4,
        "Web Development": 4,
        "DevOps": 5,
        "Cloud": 5,
        "Security": 6,
        "General": 7
    }
    
    path.sort(key=lambda x: category_priority.get(x["category"], 10))
    return path


def get_skill_categories(skills: List[str]) -> Dict[str, List[str]]:
    """
    Group skills by category.
    
    Args:
        skills: List of skill names
        
    Returns:
        Dict mapping category to list of skills
    """
    categories = {}
    for skill in skills:
        details = get_skill_details(skill)
        cat = details["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(skill)
    return categories
