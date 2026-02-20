import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Our First I Love You 💖", page_icon="💌")

# --------------------------
# Custom Styling
# --------------------------
st.markdown("""
<style>
    body {
        background-color: #fff0f5;
    }
    .slide-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 40vh;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 28px;
        color: #b30059;
    }
    .slide-text {
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------
# Slides (Image + Text)
# --------------------------
slides = [
    {"text": "Hey mister, are you still falling in love with me?"},
    {"image": "slide1.jpg", "text": "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না"},
    {"image": "slide2.jpg", "text": "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম"},
    {"image": "slide3.jpg", "text": "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'"},
    {"image": "slide4.jpg", "text": "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই"}
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

# Show image only if it exists
if "image" in current_slide:
    image_path = Path(__file__).parent / current_slide["image"]
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, use_column_width=True)
    else:
        st.error(f"Image not found: {current_slide['image']}")

# Show text
st.markdown(
    f'<div class="slide-text">{current_slide["text"]}</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# Navigation
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
