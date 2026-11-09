# Data Science Portfolio

This repository contains a growing collection of Data Science projects developed
through hands-on training and independent portfolio work.

The projects document my progression from Python fundamentals and data
preparation to exploratory data analysis, statistical inference, SQL,
reproducible data workflows, interactive applications, and supervised machine
learning.

My goal is to present work that is not only technically correct, but also clear,
reproducible, and connected to practical business questions.

> **Portfolio status:** actively expanding. Additional Data Science and Machine
> Learning projects will be added as they are completed and prepared for public
> presentation.

---

## Featured Projects

### 1. Beta Bank Customer Churn Prediction

[View project](projects/11-beta-bank-customer-churn-prediction/)

Supervised machine learning project focused on predicting customer churn from
imbalanced data using preprocessing, model comparison, hyperparameter tuning,
class weighting, and upsampling.

Highlights:

- Prepared independent training, validation, and test datasets.
- Treated missing values without using information from reserved datasets.
- Applied One-Hot Encoding and feature standardization.
- Compared Decision Tree, Random Forest, and Logistic Regression models.
- Evaluated class weighting and upsampling strategies.
- Selected an upsampled Random Forest with a validation F1 of 0.6384.
- Achieved a final test F1 of 0.6250 and AUC-ROC of 0.8655.

**Tools:** Python, pandas, scikit-learn, Jupyter Notebook

---

### 2. Megaline Mobile Plan Classification

[View project](projects/10-megaline-mobile-plan-classification/)

Supervised machine learning project for predicting whether customer usage
patterns correspond to the Smart or Ultra mobile plan in a fictional
telecommunications scenario.

Highlights:

- Prepared stratified training, validation, and test datasets.
- Compared Decision Tree, Random Forest, and Logistic Regression classifiers.
- Tuned model hyperparameters using validation performance.
- Selected a Random Forest model with a validation accuracy of 0.8320.
- Achieved a final test accuracy of 0.8149.
- Compared the final model against a majority-class baseline of 0.6936.

**Tools:** Python, pandas, scikit-learn, Jupyter Notebook

---

### 3. Chicago Taxi Rides Analysis

[View project](projects/08-chicago-taxi-rides-analysis/)

Analysis of Chicago taxi activity combining SQL, Python, exploratory analysis,
and statistical hypothesis testing.

Highlights:

- Analyzed taxi company activity and destination patterns.
- Tested whether weather conditions were associated with differences in
  Saturday trip duration between the Loop and O'Hare.
- Reconstructed the SQL workflow locally in PostgreSQL.
- Added a reproducible pipeline using public Chicago taxi data.
- Included a deterministic 100,000-row sample for practical GitHub
  reproducibility.
- Documented the distinction between the original academic results and the
  locally reconstructed database.

**Tools:** Python, pandas, Matplotlib, SciPy, PostgreSQL, SQL, Requests,
Beautiful Soup, lxml

---

### 4. Used Vehicle Listings Dashboard

[View project](projects/07-used-vehicle-listings-dashboard/)

Interactive web application for exploring used-vehicle advertisements in the
United States.

Highlights:

- Built an interactive Streamlit application.
- Visualized vehicle mileage distribution.
- Explored the relationship between price and mileage.
- Added a Jupyter Notebook with exploratory data analysis.
- Deployed the application publicly on Render.

**Tools:** Python, pandas, Plotly, Streamlit, Jupyter Notebook

