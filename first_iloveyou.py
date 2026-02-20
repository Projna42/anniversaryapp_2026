import streamlit as st

st.set_page_config(
    page_title="Our Special Day ❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Hide header + footer */
header {visibility: hidden;}
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

/* Remove ALL padding */
.block-container {
    padding: 0 !important;
    margin: 0 !important;
}

/* Remove extra top space */
.css-18e3th9 {
    padding-top: 0 !important;
}

/* Fullscreen wrapper */
.fullscreen-center {
    position: fixed;
    inset: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
    background-color: #fff5f8;
    padding: 20px;
}

/* Text */
.medium {
    font-size: 6vw;
}

.big {
    font-size: 10vw;
    font-weight: 800;
}

/* Desktop font caps */
@media (min-width: 768px) {
    .medium { font-size: 28px; }
    .big { font-size: 48px; }
}

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

# Render center container
st.markdown('<div class="fullscreen-center">', unsafe_allow_html=True)

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
