import streamlit as st


def render_upload():

    with st.container(border=True):

        st.markdown("### 📄 Upload Document")

        st.caption(
            "Upload a PDF to create your private knowledge base."
        )

        uploaded_file = st.file_uploader(
    label="Choose a PDF",
    type=["pdf"],
    help="Supported format: PDF",
)

        col1, col2 = st.columns(2)

        with col1:
            st.caption("📑 PDF")

        with col2:
            st.caption("⚡ Local AI")

    return uploaded_file