import streamlit as st
from pathlib import Path
import base64

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

# ---------- SLIDES ----------
slides = [
    {"image": "slide1.jpg", "text": "কারণ আমি তো চুমু দেওয়া আর নেওয়ার মধ্যে পার্থক্য জানি না"},
    {"image": "slide2.jpg", "text": "কারণ আমি তো বড্ড অগোছালো, বাচ্চাদের থেকেও অধম"},
    {"image": "slide3.jpg", "text": "কারণ আমি তো 'আপনাকে অনেক ভালোবাসি'"},
    {"image": "slide4.jpg", "text": "কারণ আমি তো তোমাকে মরার আগ পর্যন্ত জ্বালাতে চাই"},
    
    # Dramatic Question Slide
    {"text": "Will you keep falling in love with me?"},

    # ✅ Final Cinematic Image Slide
    {"image": "slide4.jpg", "text": ""}
]

slides_js = ",".join([f'"{s}"' for s in slides])

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
    letter-spacing: 1px;
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
    transition: 0.4s;
}}

button:hover {{
    background-color: #ff1a8c;
    transform: translateX(-50%) scale(1.1);
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

.cursor {{
    border-right: 3px solid white;
    animation: blink 1s infinite;
}}

@keyframes blink {{
    0% {{border-color: white;}}
    50% {{border-color: transparent;}}
    100% {{border-color: white;}}
}}

</style>
</head>
<body>

<div class="background"></div>
<div class="overlay"></div>

<div class="container">
    <div id="text"></div>
</div>

<button onclick="startShow()">Begin 💖</button>

{f'<audio id="bgmusic" loop src="data:audio/mp3;base64,{music_base64}"></audio>' if music_base64 else ''}

<script>

let slides = [{slides_js}];
let index = 0;
let started = false;

function typeWriter(text, element, speed=50) {{
    let i = 0;
    element.innerHTML = "";
    function typing() {{
        if (i < text.length) {{
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, speed);
        }}
    }}
    typing();
}}

function showSlide() {{
    const textDiv = document.getElementById("text");
    typeWriter(slides[index], textDiv, 50);
    index++;
    if (index < slides.length) {{
        setTimeout(showSlide, 6000);
    }}
}}

function startShow() {{
    if (!started) {{
        started = true;
        document.querySelector("button").style.display = "none";
        document.getElementById("bgmusic")?.play();
        showSlide();
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
