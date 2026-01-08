# src/ui/layout.py

import streamlit as st
from PIL import Image


def upload_and_preview_image():
    uploaded_file = st.file_uploader(
        "이미지 파일을 업로드하세요", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is None:
        return None

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="업로드된 이미지", use_container_width=True)

    return image


def show_result(label: str, confidence: float):
    st.metric(label="예측 결과", value=label, delta=f"{confidence * 100:.2f}%")


def show_topk_results(results):
    """
    results: [
      {"label": str, "score": float},
      ...
    ]
    """

    st.markdown("### 📊 모델 예측 결과")

    for i, pred in enumerate(results, start=1):
        label = pred["label"]
        score = pred["score"]

        if i == 1:
            # ✅ Top-1 강조
            st.markdown(
                f"""
<div style="
    background-color:#E8F5E9;
    padding:14px;
    border-radius:8px;
    border-left:6px solid #2E7D32;
">
🥇 <strong>{label}</strong><br>
신뢰도: <strong>{score * 100:.2f}%</strong>
</div>
""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(f"- **{i}. {label}** : {score * 100:.2f}%")

        st.progress(score)
