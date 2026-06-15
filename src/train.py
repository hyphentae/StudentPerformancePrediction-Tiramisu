# src/train.py
import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

import pickle

from preprocessing import build_preprocessor


def main():
    # путь к корню проекта: ../ от src
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", "students.csv")

    # 1. Загружаем данные
    df = pd.read_csv(data_path)

    # предполагаем, что целевая колонка называется "math_score"
    X = df.drop("math score", axis=1)
    y = df["math score"]

    # 2. train / test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Препроцессор
    preprocessor = build_preprocessor()

    # 4. Модели для сравнения
    models = {
        "Linear Regression": LinearRegression(),
        "Ridge": Ridge(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    }

    best_model = None
    best_name = None
    best_r2 = -999.0

    print(f"{'Model':<20} {'R2':>8} {'MAE':>8} {'RMSE':>8}")
    print("-" * 50)

    # 5. Обучаем и оцениваем каждую модель
    for name, model in models.items():
        pipe = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ("model", model),
            ]
        )

        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        print(f"{name:<20} {r2:>8.4f} {mae:>8.4f} {rmse:>8.4f}")

        if r2 > best_r2:
            best_r2 = r2
            best_model = pipe
            best_name = name

    print()
    print(f"Best model: {best_name} (R2 = {best_r2:.4f})")

    # 6. Сохраняем лучшую модель в корне проекта рядом с app.py
    model_path = os.path.join(base_dir, "model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(best_model, f)

    print(f"Saved best model to: {model_path}")


if __name__ == "__main__":
    main()