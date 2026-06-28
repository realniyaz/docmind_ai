import streamlit as st

from src.services.rag_pipeline import RAGPipeline


def get_pipeline():

    if st.session_state.pipeline is None:

        st.session_state.pipeline = RAGPipeline()

    return st.session_state.pipeline