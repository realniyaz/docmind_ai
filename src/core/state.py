import streamlit as st


DEFAULT_STATE = {
    "pipeline": None,
    "messages": [],
    "pdf_processed": False,
    "pdf_name": "",
    "pdf_stats": {},
    "theme": "light",
}


def initialize_state():

    """
    Initialize Streamlit Session State
    """

    for key, value in DEFAULT_STATE.items():

        if key not in st.session_state:

            st.session_state[key] = value


def reset_chat():

    st.session_state.messages = []


def reset_pdf():

    st.session_state.pdf_processed = False

    st.session_state.pdf_name = ""

    st.session_state.pdf_stats = {}


def reset_all():

    reset_chat()

    reset_pdf()