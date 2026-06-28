import streamlit as st


def render_hero():

    pdf_loaded = st.session_state.get(
        "pdf_processed",
        False
    )

    status = "🟢 Ready" if pdf_loaded else "🟡 Waiting for PDF"

    with st.container(border=True):

        left, right = st.columns(
            [4, 1],
            gap="large"
        )

        with left:

            st.title("🤖 DocMind AI")

            st.caption(
                "Private AI Document Assistant powered by Local LLMs."
            )

            st.write("")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.success("🦙 Llama 3.2")

            with c2:
                st.info("🧠 MiniLM")

            with c3:
                st.info("💾 ChromaDB")

            with c4:
                st.success("🔒 Local")

        with right:

            st.metric(
                "Status",
                status
            )

            st.write("")

            st.caption("### Features")

            st.write("📄 Chat with PDFs")

            st.write("🔍 Semantic Search")

            st.write("⚡ Fast Retrieval")