**Live application:**  
[Open the live application](https://used-vehicle-listings-dashboard.onrender.com)

---

### 5. Video Game Sales Market Analysis

[View project](projects/06-video-game-sales-market-analysis/)

Integrated market analysis using historical video game sales data to identify
commercial patterns relevant to advertising and product strategy.

Highlights:

- Performed data cleaning and exploratory analysis.
- Examined platform life cycles and sales performance.
- Compared regional market behavior across North America, Europe, and Japan.
- Evaluated relationships between reviews and global sales.
- Applied statistical hypothesis testing to user-rating comparisons.

**Tools:** Python, pandas, NumPy, Matplotlib, SciPy

---

### 6. Megaline Telecom Plan Revenue Analysis

[View project](projects/05-megaline-telecom-plan-revenue-analysis/)

Statistical analysis of customer usage and monthly revenue for two fictional
telecommunications plans.

Highlights:

- Aggregated calls, messages, and internet usage at the monthly customer level.
- Calculated customer revenue from plan rules and excess usage.
- Compared customer behavior and revenue distributions.
- Used Welch's t-tests to evaluate differences in average monthly revenue.

**Tools:** Python, pandas, NumPy, Matplotlib, SciPy

---

## Project Index

| # | Project | Main Focus |
| --- | --- | --- |
| 11 | [Beta Bank Customer Churn Prediction](projects/11-beta-bank-customer-churn-prediction/) | Imbalanced classification, F1, AUC-ROC, resampling, hyperparameter tuning |
| 10 | [Megaline Mobile Plan Classification](projects/10-megaline-mobile-plan-classification/) | Supervised classification, model comparison, hyperparameter tuning, baseline evaluation |
| 08 | [Chicago Taxi Rides Analysis](projects/08-chicago-taxi-rides-analysis/) | SQL, PostgreSQL, EDA, statistical testing, reproducibility |
| 07 | [Used Vehicle Listings Dashboard](projects/07-used-vehicle-listings-dashboard/) | Interactive data application, EDA, visualization |
| 06 | [Video Game Sales Market Analysis](projects/06-video-game-sales-market-analysis/) | EDA, market segmentation, correlation, hypothesis testing |
| 05 | [Megaline Telecom Plan Revenue Analysis](projects/05-megaline-telecom-plan-revenue-analysis/) | Aggregation, revenue analysis, statistical inference |
| 04 | [Instacart Grocery Shopping Analysis](projects/04-instacart-grocery-shopping-analysis/) | Multi-table data wrangling, customer behavior, visualization |
| 03 | [Music Streaming Data Wrangling](projects/03-music-streaming-data-wrangling/) | pandas, data cleaning, grouping, behavioral comparison |
| 02 | [Customer Data Processing and Segmentation](projects/02-customer-data-processing-and-segmentation/) | Python functions, reusable processing logic, segmentation |
| 01 | [Customer Data Preparation](projects/01-customer-data-preparation/) | Python fundamentals, cleaning, validation, transformation |

---

## Skills Demonstrated

Across the current projects, this portfolio includes practical work with:

### Programming and Data Processing

- Python
- pandas
- NumPy
- Data cleaning and validation
- Missing-value and duplicate analysis
- Data type conversion
- Reusable functions and processing logic
- Multi-table data integration

### Exploratory Data Analysis

- Descriptive statistics
- Aggregation and grouping
- Customer and product behavior analysis
- Time-based analysis
- Market segmentation
- Correlation analysis
- Data visualization with Matplotlib and Plotly

### Statistics

- Hypothesis formulation
- Significance levels and p-values
- Independent two-sample t-tests
- Welch's t-test
- Levene's test
- Statistical interpretation

### Machine Learning

- Supervised classification
- Feature and target separation
- Train, validation, and test dataset design
- Stratified dataset splitting
- Missing-value imputation
- One-Hot Encoding
- Feature standardization
- Decision trees
- Random forests
- Logistic regression
- Hyperparameter tuning
- Class imbalance analysis
- Class weighting
- Upsampling
- Accuracy, F1, and AUC-ROC evaluation
- Majority-class baseline evaluation
- Final testing on previously unseen data

### SQL and Data Reproducibility

- PostgreSQL
- SQL querying and aggregation
- Joins and derived fields
- Local schema reconstruction
- CSV-to-database workflows
- Reproducible sampling
- Validation scripts
- Public-data ingestion

### Applications and Deployment

- Streamlit
- Plotly
- Render
- Jupyter Notebook

---

## Repository Structure

```text
data-science-portfolio/
├── projects/
│   ├── 01-customer-data-preparation/
│   ├── 02-customer-data-processing-and-segmentation/
│   ├── 03-music-streaming-data-wrangling/
│   ├── 04-instacart-grocery-shopping-analysis/
│   ├── 05-megaline-telecom-plan-revenue-analysis/
│   ├── 06-video-game-sales-market-analysis/
│   ├── 07-used-vehicle-listings-dashboard/
│   ├── 08-chicago-taxi-rides-analysis/
│   ├── 10-megaline-mobile-plan-classification/
│   └── 11-beta-bank-customer-churn-prediction/
│
└── exercises/
    ├── sprint-02/
    ├── sprint-03/
    ├── sprint-04/
    ├── sprint-05/
    ├── sprint-06/
    ├── sprint-07/
    ├── sprint-10/
    └── sprint-11/
```

Sprint 9 contained theory and career-preparation material rather than a
portfolio project, so there is intentionally no Sprint 9 project directory.

### `projects/`

Contains the main portfolio projects. Each project is organized as a
self-contained unit with its own README and, where applicable, notebooks,
scripts, datasets, dependencies, SQL files, and supporting documentation.

### `exercises/`

Contains selected course exercises retained separately from the main projects
so that practice material does not obscure the portfolio projects.

---

## How to Review This Portfolio

For a quick review, I recommend starting with:

1. [Beta Bank Customer Churn Prediction](projects/11-beta-bank-customer-churn-prediction/) —
   imbalanced classification, F1/AUC-ROC evaluation, resampling, and model tuning.
2. [Megaline Mobile Plan Classification](projects/10-megaline-mobile-plan-classification/) —
   supervised classification, model comparison, and baseline evaluation.
3. [Chicago Taxi Rides Analysis](projects/08-chicago-taxi-rides-analysis/) —
   SQL, Python, statistics, and reproducibility.
4. [Used Vehicle Listings Dashboard](projects/07-used-vehicle-listings-dashboard/) —
   interactive application and deployment.

Each project README explains the objective, methodology, technologies, and
execution instructions in more detail.

---

## About the Project Data

Several projects originate from Data Science training exercises and therefore
use educational or fictional business scenarios.

Where additional reconstruction or portfolio-specific engineering work was
performed, it is documented explicitly. The Chicago taxi project, for example,
separates the original academic results from the independently reconstructed
local PostgreSQL workflow.

---

## Ongoing Development

This repository is being developed progressively as additional topics are
completed and earlier work is prepared for public presentation.

Future updates will expand the portfolio into additional areas of Data Science
and Machine Learning while preserving the same emphasis on:

- reproducible analysis;
- readable and maintainable code;
- clear documentation;
- appropriate statistical interpretation;
- and practical problem solving.
