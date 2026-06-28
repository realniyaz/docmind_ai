import streamlit as st

from src.ui.components.upload import render_upload
from src.ui.components.status import (
    ready,
    warning,
)


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar():

    with st.sidebar:

        # --------------------------------------------------
        # BRAND
        # --------------------------------------------------

        st.markdown("""
# 🤖 DocMind AI

<span style="color:#6B7280;font-size:14px;">
Private AI Document Assistant
</span>
""", unsafe_allow_html=True)

        st.divider()

        # --------------------------------------------------
        # UPLOAD
        # --------------------------------------------------

        uploaded_file = render_upload()

        st.divider()

        # --------------------------------------------------
        # KNOWLEDGE BASE
        # --------------------------------------------------

        st.markdown("### 📚 Knowledge Base")

        if st.session_state.get(
            "pdf_processed",
            False
        ):

            ready("Knowledge Base Ready")

            st.markdown(f"""
<div style="
background:#F8FAFC;
padding:14px;
border-radius:14px;
border:1px solid #E5E7EB;
margin-top:10px;
margin-bottom:15px;
">

<b>📄 {st.session_state.get("pdf_name","Unknown.pdf")}</b>

</div>
""", unsafe_allow_html=True)

            stats = st.session_state.get(
                "pdf_stats",
                {}
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Pages",
                    stats.get(
                        "pages",
                        "--"
                    )
                )

            with col2:

                st.metric(
                    "Chunks",
                    stats.get(
                        "chunks",
                        "--"
                    )
                )

        else:

            warning(
                "No PDF Indexed"
            )

        st.divider()

        # --------------------------------------------------
        # ACTIONS
        # --------------------------------------------------

        st.markdown("### ⚡ Quick Actions")

        process = st.button(
            "🚀 Process PDF"
        )

        clear = st.button(
            "💬 Clear Chat"
        )

        reset = st.button(
            "♻ Reset Session"
        )

        st.divider()

        # --------------------------------------------------
        # MODEL INFO
        # --------------------------------------------------

        st.markdown("### 🧠 AI Engine")

        st.markdown("""
<div class="card" style="padding:16px;">

<b>LLM</b><br>
🦙 Llama 3.2

<br><br>

<b>Embedding</b><br>
🧠 all-MiniLM-L6-v2

<br><br>

<b>Vector DB</b><br>
💾 ChromaDB

<br><br>

<b>Mode</b><br>
🟢 Fully Local

</div>
""", unsafe_allow_html=True)

        st.divider()

        st.caption("DocMind AI v1.0")

    return {

        "uploaded_file": uploaded_file,

        "process": process,

        "clear": clear,

        "reset": reset,

    }