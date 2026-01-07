# src/ui/layout.py

import streamlit as st
from PIL import Image

def upload_and_preview_image():
    uploaded_file = st.file_uploader(
        "이미지 파일을 업로드하세요",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is None:
        return None

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="업로드된 이미지", use_container_width=True)

    return image


def show_result(label: str, confidence: float):
    st.metric(
        label="예측 결과",
        value=label,
        delta=f"{confidence * 100:.2f}%"
    )
