from transformers import AutoImageProcessor, ViTForImageClassification
import torch
import streamlit as st

@st.cache_resource
def load_vit_model():
    processor = AutoImageProcessor.from_pretrained(
        "google/vit-base-patch16-224"
    )
    model = ViTForImageClassification.from_pretrained(
        "google/vit-base-patch16-224"
    )
    model.eval()
    return processor, model
