import streamlit as st

st.set_page_config(page_title="Our First I Love You 💖", layout="wide")

# -----------------------------
# Slides
# -----------------------------
slides = [
    {"image": "slide1.jpg", "text": "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না"},
    {"image": "slide2.jpg", "text": "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম"},
    {"image": "slide3.jpg", "text": "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'"},
    {"image": "slide4.jpg", "text": "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই"},
    {"text": "Will you keep falling in love with me?"},
    {"image": "slide4.jpg", "text": ""}
]

# -----------------------------
# Session state
# -----------------------------
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

current_slide = slides[st.session_state.slide_index]

# -----------------------------
# Display Image
# -----------------------------
if "image" in current_slide:
    st.image(current_slide["image"], use_container_width=True)

# -----------------------------
# Display Text
# -----------------------------
if "text" in current_slide and current_slide["text"]:
    st.markdown(
        f"<h2 style='text-align:center;'>{current_slide['text']}</h2>",
        unsafe_allow_html=True
    )

# -----------------------------
# Navigation
# -----------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    left, right = st.columns(2)

    with left:
        if st.button("Previous"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1

    with right:
        if st.button("Next"):
            if st.session_state.slide_index < len(slides) - 1:
                st.session_state.slide_index += 1
