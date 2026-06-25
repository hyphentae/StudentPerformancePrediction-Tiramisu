# Student Performance Prediction

Educational Practice 2025–2026 Summer Project  
Team: **Tiramisu**  
Group: **IT-2512**  
Track: **Machine Learning**

## About the project

This is our Educational Practice mini-project.  
We chose the Machine Learning track and made a simple project for predicting student performance.

The main idea of the project is to predict a student's **math score** using information from the dataset, such as reading score, writing score, lunch type, test preparation course, and other student background features.

This project was made as a first-year student team project, so our main goal was to understand the full basic Machine Learning workflow:

- how to work with a dataset;
- how to prepare data before training;
- how to train models;
- how to check model results;
- how to use the model in a small web application.

## Team information

| Field | Information |
|------|-------------|
| Academic group | IT-2512 |
| Team name | Tiramisu |
| Project track | Machine Learning |
| Project topic | Student performance prediction |

## Team members

| No. | Name | Role | Main contribution |
|---:|------|------|-------------------|
| 1 | Aisultan Beiimbet | Team Lead | Flask web app, project setup, README, integration, final submission |
| 2 | Miras Zhumazhan | ML Engineer | Model training, model comparison, evaluation results |
| 3 | Alizhan Manap | Data Analyst | Dataset, data preprocessing, basic data analysis |

## Problem statement

Student performance can depend on many factors. For example, reading score and writing score can be related to math score. Also, background features such as lunch type or test preparation course may give useful information.

In this project, we tried to build a Machine Learning model that predicts the final math score of a student. This is a regression task, because the result is a number.

## Dataset

We used a student performance dataset with 1,000 student records.

Main columns in the dataset:

| Type | Columns |
|------|---------|
| Categorical features | gender, race/ethnicity, parental level of education, lunch, test preparation course |
| Numerical features | reading score, writing score |
| Target column | math score |

## What the project does

The project:

1. Loads the dataset.
2. Prepares the data for Machine Learning.
3. Splits the data into features and target.
4. Trains regression models.
5. Checks model quality using evaluation metrics.
6. Saves or uses the best model.
7. Runs a Flask web app where the user can enter student information.
8. Shows the predicted math score.

## Tools and technologies

| Category | Tools |
|---------|-------|
| Programming language | Python |
| Data processing | pandas, NumPy |
| Machine Learning | scikit-learn |
| Web application | Flask |
| Frontend | HTML |
| Version control | Git and GitHub |


## How to run the project

### 1. Clone the repository

```bash
git clone https://github.com/aitu-educational-practice-2026/educational-practice-project-tiramisu.git
cd educational-practice-project-tiramisu
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

For macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python run.py
```

### 5. Open the web application

After running the project, open this link in the browser:

```text
http://127.0.0.1:5000
```

Then fill in the form and click the prediction button to get the predicted math score.

## Model evaluation

For evaluation, we used regression metrics such as:

- R² score;
- MAE;
- RMSE.

These metrics help us understand how close the predicted math scores are to the real values.

## Demo video

Demo video link: `https://youtu.be/6uMGwwZqiAc`

In the demo video, we show:

1. Our GitHub repository.
2. How the project runs.
3. Main model result or prediction example.
4. Team members' contributions.

## Report

The full report is submitted separately as a PDF file.  
It includes project overview, methodology, screenshots, evaluation results, difficulties, conclusion, and links.

## Submission

The final submission is made by the team leader on Moodle.

Submission includes:

- GitHub repository link;
- Report PDF;
- Demo video link;
- Contribution table.

## Conclusion

During this project, we practiced the basic steps of a Machine Learning project. We learned how to prepare data, train a model, evaluate results, and connect the model to a simple web application. The project helped us understand how Machine Learning can be used for student performance prediction.

Made by **Team Tiramisu**.
