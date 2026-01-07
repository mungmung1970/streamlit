# src/inference/classify.py

import torch

def classify_image(image, processor, model):
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_idx = logits.argmax(-1).item()
    label = model.config.id2label[predicted_idx]
    confidence = torch.softmax(logits, dim=-1)[0][predicted_idx].item()

    return label, confidence
