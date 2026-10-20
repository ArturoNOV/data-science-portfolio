/*
Course project SQL task 1:
Count the number of taxi trips made by each company on
November 15 and 16, 2017. Return the trip count as
trips_amount and sort the results in descending order.
*/

SELECT
    c.company_name,
    COUNT(t.trip_id) AS trips_amount
FROM trips AS t
LEFT JOIN cabs AS c
    ON c.cab_id = t.cab_id
WHERE CAST(t.start_ts AS date) BETWEEN DATE '2017-11-15'
    AND DATE '2017-11-16'
GROUP BY c.company_name
ORDER BY trips_amount DESC;


/*
Course project SQL task 2:
Count the number of trips made by taxi companies whose
names contain "Yellow" or "Blue" from November 1 through
November 7, 2017. Return the trip count as trips_amount
and group the results by company_name.
*/

SELECT
    c.company_name,
    COUNT(t.trip_id) AS trips_amount
FROM trips AS t
LEFT JOIN cabs AS c
    ON c.cab_id = t.cab_id
WHERE CAST(t.start_ts AS date) BETWEEN DATE '2017-11-01'
    AND DATE '2017-11-07'
    AND (
        c.company_name LIKE '%Yellow%'
        OR c.company_name LIKE '%Blue%'
    )
GROUP BY c.company_name
ORDER BY trips_amount DESC;


/*
Course project SQL task 3:
For November 1 through November 7, 2017, count the trips
made by Flash Cab and Taxi Affiliation Services. Combine
all other taxi companies into an "Other" group. Return
the company group as company and the trip count as
trips_amount, sorted in descending order.
*/

SELECT
    CASE
        WHEN c.company_name IN (
            'Flash Cab',
            'Taxi Affiliation Services'
        )
        THEN c.company_name
        ELSE 'Other'
    END AS company,
    COUNT(t.trip_id) AS trips_amount
FROM trips AS t
LEFT JOIN cabs AS c
    ON c.cab_id = t.cab_id
WHERE CAST(t.start_ts AS date) BETWEEN DATE '2017-11-01'
    AND DATE '2017-11-07'
GROUP BY
    CASE
        WHEN c.company_name IN (
            'Flash Cab',
            'Taxi Affiliation Services'
        )
        THEN c.company_name
        ELSE 'Other'
    END
ORDER BY trips_amount DESC;


/*
Course project SQL task 4:
Retrieve the neighborhood identifiers for O'Hare and
the Loop from the neighborhoods table.
*/

SELECT
    name,
    neighborhood_id
FROM neighborhoods
WHERE name IN ('O''Hare', 'Loop');


/*
Course project SQL task 5:
Classify each hourly weather record as "Bad" when the
description contains "rain" or "storm", and as "Good"
otherwise. Return the timestamp and the derived
weather_conditions field.
*/

SELECT
    ts,
    CASE
        WHEN description LIKE '%rain%'
            OR description LIKE '%storm%'
        THEN 'Bad'
        ELSE 'Good'
    END AS weather_conditions
FROM weather_records
ORDER BY ts;


/*
Course project SQL task 6:
Retrieve Saturday trips that started in the Loop
(pickup_location_id = 50) and ended at O'Hare
(dropoff_location_id = 63). Join each trip to its hourly
weather record, classify the weather as "Good" or "Bad",
and return the trip start time, weather condition, and
duration. Trips without matching weather data are excluded.
*/

SELECT
    t.start_ts,
    w.weather_conditions,
    t.duration_seconds
FROM trips AS t
INNER JOIN (
    SELECT
        ts,
        CASE
            WHEN description LIKE '%rain%'
                OR description LIKE '%storm%'
            THEN 'Bad'
            ELSE 'Good'
        END AS weather_conditions
    FROM weather_records
) AS w
    ON t.start_ts = w.ts
WHERE t.pickup_location_id = 50
    AND t.dropoff_location_id = 63
    AND EXTRACT(DOW FROM t.start_ts) = 6
ORDER BY t.trip_id;
