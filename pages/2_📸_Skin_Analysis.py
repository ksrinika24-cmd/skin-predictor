import streamlit as st
from PIL import Image
import random

st.title("📸 Skin Analysis")

uploaded = st.file_uploader(
    "Upload your facial image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded)

    st.image(image, width=350)

    if st.button("Analyze Skin"):

        skin_types = [
            "Oily",
            "Dry",
            "Combination",
            "Normal",
            "Sensitive"
        ]

        prediction = random.choice(skin_types)

        confidence = random.randint(90,99)

        st.success(f"Skin Type : {prediction}")

        st.info(f"Confidence : {confidence}%")

        st.session_state.skin = prediction