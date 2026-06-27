import streamlit as st


def create_buttons():
    """
    Create all action buttons.
    Returns all button states.
    """

    col1, col2, col3 = st.columns(3)

    with col1:
        review_btn = st.button(
            "📄 Resume Review",
            use_container_width=True,
        )

    with col2:
        ats_btn = st.button(
            "🎯 ATS Match Score",
            use_container_width=True,
        )

    with col3:
        improve_btn = st.button(
            "✨ Improve Resume",
            use_container_width=True,
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        skills_btn = st.button(
            "📚 Missing Skills",
            use_container_width=True,
        )

    with col5:
        interview_btn = st.button(
            "💼 Interview Questions",
            use_container_width=True,
        )

    with col6:
        cover_btn = st.button(
            "📝 Cover Letter",
            use_container_width=True,
        )

    st.markdown("---")

    rewrite_btn = st.button(
        "🖋 Rewrite Resume",
        use_container_width=True,
    )

    return (
        review_btn,
        ats_btn,
        improve_btn,
        skills_btn,
        interview_btn,
        cover_btn,
        rewrite_btn,
    )