import streamlit as st
from pathlib import Path
import base64
import json

st.set_page_config(layout="wide")

# ---------- LOAD MUSIC ----------
music_base64 = ""
music_file = Path("music.mp3")
if music_file.exists():
    with open(music_file, "rb") as f:
        music_base64 = base64.b64encode(f.read()).decode()

# ---------- LOAD BACKGROUND IMAGE ----------
bg_base64 = ""
bg_file = Path("background.jpg")
if bg_file.exists():
    with open(bg_file, "rb") as f:
        bg_base64 = base64.b64encode(f.read()).decode()

# ---------- TEXT SLIDES ----------
slides = [
    "Hey mister...",
    "Are you still falling in love with me?",
    "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না...",
    "কারণ আমি তো বড্ড অগোছালো...",
    "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'...",
    "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই...",
    "But tell me something...",
    "Will you keep falling in love with me? 💍"
]

slides_js = json.dumps(slides)

# ---------- IMAGE SLIDES ----------
image_files = ["slide1.jpg", "slide2.jpg", "slide3.jpg"]

image_slides = []
for img in image_files:
    if Path(img).exists():
        with open(img, "rb") as f:
            image_slides.append(base64.b64encode(f.read()).decode())

images_js = json.dumps(image_slides)

# ---------- HTML ----------
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
    font-family: Georgia, serif;
    color: white;
}}

.background {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("data:image/jpg;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    filter: blur(8px) brightness(0.4);
    z-index: -2;
}}

.overlay {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(0,0,0,0.6), rgba(20,0,20,0.9));
    z-index: -1;
}}

.container {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    padding: 40px;
    font-size: 2.2rem;
}}

#slideImage {{
    max-width: 70%;
    border-radius: 20px;
    margin-top: 30px;
    display: none;
}}

button {{
    position: absolute;
    bottom: 60px;
    left: 50%;
    transform: translateX(-50%);
    background-color: #ff4da6;
    border: none;
    padding: 15px 45px;
    border-radius: 50px;
    color: white;
    font-size: 18px;
    cursor: pointer;
}}

.heart {{
    position: fixed;
    bottom: -20px;
    font-size: 20px;
    animation: floatUp 12s linear infinite;
    color: #ff66cc;
    opacity: 0.8;
}}

@keyframes floatUp {{
    0% {{transform: translateY(0); opacity: 1;}}
    100% {{transform: translateY(-100vh); opacity: 0;}}
}}

</style>
</head>
<body>

<div class="background"></div>
<div class="overlay"></div>

<div class="container">
    <div>
        <div id="text"></div>
        <img id="slideImage">
    </div>
</div>

<button onclick="startShow()">Begin 💖</button>

{f'<audio id="bgmusic" loop src="data:audio/mp3;base64,{music_base64}"></audio>' if music_base64 else ''}

<script>

let slides = {slides_js};
let images = {images_js};

let textIndex = 0;
let imageIndex = 0;
let started = false;

function typeWriter(text, element, speed, callback) {{
    let i = 0;
    element.innerHTML = "";

    function typing() {{
        if (i < text.length) {{
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }} else {{
            if (callback) callback();
        }}
    }}
    typing();
}}

function showTextSlides() {{
    const textDiv = document.getElementById("text");

    typeWriter(slides[textIndex], textDiv, 50, function() {{
        textIndex++;

        if (textIndex < slides.length) {{
            setTimeout(showTextSlides, 2000);
        }} else {{
            setTimeout(startImageSlideshow, 2000);
        }}
    }});
}}

function startImageSlideshow() {{
    const textDiv = document.getElementById("text");
    const img = document.getElementById("slideImage");

    textDiv.style.display = "none";
    img.style.display = "block";

    function showNextImage() {{
        if (imageIndex >= images.length) return;

        img.src = "data:image/jpg;base64," + images[imageIndex];
        imageIndex++;
        setTimeout(showNextImage, 4000);
    }}

    showNextImage();
}}

function startShow() {{
    if (!started) {{
        started = true;
        document.querySelector("button").style.display = "none";
        document.getElementById("bgmusic")?.play();
        showTextSlides();
    }}
}}

// Floating hearts
for (let i = 0; i < 20; i++) {{
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "💖";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (8 + Math.random()*6) + "s";
    document.body.appendChild(heart);
}}

</script>

</body>
</html>
"""

st.components.v1.html(html_code, height=900)
