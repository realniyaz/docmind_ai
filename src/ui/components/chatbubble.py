import time
import streamlit as st


# ==========================================================
# USER MESSAGE
# ==========================================================

def render_user(message: str):

    with st.chat_message(
        "user",
        avatar="🧑‍💻"
    ):

        st.markdown(message)


# ==========================================================
# ASSISTANT MESSAGE
# ==========================================================

def render_assistant(message: str):

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        st.markdown(message)


# ==========================================================
# STREAMING RESPONSE
# ==========================================================

def typing_animation(
    message: str,
    speed: float = 0.01
):

    placeholder = st.empty()

    response = ""

    for word in message.split():

        response += word + " "

        placeholder.markdown(response + "▌")

        time.sleep(speed)

    placeholder.markdown(response)

    return response


# ==========================================================
# THINKING STATUS
# ==========================================================

def thinking():

    return st.status(
        "🧠 Thinking...",
        expanded=True
    )


# ==========================================================
# UPDATE STATUS
# ==========================================================

def update_status(
    status,
    step: str
):

    status.write(step)


# ==========================================================
# COMPLETE STATUS
# ==========================================================

def complete_status(
    status
):

    status.update(
        label="✅ Response Ready",
        state="complete",
        expanded=False
    )


# ==========================================================
# ERROR STATUS
# ==========================================================

def error_status(
    status,
    message: str
):

    status.update(
        label="❌ Error",
        state="error",
        expanded=True
    )

    status.write(message)


# ==========================================================
# RESPONSE TIME
# ==========================================================

def response_time(seconds: float):

    st.caption(
        f"⚡ Generated in **{seconds:.2f}s**"
    )


# ==========================================================
# EMPTY CHAT
# ==========================================================

def render_empty_chat():

    st.info(
        """
### 👋 Welcome to DocMind AI

Upload a PDF and start asking questions.

#### Examples

- Summarize this document
- Explain the main concepts
- List all important points
- Give me interview questions
- Create study notes
"""
    )