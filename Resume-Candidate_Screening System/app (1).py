import streamlit as st
import pandas as pd
import numpy as np
import math
import tempfile
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pdfminer.high_level import extract_text
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import io
from pipeline import ResumeScreeningPipeline
from utils import clean_text, extract_skills, extract_years_experience, extract_education_score

# ---------------------------
# LOAD DATA
# ---------------------------
@st.cache_data
def load_data():
    df_resume = pd.read_csv("Resume.csv")
    df_jd     = pd.read_csv("jd.csv")
    return df_resume, df_jd

df_resume, df_jd = load_data()

# ---------------------------
# READ PDF
# ---------------------------
def read_resume(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    return extract_text(tmp_path)

# ---------------------------
# SUGGESTIONS
# ---------------------------
def generate_suggestions(result):
    suggestions = []

    if result["skill_match_pct"] < 60:
        suggestions.append("Add more relevant technical skills.")
    if result["tfidf_score"] < 50:
        suggestions.append("Improve keyword matching.")
    if result["exp_score"] < 50:
        suggestions.append("Highlight more experience.")
    if result["edu_score"] < 50:
        suggestions.append("Add certifications.")

    return suggestions

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("📄 Resume/Candidate Screening System")
st.header("📄 Upload Resume & Analyze")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file:

    # -------- READ RESUME --------
    resume_text = read_resume(uploaded_file)

    temp_df = pd.DataFrame([{
        "ID": 1,
        "Resume_str": resume_text,
        "Category": "Uploaded"
    }])
# ---------------------------
# ROLE SELECT
# ---------------------------
TARGET_ROLE = st.selectbox(
    "Select Target Role",
    ["Data Scientist","Machine Learning Engineer","Software Engineer",
     "DevOps Engineer","Data Analyst"]
)

# ---------------------------
# RUN PIPELINE BUTTON
# ---------------------------
if st.button("🚀 Run Screening"):
    pipeline = ResumeScreeningPipeline(TARGET_ROLE, df_jd, df_resume)
    results_df = pipeline.run()

    st.session_state["results_df"] = results_df
    st.session_state["pipeline"] = pipeline

# ---------------------------
# STOP IF NOT RUN
# ---------------------------
if "results_df" not in st.session_state:
    st.warning("⚠️ Click 'Run Screening' to generate dashboard")
    st.stop()

# ---------------------------
# LOAD FROM SESSION
# ---------------------------
results_df = st.session_state["results_df"]
pipeline   = st.session_state["pipeline"]

def generate_pdf_report(results_df, gap_df):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    elements = []

    # ---------------- TITLE ----------------
    title = Paragraph("Resume Screening Report", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    date = Paragraph(f"Generated on: {datetime.datetime.now()}", styles["Normal"])
    elements.append(date)
    elements.append(Spacer(1, 12))

    # ---------------- KPIs ----------------
    total = len(results_df)
    avg = results_df["composite_score"].mean()
    top = results_df["composite_score"].max()
    rec = (results_df["composite_score"] >= 70).sum()

    kpi_data = [
        ["Total Resumes", total],
        ["Average Score", f"{avg:.2f}%"],
        ["Top Score", f"{top:.2f}%"],
        ["Recommended", rec],
    ]

    kpi_table = Table(kpi_data)
    kpi_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        ("BACKGROUND", (0, 1), (-1, -1), colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.white),
    ]))

    elements.append(kpi_table)
    elements.append(Spacer(1, 20))

    # ---------------- TOP CANDIDATES ----------------
    elements.append(Paragraph("Top Candidates", styles["Heading2"]))

    top10 = results_df.sort_values("composite_score", ascending=False).head(10)

    table_data = [["Name", "Score"]] + [
        [row.get("name", "N/A"), f"{row['composite_score']:.2f}%"]
        for _, row in top10.iterrows()
    ]

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # ---------------- SKILL GAPS ----------------
    elements.append(Paragraph("Top Skill Gaps", styles["Heading2"]))

    gap_data = [["Skill", "Missing Count"]] + gap_df.head(10).values.tolist()

    gap_table = Table(gap_data)
    gap_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkred),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(gap_table)

    # ---------------- BUILD PDF ----------------
    doc.build(elements)
    buffer.seek(0)

    return buffer
# ---------------------------
# TABS
# ---------------------------
tab1, tab2 = st.tabs(["📊 Dashboard", "📁 Data"])

