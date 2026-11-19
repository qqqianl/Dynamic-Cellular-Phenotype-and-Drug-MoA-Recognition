"""Classification and retrieval metrics for learned cell representations."""

from __future__ import annotations

import numpy as np


def classification_metrics(labels, logits) -> dict[str, float | int]:
    labels = np.asarray(labels, dtype=int)
    predictions = np.asarray(logits).argmax(axis=1)
    if len(labels) != len(predictions):
        raise ValueError("labels and logits must contain the same number of samples")
    return {
        "samples": int(len(labels)),
        "correct": int((labels == predictions).sum()),
        "accuracy": float((labels == predictions).mean()),
    }


def retrieval_rank1(query_features, gallery_features, query_labels, gallery_labels) -> float:
    """Compute cosine-similarity Rank-1 accuracy."""
    queries = np.asarray(query_features, dtype=np.float32)
    gallery = np.asarray(gallery_features, dtype=np.float32)
    queries /= np.maximum(np.linalg.norm(queries, axis=1, keepdims=True), 1e-12)
    gallery /= np.maximum(np.linalg.norm(gallery, axis=1, keepdims=True), 1e-12)
    nearest = (queries @ gallery.T).argmax(axis=1)
    return float((np.asarray(gallery_labels)[nearest] == np.asarray(query_labels)).mean())

