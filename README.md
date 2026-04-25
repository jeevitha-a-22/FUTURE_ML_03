# 🧠 Resume Screening AI System:

Python · Streamlit · scikit-learn · Plotly · NLP · ReportLab <br>
An end-to-end AI-powered resume screening and candidate ranking system that analyzes resumes, extracts skills, computes intelligent scores, ranks candidates, and generates recruiter-ready reports — with an interactive dashboard.

## 📦 Datasets : <br>
The notebook supports three optional Kaggle datasets uploaded in Step 2. If none are uploaded, it falls back to 100 fully synthetic resumes + 6 synthetic JDs.<br>
### Dataset	Kaggle Link : <br>
Resume Dataset -> https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset	-> Resume pool to screen <br>
Job Descriptions ->  https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset -> JD profiles for each role <br>

## ▶ Live Demo: <br>
### 📊 Streamlit Dashboard : <br>
#### 📄 What the App Does: <br>
The Streamlit app replicates a full AI resume screening pipeline inside a clean dashboard UI: <br>

##### 📥 Resume Input Options : <br>
Upload multiple resumes (.pdf, .docx, .txt) <br>
Paste resume text directly <br>
Load sample/demo resumes for testing <br>

##### 🎯 Job Role Selection: <br>
Choose a target role from: <br>
Data Scientist <br>
Machine Learning Engineer <br>
Full Stack Developer <br>
DevOps Engineer <br>
Data Analyst <br>
Software Engineer <br>

##### ⚙️ AI Screening Pipeline : <br>
The system performs: <br>
🧹 Text cleaning & preprocessing <br>
🧠 Skill extraction (NLP-based) <br>
📊 Experience & education scoring <br>
📌 Keyword matching with job description <br>
⚖️ Weighted final ranking score <br>

##### 📊 Dashboard Features : <br>
###### 📈 Candidate Ranking Table : <br>
Ranked list of all candidates <br>
Overall match score <br>
Skill match percentage <br>

###### 📊 Visualization Panels :<br>
Skill match comparison (bar chart) <br>
Score distribution analysis <br>
Role-wise suitability comparison <br>
Performance insights dashboard <br>

###### 🧾 Detailed Candidate Report : <br>
For each resume: <br>
Extracted skills <br>
Experience level <br>
Education score <br>
Final AI match score <br>

###### 📁 Export Option <br>
Download ranked results as CSV <br>
Save screening report for HR use <br>

-📄 PDF Report Generator <br> 
-📈 Interactive Analytics Panels <br>

## 🎯 Project Overview: <br>
This project builds a machine learning–driven recruitment screening system that automates resume evaluation and ranking. <br>
It combines: <br>
-NLP-based skill extraction <br>
-TF-IDF similarity scoring <br>
-Rule-based experience & education analysis <br>
-Weighted composite scoring model <br>
-Interactive Streamlit dashboard <br>

The system helps recruiters: <br>
-Screen resumes faster <br>
-Identify top candidates instantly <br>
-Detect skill gaps in applicant pools <br>
-Generate automated hiring reports <br>

## ✨ Features <br>
### 🧠 AI Screening Engine: <br>
-Resume parsing & preprocessing <br>
-Skill extraction from 148+ skill taxonomy <br>
-Experience estimation using regex NLP <br>
-Education scoring system <br>

### 📊 Smart Ranking System: <br>
-Composite scoring (0–100%) <br>
-Automatic candidate classification: <br>
-Highly Recommended <br>
-Potential Fit <br>
-Not Recommended <br>

### 📈 Interactive Dashboard : <br>
-KPI metric cards <br>
-Candidate distribution pie chart <br>
-Top 10 ranked candidates <br>
-Category-wise performance analysis <br>
-Skill gap detection <br>
-Score distribution histogram <br>

### ⚠️ Skill Gap Analysis: <br>
-Identifies most missing skills in applicants <br>
-Helps recruiters understand hiring gaps <br>

