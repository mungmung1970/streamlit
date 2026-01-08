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


import torch


def classify_image_topk(image, processor, model, top_k=5):
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.softmax(logits, dim=-1)[0]

    topk_probs, topk_indices = probs.topk(top_k)

    results = []
    for idx, prob in zip(topk_indices, topk_probs):
        results.append(
            {"label": model.config.id2label[idx.item()], "score": prob.item()}
        )

    return results
