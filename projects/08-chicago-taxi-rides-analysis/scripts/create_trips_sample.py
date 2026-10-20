from pathlib import Path
import pandas as pd


# ------------------------------------------------------------
# Rutas
# ------------------------------------------------------------

project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "datasets" / "reproducibility"

trips_file = data_folder / "trips.csv"
sample_file = data_folder / "trips_sample.csv"


# ------------------------------------------------------------
# Configuración del sample
# ------------------------------------------------------------

sample_size = 100_000
random_seed = 42


# ------------------------------------------------------------
# Cargar dataset completo
# ------------------------------------------------------------

print("Cargando trips.csv...")

trips = pd.read_csv(
    trips_file,
    parse_dates=["start_ts", "end_ts"]
)

print(f"Registros disponibles: {len(trips):,}")


# ------------------------------------------------------------
# Crear sample reproducible
# ------------------------------------------------------------

trips_sample = (
    trips
    .sample(
        n=min(sample_size, len(trips)),
        random_state=random_seed
    )
    .sort_values(["start_ts", "trip_id"])
    .reset_index(drop=True)
)


# ------------------------------------------------------------
# Guardar sample
# ------------------------------------------------------------

trips_sample.to_csv(
    sample_file,
    index=False,
    date_format="%Y-%m-%d %H:%M:%S"
)

print("\nSample guardado correctamente.")
print(f"Archivo: {sample_file.resolve()}")
print(f"Registros: {len(trips_sample):,}")


# ------------------------------------------------------------
# Verificar cobertura temporal
# ------------------------------------------------------------

print("\nCobertura temporal:")
print("Fecha mínima:", trips_sample["start_ts"].min())
print("Fecha máxima:", trips_sample["start_ts"].max())
print(
    "Días distintos:",
    trips_sample["start_ts"].dt.date.nunique()
)


# ------------------------------------------------------------
# Verificar viajes necesarios para el proyecto
# Loop = 50
# O'Hare = 63
# Saturday = 5 en pandas (Monday = 0)
# ------------------------------------------------------------

loop_ohare_saturdays = trips_sample[
    (trips_sample["pickup_location_id"] == 50)
    & (trips_sample["dropoff_location_id"] == 63)
    & (trips_sample["start_ts"].dt.dayofweek == 5)
]

print(
    "\nViajes Loop -> O'Hare en sábado:",
    len(loop_ohare_saturdays)
)


# ------------------------------------------------------------
# Verificación general
# ------------------------------------------------------------

print("\nDimensiones:")
print(trips_sample.shape)

print("\nTipos de datos:")
print(trips_sample.dtypes)

print("\nValores nulos:")
print(trips_sample.isna().sum())
