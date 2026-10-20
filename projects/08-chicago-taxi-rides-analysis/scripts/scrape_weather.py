"""
Escribe un código para analizar los datos sobre el clima en Chicago en noviembre de 2017 desde el sitio web:

[https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html)

El nombre del DataFrame debe ser weather_records y tienes que especificarlo cuando buscas: attrs={"id": "weather_records"}.
Imprime el DataFrame completo.
"""

import pandas as pd
import requests # Importa la librería para enviar solicitudes al servidor
from bs4 import BeautifulSoup # Importa la librería para analizar la página web
from pathlib import Path

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)  # solicitud GET
soup = BeautifulSoup(req.text, 'lxml')

weather_table = soup.find('table', attrs={"id": "weather_records"})  # Guardamos la tabla HTML encontrada en la variable weather_table

headers = [] # Lista donde almacenaremos los encabezados de las columnas

for header in weather_table.find_all('th'):  # Obtenemos los encabezados de las columnas contenidos en etiquetas <th>
    headers.append(header.text.strip())

content = []  # Lista donde almacenaremos los datos de la tabla

for row in weather_table.find_all('tr'): # Cada fila de la tabla está dentro de una etiqueta <tr>
    if not row.find_all('th'): # Ignoramos la fila que contiene los encabezados
        content.append([element.text.strip() for element in row.find_all('td')])

weather_records = pd.DataFrame( # DataFrame con los datos de la tabla
        content,
        columns=headers
)

print(weather_records)


# Adaptamos los nombres de las columnas al esquema de la tabla SQL weather_records
weather_records = weather_records.rename(
    columns={
        "Date and time": "ts",
        "Temperature": "temperature",
        "Description": "description"
    }
)

# Agregamos un identificador único para cada registro
weather_records.insert(
    0,
    "record_id",
    range(1, len(weather_records) + 1)
)

# Convertimos las columnas a los tipos de datos adecuados
weather_records["ts"] = pd.to_datetime(weather_records["ts"])
weather_records["temperature"] = pd.to_numeric(
    weather_records["temperature"]
)

project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "datasets" / "reproducibility"

output_file = data_folder / "weather_records.csv"

# Guardamos el DataFrame como CSV
weather_records.to_csv(
    output_file,
    index=False,
    date_format="%Y-%m-%d %H:%M:%S"
)

print(f"\nArchivo creado: {output_file}")
print(f"Registros guardados: {len(weather_records)}")