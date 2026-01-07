import streamlit as st


@st.cache_resource
def load_vit_model(model_name: str):
    from transformers import AutoImageProcessor, ViTForImageClassification

    processor = AutoImageProcessor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(model_name)
    model.eval()

    return processor, model
