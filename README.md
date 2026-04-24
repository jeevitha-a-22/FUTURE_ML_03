# 🧠 Resume Screening AI System:

Python · Streamlit · scikit-learn · Plotly · NLP · ReportLab
An end-to-end AI-powered resume screening and candidate ranking system that analyzes resumes, extracts skills, computes intelligent scores, ranks candidates, and generates recruiter-ready reports — with an interactive dashboard.

▶ Live Demo:
-📊 Streamlit Dashboard
-📄 PDF Report Generator
-📈 Interactive Analytics Panels

🎯 Project Overview:
This project builds a machine learning–driven recruitment screening system that automates resume evaluation and ranking.
It combines:
-NLP-based skill extraction
-TF-IDF similarity scoring
-Rule-based experience & education analysis
-Weighted composite scoring model
-Interactive Streamlit dashboard

The system helps recruiters:
-Screen resumes faster
-Identify top candidates instantly
-Detect skill gaps in applicant pools
-Generate automated hiring reports

✨ Features
🧠 AI Screening Engine:
-Resume parsing & preprocessing
-Skill extraction from 148+ skill taxonomy
-Experience estimation using regex NLP
-Education scoring system

📊 Smart Ranking System:
-Composite scoring (0–100%)
-Automatic candidate classification:
-Highly Recommended
-Potential Fit
-Not Recommended

📈 Interactive Dashboard :
-KPI metric cards
-Candidate distribution pie chart
-Top 10 ranked candidates
-Category-wise performance analysis
-Skill gap detection
-Score distribution histogram

⚠️ Skill Gap Analysis:
-Identifies most missing skills in applicants
-Helps recruiters understand hiring gaps

📄 Report Generator:
-One-click PDF report export
-Includes:
-KPI summary
-Top candidates
-Skill gap analysis
-HR-ready document output

🏗️ System Architecture:
┌──────────────────────────────┐
│      INPUT LAYER             │
│  Resume Upload / Dataset     │
└─────────────┬────────────────┘
              ▼
┌──────────────────────────────┐
│   TEXT PREPROCESSING        │
│  - Cleaning                 │
│  - Tokenization             │
│  - Normalization            │
└─────────────┬────────────────┘
              ▼
┌──────────────────────────────┐
│   FEATURE ENGINEERING       │
│  - Skill Extraction         │
│  - TF-IDF Similarity        │
│  - Experience Estimation    │
│  - Education Scoring        │
└─────────────┬────────────────┘
              ▼
┌──────────────────────────────┐
│   SCORING ENGINE            │
│ Composite Score (0–100%)    │
└─────────────┬────────────────┘
              ▼
┌──────────────────────────────┐
│   STREAMLIT DASHBOARD       │
│ KPI + Charts + Insights     │
└─────────────┬────────────────┘
              ▼
┌──────────────────────────────┐
│   REPORT GENERATION         │
│ PDF Export (HR-ready)       │
└──────────────────────────────┘

🧠 Skill Intelligence Engine:
📌 148 Skills across 9 Categories
-Programming Languages (Python, Java, C++, SQL)
-Machine Learning (NLP, Deep Learning, LLMs)
-Frameworks (TensorFlow, PyTorch, Scikit-learn)
-Data Tools (Pandas, Spark, Tableau)
-Databases (MySQL, MongoDB, PostgreSQL)
-Cloud & DevOps (AWS, Docker, Kubernetes)
-Web Development (React, Flask, Django)
-Soft Skills (Communication, Leadership)
-Statistics (A/B Testing, Hypothesis Testing)

⚡ Smart Matching Logic:
-Longest-first greedy matching
-Prevents false positives (e.g., "machine learning" ≠ "learning")

📊 Dashboard Overview:
📌 KPI Cards:
-Total resumes processed
-Top score
-Average score
-Recommended candidates
🥧 Charts:
-Candidate status distribution (Pie)
-Top 10 candidate ranking (Bar)
-Category performance (Bar)
-Skill gap analysis (Bar)
-Score distribution (Histogram)

📄 Report Generator:
The system generates a downloadable PDF report containing:
✔ KPI summary
✔ Candidate ranking table
✔ Top 10 profiles
✔ Skill gap insights
✔ Hiring recommendation summary

🛠️ Tech Stack:
| Layer         | Technology     |
| ------------- | -------------- |
| Frontend      | Streamlit      |
| ML            | Scikit-learn   |
| NLP           | TF-IDF, Regex  |
| Visualization | Plotly, Altair |
| Data          | Pandas, NumPy  |
| Reporting     | ReportLab      |
| Language      | Python 3.9+    |

🔮 Future Improvements :
🤖 Transformer-based semantic matching (BERT / Sentence Transformers)
📄 Direct PDF resume parsing
🧠 Explainable AI scoring breakdown
📧 Email report automation for recruiters
🗄️ Database integration for ATS system
🌐 Cloud deployment (AWS / Streamlit Cloud)
⚖️ Bias reduction & fairness scoring

📓 Notebook Walkthrough :
| Step  | Cell / Module         | What It Does                                                                                  |
| ----- | --------------------- | --------------------------------------------------------------------------------------------- |
| 1     | Install & Import      | Loads pandas, numpy, matplotlib, sklearn                                                      |
| 2     | Upload Datasets       | Kaggle CSV upload widget (Colab) or synthetic fallback                                        |
| 3     | Skill Taxonomy        | Defines 148 skills across 9 categories                                                        |
| 4     | Text Preprocessing    | `clean_text()`, `extract_skills()`, `extract_years_experience()`, `extract_education_score()` |
| 5     | Synthetic Data        | Generates 100 realistic resumes + 6 JDs if no CSVs uploaded                                   |
| 6     | Load Datasets         | Smart CSV loader with column-name normalization                                               |
| 7     | ML Pipeline Class     | `ResumeScreeningPipeline` — core scoring engine                                               |
| 8     | Run Pipeline          | Screens all resumes for `TARGET_ROLE = "Data Scientist"`                                      |
| 9     | Analytics             | Category leaderboard + skill gap report (top 20 missing skills)                               |
| 10    | Recruiter Dashboard   | 6-panel matplotlib figure — main visualization dashboard                                      |
| 11    | Skill Gap Heatmap     | Matrix of required skills × top 15 candidates                                                 |
| 12    | Analytics Deep-Dive   | 4-chart panel (category scores, resume distribution, percentile curve, skill frequency)       |
| 13    | Multi-Role Comparison | Runs pipeline for all 6 roles and generates comparison chart                                  |
| 14    | Export & Download     | CSV + all PNG charts auto-downloaded in Colab                                                 |
| BONUS | Personal Analyzer     | Upload your own resume → personalized visual report                                           |

📄 License :
This project was completed as part of the Machine Learning Internship Program at Future Interns, focusing on real-world, industry-relevant NLP applications.

Made by Jeevitha | Future Interns Machine Learning Track
