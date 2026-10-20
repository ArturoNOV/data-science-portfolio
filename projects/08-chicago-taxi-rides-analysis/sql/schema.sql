CREATE TABLE cabs (
    cab_id INTEGER,
    vehicle_id TEXT,
    company_name TEXT
);

CREATE TABLE neighborhoods (
    neighborhood_id INTEGER,
    name TEXT
);

CREATE TABLE trips (
    trip_id INTEGER,
    cab_id INTEGER,
    start_ts TIMESTAMP,
    end_ts TIMESTAMP,
    duration_seconds INTEGER,
    distance_miles DOUBLE PRECISION,
    pickup_location_id INTEGER,
    dropoff_location_id INTEGER
);

CREATE TABLE weather_records (
    record_id INTEGER,
    ts TIMESTAMP,
    temperature DOUBLE PRECISION,
    description TEXT
);