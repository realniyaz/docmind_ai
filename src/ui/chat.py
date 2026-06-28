import time
import streamlit as st

from src.ui.components.chatbubble import (
    render_user,
    render_assistant,
    typing_animation,
    thinking,
    response_time,
)

from src.ui.components.cards import (
    render_source_card,
)


# ==========================================================
# CHAT
# ==========================================================

def render_chat(pipeline):

    st.markdown("## 💬 AI Conversation")

    if not st.session_state.get("pdf_processed", False):

        st.info(
            "👈 Upload and process a PDF to start chatting."
        )

        return

    display_history()

    question = st.chat_input(
        "Ask anything about your document..."
    )

    if question:

        handle_question(
            pipeline,
            question
        )


# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

def display_history():

    messages = st.session_state.get(
        "messages",
        []
    )

    if not messages:

        st.markdown("""
<div class="card" style="text-align:center;padding:50px;">

<h3>🚀 Start Your Conversation</h3>

<p style="color:#6B7280;">
Ask questions, summarize your PDF, extract insights,
or explore any topic from your uploaded document.
</p>

</div>
""", unsafe_allow_html=True)

        return

    for message in messages:

        if message["role"] == "user":

            render_user(
                message["content"]
            )

        else:

            render_assistant(
                message["content"]
            )

            sources = message.get(
                "sources",
                []
            )

            if sources:

                with st.expander(
                    f"📚 Sources ({len(sources)})",
                    expanded=False
                ):

                    for source in sources:

                        render_source_card(
                            source["source"],
                            source["page"]
                        )


# ==========================================================
# HANDLE QUESTION
# ==========================================================

def handle_question(
    pipeline,
    question,
):

    # -------------------------------
    # Save User Message
    # -------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    render_user(question)

    # -------------------------------
    # Generate Response
    # -------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        status = thinking()

        start = time.perf_counter()

        try:

            result = pipeline.ask(
                question
            )

            elapsed = round(
                time.perf_counter() - start,
                2
            )

            answer = result["answer"]

            sources = result.get(
                "sources",
                []
            )

            typing_animation(
                answer
            )

            status.update(
                label="Response Generated",
                state="complete"
            )

            response_time(
                elapsed
            )

            st.session_state.response_time = (
                f"{elapsed}s"
            )

            if sources:

                with st.expander(
                    f"📚 Sources ({len(sources)})"
                ):

                    for source in sources:

                        render_source_card(
                            source["source"],
                            source["page"]
                        )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                }
            )

        except Exception as e:

            status.update(
                label="Error",
                state="error"
            )

            st.error(str(e))