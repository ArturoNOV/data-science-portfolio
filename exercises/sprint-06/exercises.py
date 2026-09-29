from pathlib import Path
import pandas as pd


# Función para acceder a los datasets.
def read_file(file, **kwargs):
    folder = Path(__file__).resolve().parent / 'datasets'
    path = folder / file

    extension = path.suffix.lower()

    if extension == '.csv':
        kwargs.setdefault('encoding', 'latin1')
        return pd.read_csv(path, **kwargs)

    elif extension in ['.xlsx', '.xls']:
        return pd.read_excel(path, **kwargs)

    else:
        raise ValueError(f'Formato no soportado: {extension}')
    
    

"""
Vamos a crear un programa que recorra el diccionario financial_info y calcule el valor
total de todas las acciones. Esto puede resultar útil para los inversores y las
inversoras que deseen obtener una visión general rápida del
rendimiento de su cartera.

Para hacer esto, necesitas utilizar un bucle for para iterar sobre el diccionario
financial_info, extraer el precio de las acciones (los precios de las acciones
almacenados como valores) y actualizar la variable total_value.

Cuando termines, muestra total_value en la pantalla.
"""

financial_info = {
    'American Express': 93,
    'Boeing': 178,
    'Coca-Cola': 45,
    'Walt Disney': 119,
    'Nike': 97,
    'JPMorgan': 96,
    'Walmart': 130
}

total_value = 0 # el valor que actualizarás en cada iteración del bucle

for value in financial_info.values():
    total_value += value

print(total_value)

print()



"""
Ahora, calculemos nuevamente el valor total de todas las acciones, pero esta vez con la
ayuda del método items():

De nuevo, vamos a crear un programa que recorra el diccionario financial_info y
calcule el valor total de todas las acciones.

Esta vez necesitas usar el método items() en lugar de values().

Cuando termines, muestra total_value en la pantalla.
"""

financial_info = {
    'American Express': 93,
    'Boeing': 178,
    'Coca-Cola': 45,
    'Walt Disney': 119,
    'Nike': 97,
    'JPMorgan': 96,
    'Walmart': 130
}

total_value = 0 # el valor que actualizarás en cada iteración del bucle

for key, value in financial_info.items():
    total_value += value

print(total_value)

print()



"""
Examina el código a continuación y luego ejecútalo para ver el resultado.
"""

bus_schedule = {
    '72': ['8:00', '12:00', '17:30'],
    '26': ['9:30', '15:00'],
    '17': ['7:30', '12:30', '15:30']
}

# iteramos sobre las claves y los valores del diccionario
for route, times in bus_schedule.items():
    # iteramos sobre los valores de la lista
    for time in times:
        # mostramos la ruta y su horario correspondiente
        print(f"Ruta {route} - Hora {time}")

print()



"""
Ejecuta el suguiente código para ver cómo funciona:
"""

movies_table = [
    ['The Shawshank Redemption', 'USA', 'drama', 1994, 142, 9.111],
    ['The Godfather', 'USA', 'drama, crime', 1972, 175, 8.730],
    ['The Dark Knight', 'USA', 'fantasy, action, thriller', 2008, 152, 8.499]
]

print(movies_table[2][3])

print()



"""
Examina el código que aparece a continuaciób y ejecútalo
"""

movies_table = [
    {'movie_name':'The Shawshank Redemption', 'country':'USA', 'genre':'drama', 'year':1994, 'duration':142, 'rating':9.111},
    {'movie_name':'The Godfather', 'country':'USA', 'genre':'drama, crime', 'year':1972, 'duration':175, 'rating':8.730},
    {'movie_name':'The Dark Knight', 'country':'USA', 'genre':'fantasy, action, thriller', 'year':2008, 'duration':152, 'rating':8.499}
]

# ahora accedemos a la columna por su nombre:
print(movies_table[2]['movie_name'])

print()



"""
Nuestro objetivo es multiplicar la cantidad y el precio de cada artículo del pedido. El
siguiente código hace exactamente esto. Primero, examínalo y luego ejecútalo para ver
cuál es el resultado. Presta atención a los comentarios que dejamos en el código.
Explican claramente lo que está pasando.
"""

order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'price': 9
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'price': 2
    }
]

# variable del precio total del pedido
total_price = 0 

# iterar sobre cada diccionario de la lista
for item in order: 
# añadir a la variable el precio del elemento multiplicado por la cantidad
    total_price += item['price'] * item['quantity']

print(total_price)

print()



"""
Examina el código que aparece a continuación y ejecútalo para ver qué produce.
"""

order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'price': 9
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'price': 2
    }
]

# variable para almacenar el resultado
filtered_order = [] 

for item in order: # iterar sobre cada diccionario de la lista
	if item['category'] == 'pizza': # si la categoría es pizza...
		filtered_order.append(item) # agregamos el diccionario a la lista filtered_order

