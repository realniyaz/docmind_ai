import streamlit as st

# ==========================================================
# CORE
# ==========================================================

from src.core.startup import startup
from src.core.dependency import get_pipeline
from src.core.state import (
    reset_chat,
    reset_pdf,
)

# ==========================================================
# UI
# ==========================================================

from src.ui.sidebar import render_sidebar
from src.ui.dashboard import (
    render_dashboard,
    render_empty_dashboard,
)
from src.ui.chat import render_chat

# ==========================================================
# COMPONENTS
# ==========================================================

from src.ui.components.cards import (
    render_pdf_card,
    render_metric_card,
)

# ==========================================================
# UTILS
# ==========================================================

from src.utils.file_manager import save_pdf


# ==========================================================
# MAIN
# ==========================================================

def main():

    # ------------------------------------------------------
    # INITIALIZE
    # ------------------------------------------------------

    startup()

    pipeline = get_pipeline()

    # ------------------------------------------------------
    # SIDEBAR
    # ------------------------------------------------------

    sidebar = render_sidebar()

    uploaded_file = sidebar["uploaded_file"]

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    if sidebar["clear"]:

        reset_chat()

        st.rerun()

    if sidebar["reset"]:

        reset_chat()

        reset_pdf()

        st.rerun()

    if sidebar["process"]:

        if uploaded_file is None:

            st.warning(
                "Please upload a PDF."
            )

        else:

            save_pdf(uploaded_file)

            with st.spinner(
                "Building Knowledge Base..."
            ):

                pipeline.index_pdf(
                    uploaded_file.name
                )

            st.session_state.pdf_processed = True

            st.session_state.pdf_name = uploaded_file.name

            st.success(
                "Knowledge Base Ready!"
            )

            st.rerun()

    # ------------------------------------------------------
    # HERO
    # ------------------------------------------------------

    if st.session_state.pdf_processed:

        render_dashboard()

    else:

        render_empty_dashboard()

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------------
    # DESKTOP LAYOUT
    # ------------------------------------------------------

    left, right = st.columns(
        [1, 2.35],
        gap="large"
    )

    # ------------------------------------------------------
    # LEFT PANEL
    # ------------------------------------------------------

    with left:

        render_pdf_card()

        st.markdown("<br>", unsafe_allow_html=True)

        stats = st.session_state.get(
            "pdf_stats",
            {}
        )

        col1, col2 = st.columns(2)

        with col1:

            render_metric_card(
                "Pages",
                stats.get("pages", "--"),
                "📄"
            )

        with col2:

            render_metric_card(
                "Chunks",
                stats.get("chunks", "--"),
                "🧩"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        col3, col4 = st.columns(2)

        with col3:

            render_metric_card(
                "Chats",
                len(
                    st.session_state.get(
                        "messages",
                        []
                    )
                ),
                "💬"
            )

        with col4:

            render_metric_card(
                "Status",
                "Ready" if st.session_state.pdf_processed else "Idle",
                "⚡"
            )

    # ------------------------------------------------------
    # CHAT PANEL
    # ------------------------------------------------------

    with right:

        render_chat(
            pipeline
        )


# ==========================================================
# ENTRY
# ==========================================================

if __name__ == "__main__":

    main()