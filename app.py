import os
import pickle

from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = {
        "gender": [request.form["gender"]],
        "race/ethnicity": [request.form["race_ethnicity"]],
        "parental level of education": [request.form["parental_level_of_education"]],
        "lunch": [request.form["lunch"]],
        "test preparation course": [request.form["test_preparation_course"]],
        "reading score": [float(request.form["reading_score"])],
        "writing score": [float(request.form["writing_score"])],
    }

    df = pd.DataFrame(data)
    pred = model.predict(df)[0]

    return render_template("index.html", prediction=round(float(pred), 2))


if __name__ == "__main__":
    app.run(debug=True)