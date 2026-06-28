import streamlit as st

from src.services.rag_pipeline import RAGPipeline

from src.ui.styles import load_css

from src.core.state import initialize_state


def initialize_pipeline():

    """
    Load pipeline only once.
    """

    if st.session_state.pipeline is None:

        with st.spinner("Loading AI Models..."):

            st.session_state.pipeline = RAGPipeline()


def startup():

    """
    Boot the entire application.
    """

    initialize_state()

    load_css()

    initialize_pipeline()