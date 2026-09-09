# Music Streaming Data Wrangling and User Behavior Analysis

**TripleTen Data Science Bootcamp — Sprint 3: Data Wrangling**

## Project Overview

This project analyzes music streaming activity from users in two fictional
cities, Springfield and Shelbyville.

The project introduces a complete data-wrangling workflow using pandas:
inspecting raw data, correcting structural inconsistencies, handling missing
values and duplicates, standardizing categorical values, and preparing the
dataset for exploratory analysis.

## Objective

Clean and prepare music streaming data and use the resulting dataset to compare
listening activity between Springfield and Shelbyville on different days of
the week.

## Tasks Performed

- Loaded and inspected a CSV dataset using pandas.
- Reviewed DataFrame structure, column names, and data quality.
- Standardized column names using lowercase and snake_case conventions.
- Identified and replaced missing values.
- Detected and removed explicit duplicate records.
- Identified and corrected implicit duplicates in music genres.
- Used filtering and grouping operations to summarize listening activity.
- Compared music playback activity by city and day.
- Created reusable functions for filtered track-count calculations.

## Data Wrangling Concepts Practiced

- pandas DataFrames
- CSV data loading
- DataFrame inspection with `head()` and `info()`
- Column renaming and standardization
- Missing-value detection and replacement
- Duplicate detection and removal
- Categorical-value standardization
- Boolean filtering
- `groupby()`
- Sorting and unique values
- Functions for reusable analysis logic

## Dataset

The project uses:

- `music_project_en.csv` — music streaming records containing user, track,
  artist, genre, city, playback time, and day information.

The dataset is stored locally in the `datasets/` directory.

## Files

- `project.ipynb` — Jupyter Notebook containing the complete step-by-step
  analysis, explanations, code, and outputs.
- `project.py` — Python script version of the project.
- `datasets/` — Dataset required by the project.
- `requirements.txt` — Python dependencies required to run the project.

## Requirements

Install the required dependency with:

```bash
pip install -r requirements.txt
```

## How to Run

Python script:

```bash
python project.py
```

The notebook can be opened with Jupyter Notebook, JupyterLab, or VS Code.