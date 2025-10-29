import pandas as pd
import numpy as np
import shap
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

DATA_PATH = "data/Dataset_Health.csv"
MODEL_PATH = "models/model.pkl"
TARGET = "Steps_Day_1"

def train_model():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=[TARGET])
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(f"Using target column: {TARGET}")
    print("Detected problem type: regression")

    model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=5, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Regression R²: {r2:.3f} | MSE: {mse:.4f}")

    print("Generating SHAP explanations...")
    try:
        explainer = shap.TreeExplainer(model)
        shap_values = explainer(X_test)
    except Exception as e:
        print(f"TreeExplainer failed: {e}")
        print("Falling back to shap.Explainer (model-agnostic)...")
        explainer = shap.Explainer(model.predict, X_test)
        shap_values = explainer(X_test)

    os.makedirs("shap_plots", exist_ok=True)
    plt.title("Feature Impact (SHAP Summary)")
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig("shap_plots/summary_plot.png", bbox_inches="tight")
    print("Saved SHAP summary plot to shap_plots/summary_plot.png")

if __name__ == "__main__":
    train_model()
