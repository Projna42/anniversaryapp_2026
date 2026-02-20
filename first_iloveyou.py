import streamlit as st
from datetime import date

st.set_page_config(page_title="Our Special Day ❤️")

# Soft romantic background
st.markdown("""
<style>
.stApp {
    background-color: #fff5f8;
}
.big-text {
    font-size:28px;
    font-weight:600;
}
</style>
""", unsafe_allow_html=True)

st.title("❤️ Do You Remember This Day? ❤️")

st.write("A small memory for us...")

if st.button("Click if you dare 💌"):
    st.markdown("---")
    
    st.markdown(
        '<p class="big-text">It was the day everything changed.</p>',
        unsafe_allow_html=True
    )

    st.write("You looked at me.")
    st.write("There was that tiny pause.")
    st.write("And then you said it...")

    st.markdown("## I love you. ❤️")

    st.balloons()

    st.markdown("""
    That moment still lives in my heart.
    And today, I celebrate the first time
    you chose me with those words.

    I still choose you.
    Every single day.
    """)
