import streamlit as st

from src.ui.components.hero import render_hero
from src.ui.components.cards import (
    render_metric_card,
    render_pdf_card,
    render_info_card,
)


# ==========================================================
# DASHBOARD
# ==========================================================

def render_dashboard():

    # ------------------------------------------------------
    # HERO
    # ------------------------------------------------------

    render_hero()

    st.write("")

    # ------------------------------------------------------
    # WORKSPACE
    # ------------------------------------------------------

    left, right = st.columns(
        [1.25, 1],
        gap="large"
    )

    with left:

        render_pdf_card()

    with right:

        render_metrics()


# ==========================================================
# METRICS
# ==========================================================

def render_metrics():

    stats = st.session_state.get(
        "pdf_stats",
        {}
    )

    pages = stats.get(
        "pages",
        "--"
    )

    chunks = stats.get(
        "chunks",
        "--"
    )

    messages = len(
        st.session_state.get(
            "messages",
            []
        )
    )

    response = st.session_state.get(
        "response_time",
        "--"
    )

    st.subheader("📊 Analytics")

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:

        render_metric_card(
            "Pages",
            pages,
            "📄"
        )

    with row1_col2:

        render_metric_card(
            "Chunks",
            chunks,
            "🧩"
        )

    st.write("")

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:

        render_metric_card(
            "Chats",
            messages,
            "💬"
        )

    with row2_col2:

        render_metric_card(
            "Latency",
            response,
            "⚡"
        )


# ==========================================================
# EMPTY DASHBOARD
# ==========================================================

def render_empty_dashboard():

    render_hero()

    st.write("")

    render_info_card(
        "👋 Welcome to DocMind AI",
        """
Upload a PDF from the sidebar to build your personal AI knowledge base.

### You can ask things like:

- 📄 Summarize this document
- 🧠 Explain complex concepts
- 🔍 Find specific information
- 📌 List important points
- 🎓 Generate study notes
- ❓ Create interview questions
        """
    )