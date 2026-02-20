import streamlit as st

# --------------------------
# Page Config
# --------------------------
st.set_page_config(page_title="Our First I Love You 💖", page_icon="💌")

# --------------------------
# Custom CSS for Centered Slides
# --------------------------
st.markdown("""
<style>
    body {
        background-color: #fff0f5;
    }
    .slide-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 60vh;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 32px;
        color: #b30059;
        padding: 20px;
    }
    .nav-buttons {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------
# Slides Content
# --------------------------
slides = [
    "The first time I said it...",
    "My heart was racing 💓",
    "I didn’t know if you felt the same...",
    "But when you smiled...",
    "I knew 💫",
    "That moment changed everything.",
    "Today marks our first 'I love you' anniversary 💖",
    "And I would say it all over again.",
    "I love you. Always. 💌"
]

# --------------------------
# Session State
# --------------------------
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# --------------------------
# Display Slide
# --------------------------
st.markdown(
    f'<div class="slide-container">{slides[st.session_state.slide_index]}</div>',
    unsafe_allow_html=True
)

# --------------------------
# Navigation Buttons
# --------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    prev, next = st.columns(2)
    
    with prev:
        if st.button("⬅️ Previous"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1

    with next:
        if st.button("Next ➡️"):
            if st.session_state.slide_index < len(slides) - 1:
                st.session_state.slide_index += 1
