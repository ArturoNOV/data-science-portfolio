import requests 


"""
1. La API web es una herramienta versátil utilizada por más que solo empresas: hay
muchos museos, bibliotecas, proyectos científicos y entusiastas que ponen su
información y servicios a disposición del público en general. Utiliza la librería
requests y el endpoint proporcionado en la url para obtener información sobre una
pintura de la colección del Museo Metropolitano. Examina la URL: el enlace base es
https://collectionapi.metmuseum.org/, luego nos dirigimos a un recurso específico.
En algún momento hay una parte v1. Esta es la versión de la API. Las diferentes
versiones pueden actuar de manera diferente, por lo que es común reflejar la actual.
Finalmente, el número 437133 es la identificación de la pintura.

Importa requests.
Llama al endpoint mediante la url proporcionada. Recupera el resultado en formato
JSON aplicándole el método apropiado. Guarda la JSON resultante en la variable
response.

Muestra artistDisplayName desde JSON llamándolo por la clave.
"""

base_url = 'https://collectionapi.metmuseum.org/'
url = base_url + 'public/collection/v1/objects/437133'

response = requests.get(url).json()
print(response['artistDisplayName'])

"""
2. Para llegar al endpoint public/collection/v1/departments utilizando la misma
URL base, simplemente agrega public/collection/v1/departments a la URL base. Guarda
la URL resultante en la variable url.

A continuación, en el precódigo, verás una línea donde almacenamos la respuesta
del endpoint y la guardamos en la variable response.

Tu objetivo ahora es convertir la respuesta en un archivo JSON. Luego, itera sobre
response.json()['departments'] y muestra los que tienen 'Art' en dpt['displayName'].
"""

base_url = 'https://collectionapi.metmuseum.org/'
url = base_url + 'public/collection/v1/departments'

response = requests.get(url)

for dpt in response.json()['departments']:
    if 'Art' in dpt['displayName']:
        print(dpt)

"""
En esta tarea, utilizarás parámetros de solicitud. La URL de esta tarea se ha
guardado en la variable url. Tu objetivo es establecer params = {'limit': 3} cuando
utilices el método get(). Esto permitirá recuperar solo las tres primeras
entradas. Almacena la respuesta en la variable response, luego conviértela a JSON y
muéstrala.
"""

url = 'https://dummyjson.com/products'
params  = {'limit': 3}

response = requests.get(url, params=params)
print(response.json())
