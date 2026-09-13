import argparse
import joblib
import numpy as np
from pathlib import Path


# Get the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load the trained Logistic Regression model
MODEL_PATH = PROJECT_ROOT / "models" / "logistic_regression_iris_model.pkl"

model = joblib.load(MODEL_PATH)

# Iris species names
species_names = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}


def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predict the Iris flower species from four measurements.
    """

    features = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    prediction = model.predict(features)[0]

    return species_names[prediction]


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Predict Iris flower species using Logistic Regression."
    )

    parser.add_argument(
        "--sepal-length",
        type=float,
        required=True,
        help="Sepal length in cm"
    )

    parser.add_argument(
        "--sepal-width",
        type=float,
        required=True,
        help="Sepal width in cm"
    )

    parser.add_argument(
        "--petal-length",
        type=float,
        required=True,
        help="Petal length in cm"
    )

    parser.add_argument(
        "--petal-width",
        type=float,
        required=True,
        help="Petal width in cm"
    )

    args = parser.parse_args()

    flower = predict_flower(
        args.sepal_length,
        args.sepal_width,
        args.petal_length,
        args.petal_width
    )

    print(f"Predicted Flower Species: {flower}")