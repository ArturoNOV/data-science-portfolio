from pathlib import Path
import pandas as pd


# Rutas de archivos
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "datasets" / "reproducibility"

raw_trips_file = data_folder / "chicago_taxi_trips_2017_11.csv"
cabs_file = data_folder / "cabs.csv"


# Cargar datos
raw_trips = pd.read_csv(raw_trips_file)
cabs = pd.read_csv(cabs_file)


# Relacionar los viajes con la tabla cabs
trips_matched = raw_trips.merge(
    cabs,
    left_on=["taxi_id", "company"],
    right_on=["vehicle_id", "company_name"],
    how="inner",
    validate="many_to_one"
)


# Verificar resultados
print(trips_matched.shape)

print(trips_matched.columns.tolist())

print(trips_matched.head())


# Crear DF
cols = [
    'trip_id',
    'cab_id',
    'trip_start_timestamp',
    'trip_end_timestamp',
    'trip_seconds',
    'trip_miles',
    'pickup_community_area',
    'dropoff_community_area'
]

trips_clean = trips_matched[cols].copy()

# Verificar DF
print(trips_clean.shape)
print(trips_clean.columns.tolist())

# Cambiamos los nombres de las columnas
trips_clean = trips_clean.rename(
    columns={
        'trip_start_timestamp': 'start_ts',
        'trip_end_timestamp': 'end_ts',
        'trip_seconds': 'duration_seconds',
        'trip_miles': 'distance_miles'
    }
)

# Imprime los nuevos nombres de columnas
print(trips_clean.columns.tolist())


# Revisamos el tipo de datos que tiene el DataFrame
print(trips_clean.dtypes)

# Convertimos start_ts y end_ts al formato de fecha.
trips_clean['start_ts'] = pd.to_datetime(
    trips_clean['start_ts'],
    errors='coerce'
)

trips_clean['end_ts'] = pd.to_datetime(
    trips_clean['end_ts'],
    errors='coerce'
)


# Verificamos que que ambas columnas ahora aparezcan como datetime64[ns]
# que no hayamos generado fechas nulas inesperadamente
# que el rango temporal siga siendo coherente con noviembre de 2017
print(trips_clean.dtypes)

print(
    trips_clean[['start_ts', 'end_ts']]
    .isna()
    .sum()
)

print(trips_clean[['start_ts', 'end_ts']].agg(['min', 'max']))

# Viajes sin fecha de finalización
print("\nViajes sin end_ts:")
print(
    trips_clean[
        trips_clean['end_ts'].isna()
    ]
)

# Viajes cuya fecha de fin es anterior a la fecha de inicio
invalid_end = trips_clean[
    trips_clean['end_ts'] < trips_clean['start_ts']
]

print("\nViajes con end_ts anterior a start_ts:")
print(f"Cantidad: {len(invalid_end)}")

print(
    invalid_end[
        [
            'trip_id',
            'start_ts',
            'end_ts',
            'duration_seconds',
            'distance_miles'
        ]
    ].head(20)
)

# Revisar en qué fechas ocurren los end_ts anteriores al start_ts
invalid_by_date = (
    invalid_end
    .assign(start_date=invalid_end['start_ts'].dt.date)
    .groupby('start_date')
    .size()
    .sort_values(ascending=False)
)

print("\nViajes con end_ts < start_ts por fecha:")
print(invalid_by_date)


# Separar los casos del cambio de horario del 5 de noviembre
dst_date = pd.Timestamp('2017-11-05').date()

invalid_dst = invalid_end[
    invalid_end['start_ts'].dt.date == dst_date
]

invalid_other = invalid_end[
    invalid_end['start_ts'].dt.date != dst_date
]

print(f"\nCasos del 5 de noviembre: {len(invalid_dst)}")
print(f"Casos de otras fechas: {len(invalid_other)}")


print("\nEjemplos de casos fuera del 5 de noviembre:")
print(
    invalid_other[
        [
            'trip_id',
            'start_ts',
            'end_ts',
            'duration_seconds',
            'distance_miles'
        ]
    ].head(30)
)


print(
    "\nValores nulos de duration_seconds "
    "entre los viajes con end_ts < start_ts:"
)

print(
    invalid_end['duration_seconds']
    .isna()
    .value_counts()
)


print("\nValores nulos en las columnas principales:")
print(
    trips_clean[
        [
            'duration_seconds',
            'distance_miles',
            'pickup_community_area',
            'dropoff_community_area'
        ]
    ].isna().sum()
)

print(
    "\nViajes con duration_seconds <= 0:",
    (trips_clean['duration_seconds'] <= 0).sum()
)


print("\nDuraciones negativas:")
print((trips_clean['duration_seconds'] < 0).sum())

print("\nDuraciones iguales a cero:")
print((trips_clean['duration_seconds'] == 0).sum())

zero_duration = trips_clean[
    trips_clean['duration_seconds'] == 0
]

