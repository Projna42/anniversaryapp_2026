import streamlit as st
from pathlib import Path
import base64

st.set_page_config(layout="wide")

# --------- LOAD MUSIC ----------
music_file = Path("music.mp3")
music_base64 = ""

if music_file.exists():
    with open(music_file, "rb") as f:
        music_base64 = base64.b64encode(f.read()).decode()

# --------- LOAD IMAGE ----------
image_file = Path("slide4.jpg")
image_base64 = ""

if image_file.exists():
    with open(image_file, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode()

# --------- SLIDES CONTENT ----------
slides = [
    "Hey mister, are you still falling in love with me?",
    "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না",
    "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম",
    "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'",
    "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই 💕"
]

slides_js = ",".join([f'"{s}"' for s in slides])

# --------- FULLSCREEN HTML ----------
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
    background: linear-gradient(135deg, #1a001a, #330033);
    color: white;
    font-family: Georgia, serif;
}}

.container {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    font-size: 2rem;
    padding: 40px;
    transition: opacity 2s ease-in-out;
}}

.fade {{
    opacity: 0;
}}

.heart {{
    position: fixed;
    bottom: -20px;
    font-size: 20px;
    animation: floatUp 12s linear infinite;
    color: #ff66cc;
}}

@keyframes floatUp {{
    0% {{transform: translateY(0); opacity: 1;}}
    100% {{transform: translateY(-100vh); opacity: 0;}}
}}

button {{
    position: absolute;
    bottom: 50px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #ff66cc;
    border: none;
    padding: 15px 40px;
    border-radius: 50px;
    color: white;
    font-size: 18px;
    cursor: pointer;
    transition: 0.3s;
}}

button:hover {{
    background-color: #ff3399;
    transform: translateX(-50%) scale(1.1);
}}

</style>
</head>
<body>

<div class="container" id="slide">
Click to Begin 💖
</div>

<button onclick="startShow()">Start Our Story</button>

{f'<audio id="bgmusic" autoplay loop src="data:audio/mp3;base64,{music_base64}"></audio>' if music_base64 else ''}

<script>



let slides = [{slides_js}];
let index = 0;
let started = false;
let interval;

function startShow() {
    if (!started) {
        started = true;
        document.querySelector("button").style.display = "none";
        document.getElementById("bgmusic")?.play();
        showSlide();
    }
}

function typeWriter(text, element, speed = 40) {
    let i = 0;
    element.innerHTML = "";

    function typing() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }
    }

    typing();
}

function showSlide() {
    const slideDiv = document.getElementById("slide");

    if (index < slides.length) {
        slideDiv.classList.add("fade");

        setTimeout(() => {
            slideDiv.classList.remove("fade");
            typeWriter(slides[index], slideDiv);
            index++;
            setTimeout(showSlide, 5000);
        }, 1000);

    } else {
        // SHOW FINAL IMAGE
        slideDiv.classList.add("fade");

        setTimeout(() => {
            slideDiv.classList.remove("fade");
            slideDiv.innerHTML = `<img src="data:image/jpg;base64,{image_base64}" style="max-width:80%; border-radius:20px; box-shadow:0 0 30px #ff66cc;">`;
        }, 1000);
    }
}

// floating hearts (unchanged)
for (let i = 0; i < 15; i++) {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "💖";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (8 + Math.random()*6) + "s";
    document.body.appendChild(heart);
}



</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=800)
