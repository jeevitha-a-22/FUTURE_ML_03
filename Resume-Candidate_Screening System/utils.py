import re
import pandas as pd

# ============================================
# 2. BASE SKILL TAXONOMY
# ============================================

SKILL_TAXONOMY = {
    "programming_languages": ["python","java","javascript","c++","c#","r","sql"],
    "ml_ai": ["machine learning","deep learning","nlp","computer vision","classification","regression"],
    "ml_frameworks": ["tensorflow","pytorch","scikit-learn","sklearn","keras"],
    "data_tools": ["pandas","numpy","matplotlib","seaborn","excel","power bi"],
    "databases": ["mysql","postgresql","mongodb","sqlite"],
    "cloud_devops": ["aws","azure","gcp","docker","kubernetes","git"],
    "web_frameworks": ["django","flask","fastapi","react","node.js"],
    "soft_skills": ["communication","teamwork","leadership","problem solving"],
    "statistics": ["statistics","probability","hypothesis testing"],
}

# ============================================
# 5. CREATE MASTER SKILL MAP
# ============================================

ALL_SKILLS = {
    skill: category
    for category, skills in SKILL_TAXONOMY.items()
    for skill in skills
}

print(f" {len(ALL_SKILLS)} skills across {len(SKILL_TAXONOMY)} categories loaded")


# ============================================
# 6. STOPWORDS
# ============================================

STOPWORDS = {
    "the","a","an","and","or","but","in","on","at","to","for","of","with","by",
    "from","is","was","are","were","be","been","have","has","had","do","did",
    "will","would","could","should","may","might","not","that","this","these",
    "those","i","we","you","he","she","they","it","my","our","your","his","her",
    "their","its","as","if","so","than","then","when","where","which","who","how",
    "what","resume","cv","profile","summary","years","year","experience",
    "work","working","worked","using","used","job","role","company",
    "required","requirements","responsibilities","skills","knowledge"
}


# ============================================
# 7. CLEAN TEXT
# ============================================

def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"[^\w\s\+\#\.\-\/]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()
    words = [w for w in words if w not in STOPWORDS]

    return " ".join(words)


# ============================================
# 8. FAST SKILL EXTRACTION
# ============================================

SKILL_PATTERN = re.compile(
    r'\b(' + '|'.join(map(re.escape, ALL_SKILLS.keys())) + r')\b'
)

def extract_skills(text):
    if not isinstance(text, str):
        return {}

    matches = SKILL_PATTERN.findall(text.lower())
    return {skill: ALL_SKILLS[skill] for skill in set(matches)}


# ============================================
# 9. EXPERIENCE EXTRACTION
# ============================================

def extract_years_experience(text):
    if not isinstance(text, str):
        return 0

    text = text.lower()

    patterns = [
        r"(\d+)\+?\s*years?\s+of\s+experience",
        r"(\d+)\+?\s*years?\s+experience",
        r"experience\s*[:–\-]\s*(\d+)",
        r"(\d+)\s*\-\s*\d+\s*years"
    ]

    for pat in patterns:
        match = re.search(pat, text)
        if match:
            return min(int(match.group(1)), 20)

    # fallback heuristic
    levels = {"junior":1,"associate":2,"mid":3,"senior":5,"lead":7,"principal":10}
    return max([v for k,v in levels.items() if k in text] + [0])


# ============================================
# 10. EDUCATION SCORE
# ============================================

def extract_education_score(text):
    if not isinstance(text, str):
        return 0.5

    text = text.lower()

    if re.search(r"\bph\.?d\b|\bdoctor", text): return 1.0
    if re.search(r"\bm\.?s\.?\b|\bm\.?tech\b|\bmaster", text): return 0.85
    if re.search(r"\bmba\b", text): return 0.82
    if re.search(r"\bb\.?s\.?\b|\bb\.?e\.?\b|\bbachelor", text): return 0.70
    if re.search(r"\bdiploma\b", text): return 0.55

    return 0.50