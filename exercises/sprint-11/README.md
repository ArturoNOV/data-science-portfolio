# Sprint 11 Exercises — Supervised Learning

## Overview

This folder contains practice exercises from Sprint 11 of the TripleTen Data
Science bootcamp.

The exercises expand on supervised learning concepts introduced in the previous
sprint and focus on preprocessing, imbalanced classification, evaluation
metrics, resampling techniques, and regression model assessment.

## Topics covered

The exercises include practice with:

- One-Hot Encoding
- Ordinal Encoding
- Feature standardization
- Train and validation splitting
- Decision Tree classification
- Logistic Regression
- Class-frequency analysis
- Constant-model baselines
- Confusion matrices
- Precision
- Recall
- F1 score
- ROC curves
- AUC-ROC
- Class weighting
- Upsampling and downsampling
- Data shuffling
- Regression metrics
- Mean Absolute Error
- Mean Squared Error
- R-squared
- Random Forest regression
- Model comparison and evaluation

## Datasets

The exercises use four datasets:

- `travel_insurance_us.csv`
- `travel_insurance_us_preprocessed.csv`
- `flights.csv`
- `flights_preprocessed.csv`

The travel insurance datasets are used for classification and class-imbalance
exercises.

The flight datasets are used for regression and model-evaluation exercises.

The script accesses all datasets through the local `datasets/` directory using a
reusable `read_file()` helper.

## Models and tools used

The exercises include:

- `DecisionTreeClassifier`
- `LogisticRegression`
- `LinearRegression`
- `RandomForestRegressor`
- `OrdinalEncoder`
- `StandardScaler`

Evaluation tools include:

- `accuracy_score`
- `confusion_matrix`
- `precision_score`
- `recall_score`
- `f1_score`
- `roc_auc_score`
- `roc_curve`
- `mean_absolute_error`
- `mean_squared_error`
- `r2_score`

## Technologies

- Python
- pandas
- NumPy
- Matplotlib
- scikit-learn

## Folder structure

```text
sprint-11/
├── README.md
├── exercises.py
├── requirements.txt
└── datasets/
    ├── flights.csv
    ├── flights_preprocessed.csv
    ├── travel_insurance_us.csv
    └── travel_insurance_us_preprocessed.csv
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

These files are practice exercises from the TripleTen Data Science bootcamp and
are separate from the main Sprint 11 project.

The purpose of this folder is to document the progression from basic supervised
learning evaluation toward handling class imbalance, threshold-independent
metrics, resampling strategies, and regression model assessment.
