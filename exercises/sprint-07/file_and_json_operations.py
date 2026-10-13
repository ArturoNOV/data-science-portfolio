from pathlib import Path
import json
import requests


"""
1. Crea un archivo llamado lines.txt y escribe el contenido de la lista dada como
líneas separadas. Utiliza el método writelines().

Recuerda que puedes escribir el contenido de una lista determinada en un archivo
como líneas separadas usando el método .join() aplicado a una cadena que separa
cada elemento de la lista. El método .join() espera la lista como entrada.

2. El precódigo tiene un código que escribe el contenido de la lista dada como
líneas separadas. Tu objetivo es leer el archivo lines.txt e imprimir líneas una
por una. Recuerda que cada línea tiene un carácter de nueva línea, '\n', el cual
debes eliminar utilizando uno de los métodos que aprendiste.
"""

script_folder = Path(__file__).resolve().parent

lines = ['uno', 'dos', 'tres']

lines = "\n".join(lines)

file_path = script_folder / 'lines.txt'

with open(file_path, 'w') as f:
    f.writelines(lines)

with open(file_path, 'r') as f:
    for line in f.readlines():
        print(line.rstrip())


"""
3. En esta tarea trabajarás con archivos JSON.

En el precódigo descargamos los datos usando la librería requests. Usamos esta URL
para descargar los datos:
https://dummyjson.com/products/category/smartphones. Una vez descargados,
extrajimos el cuerpo principal de la respuesta usando el atributo .text de la
misma.

Ahora es tu momento de brillar. Analiza los datos descargados como un archivo JSON:
puedes utilizar la librería json y su función apropiada. Almacena los datos
analizados en la variable json_data. Puedes hacerlo con json_data como con un
diccionario Python normal.

Ahora, extrae la lista de productos de json_data y guárdala en la variable products.
Esta lista se almacena como un valor, que puedes extraer utilizando la clave
'products'.

A continuación, verás que hemos creado una lista vacía llamada items; además, hemos
inicializado la ariable brand para almacenar el valor 'Samsung'.

Tu objetivo es recorrer la lista products. Cada entrada en products es un
diccionario. Extrae el nombre de la marca usando la clave 'brand' y, si coincide
con el valor de la variable brand, agrega la entrada completa a la lista items.

Al final, crea un archivo 'samsung_items.json' y guarda items en él.
"""

# obtener datos de internet
response = requests.get('https://dummyjson.com/products/category/smartphones')
text = response.text

json_data = json.loads(text)
products = json_data['products']

items = []
brand = 'Samsung'

for entry in products:
    if entry['brand'] == brand:
        items.append(entry)

file_path = script_folder / 'samsung_items.json'

with open(file_path, 'w') as f:
    json.dump(items, f)
