# ml_engine/predict.py
# -----------------------------------
# Handles ML prediction using a trained model
# -----------------------------------

import os
import json
import pickle
import pandas as pd
import numpy as np
from .mapping import build_feature_vector

# -----------------------------------
# Base directory of this file (ml_engine/)
# -----------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----------------------------------
# Load feature configuration
# -----------------------------------
FEATURE_ORDER_PATH = os.path.join(BASE_DIR, "feature_order.json")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

with open(FEATURE_ORDER_PATH, "r") as f:
    FEATURE_ORDER = json.load(f)

# -----------------------------------
# Load trained ML artifacts
# -----------------------------------
with open(MODEL_PATH, "rb") as f:
    MODEL = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    SCALER = pickle.load(f)

# -----------------------------------
# Prediction function
# -----------------------------------
def predict_risk(user_answers):
    """
    Takes user answers as a dictionary and returns
    a human-friendly risk category.
    """

    # Convert user answers into numeric feature vector
    vector = build_feature_vector(user_answers, feature_order_path=FEATURE_ORDER_PATH)

    # Wrap input in DataFrame to preserve feature names
    X_df = pd.DataFrame([vector], columns=FEATURE_ORDER)

    # Apply same scaling used during training
    X_scaled = SCALER.transform(X_df)

    # Make prediction
    prediction = MODEL.predict(X_scaled)[0]

    # Convert numeric output to readable result
    return "Higher Pattern Concern" if prediction == 0 else "Lower Pattern Concern"


# -----------------------------------
# Simple local tests (safe to remove later)
# -----------------------------------
if __name__ == "__main__":
    test_case_1 = {
        "size": 2,
        "texture": 1,
        "shape": 1,
        "edge": 2,
        "complexity": 1
    }

    test_case_2 = {
        "size": 8,
        "texture": 7,
        "shape": 6,
        "edge": 8,
        "complexity": 7
    }

    print("Test 1 - Lower-like values:", predict_risk(test_case_1))
    print("Test 2 - Higher-like values:", predict_risk(test_case_2))