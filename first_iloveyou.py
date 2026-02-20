import streamlit as st

st.set_page_config(page_title="Our Moment ❤️")

# --- Styling ---
st.markdown("""
<style>
.big {
    font-size:40px;
    font-weight:800;
    text-align:center;
}
.medium {
    font-size:26px;
    text-align:center;
}
.stApp {
    background-color:#fff5f8;
}
</style>
""", unsafe_allow_html=True)

# --- Session state for slide tracking ---
if "slide" not in st.session_state:
    st.session_state.slide = 0

# --- Slides ---
slides = [
    "সেই দিনটা মনে আছে?",
    "তুমি একটু থেমে গিয়েছিলে...",
    "আমার হৃদয় তখন কাঁপছিল।",
    "তারপর তুমি বলেছিলে —",
    "আমি তোমাকে ভালোবাসি ❤️"
]

# --- Display current slide ---
if st.session_state.slide < len(slides) - 1:
    st.markdown(
        f'<div class="medium">{slides[st.session_state.slide]}</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f'<div class="big">{slides[st.session_state.slide]}</div>',
        unsafe_allow_html=True
    )
    st.balloons()

# --- Button ---
if st.button("Next ❤️"):
    if st.session_state.slide < len(slides) - 1:
        st.session_state.slide += 1
        st.rerun()
