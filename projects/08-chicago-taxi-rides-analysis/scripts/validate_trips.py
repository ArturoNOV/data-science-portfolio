from pathlib import Path
import sys

import pandas as pd


# ------------------------------------------------------------
# Seleccionar archivo
# ------------------------------------------------------------

project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "datasets" / "reproducibility"

if len(sys.argv) > 1:
    file = Path(sys.argv[1])
else:
    file = data_folder / "trips_sample.csv"


# ------------------------------------------------------------
# Verificar existencia
# ------------------------------------------------------------

if not file.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo: {file}"
    )


# ------------------------------------------------------------
# Cargar datos
# ------------------------------------------------------------

print(f"Verificando: {file}")

trips = pd.read_csv(
    file,
    parse_dates=["start_ts", "end_ts"]
)


# ------------------------------------------------------------
# Estructura general
# ------------------------------------------------------------

print("\nDimensiones:")
print(trips.shape)

print("\nTipos:")
print(trips.dtypes)

print("\nValores nulos:")
print(trips.isna().sum())


# ------------------------------------------------------------
# Verificar trip_id
# ------------------------------------------------------------

print("\nTrip ID:")
print("Mínimo:", trips["trip_id"].min())
print("Máximo:", trips["trip_id"].max())
print("Únicos:", trips["trip_id"].nunique())
print("Duplicados:", trips["trip_id"].duplicated().sum())


# ------------------------------------------------------------
# Verificar cab_id
# ------------------------------------------------------------

print("\nCab ID inexistentes:")
print(trips["cab_id"].isna().sum())


# ------------------------------------------------------------
# Cobertura temporal
# ------------------------------------------------------------

print("\nRango start_ts:")
print("Mínimo:", trips["start_ts"].min())
print("Máximo:", trips["start_ts"].max())

print(
    "Días distintos:",
    trips["start_ts"].dt.date.nunique()
)


# ------------------------------------------------------------
# Verificar viajes Loop -> O'Hare en sábado
# ------------------------------------------------------------

loop_ohare_saturdays = trips[
    (trips["pickup_location_id"] == 50)
    & (trips["dropoff_location_id"] == 63)
    & (trips["start_ts"].dt.dayofweek == 5)
]

print("\nViajes Loop -> O'Hare en sábado:")
print(len(loop_ohare_saturdays))