print("\nEjemplos de viajes con duración igual a cero:")
print(
    zero_duration[
        [
            'trip_id',
            'start_ts',
            'end_ts',
            'duration_seconds',
            'distance_miles',
            'pickup_community_area',
            'dropoff_community_area'
        ]
    ].head(20)
)

print(
    "\nViajes con duración cero y distancia mayor que cero:",
    (
        (trips_clean['duration_seconds'] == 0)
        & (trips_clean['distance_miles'] > 0)
    ).sum()
)

# ------------------------------------------------------------
# Limpiar registros con duración o fechas inválidas
# ------------------------------------------------------------

valid_trips = (
    trips_clean['duration_seconds'].notna()
    & (trips_clean['duration_seconds'] > 0)
    & trips_clean['end_ts'].notna()
    & (trips_clean['end_ts'] >= trips_clean['start_ts'])
)

trips_clean = trips_clean[valid_trips].copy()


# ------------------------------------------------------------
# Verificar resultado de la limpieza
# ------------------------------------------------------------

print("\nFilas después de limpiar duración y fechas:")
print(trips_clean.shape)

print("\nDuraciones nulas:")
print(trips_clean['duration_seconds'].isna().sum())

print("\nDuraciones <= 0:")
print((trips_clean['duration_seconds'] <= 0).sum())

print("\nEnd_ts nulos:")
print(trips_clean['end_ts'].isna().sum())

print("\nEnd_ts anteriores a start_ts:")
print((trips_clean['end_ts'] < trips_clean['start_ts']).sum())


# ------------------------------------------------------------
# Ajustar timestamps a la hora
# ------------------------------------------------------------

trips_clean['start_ts'] = trips_clean['start_ts'].dt.floor('h')
trips_clean['end_ts'] = trips_clean['end_ts'].dt.floor('h')


# ------------------------------------------------------------
# Verificar el resultado
# ------------------------------------------------------------

print("\nPrimeras fechas después de ajustar a la hora:")
print(
    trips_clean[
        ['start_ts', 'end_ts']
    ].head()
)

print("\nRango de fechas:")
print(
    trips_clean[
        ['start_ts', 'end_ts']
    ].agg(['min', 'max'])
)


# ------------------------------------------------------------
# Correspondencia entre Community Areas de Chicago
# y neighborhood_id de la tabla neighborhoods de TripleTen
# ------------------------------------------------------------

community_to_neighborhood = {
    1: 70,   # Rogers Park
    2: 89,   # West Ridge
    3: 82,   # Uptown
    4: 46,   # Lincoln Square
    5: 59,   # North Center
    6: 44,   # Lake View
    7: 45,   # Lincoln Park
    8: 68,   # Near North Side -> River North
    9: 26,   # Edison Park
    10: 62,  # Norwood Park
    11: 42,  # Jefferson Park
    12: 73,  # Forest Glen -> Sauganash,Forest Glen
    13: 61,  # North Park
    14: 0,   # Albany Park
    15: 66,  # Portage Park
    16: 40,  # Irving Park
    17: 22,  # Dunning
    18: 53,  # Montclare
    19: 9,   # Belmont Cragin
    20: 37,  # Hermosa
    21: 8,   # Avondale
    22: 49,  # Logan Square
    23: 38,  # Humboldt Park
    24: 90,  # West Town
    25: 6,   # Austin
    26: 30,  # West Garfield Park -> Garfield Park
    27: 30,  # East Garfield Park -> Garfield Park
    28: 87,  # Near West Side -> West Loop
    29: 60,  # North Lawndale
    30: 48,  # South Lawndale -> Little Village
    31: 51,  # Lower West Side
    32: 50,  # Loop
    33: 57,  # Near South Side
    34: 3,   # Armour Square
    35: 21,  # Douglas
    36: 64,  # Oakland
    37: 28,  # Fuller Park
    38: 33,  # Grand Boulevard
    39: 43,  # Kenwood
    40: 84,  # Washington Park
    41: 39,  # Hyde Park
    42: 92,  # Woodlawn
    43: 77,  # South Shore
    44: 17,  # Chatham
    45: 7,   # Avalon Park
    46: 75,  # South Chicago
    47: 15,  # Burnside
    48: 16,  # Calumet Heights
    49: 71,  # Roseland
    50: 67,  # Pullman
    51: 76,  # South Deering
    52: 23,  # East Side
    53: 88,  # West Pullman
    54: 69,  # Riverdale
    55: 36,  # Hegewisch
    56: 31,  # Garfield Ridge
    57: 2,   # Archer Heights
    58: 13,  # Brighton Park
    59: 52,  # Mckinley Park
    60: 12,  # Bridgeport
    61: 58,  # New City
    62: 85,  # West Elsdon
    63: 29,  # Gage Park
    64: 20,  # Clearing
    65: 86,  # West Lawn
    66: 18,  # Chicago Lawn
    67: 27,  # West Englewood -> Englewood
    68: 27,  # Englewood
    69: 34,  # Greater Grand Crossing -> Grand Crossing
    70: 4,   # Ashburn
    71: 5,   # Auburn Gresham
    72: 10,  # Beverly
    73: 83,  # Washington Heights
    74: 55,  # Mount Greenwood
    75: 54,  # Morgan Park
    76: 63,  # O'Hare
    77: 25   # Edgewater
}

