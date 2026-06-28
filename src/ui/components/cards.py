import streamlit as st


# ==========================================================
# METRIC CARD
# ==========================================================

def render_metric_card(
    title: str,
    value,
    icon: str = "📊",
):

    with st.container(border=True):

        st.markdown(
            f"""
### {icon}

## {value}

**{title}**
"""
        )


# ==========================================================
# INFO CARD
# ==========================================================

def render_info_card(
    title: str,
    body: str,
):

    with st.container(border=True):

        st.subheader(title)

        st.markdown(body)


# ==========================================================
# SOURCE CARD
# ==========================================================

def render_source_card(
    source: str,
    page: int,
):

    with st.container(border=True):

        st.markdown(f"**📄 {source}**")

        st.caption(f"Page {page + 1}")


# ==========================================================
# KNOWLEDGE BASE CARD
# ==========================================================

def render_pdf_card():

    if not st.session_state.get(
        "pdf_processed",
        False
    ):
        return

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

    filename = st.session_state.get(
        "pdf_name",
        "Unknown.pdf"
    )

    with st.container(border=True):

        left, right = st.columns(
            [4, 1]
        )

        with left:

            st.subheader("📚 Knowledge Base")

        with right:

            st.success("Ready")

        st.divider()

        st.markdown(f"### 📄 {filename}")

        st.caption(
            "Indexed and ready for semantic search"
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Pages",
                pages,
                delta=None
            )

        with col2:

            st.metric(
                "Chunks",
                chunks,
                delta=None
            )