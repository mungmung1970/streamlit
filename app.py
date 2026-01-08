# app.py
import sys
import os

# -------------------------------------------------
# Python path 설정 (Cloud 안정화)
# -------------------------------------------------
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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
# 페이지 설정 (⚠ 반드시 최상단)
# -------------------------------------------------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)

st.title("🖼️ Image Classification App")

# -------------------------------------------------
# 모델 로딩 (단 1회)
# -------------------------------------------------
try:
    processor, model = load_vit_model(MODEL_NAME)
except Exception as e:
    st.error("모델 로딩 중 오류 발생")
    st.exception(e)
    st.stop()

# -------------------------------------------------
# UI + 추론
# -------------------------------------------------
image = upload_and_preview_image()

if image is not None:
    if st.button("분류 실행"):
        with st.spinner("이미지를 분석 중입니다..."):
            results = classify_image_topk(
                image=image,
                processor=processor,
                model=model,
                top_k=5,
            )

        show_topk_results(results)
