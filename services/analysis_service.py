from services.pdf_service import extract_text_from_pdf
from services.gemini_service import get_gemini_response


def analyze_resume(uploaded_file, job_description, prompt):
    """
    Complete Resume Analysis Pipeline

    1. Extract text from PDF
    2. Send prompt to Gemini
    3. Return AI response
    """

    resume_text = extract_text_from_pdf(uploaded_file)

    response = get_gemini_response(
        job_description,
        resume_text,
        prompt
    )

    return response