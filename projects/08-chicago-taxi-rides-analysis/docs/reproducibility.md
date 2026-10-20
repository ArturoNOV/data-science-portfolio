# Local SQL Reconstruction and Reproducibility

## Overview

The original course project was completed in TripleTen's environment using
precomputed SQL query results provided as CSV files.

The Python notebook included in this repository continues to use those original
course files:

- `datasets/project_sql_result_01.csv`
- `datasets/project_sql_result_04.csv`
- `datasets/project_sql_result_07.csv`

To make the SQL portion of the project reproducible outside the TripleTen
platform, an additional local PostgreSQL reconstruction was created.

This reconstruction is separate from the original academic results and is
intended to demonstrate the complete data pipeline, SQL logic, and local
database workflow.

Because the original TripleTen database is not publicly available, numerical
results produced by the reconstructed database are not expected to match the
original course results exactly.

---

## Original Project Data Flow

The original project followed this workflow:

```text
TripleTen SQL environment
        ↓
Course project SQL tasks
        ↓
SQL query results
        ↓
project_sql_result_*.csv
        ↓
project.ipynb
        ↓
Exploratory analysis and hypothesis testing
```

The notebook in this repository preserves that original workflow by using the
three CSV files supplied for the project.

---

## Local Reconstruction Architecture

The local reconstruction reproduces the main database structure needed by the
course project:

```text
City of Chicago Taxi Trips API
        ↓
download_chicago_trips.py
        ↓
~1.9 million November 2017 taxi trips
        ↓
build_trips.py
        ↓
~1.79 million reconstructed trips
        ↓
create_trips_sample.py
        ↓
100,000-row reproducible sample
        ↓
PostgreSQL
        ↓
project_queries.sql
```

Weather data follows a separate pipeline:

```text
TripleTen weather source
        ↓
scrape_weather.py
        ↓
weather_records.csv
        ↓
PostgreSQL
```

---

## Reconstructed Tables

The local PostgreSQL database contains four tables used by the project:

- `cabs`
- `neighborhoods`
- `trips`
- `weather_records`

Their definitions are available in:

```text
sql/schema.sql
```

The GitHub-friendly datasets used to populate these tables are stored in:

```text
datasets/reproducibility/
```

and include:

```text
cabs.csv
neighborhoods.csv
trips_sample.csv
weather_records.csv
```

---

## Chicago Taxi Trips Source

Taxi trip data was reconstructed from the public City of Chicago Taxi Trips
dataset.

Dataset identifier:

```text
wrvz-psew
```

Only trips from November 2017 were downloaded.

The reconstruction script retrieves only the fields required to reproduce the
analysis rather than downloading every available source column.

---

## Raw Data Download

The download process is implemented in:

```text
scripts/download_chicago_trips.py
```

The script:

- downloads the data in blocks of 25,000 rows;
- filters the source to November 2017;
- avoids large `OFFSET` queries;
- uses keyset pagination based on timestamp and trip identifier;
- supports resuming an interrupted download;
- retries failed requests automatically.

The resulting raw file contains approximately 1.9 million records:

```text
datasets/reproducibility/chicago_taxi_trips_2017_11.csv
```

Because of its size, this file is not intended to be stored in GitHub.

---

## Reconstructing the Trips Table

The transformation is performed by:

```text
scripts/build_trips.py
```

This script converts the public Chicago data into a structure compatible with
the tables used in the course project.

### Cab Matching

Chicago taxi records are matched against the reconstructed `cabs` table using
the available taxi and company identifiers.

### Data Quality Filtering

Records with unusable timestamps or invalid trip durations are removed before
the final table is generated.

### Timestamp Normalization

Trip timestamps are normalized to hourly values so they can be joined with the
hourly weather observations used by the project.

### Neighborhood Mapping

Chicago Community Areas are mapped to the neighborhood identifiers required by
the project.

Two mappings are especially important for the final hypothesis test:

```text
Loop   → neighborhood_id 50
O'Hare → neighborhood_id 63
```

Trips without a usable mapped location are assigned to an undefined location
used by the reconstructed dataset.

### Trip Identifiers

The public source does not provide identifiers compatible with the original
TripleTen database, so sequential integer trip identifiers are generated for
the reconstructed table.

The complete reconstructed dataset contains approximately 1.79 million trips:

```text
datasets/reproducibility/trips.csv
```

This full file is also excluded from GitHub because of its size.

---

## Weather Data Reconstruction

Weather data is generated with:

```text
scripts/scrape_weather.py
```

The script retrieves the hourly weather table used for the exercise and
converts it into the following structure:

