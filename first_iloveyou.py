import streamlit as st

st.set_page_config(page_title="Our Moment ❤️", layout="wide")

# --- Styling ---
st.markdown("""
<style>
.stApp {
    background-color:#fff5f8;
}

.center-container {
    height: 50vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.medium {
    font-size: 28px;
}

.big {
    font-size: 48px;
    font-weight: 800;
}
</style>
""", unsafe_allow_html=True)

# --- Session state ---
if "slide" not in st.session_state:
    st.session_state.slide = 0

slides = [
    "সেই দিনটা মনে আছে?",
    "তুমি একটু থেমে গিয়েছিলে...",
    "আমার হৃদয় তখন কাঁপছিল।",
    "তারপর তুমি বলেছিলে —",
    "আমি তোমাকে ভালোবাসি ❤️"
]

# --- Display ---
st.markdown('<div class="center-container">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)

# --- Button ---
col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Next ❤️"):
        if st.session_state.slide < len(slides) - 1:
            st.session_state.slide += 1
            st.rerun()
