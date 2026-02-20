import streamlit as st

st.set_page_config(
    page_title="Our Special Day ❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header & footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Remove default padding */
[data-testid="stAppViewContainer"] {
    padding: 0;
    margin: 0;
}

html, body {
    height: 100%;
    overflow: hidden;
}

.stApp {
    background-color: #fff5f8;
}

/* Fullscreen center container */
.center-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
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

/* Desktop font limits */
@media (min-width: 768px) {
    .medium { font-size: 28px; }
    .big { font-size: 48px; }
}

/* Center button */
div.stButton > button {
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# Session state
if "slide" not in st.session_state:
    st.session_state.slide = 0

slides = [
    "সেই দিনটা মনে আছে?",
    "তুমি একটু থেমে গিয়েছিলে...",
    "আমার হৃদয় তখন কাঁপছিল।",
    "তারপর তুমি বলেছিলে —",
    "আমি তোমাকে ভালোবাসি ❤️"
]

# Center container
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
