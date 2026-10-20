\set ON_ERROR_STOP on

BEGIN;

TRUNCATE TABLE
    trips,
    weather_records,
    cabs,
    neighborhoods;

\copy cabs FROM 'datasets/reproducibility/cabs.csv' WITH (FORMAT csv, HEADER true);
\copy neighborhoods FROM 'datasets/reproducibility/neighborhoods.csv' WITH (FORMAT csv, HEADER true);
\copy trips FROM 'datasets/reproducibility/trips_sample.csv' WITH (FORMAT csv, HEADER true);
\copy weather_records FROM 'datasets/reproducibility/weather_records.csv' WITH (FORMAT csv, HEADER true);

COMMIT;
