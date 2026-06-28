import streamlit as st


def initialize():

    defaults = {

        "messages": [],

        "pdf_processed": False,

        "pdf_name": "",

        "pipeline": None,

        "stats": {}

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def clear_chat():

    st.session_state.messages = []


def reset_pdf():

    st.session_state.pdf_processed = False

    st.session_state.pdf_name = ""

    st.session_state.stats = {}