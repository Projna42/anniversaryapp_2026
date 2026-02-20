import streamlit as st

st.set_page_config(
    page_title="Our Special Day ❤️",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    height: 100%;
    margin: 0;
}

.stApp {
    background-color: #fff5f8;
}

/* Full screen center wrapper */
.center-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
    text-align: center;
    padding: 20px;
}

/* Text styles */
.medium {
    font-size: 6vw;
}

.big {
    font-size: 10vw;
    font-weight: 800;
}

/* Limit font size on large screens */
@media (min-width: 768px) {
    .medium { font-size: 28px; }
    .big { font-size: 48px; }
}

/* Button center */
div.stButton > button {
    display: block;
    margin: 30px auto 0 auto;
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "slide" not in st.session_state:
    st.session_state.slide = 0

slides = [
    "সেই দিনটা মনে আছে?",
    "তুমি একটু থেমে গিয়েছিলে...",
    "আমার হৃদয় তখন কাঁপছিল।",
    "তারপর তুমি বলেছিলে —",
    "আমি তোমাকে ভালোবাসি ❤️"
]

# ---------- Content ----------
st.markdown('<div class="center-wrapper">', unsafe_allow_html=True)

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

if st.button("Next ❤️"):
    if st.session_state.slide < len(slides) - 1:
        st.session_state.slide += 1
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
