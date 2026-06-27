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
"""
    )

    # Push footer to bottom
    st.markdown("", unsafe_allow_html=True)

    # Footer
    st.markdown(
        """
        <hr>
        <div style="text-align:center; color:gray; font-size:14px;">
            👨‍💻 Developed with ❤️ by <b>Jemis Kevadiya</b><br>
            © 2026 AI Resume ATS Analyzer. All Rights Reserved.
        </div>
        """,
        unsafe_allow_html=True,
    )