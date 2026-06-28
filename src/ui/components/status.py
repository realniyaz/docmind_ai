import streamlit as st


# ==========================================================
# READY
# ==========================================================

def ready(message="Knowledge Base Ready"):

    st.success(
        message,
        icon="✅"
    )


# ==========================================================
# PROCESSING
# ==========================================================

def processing(message="Processing Document..."):

    st.info(
        message,
        icon="⏳"
    )


# ==========================================================
# WARNING
# ==========================================================

def warning(message):

    st.warning(
        message,
        icon="⚠️"
    )


# ==========================================================
# ERROR
# ==========================================================

def error(message):

    st.error(
        message,
        icon="🚨"
    )


# ==========================================================
# OFFLINE
# ==========================================================

def offline():

    st.caption(
        "🟢 Local AI • Offline Mode"
    )


# ==========================================================
# BADGE
# ==========================================================

def badge(
    text,
    color="#2563EB"
):

    st.markdown(
        f"""
<div style="
display:inline-block;
padding:7px 14px;
background:{color}15;
border:1px solid {color}40;
border-radius:999px;
color:{color};
font-size:13px;
font-weight:600;
">

{text}

</div>
""",
        unsafe_allow_html=True
    )