# mostramos la lista filtrada de diccionarios
print(filtered_order) 

print()



"""
Volvamos al diccionario order. Halla el precio total para todas las pizzas en order y
muéstralo. Usa el mismo método que en los ejemplos de esta lección. Si tienes
dificultades para resolverlo, consulta la pista.
"""

order = [
    {
        'item': 'Margherita pizza',
        'category': 'pizza',
        'quantity': 2,
        'comment': 'Add extra cheese please!',
        'price': 9 # precio por elemento
    },
    {
        'item': 'Ham pizza',
        'category': 'pizza',
        'quantity': 1,
        'comment': '',
        'price': 12
    },
    {
        'item': 'Pepsi 1 l',
        'category': 'beverages',
        'quantity': 3,
        'comment': '',
        'price': 2
    },
    {
        'item': 'Apple juice 0.5 l',
        'category': 'beverages',
        'quantity': 1,
        'comment': '',
        'price': 1
    },
    {
        'item': 'Croissant with cheese',
        'category': 'baked foods',
        'quantity': 2,
        'comment': '',
        'price': 1
    }
]

total_price = 0

for item in order:
    if item['category'] == 'pizza':
        total_price += item['price'] * item['quantity']

print(total_price)

print()



"""
Volvamos a nuestro ejemplo de las películas. Ahora, tienes como objetivo escribir una
función, filter_by_genre(), con dos parámetros:

genre=: el nombre del género, por defecto 'drama'.
data=: datos sobre las películas, sin valor por defecto.
La función debe devolver una lista de listas que solamente contengan películas con el
género pasado en el parámetro genre=.
"""

# esta función imprime las tablas filtradas.
def print_movie_info(data):
    for movie in data:
        print(movie)


def filter_by_genre(data, genre='drama'):
    filtered_results = []
    for row in data:
        if genre in row[3]:
            filtered_results.append(row)
    return filtered_results


movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# a continuación ejecutamos dos funciones para obtener resultados.
movies_filtered = filter_by_genre(movies_info)
print_movie_info(movies_filtered)

print()



"""
Extrae la columna 'track' del DataFrame original y almacénala en la variable tracks.
Este será tu Series. A continuación, obtén los primeros 20 elementos de este Series y
guárdalos en la variable top20. Muestra la variable.
"""

df = read_file('music_log_chpt_11.csv')

tracks = df['track']
top20 = tracks.loc[:19]

print(top20)

print()



"""
Tu objetivo ahora es filtrar el DataFrame original extrayendo solo las canciones pop.
¿Cómo lo harías?

En primer lugar, extrae la columna 'genre' del DataFrame original y almacénala en la
variable genre.
De este modo se creará un Series. Ahora comprueba que los valores del Series sean
iguales a 'pop'.
El primer paso consiste en extraer la columna 'genre' del DataFrame original y
almacenarla en la variable genre. 

A continuación, teniendo en cuenta el ejemplo anterior, hay que comprobar que los
valores del Series sean iguales a 'pop'. El resultado de esta comprobación se almacena
en la variable pop_genre_check. 

Finalmente, utiliza la variable pop_genre_check para filtrar el DataFrame original df
para incluir solo las canciones pop. Almacena este DataFrame filtrado en la variable
pop_df y muéstrala.
"""

df = read_file('music_log_chpt_11.csv')

genre = df['genre']
pop_genre_check = genre == 'pop'
pop_df = df[pop_genre_check]

print(pop_df)

print()



"""
Llevaremos a cabo un análisis parecido solo para las canciones pop. En el siguiente
código, filtramos el DataFrame original para extraer todas las filas correspondientes a
canciones pop. Luego, como hicimos en la lección, eliminamos todas las filas donde la
columna 'total_play' tiene menos de 30 segundos porque asumimos que tales pistas se
saltan.

Busquemos la reproducción más larga de una pista de pop. Calcúlala y muestra el
resultado.
"""

df = read_file('music_log_processed.csv')

pop_tracks = df[df['genre'] == 'pop']
pop_tracks = pop_tracks[pop_tracks['total_play'] > 30]

max_dur = pop_tracks['total_play'].max()

print(max_dur)

print()



"""
Ya habíamos encontrado el valor máximo en el ejercicio anterior. Tu objetivo es
calcular los valores medios y medianos para la columna 'total_play' e imprimirlos.
"""

df = read_file('music_log_processed.csv')

pop_tracks = df[df['genre'] == 'pop']
pop_tracks = pop_tracks[pop_tracks['total_play'] > 30]

pop_mean = pop_tracks['total_play'].mean()
pop_median = pop_tracks['total_play'].median()

print(pop_mean)
print(pop_median)

print()
