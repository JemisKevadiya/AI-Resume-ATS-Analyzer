import google.generativeai as genai

from config.settings import GEMINI_MODEL


def get_gemini_response(job_description, resume_text, prompt):
    """
    Generate response using Gemini.
    """

    model = genai.GenerativeModel(GEMINI_MODEL)

    final_prompt = f"""
{prompt}

-----------------------------
JOB DESCRIPTION
-----------------------------
{job_description}

-----------------------------
RESUME
-----------------------------
{resume_text}
"""

    response = model.generate_content(final_prompt)

    return response.text