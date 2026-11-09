# Beta Bank Customer Churn Prediction

## Project overview

This project develops a supervised machine learning model to predict customer
churn for a fictional financial institution, Beta Bank.

The objective is to identify customers who are more likely to leave the bank
using demographic, financial, and account-related characteristics. The project
focuses on class imbalance, model comparison, hyperparameter tuning, and
evaluation with metrics that are more informative than accuracy alone.

The project was completed as part of the TripleTen Data Science bootcamp.

## Objective

Build a classification model that achieves an **F1 score of at least 0.59** on
the reserved test dataset.

The workflow includes:

- Initial data inspection and validation
- Missing-value analysis and treatment
- Removal of identifier columns
- One-Hot Encoding of categorical variables
- Train, validation, and test splitting
- Feature standardization where appropriate
- Analysis of class imbalance
- Comparison of multiple classification algorithms
- Class weighting and upsampling
- Hyperparameter tuning
- Final evaluation using F1 and AUC-ROC

## Dataset

The dataset contains **10,000 customer records** and 14 original columns.

The target variable is:

- `Exited = 0` — customer remained with the bank
- `Exited = 1` — customer left the bank

The initial analysis identified:

- 909 missing values in `Tenure`
- No fully duplicated rows
- No duplicated `CustomerId` values
- A substantial class imbalance, with approximately 20% of customers belonging
  to the positive churn class

Identifier fields such as row number, customer ID, and surname were excluded
from model training.

## Data preparation

The dataset was divided into:

- **60% training**
- **20% validation**
- **20% test**

The target distribution was preserved across the subsets.

Missing `Tenure` values were imputed using the median learned from the training
data only.

Categorical variables were transformed with One-Hot Encoding. Numerical
features were standardized where required, using parameters learned exclusively
from the training set.

This approach helps prevent information leakage from the validation or test
datasets into model training.

## Models evaluated

The project compares three classification algorithms:

- Decision Tree
- Random Forest
- Logistic Regression

Initial models were trained without correcting the class imbalance. Additional
experiments then evaluated:

- `class_weight='balanced'`
- Hyperparameter tuning
- Upsampling of the minority class

## Initial model performance

The first models showed that accuracy alone would not be sufficient for this
problem because of the imbalance in the target variable.

Validation results included:

| Model | F1 validation | AUC-ROC validation |
| --- | ---: | ---: |
| Random Forest | 0.5556 | 0.8536 |
| Decision Tree | 0.4982 | 0.6868 |
| Logistic Regression | 0.3215 | 0.7876 |

The tree-based models also showed strong overfitting in their initial
configurations, which motivated further tuning.

## Hyperparameter tuning and class balancing

The strongest Decision Tree configuration reached:

- `max_depth = 8`
- Validation F1: **0.5796**
- Validation AUC-ROC: **0.8074**

The strongest Random Forest configuration using class weights reached:

- `n_estimators = 100`
- `max_depth = 10`
- `class_weight = 'balanced'`
- Validation F1: **0.6376**
- Validation AUC-ROC: **0.8656**

A separate Random Forest trained on an upsampled training dataset achieved:

- `n_estimators = 100`
- `max_depth = 10`
- Validation F1: **0.6384**
- Validation AUC-ROC: **0.8647**

The upsampled Random Forest produced the highest validation F1 and was selected
for final evaluation.

## Final model

The selected model was:

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=12345
)
```

The model was trained on an upsampled version of the training dataset.

Final test results:

- **F1 score: 0.6250**
- **AUC-ROC: 0.8655**

The F1 score exceeded the project requirement of 0.59.

The difference between validation and test F1 was only 0.0134, indicating that
the selected model maintained similar performance on previously unseen data.

## Model comparison

The most relevant validation results were:

| Model | Balancing approach | F1 validation | AUC-ROC validation |
| --- | --- | ---: | ---: |
| Random Forest | Upsampling | 0.6384 | 0.8647 |
| Random Forest | Class weight | 0.6376 | 0.8656 |
| Decision Tree | No balancing | 0.5796 | 0.8074 |
| Random Forest | No balancing | 0.5705 | 0.8705 |
| Logistic Regression | Class weight | 0.5113 | 0.7918 |

The two balanced Random Forest approaches produced very similar results. The
upsampling configuration was selected because it obtained the highest F1 score
in validation.

## Key conclusions

- The target variable was substantially imbalanced, making F1 a more useful
  primary metric than accuracy.
- Initial unrestricted tree models showed clear signs of overfitting.
- Hyperparameter tuning substantially improved model generalization.
- Both class weighting and upsampling improved Random Forest performance.
- The selected upsampled Random Forest exceeded the required F1 threshold on the
  independent test set.
- AUC-ROC remained stable between validation and test, supporting the model's
  ability to distinguish between customers who leave and those who remain.
- Model predictions should be interpreted as estimates of churn risk rather
  than certainty about future customer behavior.

## Technologies

- Python
- pandas
- scikit-learn
- Jupyter Notebook

## Project structure

```text
11-beta-bank-customer-churn-prediction/
├── README.md
├── project.ipynb
├── project.py
├── requirements.txt
└── datasets/
    └── Churn.csv
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

The Jupyter Notebook version can also be opened and executed from the project
directory.

## Notes

This is an academic Data Science project based on a fictional business scenario
provided as part of the TripleTen Data Science bootcamp.

The project demonstrates a supervised classification workflow for imbalanced
data, including preprocessing, model comparison, hyperparameter tuning,
resampling, validation, and final testing.
