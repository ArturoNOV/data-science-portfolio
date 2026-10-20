# Chicago Taxi Rides Analysis

## Project Overview

This project analyzes taxi activity in Chicago during November 2017 for Zuber,
a fictional ride-sharing company used in the TripleTen Data Science curriculum.

The analysis combines SQL-based data extraction with Python exploratory data
analysis and statistical hypothesis testing. The main goals are to identify the
most active taxi companies and destination neighborhoods and to evaluate
whether weather conditions are associated with differences in trip duration
between the Loop and O'Hare International Airport.

The original academic analysis is preserved in `project.ipynb`. In addition,
this repository includes a local PostgreSQL reconstruction so the SQL portion
of the project can be reproduced outside the TripleTen environment.

---

## Objectives

The project addresses three main questions:

1. Which taxi companies completed the most trips during the selected period?
2. Which Chicago neighborhoods were the most common trip destinations?
3. Does the average duration of Saturday trips from the Loop to O'Hare differ
   between good and bad weather conditions?

---

## Technologies

- Python
- pandas
- matplotlib
- SciPy
- Jupyter Notebook
- PostgreSQL
- SQL
- Requests
- Beautiful Soup
- lxml

---

## Analysis

### Taxi Companies

The SQL portion of the project aggregates trips by taxi company and compares
the most active operators during November 2017.

The Python analysis then uses the original course query results to visualize and
compare trip volumes across companies.

### Destination Neighborhoods

Average trip counts are analyzed by destination neighborhood to identify the
areas receiving the highest taxi traffic.

### Weather and Trip Duration

Saturday trips from the Loop to O'Hare are divided into two weather groups:

- **Good** — weather descriptions without rain or storm conditions.
- **Bad** — weather descriptions containing rain or storm conditions.

After removing zero-duration trips, the analysis compares trip durations
between the two groups.

A Levene test is used to evaluate the equality-of-variance assumption, followed
by an independent two-sample t-test.

---

## Key Findings

- Flash Cab was one of the most active taxi companies in the analyzed data.
- A relatively small group of neighborhoods accounted for a large share of
  destination traffic.
- Saturday Loop-to-O'Hare trips were longer on average during bad weather.
- The mean trip duration was approximately 2,013 seconds in good weather and
  2,427 seconds in bad weather, a difference of about 414 seconds.
- The statistical test produced a p-value of approximately `1.33e-11`, so the
  null hypothesis of equal mean trip duration was rejected at the 5%
  significance level.
- The result indicates a statistically significant association between weather
  conditions and trip duration in the analyzed sample. It does not establish
  causation.

---

## Data Sources

This repository contains two distinct data layers.

### Original Academic Results

The notebook uses the original SQL result files supplied for the TripleTen
course project:

```text
datasets/project_sql_result_01.csv
datasets/project_sql_result_04.csv
datasets/project_sql_result_07.csv
```

These files preserve the original academic analysis and are the direct inputs
to `project.ipynb`.

### Local Reproducibility Data

The SQL workflow was reconstructed locally using public Chicago taxi data and
the supporting course datasets.

The GitHub-friendly reconstruction files are stored in:

```text
datasets/reproducibility/
```

They include:

```text
cabs.csv
neighborhoods.csv
trips_sample.csv
weather_records.csv
```

The included `trips_sample.csv` contains a deterministic 100,000-row sample of
the larger reconstructed trips dataset.

The reconstructed PostgreSQL database is intended for reproducibility and is
not an exact copy of TripleTen's original database. Therefore, local SQL query
totals are not expected to match the original course results exactly.

For the full reconstruction methodology, see
[`docs/reproducibility.md`](docs/reproducibility.md).

---

## Project Structure

```text
08-chicago-taxi-rides-analysis/
├── README.md
├── project.ipynb
├── requirements.txt
│
├── datasets/
│   ├── project_sql_result_01.csv
│   ├── project_sql_result_04.csv
│   ├── project_sql_result_07.csv
│   └── reproducibility/
│       ├── cabs.csv
│       ├── neighborhoods.csv
│       ├── trips_sample.csv
│       └── weather_records.csv
│
├── scripts/
│   ├── build_trips.py
│   ├── create_trips_sample.py
│   ├── download_chicago_trips.py
│   ├── scrape_weather.py
│   └── validate_trips.py
│
├── sql/
│   ├── load_sample_data.sql
│   ├── project_queries.sql
│   └── schema.sql
│
└── docs/
    └── reproducibility.md
```

---

## Quick Start

### Python Analysis

Create or activate a Python environment and install the required packages:

```bash
pip install -r requirements.txt
```

Then open:

```text
project.ipynb
```

The notebook reads the three original TripleTen SQL result files directly from
the `datasets/` folder.

### PostgreSQL Sample Workflow

Create an empty PostgreSQL database and connect to it with `psql`.

For example:

```sql
CREATE DATABASE chicago_taxi_portfolio;
```

From the project root, create the tables:

```text
\i sql/schema.sql
```

Load the included reproducibility datasets:

```text
\i sql/load_sample_data.sql
```

Run the project SQL queries:

```text
\i sql/project_queries.sql
```

The tested sample load contains:

```text
cabs               5,529 rows
neighborhoods          94 rows
trips              100,000 rows
weather_records        697 rows
```

The final Loop-to-O'Hare query returns 66 Saturday trips in the included sample.

---

## Full Data Reconstruction

The complete local taxi dataset can be rebuilt from the public source by
running the following scripts from the project root:

```bash
python scripts/download_chicago_trips.py
python scripts/build_trips.py
python scripts/create_trips_sample.py
python scripts/validate_trips.py
```

Weather data can be regenerated separately with:

```bash
python scripts/scrape_weather.py
```

The full reconstruction produces large intermediate files that are intentionally
excluded from version control.

See [`docs/reproducibility.md`](docs/reproducibility.md) for details about the
data pipeline, sampling strategy, mappings, validation, and limitations.
