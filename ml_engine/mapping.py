# mapping.py
import json


FEATURE_GROUPS = {
    "size": [
        "mean radius",
        "mean area",
        "worst radius",
        "worst area"
    ],
    "texture": [
        "mean texture",
        "texture error",
        "worst texture"
    ],
    "shape": [
        "mean symmetry",
        "symmetry error",
        "worst symmetry"
    ],
    "edge": [
        "mean concavity",
        "mean concave points",
        "worst concavity",
        "worst concave points"
    ],
    "complexity": [
        "mean fractal dimension",
        "fractal dimension error",
        "worst fractal dimension"
    ]
}



SCALE_MAP = {
    1: -2.0,
    2: -1.0,
    3:  0.0,
    4:  1.0,
    5:  2.0
}

def build_feature_vector(user_answers, feature_order_path="feature_order.json"):
    # Load feature order
    with open(feature_order_path, "r") as f:
        feature_order = json.load(f)

    # Start with neutral values
    features = {name: 0.0 for name in feature_order}

    # Apply user answers
    for question, answer in user_answers.items():
        if question not in FEATURE_GROUPS:
            continue

        value = SCALE_MAP.get(answer, 0.0)

        for feature in FEATURE_GROUPS[question]:
            if feature in features:
                features[feature] = value

    # Return ordered list
    return [features[name] for name in feature_order]



if __name__ == "__main__":
    sample_answers = {
        "size": 5,
        "texture": 3,
        "shape": 2,
        "edge": 4,
        "complexity": 3
    }

    vector = build_feature_vector(sample_answers)
    print("Feature vector length:", len(vector))
    print(vector)