```text
record_id
ts
temperature
description
```

The resulting file is:

```text
datasets/reproducibility/weather_records.csv
```

It contains 697 hourly observations.

The `weather_conditions` field used by the SQL analysis is not stored in the
CSV. It is derived in SQL with a `CASE` expression:

```text
Bad  → descriptions containing "rain" or "storm"
Good → all other descriptions
```

---

## GitHub Sampling Strategy

The complete reconstructed trips dataset is too large for a practical portfolio
repository.

For that reason, the repository includes a deterministic sample created by:

```text
scripts/create_trips_sample.py
```

The sample contains:

```text
100,000 rows
```

and is generated with:

```text
random_state = 42
```

The sample preserves the trip identifiers assigned during the full
reconstruction.

The resulting file is:

```text
datasets/reproducibility/trips_sample.csv
```

This sample allows the PostgreSQL workflow and project queries to be executed
without downloading or storing the full reconstructed dataset.

---

## Sample Validation

The included sample was validated with:

```text
scripts/validate_trips.py
```

The validation confirmed:

```text
Rows:                         100,000
Unique trip IDs:              100,000
Duplicate trip IDs:           0
Distinct November dates:      30
Invalid cab references:       0
Saturday Loop → O'Hare trips: 66
```

The sample covers the entire November 2017 period.

Eight records contain missing values in `distance_miles`. This field is not
required by the core SQL queries used in the project.

---

## PostgreSQL Reconstruction

### 1. Create a Database

Create an empty PostgreSQL database.

For example:

```sql
CREATE DATABASE chicago_taxi_portfolio;
```

Connect to it before running the remaining files.

### 2. Create the Tables

From the project root, run:

```text
\i sql/schema.sql
```

This creates:

```text
cabs
neighborhoods
trips
weather_records
```

### 3. Load the Sample Data

Run:

```text
\i sql/load_sample_data.sql
```

The tested sample load produces:

```text
cabs               5,529 rows
neighborhoods          94 rows
trips              100,000 rows
weather_records        697 rows
```

The loading script uses PostgreSQL `psql` `\copy` commands, so it should be
executed from the root directory of the project.

### 4. Execute the Project Queries

Run:

```text
\i sql/project_queries.sql
```

This executes the six SQL tasks associated with the course project.

They cover:

1. taxi trips by company;
2. trips by companies containing "Yellow" or "Blue";
3. comparison of Flash Cab, Taxi Affiliation Services, and other companies;
4. identification of the Loop and O'Hare neighborhood IDs;
5. classification of hourly weather as Good or Bad;
6. Saturday Loop-to-O'Hare trips joined with hourly weather conditions.

The sixth query returns 66 matching trips when executed against the included
100,000-row sample.

---

## Quick Reproduction Workflow

The fastest way to reproduce the SQL portion of the repository is to use the
datasets already included in GitHub:

```text
Create empty PostgreSQL database
        ↓
sql/schema.sql
        ↓
sql/load_sample_data.sql
        ↓
sql/project_queries.sql
```

This workflow does not require downloading the full Chicago taxi dataset.

---

## Full Reconstruction Workflow

To rebuild the taxi data from the original public source, run the scripts from
the project root in the following order:

```text
python scripts/download_chicago_trips.py
python scripts/build_trips.py
python scripts/create_trips_sample.py
python scripts/validate_trips.py
```

Weather data can be regenerated separately with:

```text
python scripts/scrape_weather.py
```

The full taxi reconstruction creates large intermediate files that are
intentionally excluded from version control.

---

## Original Results vs. Reconstructed Results

There are two distinct data layers in this repository.

### Original Academic Results

```text
datasets/project_sql_result_01.csv
datasets/project_sql_result_04.csv
datasets/project_sql_result_07.csv
```

These files are the inputs used by `project.ipynb` and preserve the original
course analysis.

### Local Reproducibility Data

```text
datasets/reproducibility/
```

These files support the PostgreSQL reconstruction and allow the SQL workflow to
be executed locally.

The reconstructed database should therefore be interpreted as a reproducibility
implementation, not as an exact copy of TripleTen's original database.

---

## Limitations

The original TripleTen source database is not publicly available.

The local reconstruction therefore relies on public Chicago taxi data,
available course datasets, and explicit mapping rules required to reproduce the
project structure.

As a result:

- local query totals can differ from the original TripleTen results;
- reconstructed trip identifiers do not correspond to the original database;
- the 100,000-row GitHub sample is intended for reproducibility rather than for
  reproducing the exact numerical results of the original notebook.

The original notebook conclusions remain based on the original TripleTen
project result files.
