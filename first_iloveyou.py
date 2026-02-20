import streamlit as st
from pathlib import Path
from PIL import Image
import base64

st.set_page_config(page_title="Our First I Love You 💖", page_icon="💌")

# --------------------------
# Load Background Music
# --------------------------
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Put your mp3 in same folder as app
music_file = Path(__file__).parent / "music.mp3"
if music_file.exists():
    autoplay_audio(str(music_file))


# --------------------------
# Romantic CSS Styling
# --------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fff0f5, #ffe6f2);
    overflow: hidden;
}

/* Slide container */
.slide-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 70vh;
    text-align: center;
    font-family: 'Georgia', serif;
    font-size: 30px;
    color: #b30059;
    animation: fadeIn 1.5s ease-in-out;
}

/* Cute buttons */
.stButton>button {
    background-color: #ff99cc;
    color: white;
    border-radius: 30px;
    border: none;
    padding: 10px 25px;
    font-size: 18px;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #ff4da6;
    transform: scale(1.1);
}

/* Floating hearts animation */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 24px;
    animation: floatUp 8s linear infinite;
    color: #ff4da6;
}

@keyframes floatUp {
    0% {transform: translateY(0); opacity: 1;}
    100% {transform: translateY(-100vh); opacity: 0;}
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

</style>
""", unsafe_allow_html=True)

# --------------------------
# Floating Hearts
# --------------------------
for i in range(15):
    st.markdown(
        f'<div class="heart" style="left:{i*7}%;">💖</div>',
        unsafe_allow_html=True
    )

# --------------------------
# Slides
# --------------------------
slides = [
    {"text": "Hey mister, are you still falling in love with me?"},
    {"image": "slide1.jpg", "text": "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না"},
    {"image": "slide2.jpg", "text": "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম"},
    {"image": "slide3.jpg", "text": "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'"},
    {"image": "slide4.jpg", "text": "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই 💕"}
]

# --------------------------
# Session State
# --------------------------
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

current_slide = slides[st.session_state.slide_index]

# --------------------------
# Display Slide
# --------------------------
st.markdown('<div class="slide-container">', unsafe_allow_html=True)

if "image" in current_slide:
    image_path = Path(__file__).parent / current_slide["image"]
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, use_column_width=True)

st.markdown(f'<div>{current_slide["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# Navigation
# --------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    prev, next = st.columns(2)

    with prev:
        if st.button("💌 Previous"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1

    with next:
        if st.button("Next 💖"):
            if st.session_state.slide_index < len(slides) - 1:
                st.session_state.slide_index += 1
