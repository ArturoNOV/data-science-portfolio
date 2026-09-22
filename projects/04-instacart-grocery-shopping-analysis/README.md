# Instacart Data Wrangling and Grocery Shopping Behavior Analysis

**TripleTen Data Science Bootcamp — Sprint 4: Data Wrangling (continued)**

## Project Overview

This project analyzes grocery shopping behavior using a modified Instacart
dataset containing information about customers, orders, products, aisles, and
departments.

The project expands on the data-wrangling workflow introduced in the previous
Sprint by working with multiple related datasets. It focuses on identifying and
correcting data quality issues and then using the cleaned data to explore
customer ordering patterns and product purchasing behavior.

## Objective

Clean, validate, and analyze Instacart order data to identify patterns in when
customers place orders, how frequently they reorder, which products are most
popular, and how products are added to shopping carts.

## Tasks Performed

* Loaded and inspected five related CSV datasets using pandas.
* Reviewed DataFrame structures, data types, missing values, and duplicates.
* Identified and removed duplicated order records.
* Investigated duplicated product names while preserving valid product IDs.
* Analyzed missing product names and assigned an appropriate replacement value.
* Investigated missing values in the time since the previous order.
* Analyzed missing cart-position values and replaced unknown positions with a
  designated value.
* Validated order-hour and day-of-week ranges.
* Analyzed customer ordering activity by hour of day and day of week.
* Examined the time customers wait before placing another order.
* Compared hourly ordering patterns between Wednesday and Saturday.
* Analyzed the distribution of the number of orders placed by each customer.
* Examined the number of products included in individual orders.
* Identified the most frequently ordered products.
* Analyzed product reorder frequency and reorder proportions.
* Calculated reorder behavior at the customer level.
* Identified the products most frequently added first to shopping carts.
* Created visualizations to support exploratory analysis and interpretation.

## Data Wrangling and Analysis Concepts Practiced

* pandas DataFrames
* CSV data loading
* DataFrame inspection with `head()` and `info()`
* Data type validation and conversion
* Missing-value analysis and replacement
* Duplicate detection and removal
* Boolean filtering
* `value_counts()`
* `groupby()` and aggregation
* `nunique()`
* DataFrame merging
* Exploratory data analysis
* Customer and product-level analysis
* Data visualization with Matplotlib

## Datasets

The project uses five related datasets:

* `instacart_orders.csv` — order-level information including customer ID,
  order sequence, day, hour, and time since the previous order.
* `products.csv` — product IDs, product names, aisle IDs, and department IDs.
* `order_products.csv` — products associated with each order, cart position,
  and reorder information.
* `aisles.csv` — aisle IDs and aisle names.
* `departments.csv` — department IDs and department names.

The datasets are stored locally in the `datasets/` directory.

## Files

* `project.ipynb` — Jupyter Notebook containing the complete step-by-step
  analysis, explanations, code, visualizations, and outputs.
* `project.py` — Python script version of the project.
* `datasets/` — Datasets required by the project.
* `requirements.txt` — Python dependencies required to run the project.

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