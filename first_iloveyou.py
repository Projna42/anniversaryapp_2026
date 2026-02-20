import streamlit as st
from pathlib import Path
from PIL import Image
import base64

st.set_page_config(page_title="Our First I Love You 💖", page_icon="💌")

# --------------------------
# Romantic CSS
# --------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #fff0f5, #ffe6f2);
}

/* Slide container */
.slide-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 65vh;
    padding-bottom: 100px;
    text-align: center;
    font-family: 'Georgia', serif;
    font-size: 60px;
    color: #b30059;
    animation: fadeIn 1.2s ease-in-out;
      
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
    transform: scale(1.08);
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -20px;
    font-size: 20px;
    animation: floatUp 10s linear infinite;
    color: #ff4da6;
    pointer-events: none;
    z-index: 0;
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
st.markdown("<div style='height:100px;'></div>", unsafe_allow_html=True)

# --------------------------
# Floating Hearts (Safe)
# --------------------------
for i in range(12):
    st.markdown(
        f'<div class="heart" style="left:{i*8}%;">💖</div>',
        unsafe_allow_html=True
    )

# --------------------------
# Music Section (Button Triggered)
# --------------------------
# --------------------------
# Music Section (Persistent)
# --------------------------
music_file = Path(__file__).parent / "music.mp3"

if "music_playing" not in st.session_state:
    st.session_state.music_playing = False

col_music1, col_music2, col_music3 = st.columns([1,2,1])

with col_music2:
    if st.button("🎵 Play Our Song and scroll down below"):
        st.session_state.music_playing = True

if music_file.exists() and st.session_state.music_playing:
    with open(music_file, "rb") as f:
        audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()

        audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)


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

st.markdown(current_slide["text"])

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
