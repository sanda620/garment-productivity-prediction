# Garment Worker Productivity Prediction and Production Analytics

## Project Overview

This project applies Data Science and Machine Learning techniques to analyse and predict worker productivity in the garment manufacturing industry.

Using historical garment production data, the project explores the factors influencing actual productivity, performs data preprocessing and exploratory data analysis, and develops regression models to predict worker productivity.

The main objective is to demonstrate how data-driven insights can support production monitoring, workforce planning, and operational decision-making in manufacturing environments.

## Objectives

- Explore and understand garment manufacturing productivity data.
- Identify factors associated with actual worker productivity.
- Perform data cleaning, preprocessing, and feature engineering.
- Develop and compare regression models.
- Apply chronological train-test splitting and date-based cross-validation.
- Evaluate model performance using appropriate regression metrics.
- Analyse prediction errors across departments and production dates.

## Dataset

**Source:** [UCI Machine Learning Repository – Productivity Prediction of Garment Employees](https://archive.ics.uci.edu/dataset/597/productivity)

- Records: 1,197
- Features: 15 original columns
- Industry: Garment manufacturing
- Target variable: `actual_productivity`

The dataset includes information about departments, teams, working hours, incentives, production targets, and other manufacturing-related factors.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook

## Project Workflow

### 1. Exploratory Data Analysis

- Examined dataset structure and statistical summaries.
- Investigated missing values and duplicate records.
- Analysed actual productivity distributions.
- Explored productivity patterns across departments, weekdays, and dates.
- Examined relationships between numerical features and actual productivity.

### 2. Data Preprocessing

- Converted date values into datetime format.
- Extracted month and day-of-month features.
- Separated independent variables and the target variable.
- Applied StandardScaler to numerical features.
- Applied OneHotEncoder to categorical features.
- Excluded WIP from the initial all-department model because all its missing values were associated with the finishing department.

### 3. Model Development

Developed and evaluated the following regression models:

- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### 4. Model Optimization

- Used chronological train-test splitting to evaluate future-date generalization.
- Applied TimeSeriesSplit using unique production dates for cross-validation.
- Used a Scikit-learn Pipeline to prevent preprocessing leakage during hyperparameter tuning.
- Applied RandomizedSearchCV to optimize Random Forest hyperparameters.
- Compared models with and without `targeted_productivity` to investigate its predictive contribution.

### 5. Model Evaluation

The final tuned Random Forest model achieved the following test results:

| Metric | Score |
|---|---:|
| MAE | 0.089323 |
| RMSE | 0.132207 |
| R² Score | 0.332342 |

The model was also evaluated through actual-versus-predicted plots, residual analysis, department-level error analysis, and daily prediction performance.

### 6. Key Findings

- `targeted_productivity` was the most important feature in the initial Random Forest feature-importance analysis.
- Removing `targeted_productivity` reduced model performance.
- The model performed better on sewing records than finishing records.
- Finishing records had higher prediction errors and a tendency toward overprediction.
- WIP was missing for all finishing records, limiting the ability to investigate its independent relationship with productivity.
- Prediction errors varied across production dates.

## Repository Structure

```text
manufacturing-demand-forecasting/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_garment_productivity_eda.ipynb
│   └── 02_data_preprocessing.ipynb
│
├── src/
│   └── data/
│       └── download_data.py
│
├── reports/
│   ├── actual_vs_predicted.png
│   ├── residual_distribution.png
│   ├── department_residuals.png
│   └── daily_prediction_error.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Limitations

- The dataset contains only 1,197 observations covering approximately 70 calendar days.
- The model's test R² score indicates that substantial productivity variation remains unexplained.
- Missing WIP values are completely associated with the finishing department.
- Department-level performance differs considerably.
- The results are based on one chronological test period and should be validated on additional production periods before real-world deployment.
