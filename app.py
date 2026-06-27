import streamlit as st

# Load configuration (this configures Gemini API)
from config import settings

# UI
from ui.layout import setup_page
from ui.buttons import create_buttons

# Services
from services.analysis_service import analyze_resume

# Prompts
from prompts import (
    RESUME_REVIEW_PROMPT,
    ATS_PROMPT,
    IMPROVE_RESUME_PROMPT,
    MISSING_SKILLS_PROMPT,
    INTERVIEW_PROMPT,
    COVER_LETTER_PROMPT,
    REWRITE_PROMPT,
)


# -------------------------------
# Page Setup
# -------------------------------
setup_page()


# -------------------------------
# User Inputs
# -------------------------------
job_description = st.text_area(
    "📋 Paste Job Description",
    height=220
)

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success("✅ Resume Uploaded Successfully")


# -------------------------------
# Buttons
# -------------------------------
(
    review_btn,
    ats_btn,
    improve_btn,
    skills_btn,
    interview_btn,
    cover_btn,
    rewrite_btn,
) = create_buttons()


# -------------------------------
# Helper Function
# -------------------------------
def process_request(prompt, title):
    """
    Common function for all buttons.
    """

    if uploaded_file is None:
        st.warning("⚠ Please upload your Resume.")
        return

    if job_description.strip() == "":
        st.warning("⚠ Please paste the Job Description.")
        return

    with st.spinner("Analyzing Resume..."):

        response = analyze_resume(
            uploaded_file,
            job_description,
            prompt
        )

    st.subheader(title)
    st.write(response)


# -------------------------------
# Button Actions
# -------------------------------

if review_btn:
    process_request(
        RESUME_REVIEW_PROMPT,
        "📄 Resume Review"
    )

if ats_btn:
    process_request(
        ATS_PROMPT,
        "🎯 ATS Match Score"
    )

if improve_btn:
    process_request(
        IMPROVE_RESUME_PROMPT,
        "✨ Resume Improvement Suggestions"
    )

if skills_btn:
    process_request(
        MISSING_SKILLS_PROMPT,
        "📚 Missing Skills"
    )

if interview_btn:
    process_request(
        INTERVIEW_PROMPT,
        "💼 Interview Questions"
    )

if cover_btn:
    process_request(
        COVER_LETTER_PROMPT,
        "📝 Cover Letter"
    )

if rewrite_btn:
    process_request(
        REWRITE_PROMPT,
        "🖋 Rewritten Resume"
    )