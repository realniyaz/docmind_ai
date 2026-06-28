import streamlit as st


# ==========================================================
# PAGE LAYOUT
# ==========================================================

def render_layout():

    """
    Creates the overall page layout.

    Returns
    -------
    left_panel : Streamlit Container
    main_panel : Streamlit Container
    """

    left_panel, main_panel = st.columns(
        [1, 2.4],
        gap="large"
    )

    return left_panel, main_panel


# ==========================================================
# DASHBOARD LAYOUT
# ==========================================================

def render_dashboard():

    """
    Creates dashboard columns.
    """

    col1, col2, col3, col4 = st.columns(4)

    return col1, col2, col3, col4


# ==========================================================
# TWO COLUMN
# ==========================================================

def two_columns():

    return st.columns(
        2,
        gap="large"
    )


# ==========================================================
# THREE COLUMN
# ==========================================================

def three_columns():

    return st.columns(
        3,
        gap="large"
    )


# ==========================================================
# FOUR COLUMN
# ==========================================================

def four_columns():

    return st.columns(
        4,
        gap="medium"
    )


# ==========================================================
# SECTION
# ==========================================================

def section(title: str):

    st.markdown(f"## {title}")

    st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# CARD
# ==========================================================

def begin_card():

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True,
    )


def end_card():

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )


# ==========================================================
# SPACING
# ==========================================================

def space(lines=1):

    for _ in range(lines):

        st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# DIVIDER
# ==========================================================

def divider():

    st.divider()


# ==========================================================
# CENTER
# ==========================================================

def center(width=3):

    left, center, right = st.columns(
        [1, width, 1]
    )

    return center


# ==========================================================
# EMPTY STATE
# ==========================================================

def empty_state():

    st.markdown(
        """
<div class="card">

<h2>👋 Welcome to DocMind AI</h2>

<p>
Upload a PDF from the sidebar and start chatting
with your documents using Local AI.
</p>

</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.caption("🦙 Llama 3.2")

    with col2:

        st.caption("💾 ChromaDB")

    with col3:

        st.caption("⚡ 100% Offline")