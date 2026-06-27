import streamlit as st

from config.settings import (
    APP_TITLE,
    APP_ICON,
    LAYOUT,
)


def setup_page():
    """
    Configure Streamlit page.
    """

    st.set_page_config(
        page_title=APP_TITLE,
        page_icon=APP_ICON,
        layout=LAYOUT,
    )

    st.title("📄 AI Resume ATS Analyzer")

    st.markdown(
        """
Upload your **Resume** and compare it with the **Job Description**
using **Google Gemini AI**.

### Available Features

- 📄 Resume Review
- 🎯 ATS Match Score
- ✨ Improve Resume
- 📚 Missing Skills
- 💼 Interview Questions
- 📝 Cover Letter Generator
- 🖋 Rewrite Resume
"""
    )