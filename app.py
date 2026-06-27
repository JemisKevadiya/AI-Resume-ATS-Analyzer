from dotenv import load_dotenv
import streamlit as st
import os
from PyPDF2 import PdfReader
import google.generativeai as genai
from prompts import (
    RESUME_REVIEW_PROMPT,
    ATS_PROMPT,
    IMPROVE_RESUME_PROMPT,
    MISSING_SKILLS_PROMPT,
    INTERVIEW_PROMPT,
    REWRITE_PROMPT,
    COVER_LETTER_PROMPT,
)

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

def get_gemini_response(job_description, resume_text, prompt):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    final_prompt = f"""
    {prompt}

    ----------------------------
    JOB DESCRIPTION
    ----------------------------
    {job_description}

    ----------------------------
    RESUME
    ----------------------------
    {resume_text}
    """

    response = model.generate_content(final_prompt)

    return response.text


# Streamlit UI
st.set_page_config(
    page_title="AI Resume ATS Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume ATS Analyzer")
st.write("Upload your Resume and compare it with the Job Description using Gemini AI.")

job_description = st.text_area(
    "Paste Job Description",
    height=220
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("Resume Uploaded Successfully ✅")


col1, col2, col3 = st.columns(3)

with col1:
    review_btn = st.button("📄 Resume Review", use_container_width=True)

with col2:
    ats_btn = st.button("🎯 ATS Match Score", use_container_width=True)

with col3:
    improve_btn = st.button("✨ Improve Resume", use_container_width=True)

col4, col5, col6 = st.columns(3)

with col4:
    skills_btn = st.button("📚 Missing Skills", use_container_width=True)

with col5:
    interview_btn = st.button("💼 Interview Questions", use_container_width=True)

with col6:
    cover_btn = st.button("📝 Cover Letter", use_container_width=True)


# Resume Review
if review_btn:

    if uploaded_file is None:
        st.warning("Please upload a Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
        job_description,
        resume_text,
        RESUME_REVIEW_PROMPT
)

        st.subheader("Resume Analysis")
        st.write(response)


# ATS Score
if ats_btn:

    if uploaded_file is None:
        st.warning("Please upload a Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
            job_description,
            resume_text,
            ATS_PROMPT
        )

        st.subheader("ATS Analysis")
        st.write(response)

if improve_btn:

    if uploaded_file is None:
        st.warning("Please upload Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
            job_description,
            resume_text,
            IMPROVE_RESUME_PROMPT
        )

        st.subheader("✨ Improved Resume Suggestions")

        st.write(response)

if skills_btn:

    if uploaded_file is None:
        st.warning("Please upload Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
            job_description,
            resume_text,
            MISSING_SKILLS_PROMPT
        )

        st.subheader("📚 Missing Skills")

        st.write(response)

if interview_btn:

    if uploaded_file is None:
        st.warning("Please upload Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
            job_description,
            resume_text,
            INTERVIEW_PROMPT
        )

        st.subheader("💼 Interview Questions")

        st.write(response)

if cover_btn:

    if uploaded_file is None:
        st.warning("Please upload Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
            job_description,
            resume_text,
            COVER_LETTER_PROMPT
        )

        st.subheader("📝 Cover Letter")

        st.write(response)

rewrite_btn = st.button(
    "🖋 Rewrite Resume",
    use_container_width=True
)

if rewrite_btn:

    if uploaded_file is None:
        st.warning("Please upload Resume.")
    elif job_description.strip() == "":
        st.warning("Please enter Job Description.")
    else:

        resume_text = extract_text_from_pdf(uploaded_file)

        response = get_gemini_response(
            job_description,
            resume_text,
            REWRITE_PROMPT
        )

        st.subheader("🖋 Rewritten Resume")

        st.write(response)