# ------------------------------------------------------------
# Verificar que todos los Community Areas tengan correspondencia
# ------------------------------------------------------------

pickup_unmapped = trips_clean.loc[
    trips_clean['pickup_community_area'].notna()
    & ~trips_clean['pickup_community_area'].isin(
        community_to_neighborhood.keys()
    ),
    'pickup_community_area'
].unique()

dropoff_unmapped = trips_clean.loc[
    trips_clean['dropoff_community_area'].notna()
    & ~trips_clean['dropoff_community_area'].isin(
        community_to_neighborhood.keys()
    ),
    'dropoff_community_area'
].unique()

print("\nCommunity Areas de pickup sin correspondencia:")
print(pickup_unmapped)

print("\nCommunity Areas de dropoff sin correspondencia:")
print(dropoff_unmapped)


# ------------------------------------------------------------
# Convertir Community Areas a neighborhood_id
# ------------------------------------------------------------

trips_clean['pickup_location_id'] = (
    trips_clean['pickup_community_area']
    .map(community_to_neighborhood)
    .fillna(80)  # Undef
    .astype('int64')
)

trips_clean['dropoff_location_id'] = (
    trips_clean['dropoff_community_area']
    .map(community_to_neighborhood)
    .fillna(80)  # Undef
    .astype('int64')
)


# ------------------------------------------------------------
# Verificar la conversión de ubicaciones
# ------------------------------------------------------------

print("\nValores nulos en las nuevas columnas:")
print(
    trips_clean[
        ['pickup_location_id', 'dropoff_location_id']
    ].isna().sum()
)

print("\nCantidad de pickups Undef:")
print((trips_clean['pickup_location_id'] == 80).sum())

print("\nCantidad de dropoffs Undef:")
print((trips_clean['dropoff_location_id'] == 80).sum())

print("\nEjemplos de la conversión:")
print(
    trips_clean[
        [
            'pickup_community_area',
            'pickup_location_id',
            'dropoff_community_area',
            'dropoff_location_id'
        ]
    ].head(10)
)


print("\nLoop (Community Area 32 -> neighborhood_id 50):")
print(
    trips_clean.loc[
        trips_clean['pickup_community_area'] == 32,
        ['pickup_community_area', 'pickup_location_id']
    ].head()
)

print("\nO'Hare (Community Area 76 -> neighborhood_id 63):")
print(
    trips_clean.loc[
        trips_clean['dropoff_community_area'] == 76,
        ['dropoff_community_area', 'dropoff_location_id']
    ].head()
)

# ------------------------------------------------------------
# Eliminar columnas de Community Area originales
# ------------------------------------------------------------

trips_clean = trips_clean.drop(
    columns=[
        'pickup_community_area',
        'dropoff_community_area'
    ]
)


# ------------------------------------------------------------
# Sustituir trip_id original por una secuencia numérica
# ------------------------------------------------------------

trips_clean = trips_clean.reset_index(drop=True)

trips_clean['trip_id'] = (
    trips_clean.index + 1
)


# ------------------------------------------------------------
# Ordenar las columnas con la estructura final de trips
# ------------------------------------------------------------

trips_clean = trips_clean[
    [
        'trip_id',
        'cab_id',
        'start_ts',
        'end_ts',
        'duration_seconds',
        'distance_miles',
        'pickup_location_id',
        'dropoff_location_id'
    ]
]


# ------------------------------------------------------------
# Verificar estructura final
# ------------------------------------------------------------

print("\nEstructura final de trips:")
print(trips_clean.shape)

print("\nColumnas:")
print(trips_clean.columns.tolist())

print("\nTipos de datos:")
print(trips_clean.dtypes)

print("\nPrimeras filas:")
print(trips_clean.head())

print("\nÚltimas filas:")
print(trips_clean.tail())


# ------------------------------------------------------------
# Verificar duración con parte decimal
# ------------------------------------------------------------

print(
    "\nDuraciones con parte decimal:",
    (trips_clean['duration_seconds'] % 1 != 0).sum()
)


# ------------------------------------------------------------
# Conversión tipo campo duración en segundos
# ------------------------------------------------------------

trips_clean['duration_seconds'] = (
    trips_clean['duration_seconds'].astype('int64')
)

print(trips_clean.dtypes)


# ------------------------------------------------------------
# Guardar tabla trips final
# ------------------------------------------------------------

trips_output_file = data_folder / "trips.csv"

trips_clean.to_csv(
    trips_output_file,
    index=False,
    date_format="%Y-%m-%d %H:%M:%S"
)

print("\nTabla trips guardada correctamente.")
print(f"Archivo: {trips_output_file.resolve()}")
print(f"Registros: {len(trips_clean):,}")
