# Sprint 10 Exercises — Introduction to Machine Learning

## Overview

This folder contains practice exercises from Sprint 10 of the TripleTen Data Science bootcamp.

The exercises introduce core supervised machine learning concepts through classification and regression tasks. They include model training, prediction, evaluation metrics, train/validation splitting, hyperparameter comparison, and baseline error calculations.

## Topics covered

The exercises include practice with:

- Creating classification targets from continuous values
- Separating features and target variables
- Training and using classification models
- Generating predictions for new observations
- Measuring classification errors
- Calculating accuracy manually and with scikit-learn
- Comparing training and test performance
- Tuning decision tree depth
- Using train/validation splits
- Tuning random forest models
- Training logistic regression models
- Calculating mean squared error (MSE)
- Calculating root mean squared error (RMSE)
- Training decision tree regressors
- Training random forest regressors
- Training linear regression models

## Models used

The exercises use the following scikit-learn estimators:

- `DecisionTreeClassifier`
- `RandomForestClassifier`
- `LogisticRegression`
- `DecisionTreeRegressor`
- `RandomForestRegressor`
- `LinearRegression`

## Datasets

The exercises use two real-estate datasets:

- `train_data_us.csv` — training data
- `test_data_us.csv` — test data

The script accesses these files through a local `datasets/` directory using a reusable `read_file()` helper.

## Technologies

- Python
- pandas
- scikit-learn

## Folder structure

```text
sprint-10/
├── README.md
├── exercises.py
├── requirements.txt
└── datasets/
    ├── train_data_us.csv
    └── test_data_us.csv
```

## Running the exercises

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the exercises:

```bash
python exercises.py
```

## Notes

These files are practice exercises from the TripleTen Data Science bootcamp and are separate from the main Sprint 10 project.

The goal of this folder is to document the progression from basic supervised learning concepts to model evaluation and hyperparameter tuning.
