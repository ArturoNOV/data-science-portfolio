# Video Game Sales Market Analysis and Statistical Hypothesis Testing

## TripleTen Data Science Bootcamp — Sprint 6: Integrated Project

## Project Overview

This project analyzes historical video game sales data for Ice, a fictional
online video game retailer operating across multiple global markets.

The analysis combines data preparation, exploratory data analysis, market
segmentation, correlation analysis, and statistical hypothesis testing. It
examines historical sales through 2016 to identify patterns related to
platform performance, video game genres, regional markets, critic and user
reviews, and ESRB ratings that could support advertising decisions for 2017.

## Objective

Prepare and analyze historical video game sales data to identify commercially
relevant patterns across platforms, genres, and geographic markets, evaluate
the relationship between reviews and sales, and use statistical hypothesis
testing to compare user ratings between selected groups.

## Tasks Performed

- Loaded and inspected historical video game sales data.
- Standardized column names and corrected data types.
- Investigated and treated missing values in game names, genres, release
  years, critic scores, user scores, and ESRB ratings.
- Converted `tbd` user scores to missing values before numerical analysis.
- Preserved missing review scores where reliable replacement values could not
  be justified.
- Created total global sales by combining regional sales.
- Examined the historical number of video game releases by year.
- Analyzed sales trends and commercial life cycles across gaming platforms.
- Selected a recent analysis period to evaluate platforms relevant to the
  2017 market.
- Compared sales distributions between major platforms.
- Evaluated the relationship between critic scores, user scores, and global
  sales using correlation analysis and scatter plots.
- Compared sales performance for games released across multiple platforms.
- Analyzed sales by video game genre.
- Built regional market profiles for North America, Europe, and Japan.
- Compared leading platforms and genres across geographic markets.
- Examined the relationship between ESRB ratings and regional sales.
- Evaluated the effect of missing ESRB classifications on market
  interpretation.
- Formulated and tested statistical hypotheses using independent
  two-sample Welch's t-tests.
- Compared average user ratings for Xbox One and PC games.
- Compared average user ratings for Action and Sports games.
- Interpreted statistical results using significance levels and p-values.

## Data Analysis Concepts Practiced

- pandas DataFrames
- Data cleaning and preprocessing
- Missing-value analysis
- Data type conversion
- Feature creation
- Data aggregation
- `groupby()` and aggregation
- Exploratory data analysis
- Descriptive statistics
- Time-based trend analysis
- Market segmentation
- Data visualization with Matplotlib
- Box plots
- Scatter plots
- Correlation analysis
- Linear trend estimation
- Regional market analysis
- Statistical hypothesis formulation
- Independent two-sample t-tests
- Welch's t-test
- Statistical significance and p-value interpretation
- SciPy statistical functions

## Dataset

The project uses:

- `games.csv` — historical video game information including game titles,
  platforms, release years, genres, regional sales, critic scores, user
  scores, and ESRB ratings.

The dataset is stored locally in the `datasets/` directory.

## Files

- `project.ipynb` — Jupyter Notebook containing the complete step-by-step
  analysis, explanations, visualizations, statistical tests, and outputs.
- `project.py` — Python script version of the project.
- `datasets/` — Dataset required by the project.
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
