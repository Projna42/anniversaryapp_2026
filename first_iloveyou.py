import streamlit as st
import base64
import time

st.set_page_config(
    page_title="Our First I Love You 💖",
    page_icon="💌",
    layout="wide"
)

# ---------------------------------
# Autoplay Music (inject once)
# ---------------------------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        audio_html = f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

if "music_loaded" not in st.session_state:
    autoplay_audio("music.mp3")
    st.session_state.music_loaded = True

# ---------------------------------
# Slides (edit timing here)
# ---------------------------------
slides = [
    {"image": "slide1.jpg", "text": "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না", "duration": 4},
    {"image": "slide2.jpg", "text": "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম", "duration": 4},
    {"image": "slide3.jpg", "text": "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'", "duration": 4},
    {"image": "slide4.jpg", "text": "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই", "duration": 4},
    {"text": "Will you keep falling in love with me?", "duration": 5},
    {"image": "final.jpg", "text": "", "duration": 100}
]

# ---------------------------------
# Placeholder for slide content
# ---------------------------------
placeholder = st.empty()

for slide in slides:

    with placeholder.container():

        # Background image
        if "image" in slide:
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url("{slide['image']}");
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                .stApp {
                    background: black;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

        # Dark overlay
        st.markdown(
            """
            <div style="
                position:fixed;
                top:0;
                left:0;
                width:100%;
                height:100%;
                background:rgba(0,0,0,0.6);
                z-index:-1;">
            </div>
            """,
            unsafe_allow_html=True
        )

        # Text
        if slide["text"]:
            st.markdown(
                f"""
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    height:80vh;
                    text-align:center;
                    color:white;
                    font-size:42px;
                    font-family:Georgia, serif;
                ">
                    {slide['text']}
                </div>
                """,
                unsafe_allow_html=True
            )

    time.sleep(slide["duration"])

# After slideshow ends, stop rerun
st.stop()
