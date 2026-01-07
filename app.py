# app.py

import streamlit as st

from src.config.settings import (
    MODEL_NAME,
    PAGE_TITLE,
    PAGE_ICON,
)
from src.model.vit_model import load_vit_model
from src.inference.classify import classify_image
from src.ui.layout import (
    upload_and_preview_image,
    show_result,
)

# -------------------------------------------------
# 페이지 설정
# -------------------------------------------------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)

st.title("🖼️ Image Classification App")

# -------------------------------------------------
# 모델 로딩
# -------------------------------------------------
processor, model = load_vit_model(MODEL_NAME)

# -------------------------------------------------
# UI + 추론
# -------------------------------------------------
image = upload_and_preview_image()

if image is not None:
    if st.button("분류 실행"):
        with st.spinner("이미지를 분석 중입니다..."):
            label, confidence = classify_image(
                image=image,
                processor=processor,
                model=model,
            )

        show_result(label, confidence)
