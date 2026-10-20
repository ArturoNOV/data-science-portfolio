"""
Descarga viajes de taxi de Chicago correspondientes a noviembre de 2017.

El script:
- descarga los datos por bloques;
- si el archivo ya existe, continúa desde el último registro descargado;
- evita OFFSET para no degradar el rendimiento;
- reintenta automáticamente si ocurre un timeout.
"""

import io
import time
from pathlib import Path

import pandas as pd
import requests


domain = "data.cityofchicago.org"
dataset_id = "wrvz-psew"

api_url = f"https://{domain}/resource/{dataset_id}.csv"

project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "datasets" / "reproducibility"

output_file = data_folder / "chicago_taxi_trips_2017_11.csv"
output_file.parent.mkdir(parents=True, exist_ok=True)

columns = (
    "trip_id,"
    "taxi_id,"
    "trip_start_timestamp,"
    "trip_end_timestamp,"
    "trip_seconds,"
    "trip_miles,"
    "pickup_community_area,"
    "dropoff_community_area,"
    "company"
)

base_where = (
    "trip_start_timestamp >= '2017-11-01T00:00:00.000' "
    "AND trip_start_timestamp < '2017-12-01T00:00:00.000'"
)

limit = 25000
max_retries = 6


# ------------------------------------------------------------
# Revisar si ya existe una descarga parcial
# ------------------------------------------------------------

total = 0
last_timestamp = None
last_trip_id = None

if output_file.exists():

    print("Archivo existente encontrado. Revisando punto de reanudación...")

    for chunk in pd.read_csv(
        output_file,
        usecols=["trip_id", "trip_start_timestamp"],
        dtype=str,
        chunksize=100000
    ):
        total += len(chunk)

        last_timestamp = chunk.iloc[-1]["trip_start_timestamp"]
        last_trip_id = chunk.iloc[-1]["trip_id"]

    print(f"Registros existentes: {total:,}")
    print(f"Último timestamp: {last_timestamp}")
    print(f"Último trip_id: {last_trip_id}")

    first_chunk = False

else:

    print("No existe una descarga previa. Iniciando desde cero.")

    first_chunk = True


# ------------------------------------------------------------
# Descargar por bloques usando keyset pagination
# ------------------------------------------------------------

while True:

    if last_timestamp is None:

        where = base_where

    else:

        where = (
            f"{base_where} "
            f"AND ("
            f"trip_start_timestamp > '{last_timestamp}' "
            f"OR ("
            f"trip_start_timestamp = '{last_timestamp}' "
            f"AND trip_id > '{last_trip_id}'"
            f")"
            f")"
        )

    params = {
        "$select": columns,
        "$where": where,
        "$order": "trip_start_timestamp,trip_id",
        "$limit": limit
    }

    # --------------------------------------------------------
    # Reintentos automáticos
    # --------------------------------------------------------

    for attempt in range(1, max_retries + 1):

        try:

            response = requests.get(
                api_url,
                params=params,
                timeout=180
            )

            response.raise_for_status()

            break

        except requests.exceptions.RequestException as error:

            print()
            print(
                f"Error en intento {attempt}/{max_retries}: "
                f"{type(error).__name__}"
            )

            if attempt == max_retries:
                print("Se alcanzó el máximo de reintentos.")
                print("Puedes ejecutar nuevamente el script;")
                print("continuará desde el último bloque guardado.")
                raise

            wait_time = attempt * 10

            print(f"Esperando {wait_time} segundos antes de reintentar...")

            time.sleep(wait_time)


    # --------------------------------------------------------
    # Convertir la respuesta en DataFrame
    # --------------------------------------------------------

    chunk = pd.read_csv(io.StringIO(response.text))

    if chunk.empty:
        break


    # --------------------------------------------------------
    # Guardar el bloque
    # --------------------------------------------------------

    chunk.to_csv(
        output_file,
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    rows_downloaded = len(chunk)

    total += rows_downloaded

    print(
        f"Descargados: {rows_downloaded:,} | "
        f"Total acumulado: {total:,}"
    )


    # --------------------------------------------------------
    # Actualizar el punto de reanudación
    # --------------------------------------------------------

    last_timestamp = str(chunk.iloc[-1]["trip_start_timestamp"])
    last_trip_id = str(chunk.iloc[-1]["trip_id"])

    first_chunk = False


    # Si recibimos menos de 25,000 registros, era el último bloque
    if rows_downloaded < limit:
        break

    time.sleep(0.5)


print()
print(f"Descarga terminada: {total:,} registros")
print(f"Archivo: {output_file.resolve()}")