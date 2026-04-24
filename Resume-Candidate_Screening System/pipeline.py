import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import clean_text, extract_skills, extract_years_experience, extract_education_score
class ResumeScreeningPipeline:
    """
    End-to-end ML Resume Screening System.
    Weights: 35% skill match | 30% TF-IDF | 15% category coverage | 12% experience | 8% education
    """
    WEIGHTS = {"tfidf": 0.30, "skill": 0.35, "category": 0.15, "exp": 0.12, "edu": 0.08}

    def __init__(self, target_role, jd_df, resume_df):
        self.target_role = target_role
        self.resume_df   = resume_df
        self.results     = None
        self.job_description = self._build_jd(jd_df)
        self.jd_clean        = clean_text(self.job_description)
        self.jd_skills       = extract_skills(self.job_description)
        self.jd_categories   = set(self.jd_skills.values())
        self.vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=8000, sublinear_tf=True, min_df=1)
        print(f"\n   Role     : {target_role}")
        print(f"   JD Skills: {len(self.jd_skills)} across {len(self.jd_categories)} categories")
        print(f"  Resumes  : {len(resume_df)} to screen")

    def _build_jd(self, jd_df):
        col   = "Job Title" if "Job Title" in jd_df.columns else "Role"
        mask  = jd_df[col].str.lower().str.contains(self.target_role.lower(), na=False)
        matched = jd_df[mask]
        if matched.empty:
            kw = self.target_role.split()[0].lower()
            matched = jd_df[jd_df[col].str.lower().str.contains(kw, na=False)]
        if matched.empty:
            raise ValueError(f"Role '{self.target_role}' not found. Available: {sorted(jd_df[col].dropna().unique())}")
        parts = []
        for _, row in matched.head(5).iterrows():
            if "Job Description" in row and pd.notna(row["Job Description"]): parts.append(str(row["Job Description"]))
            if "skills"          in row and pd.notna(row.get("skills","")):    parts.append(str(row["skills"]))
        return " ".join(parts)

    def _score_one(self, resume_text, category):
        rc  = clean_text(resume_text)
        rsk = extract_skills(resume_text)
        tf  = self.vectorizer.fit_transform([self.jd_clean, rc])
        cos = float(cosine_similarity(tf[0:1], tf[1:2])[0][0])
        req, cand = set(self.jd_skills), set(rsk)
        matched, missing, bonus = req & cand, req - cand, cand - req
        skr  = len(matched) / max(len(req), 1)
        catc = len(self.jd_categories & set(rsk.values())) / max(len(self.jd_categories), 1)
        yrs  = extract_years_experience(resume_text)
        exps = min(yrs / 8.0, 1.0)
        edus = extract_education_score(resume_text)
        comp = (self.WEIGHTS["tfidf"]*cos + self.WEIGHTS["skill"]*skr +
                self.WEIGHTS["category"]*catc + self.WEIGHTS["exp"]*exps + self.WEIGHTS["edu"]*edus)
        return {"category": category, "composite_score": round(comp*100,2), "tfidf_score": round(cos*100,2),
                "skill_match_pct": round(skr*100,2), "category_pct": round(catc*100,2),
                "exp_score": round(exps*100,2), "edu_score": round(edus*100,2),
                "est_years_exp": yrs, "matched_skills": sorted(matched), "missing_skills": sorted(missing),
                "bonus_skills": sorted(bonus), "total_skills": len(cand),
                "snippet": resume_text[:180].replace("\n"," ").strip()+"..."}

    def run(self):
        print(f"\n    Screening {len(self.resume_df)} resumes...")
        records = []
        for idx, row in self.resume_df.iterrows():
            sc = self._score_one(str(row.get("Resume_str","")), str(row.get("Category","Unknown")))
            sc["resume_id"] = row.get("ID", idx); records.append(sc)
        df = pd.DataFrame(records).sort_values("composite_score", ascending=False).reset_index(drop=True)
        df.insert(0, "rank", df.index + 1)
        df["status"] = df["composite_score"].apply(
            lambda s: " Highly Recommended" if s>=70 else "  Potential Fit" if s>=50 else " Not Recommended")
        self.results = df
        rec = (df["composite_score"]>=70).sum(); pot = ((df["composite_score"]>=50)&(df["composite_score"]<70)).sum()
        print(f"   Done!  Top: {df['composite_score'].max():.1f}% |  {rec}  ⚠️ {pot}   {(df['composite_score']<50).sum()}")
        return df

    def category_leaderboard(self):
        return (self.results.groupby("category")["composite_score"]
                .agg(["mean","max","count"])
                .rename(columns={"mean":"avg_score","max":"top_score","count":"n_resumes"})
                .sort_values("avg_score", ascending=False).round(2))

    def skill_gap_report(self, top_n=20):
        counter = Counter()
        for ms in self.results.head(top_n)["missing_skills"]:
            if isinstance(ms, list): counter.update(ms)
        return pd.DataFrame(counter.most_common(), columns=["skill","frequency"])

    def print_report(self, n=10):
        line = "═"*70
        print(f"\n{line}\n  TOP {n} — {self.target_role.upper()}  |  JD Skills: {len(self.jd_skills)}  |  Screened: {len(self.results)}\n{line}")
        for _, r in self.results.head(n).iterrows():
            print(f"\n  #{int(r['rank']):>3}  {r['status']}")
            print(f"       Category : {r['category']}  |  Est. Exp: {r['est_years_exp']} yrs")
            print(f"       Score    : {r['composite_score']:.1f}%  |  Skill Match: {r['skill_match_pct']:.1f}%  |  TF-IDF: {r['tfidf_score']:.1f}%")
            print(f"       Matched  : {', '.join(r['matched_skills'][:7])}{'…' if len(r['matched_skills'])>7 else ''}")
            print(f"       Missing  : {', '.join(r['missing_skills'][:6]) or 'None '}")
        print(f"\n{line}\n")

     