### 📄 Report Generator: <br>
-One-click PDF report export <br>
-Includes: <br>
-KPI summary <br>
-Top candidates <br>
-Skill gap analysis <br>
-HR-ready document output <br>

## 🏗️ System Architecture: <br>
┌──────────────────────────────┐
│      INPUT LAYER             │
│  Resume Upload / Dataset     │
└─────────────┬────────────────┘
              ▼ <br>
┌──────────────────────────────┐
│   TEXT PREPROCESSING        │
│  - Cleaning                 │
│  - Tokenization             │
│  - Normalization            │
└─────────────┬────────────────┘
              ▼ <br>
┌──────────────────────────────┐
│   FEATURE ENGINEERING       │
│  - Skill Extraction         │
│  - TF-IDF Similarity        │
│  - Experience Estimation    │
│  - Education Scoring        │
└─────────────┬────────────────┘
              ▼ <br>
┌──────────────────────────────┐
│   SCORING ENGINE            │
│ Composite Score (0–100%)    │
└─────────────┬────────────────┘
              ▼ <br>
┌──────────────────────────────┐
│   STREAMLIT DASHBOARD       │
│ KPI + Charts + Insights     │
└─────────────┬────────────────┘
              ▼ <br>
┌──────────────────────────────┐
│   REPORT GENERATION         │
│ PDF Export (HR-ready)       │
└──────────────────────────────┘

## 🧠 Skill Intelligence Engine: <br>
### 📌 148 Skills across 9 Categories <br>
-Programming Languages (Python, Java, C++, SQL) <br>
-Machine Learning (NLP, Deep Learning, LLMs) <br>
-Frameworks (TensorFlow, PyTorch, Scikit-learn) <br>
-Data Tools (Pandas, Spark, Tableau) <br>
-Databases (MySQL, MongoDB, PostgreSQL) <br>
-Cloud & DevOps (AWS, Docker, Kubernetes) <br>
-Web Development (React, Flask, Django) <br>
-Soft Skills (Communication, Leadership) <br>
-Statistics (A/B Testing, Hypothesis Testing) <br>

### ⚡ Smart Matching Logic: <br>
-Longest-first greedy matching <br>
-Prevents false positives (e.g., "machine learning" ≠ "learning") <br>

## 📊 Dashboard Overview: <br>
### 📌 KPI Cards: <br>
-Total resumes processed <br>
-Top score <br>
-Average score <br> 
-Recommended candidates <br>
### 🥧 Charts: <br>
-Candidate status distribution (Pie) <br>
-Top 10 candidate ranking (Bar)<br>
-Category performance (Bar) <br>
-Skill gap analysis (Bar) <br>
-Score distribution (Histogram) <br>

## 📄 Report Generator: <br>
The system generates a downloadable PDF report containing: <br>
✔ KPI summary <br>
✔ Candidate ranking table <br>
✔ Top 10 profiles <br>
✔ Skill gap insights <br>
✔ Hiring recommendation summary <br>

## 🛠️ Tech Stack:
| Layer         | Technology     |
| ------------- | -------------- |
| Frontend      | Streamlit      |
| ML            | Scikit-learn   |
| NLP           | TF-IDF, Regex  |
| Visualization | Plotly, Altair |
| Data          | Pandas, NumPy  |
| Reporting     | ReportLab      |
| Language      | Python 3.9+    |

## 🔮 Future Improvements : <br>
🤖 Transformer-based semantic matching (BERT / Sentence Transformers)<br>
📄 Direct PDF resume parsing <br>
🧠 Explainable AI scoring breakdown <br>
📧 Email report automation for recruiters <br>
🗄️ Database integration for ATS system <br>
🌐 Cloud deployment (AWS / Streamlit Cloud) <br>
⚖️ Bias reduction & fairness scoring <br>

## 📓 Notebook Walkthrough :
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

## 📄 License : <br>
This project was completed as part of the Machine Learning Internship Program at Future Interns, focusing on real-world, industry-relevant NLP applications. <br>

Made by Jeevitha | Future Interns Machine Learning Track
