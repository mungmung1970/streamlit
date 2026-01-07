# src/model/vit_model.py

import streamlit as st
from transformers import ViTImageProcessor, ViTForImageClassification

@st.cache_resource
def load_vit_model(model_name: str):
    processor = ViTImageProcessor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(model_name)
    model.eval()
    return processor, model