# =========================================================
# DASHBOARD TAB
# =========================================================
with tab1:

    st.header("📊 Dashboard")

    # ---------------- DARK THEME ----------------
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ---------------- KPI CALCULATIONS ----------------
    results_df["status"] = results_df["composite_score"].apply(
        lambda x: "Highly Recommended" if x >= 70
        else "Potential Fit" if x >= 50
        else "Not Recommended"
    )

    total_resumes = len(results_df)
    top_score = results_df["composite_score"].max()
    avg_score = results_df["composite_score"].mean()
    recommended = (results_df["composite_score"] >= 70).sum()

    # ---------------- KPI CARDS ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Resumes", total_resumes)
    col2.metric("Top Score", f"{top_score:.1f}%")
    col3.metric("Avg Score", f"{avg_score:.1f}%")
    col4.metric("Recommended", recommended)

    # ---------------- PIE CHART (STATUS) ----------------
    st.subheader("🥧 Candidate Status Distribution")

    status_counts = results_df["status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]

    fig_pie = px.pie(
        status_counts,
        names="Status",
        values="Count",
        hole=0.45,
        color_discrete_sequence=["#00cc96", "#ffa15a", "#ef553b"]
    )

    fig_pie.update_traces(textinfo="percent+label")
    fig_pie.update_layout(template="plotly_dark")

    st.plotly_chart(fig_pie, use_container_width=True)

    # ---------------- TOP 10 CANDIDATES ----------------
    st.subheader("🏆 Top 10 Candidates")

    top10 = results_df.sort_values("composite_score", ascending=False).head(10)

    fig_top = px.bar(
        top10,
        x="composite_score",
        y=top10["name"] if "name" in top10.columns else top10.index,
        orientation="h",
        color="composite_score",
        color_continuous_scale="Viridis"
    )

    fig_top.update_layout(template="plotly_dark", yaxis_title="", xaxis_title="Score (%)")
    fig_top.update_yaxes(autorange="reversed")

    st.plotly_chart(fig_top, use_container_width=True)

    # ---------------- CATEGORY PERFORMANCE ----------------
    st.subheader("📊 Category Performance")

    cat_scores = results_df.groupby("category")["composite_score"].mean().reset_index()

    fig_cat = px.bar(
        cat_scores,
        x="category",
        y="composite_score",
        color="composite_score",
        color_continuous_scale="Blues"
    )

    fig_cat.update_layout(template="plotly_dark", xaxis_title="Category", yaxis_title="Avg Score")

    st.plotly_chart(fig_cat, use_container_width=True)

    # ---------------- SKILL GAP ----------------
    st.subheader("⚠️ Top Skill Gaps")

    gap_df = pipeline.skill_gap_report().head(10)

    fig_gap = px.bar(
        gap_df,
        x="frequency",
        y="skill",
        orientation="h",
        color="frequency",
        color_continuous_scale="Reds"
    )

    fig_gap.update_layout(template="plotly_dark", xaxis_title="Missing Count", yaxis_title="Skill")
    fig_gap.update_yaxes(autorange="reversed")

    st.plotly_chart(fig_gap, use_container_width=True)

    # ---------------- SCORE DISTRIBUTION ----------------
    st.subheader("📈 Score Distribution")

    fig_hist = px.histogram(
        results_df,
        x="composite_score",
        nbins=20,
        color_discrete_sequence=["#636EFA"]
    )

    fig_hist.update_layout(template="plotly_dark", xaxis_title="Score", yaxis_title="Count")

    st.plotly_chart(fig_hist, use_container_width=True)

    st.subheader("📄 Generate Report")

    if st.button("Download PDF Report"):

        gap_df = pipeline.skill_gap_report()

        pdf_file = generate_pdf_report(results_df, gap_df)

        st.download_button(
           label="⬇️ Download Resume Report",
           data=pdf_file,
           file_name="resume_screening_report.pdf",
           mime="application/pdf"
    )
# =========================================================
# DATA TAB
# =========================================================
with tab2:

    st.header("📁 Data View")

    st.subheader("Results")
    st.dataframe(results_df)

    st.subheader("Leaderboard")
    st.dataframe(pipeline.category_leaderboard())

    st.subheader("Skill Gaps")
    st.dataframe(pipeline.skill_gap_report())

# ---------------------------
# SUGGESTIONS
# ---------------------------
st.subheader("💡 Suggestions")

result = results_df.iloc[0]
suggestions = generate_suggestions(result)

for s in suggestions:
    st.write("•", s)