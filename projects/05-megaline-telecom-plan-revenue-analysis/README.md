# Megaline Telecom Plan Revenue Analysis and Statistical Hypothesis Testing

**TripleTen Data Science Bootcamp — Sprint 5: Statistical Data Analysis**

## Project Overview

This project analyzes customer usage and revenue data for Megaline, a fictional
telecommunications company offering two prepaid plans: Surf and Ultimate.

The analysis combines data preparation, monthly customer-level aggregation,
exploratory data analysis, revenue calculations, and statistical hypothesis
testing. The objective is to compare customer behavior across the two plans and
determine whether their average monthly revenues differ significantly.

## Objective

Prepare and analyze telecommunications usage data to compare customer behavior
and monthly revenue between the Surf and Ultimate plans, and use statistical
hypothesis testing to evaluate differences in revenue between plans and
geographic regions.

## Tasks Performed

- Loaded and inspected five related customer and usage datasets.
- Reviewed data types, missing values, and dataset structure.
- Converted registration, churn, call, message, and internet session dates to
  appropriate datetime types.
- Renamed plan-related fields for consistency with the project data dictionary.
- Converted included mobile data allowances from megabytes to gigabytes.
- Rounded individual call durations according to Megaline billing rules.
- Aggregated monthly calls, minutes, messages, and internet usage for each
  customer.
- Converted monthly internet usage from megabytes to billable gigabytes.
- Combined customer usage, plan, and geographic information into a monthly
  analysis dataset.
- Calculated monthly revenue for each customer according to plan allowances,
  subscription fees, and excess usage charges.
- Compared monthly call, message, internet, and revenue distributions between
  Surf and Ultimate customers.
- Calculated descriptive statistics including means and variances.
- Used histograms and box plots to examine customer behavior and revenue
  distributions.
- Performed a two-sample Welch's t-test to compare average monthly revenue
  between the Surf and Ultimate plans.
- Performed a second Welch's t-test to compare average monthly revenue between
  customers in the NY-NJ area and customers in other regions.

## Statistical Analysis Concepts Practiced

- pandas DataFrames
- Data cleaning and type conversion
- Datetime processing
- Monthly data aggregation
- `groupby()` and aggregation
- DataFrame merging
- Missing-value handling
- NumPy calculations
- Descriptive statistics
- Mean and variance
- Histograms
- Box plots
- Statistical distributions
- Hypothesis formulation
- Significance levels and p-values
- Independent two-sample t-tests
- Welch's t-test
- Statistical interpretation with SciPy

## Datasets

The project uses five related datasets:

- `megaline_users.csv` — customer information including location, registration
  date, churn date, and subscribed plan.
- `megaline_calls.csv` — individual customer calls and call durations.
- `megaline_messages.csv` — individual text messages sent by customers.
- `megaline_internet.csv` — individual mobile internet sessions and data usage.
- `megaline_plans.csv` — plan allowances, monthly fees, and excess usage rates
  for Surf and Ultimate.

The datasets are stored locally in the `datasets/` directory.

## Files

- `project.ipynb` — Jupyter Notebook containing the complete step-by-step
  analysis, explanations, statistical tests, visualizations, and outputs.
- `project.py` — Python script version of the project.
- `datasets/` — Datasets required by the project.
- `requirements.txt` — Python dependencies required to run the project.

## Requirements

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

## How to Run

Python script:

```bash
python project.py
```

The notebook can be opened with Jupyter Notebook, JupyterLab, or VS Code.