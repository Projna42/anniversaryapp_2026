import streamlit as st
import base64
import os

st.set_page_config(page_title="Our First I Love You 💖", page_icon="💌", layout="wide")

# ==============================
# Load Music (auto-play safe)
# ==============================
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Only load once
if "music_started" not in st.session_state:
    autoplay_audio("music.mp3")  # Put music.mp3 in same folder
    st.session_state.music_started = True

# ==============================
# Slides
# ==============================
slides = [
    {"image": "slide1.jpg", "text": "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না"},
    {"image": "slide2.jpg", "text": "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম"},
    {"image": "slide3.jpg", "text": "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'"},
    {"image": "slide4.jpg", "text": "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই"},
    {"text": "Will you keep falling in love with me?"},
    {"image": "slide4.jpg", "text": ""}
]

if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

current_slide = slides[st.session_state.slide_index]

# ==============================
# CSS Styling
# ==============================
st.markdown("""
<style>

html, body, .stApp {
    height: 100%;
    margin: 0;
    overflow: hidden;
    background: black;
}

/* Blur overlay */
.overlay {
    position: fixed;
    top:0; left:0;
    width:100%; height:100%;
    backdrop-filter: blur(12px);
    background: rgba(0,0,0,0.4);
}

/* Typewriter */
.typewriter {
    position: absolute;
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);
    color: white;
    font-size: 42px;
    font-family: Georgia, serif;
    text-align: center;
    animation: fadeIn 3s ease-in-out forwards;
}

/* Fade animation */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 24px;
    animation: float 10s linear infinite;
    color: #ff4d6d;
}

@keyframes float {
    0% {transform: translateY(0) scale(1);}
    100% {transform: translateY(-100vh) scale(1.5);}
}

/* Cute buttons */
.stButton>button {
    background-color: #ff4d6d;
    color: white;
    font-size: 20px;
    border-radius: 30px;
    padding: 10px 25px;
    border: none;
    box-shadow: 0 0 20px #ff4d6d;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #ff1e56;
    transform: scale(1.1);
    box-shadow: 0 0 30px #ff1e56;
}

.bottom-space {
    height: 150px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# Background Image
# ==============================
if "image" in current_slide:
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{current_slide['image']}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

# Overlay
st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)

# ==============================
# Floating Hearts Generator
# ==============================
for i in range(15):
    st.markdown(
        f'<div class="heart" style="left:{i*7}%;">💖</div>',
        unsafe_allow_html=True
    )

# ==============================
# Text Display
# ==============================
if "text" in current_slide and current_slide["text"]:
    st.markdown(f"""
        <div class="typewriter">
            {current_slide["text"]}
        </div>
    """, unsafe_allow_html=True)

# ==============================
# Navigation
# ==============================
col1, col2, col3 = st.columns([1,2,1])

with col2:
    prev, next_btn = st.columns(2)

    with prev:
        if st.button("⬅️ Previous"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1

    with next_btn:
        if st.button("Next ➡️"):
            if st.session_state.slide_index < len(slides) - 1:
                st.session_state.slide_index += 1

st.markdown('<div class="bottom-space"></div>', unsafe_allow_html=True)
