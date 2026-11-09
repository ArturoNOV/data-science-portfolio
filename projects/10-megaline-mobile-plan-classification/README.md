# Megaline Mobile Plan Classification

## Project overview

This project develops a supervised machine learning classification model for a fictional telecommunications company, Megaline.

The goal is to predict whether a customer is better represented by the **Smart** or **Ultra** mobile plan based on monthly usage behavior, including calls, minutes, text messages, and mobile data consumption.

The project was completed as part of the TripleTen Data Science bootcamp.

## Objective

Build and evaluate a classification model capable of predicting the customer's mobile plan with an accuracy of at least **0.75**.

The workflow includes:

- Initial data inspection and validation
- Train, validation, and test dataset splitting
- Stratification to preserve class proportions
- Comparison of multiple classification algorithms
- Hyperparameter tuning
- Final evaluation on previously unseen test data
- Comparison against a majority-class baseline

## Dataset

The dataset contains **3,214 observations** and the following variables:

- `calls` — number of calls
- `minutes` — total call duration in minutes
- `messages` — number of text messages
- `mb_used` — mobile data consumption in megabytes
- `is_ultra` — target variable:
  - `0` = Smart plan
  - `1` = Ultra plan

The initial analysis found no missing values or duplicated rows.

The target variable is moderately imbalanced:

- Smart: approximately 69%
- Ultra: approximately 31%

A stratified split was therefore used to maintain similar class proportions across the training, validation, and test datasets.

## Data preparation

The data was divided into:

- **60% training**
- **20% validation**
- **20% test**

A fixed `random_state` was used to make the results reproducible.

The test dataset was kept separate during model selection and hyperparameter tuning.

## Models evaluated

Three classification algorithms were compared.

### Decision Tree

Different values of `max_depth` from 1 to 10 were evaluated.

Best validation result:

- `max_depth = 5`
- Validation accuracy: **0.8165**

### Random Forest

Multiple combinations of `n_estimators` and `max_depth` were evaluated.

Best configuration:

- `n_estimators = 10`
- `max_depth = 8`
- Validation accuracy: **0.8320**

### Logistic Regression

The logistic regression model achieved:

- Training accuracy: **0.7464**
- Validation accuracy: **0.7558**

## Model comparison

| Model | Validation accuracy |
| --- | ---: |
| Random Forest | 0.8320 |
| Decision Tree | 0.8165 |
| Logistic Regression | 0.7558 |

The Random Forest model produced the strongest validation performance and was selected for final evaluation.

## Final model

The selected Random Forest model was retrained using the combined training and validation datasets.

Final results:

- Training accuracy: **0.8608**
- Test accuracy: **0.8149**

The test result exceeds the minimum project requirement of 0.75.

## Sanity check

A majority-class classifier was used as a baseline.

Because Smart (`0`) is the most frequent class, the baseline always predicts Smart.

Results:

- Majority-class baseline accuracy: **0.6936**
- Random Forest test accuracy: **0.8149**

The trained model therefore improves accuracy by approximately **12.1 percentage points** over the simple baseline strategy.

## Key conclusions

- All three evaluated models reached or exceeded the project's target validation accuracy.
- Random Forest produced the strongest validation performance.
- The selected model retained good performance on previously unseen test data.
- The final model significantly outperformed the majority-class baseline.
- Increasing model complexity did not automatically improve validation performance, highlighting the importance of hyperparameter tuning and independent validation data.

## Technologies

- Python
- pandas
- scikit-learn
- Jupyter Notebook

## Project structure

```text
10-megaline-mobile-plan-classification/
├── README.md
├── project.ipynb
├── project.py
├── requirements.txt
└── datasets/
    └── users_behavior.csv
```

## Running the project

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Python version:

```bash
python project.py
```

The Jupyter Notebook version can also be opened and executed from the project directory.

## Notes

This is an academic Data Science project based on a fictional business scenario provided as part of the TripleTen Data Science bootcamp.

The objective is to demonstrate a reproducible supervised classification workflow, including model comparison, validation, hyperparameter selection, final testing, and baseline evaluation.
