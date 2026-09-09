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
Utiliza el atributo dtypes para conocer los tipos de datos de las columnas del DataFrame df.
Almacena el resultado en la variable data_types y muéstralo.
"""


df = read_file('music_log_chpt_11.csv')

data_types = df.dtypes

print(data_types)
print()


"""
Utiliza el atributo columns para obtener los nombres de todas las columnas en el DataFrame df.
Almacena el resultado en la variable column_names y muéstralo.
"""

column_names = df.columns 

print(column_names)
print()



"""
Utiliza el atributo shape para obtener las dimensiones (filas y columnas) del DataFrame df.
Almacena el resultado en la variable data_shape y muéstralo.
"""

data_shape = df.shape

print(data_shape)
print()



"""
Utiliza el método info() para mostrar un resumen del DataFrame df.
No es necesario almacenar el resultado, simplemente utiliza el método para obtener la información.
"""

df.info()
print()



"""
Eres un analista de una tienda online. Has recibido datos sobre los productos en diferentes categorías.
Debes inspeccionar el DataFrame para garantizar que los tipos de datos sean correctos y que las columnas
estén en su formato adecuado. Usa dtypes para verificar los tipos de datos y columns para asegurarte de que
los nombres de las columnas estén correctamente listados.
"""

data = {'product_id': [101, 102, 103],
        'product_name': ['Laptop', 'Smartphone', 'Tablet'],
        'price': [1500, 800, 300],
        'category': ['Electronics', 'Electronics', 'Electronics']}

df = pd.DataFrame(data)

data_types = df.dtypes 
column_names = df.columns 

print(data_types)
print(column_names)
print()



"""
Como parte de tu análisis, necesitas verificar si la cantidad de productos en la tienda es la correcta.
Utiliza shape para verificar el tamaño del DataFrame y info() para asegurarte de que todas las columnas
tienen 3 filas completas.
"""

data = {'product_id': [101, 102, 103],
        'product_name': ['Laptop', 'Smartphone', 'Tablet'],
        'price': [1500, 800, 300],
        'category': ['Electronics', 'Electronics', 'Electronics']}

df = pd.DataFrame(data)

data_shape = df.shape 
print(data_shape)

df.info()
print()



"""
Crea una lista anidada, music, con cuatro elementos. Cada sublista debe
almacenar dos valores de tipo string: artista y nombre de la canción.

'Bob Dylan' — 'Like A Rolling Stone'
'John Lennon' — 'Imagine'
'The Beatles' — 'Hey Jude'
'Nirvana' — 'Smells Like Teen Spirit'
"""

music = [
        ['Bob Dylan', 'Like A Rolling Stone'],
        ['John Lennon', 'Imagine'],
        ['The Beatles', 'Hey Jude'],
        ['Nirvana', 'Smells Like Teen Spirit']
]



"""
Crea una lista llamada entries que tenga dos elementos: los nombres de las
columnas 'artist' y 'track'. Luego, utiliza DataFrame() para crear una tabla
a partir de las listas music y entries. Guarda el resultado en la variable
playlist y luego muéstralo.
"""

music = [
        ['Bob Dylan', 'Like A Rolling Stone'],
        ['John Lennon', 'Imagine'],
        ['The Beatles', 'Hey Jude'],
        ['Nirvana', 'Smells Like Teen Spirit']
]

entries = ['artist', 'track']
playlist = pd.DataFrame(data=music, columns=entries)
print(playlist)
print()



"""
Ejercicio 1
Crea una lista anidada, sales_data, con cinco elementos. Cada sublista debe
almacenar cuatro valores: product_name (nombre del producto), region (región
de ventas), units_sold (unidades vendidas) y revenue (ingresos en dólares).

'Laptop' — 'North America' — 120 — 120000
'Smartphone' — 'Europe' — 340 — 170000
'Tablet' — 'Asia' — 210 — 63000
'Headphones' — 'South America' — 150 — 45000
'Smartwatch' — 'Africa' — 95 — 28500
"""

sales_data = [
        ['Laptop', 'North America', 120, 120000],
        ['Smartphone', 'Europe', 340, 170000],
        ['Tablet', 'Asia', 210, 63000],
        ['Headphones', 'South America', 150, 45000],
        ['Smartwatch', 'Africa', 95, 28500]
]



"""
Ejercicio 2
Crea una lista llamada columns que tenga cuatro elementos: 'product_name',
'region', 'units_sold', y 'revenue'. Luego, utiliza DataFrame() para crear
una tabla a partir de las listas sales_data y columns. Guarda el resultado
en la variable sales_report y luego muéstralo.
"""

sales_data = [
        ['Laptop', 'North America', 120, 120000],
        ['Smartphone', 'Europe', 340, 170000],
        ['Tablet', 'Asia', 210, 63000],
        ['Headphones', 'South America', 150, 45000],
        ['Smartwatch', 'Africa', 95, 28500]
]


columns = ['product_name', 'region', 'units_sold', 'revenue']
sales_report = pd.DataFrame(data=sales_data, columns=columns)
print(sales_report)
print()



"""
Ejercicio 1
El Pima Indians Diabetes Database es un conjunto de datos de diagnóstico de
diabetes basado en ciertas mediciones médicas de la comunidad Pima, donde se
registran diferentes variables como el número de embarazos, niveles de glucosa,
presión arterial e índice de masa corporal, entre otras. 

Uno de los primeros pasos cuando se trabaja en ciencia de datos es aprender a
importar y cargar datos dentro de tu ambiente de trabajo. En este ejercicio, deberás
cargar los datos almacenados en un archivo csv. Para ello, trabajaremos con el Pima
Indians Diabetes Database que es un conjunto de datos de diagnóstico de diabetes
basado en ciertas mediciones médicas de la comunidad Pima.

Tu objetivo es cargar el archivo diabetes.csv en tu ambiente de trabajo, que se
encuentra almacenado en la carpeta datasets.
"""

# Carga del archivo CSV
df = read_file('diabetes.csv')

# Mostrar la información estructural del DataFrame
df.info()
print()



"""
Ejercicio 2
Los archivos de Excel también son una fuente común de datos. Al igual que el
ejercicio anterior, tu objetivo es cargar el mismo dataset, pero en esta ocasión este
se encuentra en formato Excel diabetes.xlsx.
"""

# Carga del archivo xlsx
diabetes_data = read_file('diabetes.xlsx')

# Mostrar la información estructural del DataFrame
diabetes_data.info()
print()



"""
Ejercicio 3
Cuando se exploran datos, es útil ver tanto el principio como el final del conjunto de
datos. Esto ayuda a identificar patrones iniciales y posibles inconsistencias.
Utiliza los métodos head() y tail() de pandas para mostrar las primeras 3 y las
últimas 3 filas del conjunto de datos.
"""

# Carga del archivo CSV
df = read_file('diabetes.csv')

# Mostrar las primeras 3 filas
print("Primeras 3 filas:")
print(df.head(3))

# Mostrar las últimas 3 filas
print("\nÚltimas 3 filas:")
print(df.tail(3))
print()



"""
Ejercicio 1
Digimon, abreviatura de "monstruos digitales", es una franquicia que gira en torno a
una mecánica central de capturar, cuidar y entrenar monstruos, y luego participar en
combates con ellos. Es similar a Pokémon. 

En este ejercicio, trabajarás con un conjunto de datos que contiene información de
diferentes digimons como el nombre, sus niveles y características. 

Tarea:
1.-Utiliza la función read_csv() para cargar el archivo CSV '/datasets/DigiDB_digimonlist.csv' 
        en un DataFrame llamado digimon_data. Asegúrate de especificar correctamente la ruta.
        del archivo en la función read_csv().
2.-Utiliza el método info() para revisar la estructura del conjunto de datos, y
        utiliza los métodos head() y tail() para visualizar las primeras y últimas filas
        del conjunto de datos.
"""

# Cargar los datos desde el archivo CSV
file_path = 'DigiDB_digimonlist.csv'
digimon_data = read_file(file_path)

# Inspeccionar la estructura del dataset
digimon_data.info()

# Mostrar las primeras 5 filas del dataset
print(digimon_data.head(5))

# Mostrar las últimas 5 filas del dataset
print(digimon_data.tail(5))
print()



"""
Ejercicio 1
Escribe código que devuelva el nombre de la canción de la octava fila del conjunto
de datos. Los nombres de las canciones se ubican en la columna 'track'. Asigna
el valor recuperado a la variable result y muéstralo. Usa la notación completa.
"""

df = read_file('music_log_chpt_11.csv')

result = df.loc[7, 'track']

print(result)
print()



"""
Ejercicio 2
Segmenta el DataFrame df, extrayendo todos los valores de la columna 'genre'
entre la tercera y la undécima fila. Almacena los valores extraídos en la variable
index_res y muéstralos. Usa la notación completa.
"""

index_res = df.loc[2:10, 'genre']

print(index_res)
print()



"""
Ejercicio 3
Selecciona las columnas 'user_id' y 'track' del DataFrame df y almacénalo
en index_res. Muestra index_res al final. Usa la notación abreviada.
"""

index_res = df[['user_id' , 'track']]

print(index_res)
print()



"""
Ejercicio 1
Es hora de ver nuevamente cómo la notación abreviada funciona en la práctica.

Selecciona la columna 'user_id' del DataFrame df utilizando la notación
abreviada y almacénala en la variable index_res. Muestra index_res al final.
"""

index_res = df['user_id']

print(index_res)
print()



"""
Ejercicio 2
Segmenta el DataFrame df extrayendo las celdas de la sexta fila para las
columnas comprendidas entre 'total play' y 'genre'. Almacena los valores
extraídos en la variable index_res y muéstralos. Usa la notación completa.
"""

index_res = df.loc[5 , 'total play':'genre']

print(index_res)
print()



"""
Ejercicio 3
Extrae de la décima a la vigésima fila, ambas incluidas, del DataFrame df
utilizando la notación abreviada y almacena el resultado en la variable index_res.
Muestra index_res al final.
"""

index_res = df[9:20]

print(index_res)
print()



"""
Ejercicio 1
Ahora vamos a practicar un poco.

Utiliza la indexación lógica para filtrar el DataFrame almacenado en la variable df.
La tabla resultante solo debe contener filas con 'genre' igual a 'jazz'.
Almacena la tabla filtrada en la variable jazz_df y muéstrala.
"""

jazz_df = df[df['genre'] == 'jazz']

print(jazz_df)
print()



"""
Ejercicio 2
Ahora vamos a utilizar la indexación lógica para filtrar el DataFrame de nuevo. Filtra
la tabla original para incluir solamente las canciones que tengan 'total play'
mayor que 90 segundos. Almacena la tabla filtrada en la variable high_total_play_df y muéstrala.
"""

high_total_play_df = df[df['total play'] > 90]

print(high_total_play_df)
print()



"""
Ejercicio 1
Ahora trabajaremos con un DataFrame simulado que contiene información sobre las
ventas en diferentes sucursales de una empresa. Nuestro objetivo es utilizar la
indexación lógica avanzada con loc para filtrar los datos y obtener información
específica del negocio.

DataFrame:

sucursal	producto	cliente	cantidad	precio_unitario	venta_total
Centro	Camiseta roja	Ana García	2	15.99	31.98
Norte	Zapatillas azules	Luis Rodríguez	1	49.99	49.99
Sur	Camisa blanca	Pedro Hernández	3	29.99	89.97
Centro	Jeans negros	María López	1	39.99	39.99
Norte	Camiseta roja	Juan Pérez	4	15.99	63.96

Utilizando el método loc, filtra el DataFrame para obtener las ventas que cumplan
con las siguientes condiciones en este orden:
1. Sucursal: sucursal "Centro" únicamente.
2. Producto: (esto lo haremos en el siguiente ejercicio).
"""

data = {
        'sucursal': ['Centro', 'Norte', 'Sur', 'Centro', 'Norte'],
        'producto': ['Camiseta roja', 'Zapatillas azules', 'Camisa blanca', 'Jeans negros', 'Camiseta roja'],
        'cliente': ['Ana Garcia', 'Luis Rodriguez', 'Pedro Hernandez', 'Maria Lopez', 'Juan Perez'],
        'cantidad': [2, 1, 3, 1, 4],
        'precio_unitario': [15.99, 49.99, 29.99, 39.99, 15.99],
        'venta_total': [31.98, 49.99, 89.97, 39.99, 63.96]
}

df = pd.DataFrame(data)


print(df.loc[df['sucursal'] == 'Centro'])
print()



"""
Ejercicio 2
Seguiremos trabajando con el mismo DataFrame simulado que contiene
información sobre las ventas en diferentes sucursales de una empresa. En esta
ocasión, nuestro objetivo es utilizar la indexación lógica avanzada con loc para
filtrar los datos por producto. 

DataFrame:

sucursal	producto	cliente	cantidad	precio_unitario	venta_total
Centro	Camiseta roja	Ana García	2	15.99	31.98
Norte	Zapatillas azules	Luis Rodríguez	1	49.99	49.99
Sur	Camisa blanca	Pedro Hernández	3	29.99	89.97
Centro	Jeans negros	María López	1	39.99	39.99
Norte	Camiseta roja	Juan Pérez	4	15.99	63.96

Utilizando el método loc, filtra el DataFrame para obtener las ventas que cumplan con las siguientes condiciones en este orden:
1. Sucursal: sucursal "Centro" únicamente (ya lo hicimos en el ejercicio anterior).
2. Producto: solo productos vendidos a un precio unitario mayor que 25.
"""

data = {
        'sucursal': ['Centro', 'Norte', 'Sur', 'Centro', 'Norte'],
        'producto': ['Camiseta roja', 'Zapatillas azules', 'Camisa blanca', 'Jeans negros', 'Camiseta roja'],
        'cliente': ['Ana Garcia', 'Luis Rodriguez', 'Pedro Hernandez', 'Maria Lopez', 'Juan Perez'],
        'cantidad': [2, 1, 3, 1, 4],
        'precio_unitario': [15.99, 49.99, 29.99, 39.99, 15.99],
        'venta_total': [31.98, 49.99, 89.97, 39.99, 63.96]
}

df = pd.DataFrame(data)

ventas_filtradas_df = df.loc[(df['sucursal'] == 'Centro')]


ventas_filtradas_df =ventas_filtradas_df.loc[(df['precio_unitario'] > 25)]

print(ventas_filtradas_df)
print()



"""
Ejercicio 1
Las empresas suelen necesitar respuestas a preguntas específicas. Por ejemplo,
pueden querer analizar los datos de un usuario con 'user_id' = '5D9AAD37'. El
user_id puede ser un documento de identidad, número de clave fiscal o código
de identificación interna. En este caso, es un código interno de la empresa
que nos permite identificar a cada usuario. 

Filtra la tabla para obtener solo las filas de este usuario y calcula la duración
media de las canciones que ha escuchado (almacenada en 'total play'). Luego, guarda
el resultado en user_mean_dur y muéstralo.
"""

df = read_file('music_log_chpt_11.csv')

user_mean_dur = df[df['user_id'] == '5D9AAD37']['total play'].mean()

print(user_mean_dur)
print()



"""
Ejercicio 2
Escribe el código para contar el número de canciones donde 'Aura' es el artista.
Para ello, necesitarás la columna 'Artist'. Almacena el resultado en la variable
aura_count. No olvides mostrar este número.
"""


df = read_file('music_log_chpt_11.csv')

aura_count = df[df['Artist'] == 'Aura']['Artist'].count()

print(aura_count)
print()



"""
Ejercicio 3
Escribe un código que calcule el número total de segundos que nuestros usuarios
escucharon canciones del artista 'Zodiac'. Almacena el resultado en la variable
zodiac_total y muéstralo.
"""

df = read_file('music_log_chpt_11.csv')

print(df.columns)
print(df.dtypes)
zodiac_total = df[df['Artist'] == 'Zodiac']['total play'].sum()

print(zodiac_total)
print()



"""
Ejercicio 1
Una plataforma de streaming de música quiere analizar los hábitos de escucha de
sus usuarios en función del género. Específicamente, quieren saber la duración
promedio de escucha para la música jazz y el tiempo total de escucha para la
música rock.

Antes de comenzar, recuerda que el DataFrame tiene 5 columnas: user_id, total play, Artist, genre y track.
"""

# Filtrar por géneros jazz y rock
jazz_df = df[df['genre'] == 'jazz']
rock_df = df[df['genre'] == 'rock']

print(jazz_df)
print(rock_df)

# Calcular la duración promedio de escucha para jazz y el tiempo total de escucha para rock
avg_jazz_duration = jazz_df['total play'].mean()
total_rock_time = rock_df['total play'].sum()

print("Duración promedio jazz:", avg_jazz_duration)
print("Tiempo total rock:", total_rock_time)
print()



"""
Ejercicio 2
La plataforma de streaming de música quiere saber cuántas canciones de música
clásica se han reproducido y cuál es el tiempo total de reproducción para la 
música pop.

La plataforma de streaming de música está analizando las estadísticas de uso de
su catálogo.

Tu tarea es ayudarlos a responder dos preguntas específicas a partir del registro
de reproducciones:
- ¿Cuántas canciones de música clásica se han reproducido?
- ¿Cuál es el tiempo total de reproducción de la música pop?

Para ello, deberás:
- Filtrar el DataFrame por género.
- Filtrar la tabla para conservar solo las filas donde el género sea "classical" o "pop".
- Contar las canciones clásicas, utilizando la columna track.
- Sumar el tiempo total de reproducción para las canciones pop, utilizando la columna total play.
- Mostrar los resultados de forma clara.

Recuerda que el DataFrame tiene 5 columnas: user_id, total play, Artist, genre y track.
"""

print(df['genre'])

# Filtrar por géneros clásicos y pop
classical_df = df[df['genre'] == 'classical']
pop_df = df[df['genre'] == 'pop']

# Calcular el conteo de canciones clásicas y el tiempo total de pop
classical_count = classical_df['track'].count()
pop_total_time = pop_df['total play'].sum()

print("Número de canciones clásicas:", classical_count)
print("Tiempo total pop:", pop_total_time)
print()



"""
¡Necesitamos tu ayuda! Nuestro equipo ha intentado leer un conjunto de datos, pero
el resultado es un desastre. ¿Puedes corregirlo?

Esto es lo que nuestro equipo ha hecho:


df = pd.read_csv("/datasets/sports.csv")
print(df.head())
Y el resultado es: 

    Messi;Football;37;7.5
Mbappe;Football;24;10    2.0
Djokovic;Tennis;36;8    NaN

Reescribe el código para que los datos sean cargados correctamente. Los datos están
separados por punto y coma. Imprime el resultado usando el método head().
"""

df = read_file("sports.csv", sep=";")
print(df.head())
print()



"""
¡Necesitamos más ayuda! Has podido subir el dataset usando el separador correcto, pero
los datos no tienen encabezado. 

Esto es lo que has hecho:

df = pd.read_csv("/datasets/sports.csv", sep=";")
print(df.head())
Y el resultado es: 

    Messi      Football    37    7,5
0    Mbappe    Football    24    10,2
1    Djokovic    Tennis    36    8,0
Carga nuevamente el archivo y reescribe el código para que los datos sean cargados
con un encabezado adecuado. Las columnas deben ser llamadas “Nombre”, “Deporte”, “Edad” y “Salario”. 

No se olvide de imprimir el resultado usando el método head().
"""

column_names = [
        'Nombre',
        'Deporte',
        'Edad',
        'Salario'
]
df = read_file("sports.csv",
                sep=";",
                header = None,
                names = column_names)

print(df.head())
print()



"""
¡Te necesitamos una vez más! Has podido subir el dataset, separarlo en columnas y
agregar el encabezado, pero hemos descubierto que los salarios no están bien 
cargados. 

Esto es lo que has hecho:

columnas = ["Nombre", "Deporte", "Edad", "Salario"]
df = pd.read_csv("/datasets/sports.csv", sep=";", header=None, names=columnas)
print(df.head())

Y el resultado es: 

    Nombre     Deporte      Edad    Salario
0    Messi       Football      37      7,5
1    Mbappe     Football      24      10,2
2    Djokovic     Tennis      36      8,0

Observa como los salarios tienen coma. Carga nuevamente el archivo y reescribe el
código para que los salarios reconozcan “,” como separador decimal.  Imprime el
resultado usando el método head().
"""

column_names = [
        'Nombre',
        'Deporte',
        'Edad',
        'Salario'
]
df = read_file("sports.csv",
                sep=";",
                header = None,
                names = column_names,
                decimal = ',')

print(df.head())
print()



"""
Tarea 1
Para esta actividad cuentas con el siguiente conjunto de datos.

  letters$colors$decimals
0            a$yellow$1a2
1               b$red$1a3
2              c$cyan$1a4

Como puedes apreciar, los datos contenidos se encuentran separados por el
delimitador  $.  Si intentamos cargar este conjunto de datos directamente
con read_csv(), la función no reconocerá el formato y retornará el código
que mostramos en el cuadro anterior.

Para lograr que pandas pueda leer y formatear correctamente nuestro conjunto
de datos, debes tener en cuenta lo siguiente: 

- La primera fila debe ser considerada como el encabezado.
- Las columnas deben estar separadas por el delimitador $.
- Los decimales deben estar separados por a.

Utilizando la función read_csv(), especifica los parámetros estudiados en esta
lección para abordar este tipo de escenarios. Al finalizar, muestra el DataFrame.

Puedes encontrar el dataset en /datasets/letters_colors_decimals.csv.
"""

df = read_file("letters_colors_decimals.csv",
                sep = '$',
                decimal = 'a')

print(df.head())
print()



"""
Carga la hoja reviews siguiendo estos pasos:
1. Lee la primera hoja del Excel almacenado en /datasets/product_reviews.xlsx
y guárdalo en un dataframe llamado df_reviews.
2. Muestra el DataFrame completo en pantalla utilizando print(). 
No uses métodos como head() ni tail();
"""

df_reviews = read_file("product_reviews.xlsx")

print(df_reviews)
print()



"""
Para obtener más información sobre los productos de este conjunto de datos, lee la
hoja products del archivo Excel en una variable llamada df_products.

Por último, no olvides mostrar el resultado en pantalla.
"""

df_products = read_file("product_reviews.xlsx",
                        sheet_name = 'products')

print(df_products)
print()



"""
Además de los nombres de los productos, el archivo Excel también contiene información
sobre cómo se clasifican los productos. Por eso había una columna 'category_id en la
tabla de la última tarea.

Lee la última hoja product_categories y guárdala en una variable llamada df_categories.
Luego, simplemente muestra el df_categories en la pantalla.
"""

df_categories = read_file("product_reviews.xlsx",
                        sheet_name = 'product_categories')

print(df_categories)
print()



"""
En este ejercicio, aprenderás a utilizar el método head() de Pandas para ver las
primeras 10 filas de un conjunto de datos. A continuación, realiza las siguientes acciones:

1. Utiliza el método head() para mostrar las primeras 10 filas del conjunto de
datos de centrales eléctricas.
2. Asegúrate de que puedes ver un resumen adecuado de las primeras filas.
"""

column_names = [
        'country',
        'name',
        'capacity_mw',
        'latitude',
        'longitude',
        'primary_fuel',
        'owner'
]
data = read_file(
        'gpp_modified.csv',
        sep='|',
        header=None,
        names=column_names,
        decimal=',',
)

print(data.head(10))
print()



"""
El siguiente ejercicio ya incluye una instrucción para mostrar las primeras 5 filas
del conjunto de datos de centrales eléctricas utilizando el método head(). Ahora,
escribe un código que realice las siguientes acciones:

1. Seleccionar 5 filas aleatorias del conjunto de datos y guardarlas en la variable
    sample. Ten en cuenta que, dada la aleatoriedad del método sample, los
    resultados pueden ser diferentes.
2. Mostrar el contenido de la variable sample.
"""

column_names = [
        'country',
        'name',
        'capacity_mw',
        'latitude',
        'longitude',
        'primary_fuel',
        'owner'
]
data = read_file(
        'gpp_modified.csv',
        sep='|',
        header=None,
        names=column_names,
        decimal=',',
)

print(data.head())
print()

sample = data.sample(5)
print(sample)
print()



"""
Ahora que tenemos una idea de cómo se ven los datos en cada columna, consulta
la información general sobre este conjunto de datos llamando al método info().
Hemos incluido el código de la tarea anterior para que puedas comparar las filas
de muestra con la salida de info(), una al lado de la otra.
"""

column_names = [
        'country',
        'name',
        'capacity_mw',
        'latitude',
        'longitude',
        'primary_fuel',
        'owner'
]
data = read_file(
        'gpp_modified.csv',
        sep='|',
        header=None,
        names=column_names,
        decimal=',',
)

sample = data.sample(5, random_state=543210)
print(sample)
print()


data.info()
print()



"""
La Fórmula 1, también conocida como F1, representa la cumbre de las carreras de
monoplazas. Gobernada por la Federación Internacional del Automóvil (FIA), se ha
convertido en un deporte reconocido mundialmente, atrayendo a millones de
fanáticos alrededor del mundo. El deporte es conocido por sus carreras a alta
velocidad, su profundidad estratégica y la búsqueda incansable de la excelencia
tanto en la pista como en el diseño e ingeniería del automóvil.

El dataset Driver Details, disponible en /datasets/Driver_Details.csv,
contiene información acerca de los pilotos que han participado en la Fórmula 1
desde 1950 a 2024. Tu objetivo es explorar preliminarmente este conjunto de datos,
con el fin de conocer cómo están estructurados los datos, así como una vista real
del contenido del mismo. Para ello:

1. Deberás cargar el dataset en tu ambiente de trabajo.
2. Utilizar el método sample() o head(), con el fin de obtener una vista inicial de
   los elementos contenidos en el dataset.
3. Utilizar el método info() para obtener una vista preliminar sobre las columnas
   presentes, el tipo de dato asociado y número de registros.
4. Validar que cada columna contenga una estructura de datos asociada a la información
   que almacenan. Por ejemplo, número con integer/float o texto con string.
"""

df = read_file("Driver_Details.csv") # carga tu dataset

print(df.head()) # llama al metodo sample() o head() sobre tu DataDrame
df.info() # llama al metodo info() sobre tu DataDrame
print()



"""
Obtén una vista general de la columna 'primary_fuel' llamando a describe()
en ella. Devuelve el resultado de la misma.
"""

column_names = [
        'country',
        'name',
        'capacity_mw',
        'latitude',
        'longitude',
        'primary_fuel',
        'owner'
]
data = read_file(
        'gpp_modified.csv',
        sep='|',
        header=None,
        names=column_names,
        decimal=',',
)

print(data['primary_fuel'].describe())
print()



"""
En el ejercicio anterior, obtuvimos una vista preliminar para una única columna,
'primary_fuel'.  Ahora, aplica el mismo método sobre todas las columnas de tipo
object. Devuelve el resultado de la misma.
"""

pd.set_option('display.max_columns', None)

column_names = [
        'country',
        'name',
        'capacity_mw',
        'latitude',
        'longitude',
        'primary_fuel',
        'owner'
]
data = read_file(
        'gpp_modified.csv',
        sep='|',
        header=None,
        names=column_names,
        decimal=',',
)

print(data.describe(include = 'object'))
print()



"""
Siguiendo con nuestro dataset de la Fórmula 1, tu objetivo será analizar en detalle
las variables numéricas y categóricas del DataFrame df.

Para ello:
1. Aplica el método describe() sobre el objeto df para obtener estadísticas generales
   de las variables numéricas.
2. Vuelve a utilizar describe(), esta vez incluyendo un parámetro que te permita
   explorar únicamente las variables categóricas dentro de df.

Este análisis te ayudará a conocer mejor la estructura de los datos, como la
cantidad de valores únicos, los más frecuentes, los promedios y rangos de los
valores numéricos.
"""

df = read_file('Driver_Details.csv')

print(df.describe())
print(df.describe(include = 'object'))
print()



"""
Para familiarizarnos con los valores ausentes (NaN), vamos a examinar las primeras
10 filas de nuestro conjunto de datos music_log_raw.

- Utiliza el método head() para mostrar las primeras 10 filas del DataFrame.
- Observa detenidamente las filas para identificar cualquier valor NaN. Recuerda
que NaN se representa como un espacio en blanco o un punto.
"""

df = read_file('music_log_raw.csv')

# Muestra las primeras 10 filas del DataFrame
print(df.head(10))
print()



"""
Intenta imprimir los valores de la columna total play.
"""


df = read_file('music_log_raw.csv')

# Imprime los valores de la columna total play
print(df['total play'])
print()



"""
Primero, debes ver si algo está mal con los nombres de las columnas y qué es. Así
que comienza por mostrar los nombres de columna de la tabla df.
"""

df = read_file('music_log_raw.csv')


print(df.columns)
print()



"""
Debes identificar tres problemas en los nombres de las columnas '  user_id',
'total play' y 'Artist'. 

Los problemas incluyen espacios innecesarios, uso de mayúsculas y nombres
con espacios.

Renombra las siguientes tres columnas en df para que sigan una convención
clara y coherente:

'  user_id' → 'user_id'

'total play' → 'total_play'

'Artist' → 'artist'

1. Crea un diccionario con los nombres actuales como claves y los nombres
   corregidos como valores.
2. Usa el método rename() del DataFrame df y pasa el diccionario con el
   parámetro columns. Importante: no utilices el parámetro inplace. En su
   lugar, guarda el resultado en una nueva variable df_new_cols.
3. Luego, muestra el atributo columns para df_new_cols para confirmar que
   los cambios se han aplicado.
"""

df = read_file('music_log_raw.csv')

# crea tu diccionario aquí
new_columns = {
        '  user_id' : 'user_id',
        'total play' : 'total_play',
        'Artist' : 'artist'
}

df_new_cols = df.rename(columns = new_columns)


print(df_new_cols.columns)
print()



"""
En el ejercicio anterior, renombraste las columnas del DataFrame df creando
una nueva variable. Ahora, realiza los mismos cambios pero usando el parámetro
inplace para modificar directamente el DataFrame df.

Renombra las siguientes tres columnas en df:

'  user_id' → 'user_id'

'total play' → 'total_play'

'Artist' → 'artist'

Crea un diccionario con los nombres antiguos como claves y los nuevos como valores,
y luego usa el método rename() con el parámetro inplace=True para realizar los
cambios directamente en df.

Finalmente, muestra el atributo columns para df para confirmar que los cambios se
han aplicado correctamente.
"""

df = read_file('music_log_raw.csv')

# Renombrar las columnas utilizando el parámetro inplace

columns_new = {
        '  user_id' : 'user_id',
        'total play' : 'total_play',
        'Artist' : 'artist'
}

df.rename(columns = columns_new, inplace = True)

# Mostrar las columnas para confirmar los cambios
print(df.columns)
print()



"""
Elimina los espacios en blanco al principio y al final de los nombres de las columnas
usando el método strip(). Aplica este cambio a una columna de ejemplo: '  User_ID'.

Guarda el resultado en una variable llamada name_stripped. Luego, imprime el valor de
esta variable para confirmar el cambio.
"""

# Nombre de la columna con espacios en blanco
column_name = '  User_ID'


name_stripped = column_name.strip()

print(name_stripped)
print()



"""
Después de eliminar los espacios en blanco, convierte el nombre de la columna a 
minúsculas usando el método lower(). Aplica este cambio a una columna de 
ejemplo: 'User_ID'.

Guarda el resultado en una variable llamada name_lowered. Luego, imprime el valor 
de esta variable para confirmar el cambio.
"""

# Nombre de la columna con mayúsculas
column_name = 'User_ID'


name_lowered = column_name.lower()

print(name_lowered)
print()



"""
Después de eliminar espacios en blanco y convertir el nombre a minúsculas,
reemplaza los espacios en blanco dentro del nombre de la columna con guiones
bajos (_) usando el método replace(). Aplica este cambio a una columna de
ejemplo: 'total play'.

Guarda el resultado en una variable llamada name_no_spaces. Luego, imprime el
valor de esta variable para confirmar el cambio.
"""

# Nombre de la columna con espacios internos
column_name = 'total play'


name_no_spaces = column_name.replace(' ','_')

print(name_no_spaces)
print()



"""
Volvamos a nuestro dataset music_log_raw.csv. Queremos que apliques los
siguientes cambios a todos los nombres de columna usando un bucle: 

1. Elimina espacios en blanco al principio y al final de cada nombre de
   columna con strip().
2. Convierte todas las letras a minúsculas con lower().
3. Reemplaza los espacios en blanco internos con guiones bajos (_) usando
   replace().

Guarda los nuevos nombres de columna en la lista new_col_names y luego
asigna esta lista al atributo columns del DataFrame para actualizarlo.

Finalmente, imprime df.columns para confirmar que los cambios se han
aplicado correctamente.
"""


df = read_file('music_log_raw.csv')

new_col_names = []

for old_name in df.columns:
        name_stripped = old_name.strip()
        name_lowered = name_stripped.lower()
        name_no_spaces = name_lowered.replace(' ', '_')
        # print(name_no_spaces)
        new_col_names.append(name_no_spaces)

df.columns = new_col_names
print(df.columns)
print()



"""
Escribe código que sume la cantidad de valores ausentes en todas las columnas
del dataset. Guarda el resultado en la variable mis_val y muéstralo.
"""


df = read_file('music_log_raw.csv')

mis_val = df.isna().sum()

print(mis_val)
print()



"""Escribe código para recorrer las columnas genre, Artist y track del
DataFrame df y reemplaza cualquier valor ausente con el string 'no_info'. La
lista de columnas a reemplazar se almacena en la variable columns_to_replace.

Después de realizar los reemplazos, comprueba la cantidad de valores ausentes
nuevamente usando isna().sum()
"""


df = read_file('music_log_raw.csv')

columns_to_replace = ['genre', 'Artist', 'track']

for col in columns_to_replace:


        df[col].fillna('no_info', inplace = True)

print(df.isna().sum())
print()



"""
Ahora, eliminemos los NaNs en la columna total play remplazándolos con 0.

Después de realizar los reemplazos, comprueba la cantidad de valores ausentes
nuevamente usando isna().sum()
"""


df = read_file('music_log_raw.csv')


df['total play'].fillna(0, inplace = True)

print(df.isna().sum())
print()



"""
Ahora, en vez de remplazar con 0, eliminemos las filas con valores ausentes (NaN)
en la columna total play.

Después de realizar la eliminación, comprueba la cantidad de valores ausentes
nuevamente usando isna().sum() para confirmar que no quedan valores NaN en dicha columna.
"""


df = read_file('music_log_raw.csv')


df.dropna(subset=['total play'], inplace = True)

print(df.isna().sum())
print()



"""
Vamos a trabajar con un DataFrame que contiene datos de producción de petróleo
de diferentes pozos. Algunos pozos no reportan valores de producción en ciertos
periodos y necesitamos rellenar estos valores ausentes para realizar un análisis
correcto.

El DataFrame tiene las siguientes columnas:
'well_id' : ID del pozo.
'production_date' : fecha de producción.
'oil_volume' : volumen de petróleo producido en barriles.
'gas_volume' : volumen de gas producido en pies cúbicos.
'region' : región donde se encuentra el pozo.
'status' : estado del pozo.

Identifica las columnas con valores ausentes (NaN) y reemplázalos con los
siguientes valores:

- Reemplaza los valores NaN en la columna 'oil_volume' con 0 (indica que no se
   produjo petróleo ese día).
- Reemplaza los valores NaN en la columna 'status' con el string 'unknown'.

Después de realizar los reemplazos, muestra la cantidad de valores ausentes en
cada columna usando isna().sum() para confirmar que los cambios se han aplicado
correctamente.
"""


# DataFrame de la producción de petróleo
data = {
        'well_id': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6'],
        'production_date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02'],
        'oil_volume': [100, None, 200, 300, None, None],
        'gas_volume': [1000, 800, 950, 1100, 850, 900],
        'region': ['North', 'North', 'South', 'South', 'West', 'West'],
        'status': ['active', None, 'active', 'inactive', None, 'active']
}

df = pd.DataFrame(data)


df['oil_volume'].fillna(0, inplace = True)
df['status'].fillna('unknown', inplace = True)

print(df.isna().sum())
print()



"""
Vamos a eliminar las filas con valores ausentes en la columna 'oil_volume' ya
que se ha decidido que no es relevante para el análisis actual.

Elimina todas las filas con valores ausentes (NaN) en la columna 'oil_volume'.
Después de realizar la eliminación, muestra la cantidad de valores ausentes en
cada columna.
"""


# DataFrame de la producción de petróleo
data = {
        'well_id': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6'],
        'production_date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02'],
        'oil_volume': [100, None, 200, 300, None, None],
        'gas_volume': [1000, 800, 950, 1100, 850, 900],
        'region': ['North', 'North', 'South', 'South', 'West', 'West'],
        'status': ['active', None, 'active', 'inactive', None, 'active']
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Eliminar filas con valores ausentes en la columna 'oil_volume'

df.dropna(subset=['oil_volume'], inplace = True)

# Mostrar la cantidad de valores ausentes en cada columna después de la eliminación
print("Valores ausentes después de la eliminación:")

print(df.isna().sum())

# Mostrar las columnas restantes del DataFrame
print("Columnas restantes:")

print(df.columns)
print()



"""
Imagina que trabajas en una plataforma de streaming musical y tienes a tu
disposición un conjunto de datos que registra las escuchas de los usuarios.
Tu objetivo es limpiar y organizar esta información para obtener una visión
más clara de los hábitos de escucha de los usuarios y así poder personalizar
mejor las recomendaciones musicales.

Tarea:

- Identifica y elimina las filas duplicadas del DataFrame, considerando todas las columnas.
- Reinicia el índice de las filas después de eliminar los duplicados.
- Cuenta el número de duplicados.
"""


# Carga de datos
df = read_file('music_log_raw.csv')

# Número de duplicados al inicio
print('Número de filas duplicadas (Inicio): ', df.duplicated().sum())

# Eliminar duplicados y reseteo de índices a nivel de filas

df = df.drop_duplicates().reset_index(drop = True)

print('Número de filas duplicadas (Final): ', df.duplicated().sum())
print()



"""
Continuando con nuestro conjunto de datos de streaming musical, queremos
conocer la diversidad de géneros musicales que se reproducen en la plataforma.

Tarea:
1. Identifica los géneros musicales únicos presentes en la columna "genre".
2. Cuenta cuántos géneros musicales diferentes existen.
"""

# Carga de datos
df = read_file('music_log_raw.csv')

# Encontrar valores únicos en la columna “genre” y 
# asignarlos a la variable “generos_unicos. 
generos_unicos = df['genre'].unique()

# Mostrar los géneros únicos
print("Géneros musicales únicos:", generos_unicos)

# Contar la cantidad de géneros únicos
cantidad_generos = df['genre'].nunique()

# Imprimir el resultado final
print("Cantidad de géneros diferentes:", cantidad_generos)
print()



"""
A veces, en los conjuntos de datos, hay duplicados implícitos, como errores
ortográficos o variaciones de un mismo valor, lo que puede causar confusión.
Por ejemplo, hard-n-heavy y hard'n'heavy pueden ser interpretados como
géneros diferentes si no se estandarizan.

Tarea:

1. Reemplaza los siguientes valores:
   - 'hard-n-heavy' por "hard'n'heavy"
2. Reemplaza los siguientes valores:
   - 'ranchera' por 'rancheras'
3. Usa el método replace() para realizar esta estandarización.
"""

df = read_file('music_log_raw.csv')

# Reemplaze los valores ‘hard-n-heavy'` por `"hard'n'heavy"`.   

df['genre'].replace('hard-n-heavy', "hard'n'heavy", inplace = True)

# Reemplaze los valores 'ranchera'` por `'rancheras'`

df['genre'].replace('ranchera', 'rancheras', inplace = True)

# Validación
generos_unicos = df['genre'].dropna().unique()
filtros = []

for g in generos_unicos:
    if g[:3] == 'har' or g[:3] == 'ran':
        filtros.append(g)

# Imprimir el resultado
print(filtros)
print()



"""
Steam es la plataforma de juegos para PC más popular del mundo, con una extensa
colección de más de 6000 juegos y una vasta comunidad de millones de jugadores.
Esta diversidad incluye desde grandes éxitos de la industria hasta títulos
independientes más pequeños, lo que hace que contar con herramientas efectivas
de descubrimiento sea un recurso extremadamente valioso. El conjunto de datos
que utilizaremos contiene un registro de los comportamientos de los usuarios en
Steam, incluyendo las siguientes columnas:

- user-id: identificador único del usuario.
- game-title: título del juego.
- behavior-name: nombre del comportamiento (compra o jugar).
- value: valor que indica la frecuencia o cantidad del comportamiento (1 para
  compras, otros valores para horas jugadas).

Tarea
Analicemos los registros duplicados. Para ello:
 1.1. Determina el número de filas duplicadas en el dataset. 
 1.2. Elimina aquellas filas que se encuentren duplicadas.
 """

# Cargar los datos 
df = read_file('steam-200k.csv')
df.columns = ['user_id', 'game_title', 'behavior_name', 'value']

# 1.1 Contar cuántas filas duplicadas hay en el DataFrame antes de limpiarlo
#COMPLETA EL CODIGO
print("Número de filas duplicadas (Inicial): ", df.duplicated().sum()) #COMPLETA EL CODIGO)

# 1.2 Eliminar todas las filas duplicadas del DataFrame
#COMPLETA EL CODIGO
df = df.drop_duplicates()

# Confirmar que las filas duplicadas han sido eliminadas correctamente
print("Número de filas duplicadas (Final): ", df.duplicated().sum()) #COMPLETA EL CODIGO)
print()



"""
Complementando el ejercicio anterior, terminaremos de trabajar con los registros
duplicados. Ahora, utilizarás el dataset de Steam ya depurado para realizar algunas
operaciones adicionales que te ayudarán a prepararlo mejor para el análisis.

Tarea
1. Reinicia los índices del DataFrame limpio (df_sin_duplicados) para que tengan
   unorden consecutivo, comenzando desde cero.
2. Muestra en pantalla todos los valores únicos que aparecen en la columna game_title.
   Esto te ayudará a tener una idea de los distintos juegos que los usuarios han registrado en la plataforma.
"""


# Cargar los datos 
df = read_file('steam-200k.csv')
df.columns = ['user_id', 'game_title', 'behavior_name', 'value']

# Mostrar el número de filas duplicadas antes de eliminarlas
print("Número de filas duplicadas (Inicial): ", df.duplicated().sum())

# Eliminar las filas duplicadas y guardar el resultado en un nuevo DataFrame
df_sin_duplicados = df.drop_duplicates()

# Verificar que ya no hay filas duplicadas
print("Número de filas duplicadas (Final): ", df_sin_duplicados.duplicated().sum())

# 1. Reiniciar los índices del DataFrame limpio (sin duplicados)
df_sin_duplicados.reset_index(drop = True)

# 2. Mostrar todos los valores únicos en la columna 'game_title'
valores_unicos = df_sin_duplicados['game_title'].unique() # Completa
print(f"Valores únicos: {valores_unicos}")
print()




"""
Utiliza el conjunto de datos music_log_processed.csv original, el cual se
encuentra preprocesado con todos los problemas eliminados. Tu objetivo es
agrupar este dataset mediante la columna 'genre' y contar cuántas canciones
hay por género musical. Cuenta usando la columna 'genre'.
"""


df = read_file('music_log_processed.csv')

genre_groups = df.groupby('genre')['genre'].count()

print(genre_groups)
print()



"""
Ejercicio 2
Calcula el tiempo total acumulado que los usuarios han pasado escuchando cada
género. Para ello, debes ocupar la columna 'total_play' , la cual contiene
exactamente el tiempo total que un usuario ha escuchado una canción. 

Hazlo e imprime el resultado final.
"""


df = read_file('music_log_processed.csv')

genre_groups = df.groupby('genre')['total_play'].sum()

print(genre_groups)
print()



"""
Volvamos a nuestro dataset de Digimons. En esta actividad, vas a poner en práctica
el método groupby() de pandas para agrupar datos según una característica común y
luego aplicar métodos de agregación para obtener estadísticas útiles.

Recuerda que el DataFrame digimon_data contiene información sobre distintos Digimon,
organizada en columnas como Number, Digimon, Stage, Type, Attribute, y estadísticas
de nivel 50 como Lv50 HP, Lv50 SP, Lv50 Atk, Lv50 Def, Lv50 Int y Lv50 Spd.

Debes agrupar los Digimons según su nivel de evolución (Stage), y luego aplicar
sobre esta agrupación diferentes métodos de agregación para obtener la siguiente 
información:

1. El número total de Digimons por nivel (Stage).
2. La suma de los valores de salud (LV 50 HP) por nivel.
3. El promedio de los valores de velocidad (Lv50 Spd) por nivel.
"""


# Cargar el archivo CSV
digimon_data = read_file('DigiDB_digimonlist.csv')

# Agrupar los datos
grouped_stage_count = digimon_data.groupby('Stage')['Digimon'].count()
grouped_stage_sum = digimon_data.groupby('Stage')['Lv 50 HP'].sum()
grouped_stage_mean = digimon_data.groupby('Stage')['Lv50 Spd'].mean()

# Mostrar los resultados
print('Distribución de los Digimons', '\n',grouped_stage_count,'\n')
print('Total de Salud', '\n',grouped_stage_sum, '\n',)
print('Promedio Nivel de Velocidad', '\n',grouped_stage_mean)
print()



"""
Usando de nuevo el dataset music_log_processed.csv ordena de forma
descendente el DataFrame por 'user_id' y almacénalo en df_ordenado.
Muestra las primeras 10 filas de df_ordenado al final.
"""


df = read_file('music_log_processed.csv')

df_ordenado = df.sort_values('user_id', ascending=False)
print(df_ordenado.head(10))
print()



"""
Usando nuevamente el dataset music_log_processed.csv filtra solo el género
metal. Ordena de forma descendente el DataFrame por 'total_play' y
almacénalo en metal_ordenado. Muestra las primeras 10 filas de
metal_ordenado al final.
"""


df = read_file('music_log_processed.csv')

metal_ordenado = df[df['genre'] == 'metal'].sort_values('total_play', ascending=False)
print(metal_ordenado.head(10))
print()



"""
En la lección anterior, agrupaste nuestros datos music_log_processed.csv por
'genre' y calculaste el tiempo total que nuestros oyentes pasaron escuchando
cada género. Como resultado, tenemos el tiempo de escucha total para cada
'genre'. Está almacenado en la variable time_by_genre en el precódigo.

Ahora, ordenemos los resultados en orden descendente y veamos los 10 géneros
principales que más escucharon nuestros oyentes. Hazlo y guarda los resultados
en la variable time_by_genre_sort.

Toma nota que para esta tarea no necesitas especificar la columna que se va a
ordenar, ya que solamente hay una columna en la variable time_by_genre.
"""


df = read_file('music_log_processed.csv')

time_by_genre = df.groupby('genre')['total_play'].sum()

time_by_genre_sort = time_by_genre.sort_values(ascending = False)

print(time_by_genre_sort.head(10))
print()



"""
Nunca es una mala idea llamar a info() en un nuevo conjunto de datos. Echemos
un vistazo a nuestro DataFrame de registros de visitantes, el cual hemos asignado
a una variable llamada df_logs.
"""


df_logs = read_file('visit_log.csv')


print(df_logs.info())



"""
Aunque info() señala que tenemos valores ausentes, si nuestro objetivo es
contar valores ausentes, entonces hay una mejor opción: el método isna().
"""


df_logs = read_file('visit_log.csv')
print(df_logs.isna().sum())



"""
Veamos otra forma de encontrar los valores ausentes. Usemos value_counts()
en la columna 'source', pero agreguemos el parámetro dropna=False.
"""


df_logs = read_file('visit_log.csv')
print(df_logs['source'].value_counts(dropna = False))



"""
Ahora aplica el método value_counts() a la columna 'email' y almacena el
resultado en la variable email_values. Esta vez, no incluyas los valores
ausentes en la salida. Imprime el resultado.
"""


df_logs = read_file('visit_log.csv')

email_values = df_logs['email'].value_counts()

print(email_values)



"""
En esta ocasión queremos extraer filas en las que la columna 'source'
tenga valores ausentes. 
"""


df_logs = read_file('visit_log.csv')


print(df_logs[df_logs['source'].isna()])



"""
Anteriormente determinamos que la columna 'email' tiene 13 953 valores no
ausentes. ¡Eso significa que más del 90% de los datos están ausentes! 

Tu tarea es:
- Utilizar isna() para identificar los valores ausentes en la columna 'email'
  del DataFrame df_logs.
- Usar ~ para negar esa condición y obtener las filas donde 'email' no está
  ausente.
- Filtra el DataFrame y guarda el resultado en una nueva variable llamada
  df_emails.
- Imprime las primeras 10 filas usando print().

Recuerda: para negar una condición al filtrar un DataFrame, puedes anteponer
el símbolo ~ a la expresión booleana. Por ejemplo: df[~df['columna'].isna()]
selecciona las filas donde los valores no están ausentes.
"""


df_logs = read_file('visit_log.csv')

df_emails = df_logs[~df_logs['email'].isna()]

print(df_emails.head(10))



"""
La columna 'source' muestra que muchas visitas al sitio provienen de enlaces de
correo electrónico de marketing. Sin embargo, algunas filas tienen valores NaN
en 'source'.

Queremos comprobar si hay alguna fila que también tenga NaN en la columna 'email'.

Si no existe ninguna fila donde ambas columnas sean NaN, eso sugiere que los 
valores ausentes en 'source' podrían corresponder a 'email' como fuente no 
registrada.

Objetivo
Filtrar el DataFrame df_logs para obtener solo las filas donde 'email' y 'source'
tienen valores NaN.

Guardar el resultado en una nueva variable llamada df_emails y mostrarlo.

Para eso tendrás que:
- Leer el archivo CSV /datasets/visit_log.csv con read_csv.
- Filtrar las filas donde la columna 'email' es NaN.
- A partir del resultado anterior, filtrar nuevamente las filas donde la columna
  'source' también sea NaN.
- Guardar el resultado en df_emails.
- Imprimir df_emails.
"""


df_logs = read_file('visit_log.csv')

df_emails = df_logs[df_logs['email'].isna()]

df_emails = df_emails[df_emails['source'].isna()]

print(df_emails)



"""
Los valores NaN en la columna 'email' sustituyen a las direcciones de correo
electrónico de los usuarios que no se suscribieron al boletín de la tienda. 
Ya que no hay forma de averiguar sus direcciones de correo electrónico, no 
podemos rellenar manualmente los valores ausentes con datos significativos.

Pero podemos rellenarlos con un valor por defecto para representar los correos
electrónicos ausentes. Sustituyamos los valores ausentes en la columna 'email'
por el string vacío '' como valor por defecto.

Utiliza el método fillna() para sustituir los valores ausentes en 'email' por
strings vacíos.
Imprime las cinco primeras filas del DataFrame.
"""

df_logs = read_file('visit_log.csv')

df_logs['email'] = df_logs['email'].fillna('')

print(df_logs.head())



"""
Debido a que no podemos conocer las direcciones de correo electrónico de los
visitantes que nunca proporcionaron una, tiene sentido usar el string vacío 
para esos valores ausentes. Pero, ¿qué pasa con los valores de fuente de tráfico
ausentes?
Esas visitas vienen de correos electrónicos, así que vamos a reemplazar
manualmente los valores vacíos en 'source' por 'email'.

Para comenzar:
- Lee los datos usando keep_default_na=False.
- Imprime todos los valores únicos en la columna 'source'.

Esto te permitirá confirmar cuántas entradas aparecen como vacías y deben ser
corregidas.
"""


df_logs = read_file('visit_log.csv',keep_default_na = False) # escribe tu código a continuación

df_sources = df_logs['source'].unique() # escribe tu código a continuación
print(df_sources)



"""
¡Genial! ¡Ahora vamos a arreglar nuestros valores ausentes!

1. Utiliza replace() para reemplazar los valores ausentes en la columna 
   'source' por el string 'email'.
2. Verifica tu trabajo llamando al método unique() en la columna 'source'
   e imprime los resultados.
"""


df_logs = read_file('visit_log.csv', keep_default_na=False)

df_logs['source'] = df_logs['source'].replace('' , 'email') # escribe tu código a continuación

print(df_logs['source'].unique())# escribe tu código a continuación)



"""
Para calcular la tasa de conversión de cada fuente de tráfico, primero determina
cuántas visitas hubo de cada fuente.

Para encontrar el número total de visitas de cada fuente de tráfico, utiliza
groupby() para agrupar los datos por la columna 'source', luego cuenta el número
de valores en la columna 'user_id' del DataFrame agrupado. Asigna el resultado en
la variable visits y luego imprímelo.

El precódigo ya contiene el trabajo que realizaste para rellenar los valores ausentes.
"""


df_logs = read_file('visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count()
print(visits)



"""A continuación, determina el número de visitas en las que se realizó una compra
para cada fuente, calculando la suma de la columna 'purchase' para cada grupo de 
fuente. Posteriormente, asigna los resultados a la variable purchases e imprímelos.
"""


df_logs = read_file('visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

purchases = df_logs.groupby('source')['purchase'].sum()
print(purchases)



"""
Calcula la tasa de conversión para cada fuente de tráfico, guarda los resultados
en conversion, e imprímelos. La tasa de conversión es la proporción de visitas en
las que se realizó una compra, o sea purchases / visits. El precódigo contiene las
visitas y compras de tu trabajo previo.
"""


df_logs = read_file('visit_log.csv', keep_default_na=False)
df_logs['source'] = df_logs['source'].replace('', 'email')

visits = df_logs.groupby('source')['user_id'].count()
purchases = df_logs.groupby('source')['purchase'].sum()

conversion = purchases / visits # divide el número de compras entre el número de visitas
print(conversion)



"""
Recuerda que queremos comparar el tiempo promedio que pasan en el sitio web
las personas que utilizan dispositivos móviles y de escritorio, luego usaremos
esos tiempos promedio para rellenar los valores ausentes.

Para comenzar:
- Filtra el DataFrame original por la columna 'device_type', que indica si la
  visita se realizó desde un dispositivo móvil o de escritorio.
- Crea dos nuevos DataFrames:
        - Uno con solo las visitas desde dispositivos de escritorio ('device_type' 
          == 'desktop') y asígnalo a la variable desktop_data.
        - Otro con las visitas desde dispositivos móviles ('device_type' == 'mobile')
          y asígnalo a la variable mobile_data.

El precódigo ya lee los datos y rellena los valores ausentes de 'age'. Este
también llama a info() por ti después de crear tus DataFrames filtrados para
que puedas revisar cuántos valores ausentes quedan en 'avg_time_on_site' para
cada tipo de dispositivo.
"""


analytics_data = read_file('web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop'] # completa esta línea
mobile_data = analytics_data[analytics_data['device_type'] == 'mobile'] # completa esta línea

desktop_data.info()
print()
mobile_data.info()
print()



"""
Ahora que los datos de escritorio y móviles están separados, calcula el tiempo
medio de visita para cada dispositivo.

Asigna la media del tiempo de visita de los usuarios de escritorio a una variable
llamada desktop_avg y la media de los usuarios móviles a mobile_avg. 

El precódigo ya contiene el código para imprimir tus resultados. Calcula el tiempo
promedio que pasan en el sitio web los usuarios de cada tipo
"""


analytics_data = read_file('web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
mobile_data =  analytics_data[analytics_data['device_type'] == 'mobile']

desktop_avg = desktop_data['time'].mean()# completa esta línea
mobile_avg = mobile_data['time'].mean()# completa esta línea

print(f"Tiempo de escritorio promedio: {desktop_avg:.2f} segundos")
print(f"Tiempo móvil promedio: {mobile_avg:.2f} segundos")



"""
Utiliza el tiempo promedio de visita de escritorio para rellenar los valores ausentes
en la columna 'time' de desktop_data y el tiempo promedio de visita móvil para
rellenarlos en mobile_data.

El precódigo contiene tu trabajo de las tareas anteriores y llama a info() para que
compruebes que los valores ausentes se hayan rellenado.

Es posible que también veas un SettingWithCopyWarning al ejecutar tu código. No hay
nada de que preocuparse en este caso, pero si deseas obtener más información al 
respecto consulta la documentación (materiales en inglés).
"""

pd.options.mode.chained_assignment = None
import warnings
warnings.filterwarnings('ignore')

analytics_data = read_file('web_analytics_data.csv')

age_avg = analytics_data['age'].mean()
analytics_data['age'] = analytics_data['age'].fillna(age_avg)

desktop_data = analytics_data[analytics_data['device_type'] == 'desktop']
mobile_data =  analytics_data[analytics_data['device_type'] == 'mobile']

desktop_avg = desktop_data['time'].mean()
mobile_avg = mobile_data['time'].mean()

desktop_data['time'] = desktop_data['time'].fillna(desktop_avg)
mobile_data['time'] = mobile_data['time'].fillna(mobile_avg)

# esto comprobará si tienes algún valor ausente
desktop_data.info()
print()
mobile_data.info()
print()



"""
En esta actividad definiremos un DataFrame. Tu trabajo consistirá en lo siguiente:

Filtrar las filas de las regiones 'North' y 'South'.
Calcular el ingreso promedio de cada región.
Usar info() para verificar los cambios.
"""


data = {
        'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'region': ['North', 'South', 'North', 'South', 'North', 'South', 'North', 'South', 'North', 'South'],
        'age': [25, 34, 45, None, 38, 50, None, 28, 42, 35],
        'revenue': [120, 80, 130, 95, None, None, 125, 90, None, 110]
}

# Convertir a DataFrame
sales_data = pd.DataFrame(data)

# Aquí es donde escribirás tu código para filtrar y calcular el promedio
north_data = sales_data[sales_data['region'] == 'North']#Escribe tu código
south_data = sales_data[sales_data['region'] == 'South']#Escribe tu código
#print(north_data)

# Imprimir los promedios calculados - Completa el código
print(f"Promedio de ingresos en 'North': {north_data['revenue'].mean()}")
print(f"Promedio de ingresos en 'South': {south_data['revenue'].mean()}")

# Comprobar si hay valores ausentes
north_data.info()
print()
south_data.info()
print()



"""
Seguiremos trabajando en el mismo caso del ejercicio 1. Esta vez, con el mismo
DataFrame, deberás utilizar el promedio de ingresos de la región 'North' para 
rellenar los valores ausentes en esa región, y lo mismo para la región 'South'.
Además, muestra los promedios calculados para cada región.

Es posible que veas un SettingWithCopyWarning al ejecutar tu código. No hay
nada de que preocuparse en este caso, pero si deseas obtener más información
al respecto consulta la documentación (materiales en inglés).
"""


data = {
        'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'region': ['North', 'South', 'North', 'South', 'North', 'South', 'North', 'South', 'North', 'South'],
        'age': [25, 34, 45, None, 38, 50, None, 28, 42, 35],
        'revenue': [120, 80, 130, 95, None, None, 125, 90, None, 110]
}

# Convertir a DataFrame
sales_data = pd.DataFrame(data)

# Filtrar los datos por región
north_data = sales_data[sales_data['region'] == 'North']
south_data = sales_data[sales_data['region'] == 'South']

# Calcular el promedio de ingresos por región
north_avg = north_data['revenue'].mean()
south_avg = south_data['revenue'].mean()

# Imprimir los promedios calculados
print(f"Promedio de ingresos en 'North': {north_avg}")
print(f"Promedio de ingresos en 'South': {south_avg}")

# Rellenar los valores ausentes con el promedio de ingresos por región
north_data['revenue'] = north_data['revenue'].fillna(north_avg) # ESCRIBE TU CODIGO
south_data['revenue'] = south_data['revenue'].fillna(south_avg) # ESCRIBE TU CODIGO

# Comprobar si aún hay valores ausentes
north_data.info()
print()
south_data.info()
print()




"""
Siguiendo con el conjunto de datos phone_stock, haz lo siguiente:

1. Cambia los nombres de los modelos de teléfonos a minúsculas usando el
   método str.lower() y guárdalos en una nueva columna llamada
   'item_lowercase', pero conserva también la columna original 'item'.
2. Imprime las primeras filas de la tabla actualizada y mira el resultado.
"""


df_stock = read_file('phone_stock.csv')

df_stock['item_lowercase'] = df_stock['item'].str.lower()

print(df_stock.head())
print()



"""
Utilizando tu recién creada columna 'item_lowercase' y el método sum(), 
calcula el número total de dos modelos de teléfono:

1) 'apple iphone xr 64gb'

2) 'samsung galaxy a30 32gb'

Para contar el número de teléfonos Apple, filtra el DataFrame a partir 
de la columna 'item_lowercase' para incluir solo las filas con 'apple 
iphone xr 64gb' como valor. A continuación, extrae la columna 'count' 
del DataFrame filtrado y aplícale el método sum(). Almacena la cantidad
total de teléfonos Apple en la variable apple.

Para los teléfonos Samsung, sigue el mismo procedimiento con la única 
diferencia de que guardes el número total de teléfonos Samsung en la 
variable samsung.

El precódigo ya contiene el código para imprimir tus resultados, no lo modifiques.
"""


df_stock = read_file('phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum() # completa esta línea de código
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum() # completa esta línea de código

print("Número total de teléfonos Apple:", apple)
print("Número total de teléfonos Samsung:", samsung)
print()



"""
Ahora elimina las filas con teléfonos duplicados llamando a 
drop_duplicates() en df_stock. Necesitamos eliminar filas únicamente
en función de la columna item_lowercase', así que asegúrate de utilizarla
como valor para el parámetro subset=.

Recuerda que después de eliminar los duplicados, tenemos que llamar al
método reset_index() con el parámetro drop=True. Esto nos permite arreglar
la indexación y eliminar el índice antiguo.

Por cierto, ¡puedes hacer todo esto con una sola línea de código! Puede
ser un poco difícil, pero intenta encontrar la manera de hacerlo.

El resultado final debería asignarse de nuevo a df_stock. Imprime las 
primeras filas del df_stock cuando hayas terminado.
"""


df_stock = read_file('phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop = True) 
print(df_stock.head()) 
print()



"""
¡Vamos a hacer algo realmente interesante! No te preocupes, estás preparado al
100% y nosotros te ayudaremos.

Ya tienes todo listo: el precódigo eliminó los duplicados y creó el DataFrame 
df_stock. También calculó los valores correctos para 'count' y los guardó en 
las variables apple y samsung.

Aquí tienes una vista del DataFrame df_stock después de eliminar duplicados:

        id                     item  count           item_lowercase
0  100480924     Apple iPhone Xr 64gb     10     apple iphone xr 64gb
1  100480959     Xiaomi Redmi 6A 16GB     44     xiaomi redmi 6a 16gb
2  100480975          HUAWEI P30 lite     38          huawei p30 lite
3  100480988  Samsung Galaxy A30 32GB     49  samsung galaxy a30 32gb
4  100481020            Honor 8X 64GB     64            honor 8x 64gb

Para actualizar un valor, puedes usar loc[] indicando el índice y la columna. 
Por ejemplo, para cambiar el valor de 'count' en la primera fila:

df_stock.loc[0, 'count'] = 33
En lugar de escribir el número directamente, usarás la variable apple. Para 
el modelo Samsung, el proceso es igual, pero usando la condición correspondiente
y la variable samsung.

Tu tarea:
Actualiza el valor de la columna 'count' en la fila con índice 0 (modelo Apple)
y en la fila con índice 3 (modelo Samsung), usando loc[] y las variables apple 
y samsung.
Usa loc[] para hacerlo y asigna los valores de las variables apple y samsung.
"""


df_stock = read_file('phone_stock.csv')
df_stock['item_lowercase'] = df_stock['item'].str.lower()

apple = df_stock[df_stock['item_lowercase'] == 'apple iphone xr 64gb']['count'].sum()
samsung = df_stock[df_stock['item_lowercase'] == 'samsung galaxy a30 32gb']['count'].sum()

df_stock = df_stock.drop_duplicates(subset='item_lowercase').reset_index(drop=True)

df_stock.loc[0, 'count'] = apple
df_stock.loc[3, 'count'] = samsung

print(df_stock.head(10))
print()



"""
Steam es la plataforma de juegos para PC más popular del mundo, con una extensa
colección de más de 6000 juegos y una vasta comunidad de millones de jugadores.
Esta diversidad incluye desde grandes éxitos de la industria hasta títulos 
independientes más pequeños, lo que hace que contar con herramientas efectivas 
de descubrimiento sea un recurso extremadamente valioso. El conjunto de datos 
que utilizaremos contiene un registro de los comportamientos de los usuarios en
Steam, incluyendo las siguientes columnas:

- user-id: identificador único del usuario.
- game-title: título del juego.
- behavior-name: nombre del comportamiento (compra o jugar).
- value: valor que indica la frecuencia o cantidad del comportamiento (1 para
  compras, otros valores para horas jugadas).

Objetivo
Vamos identificar y eliminar las filas duplicadas en el dataset. Al final,
verificaremos que se hayan eliminado correctamente.

Tu tarea:
- Elimina las filas duplicadas del DataFrame df y guarda el resultado en la
  variable df_sin_duplicados.
- Reinicia el índice del nuevo DataFrame.
- Por último, asegúrate de que los duplicados han sido eliminados verificando
  que df_sin_duplicados.duplicated().sum() sea igual a 0.
"""


# Cargar los datos (asegúrate de reemplazar 'steam_videogames.csv' por el nombre correcto del archivo)
df = read_file('steam-200k.csv')
df.columns = ['user_id', 'game_title', 'behavior_name', 'value']

# Mostrar DataFrame inicial
print(df.head(5))

# 1. Eliminar filas duplicadas y contar duplicados
print('Número de filas duplicadas (Inicial): ', df.duplicated().sum())
df_sin_duplicados = df.drop_duplicates() # tu código

df_sin_duplicados.reset_index(drop=True, inplace=True)
print('Número de filas duplicadas (Final): ', df_sin_duplicados.duplicated().sum())
print()



"""
Siguiendo con nuestro  DataFrame que contiene la flor y el insecto oficiales
de cuatro estados de EE.UU., utiliza loc[] para retornar la columna 'flower' 
e 'insect' para los estados 1 y 3.
"""


states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

filtered_df = df.loc[['state 1','state 3'] , ['flower','insect']]
print(filtered_df)
print()



"""
Esta vez, utiliza loc[] para obtener solo la columna 'insect' para todos los
estados, excepto Alabama.
"""


states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)

print(df.loc['state 2':,'insect'])
print()



"""
Utiliza loc[] para extraer las flores de Alabama, Alaska y Arizona, y guarda el
resultado en la variable flowers. Luego, muestra esta variable.

El precódigo ya crea el DataFrame por ti y establece la columna 'state' como
índice, así que asegúrate de usar los nombres de los estados como valores del
índice en loc[].
"""


states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
df = df.set_index('state')

flowers = df.loc[['Alabama', 'Alaska', 'Arizona'],'flower']
print(flowers)
print()



"""
Ahora utiliza iloc[] para indexar exactamente la misma parte del DataFrame
que usaste en la última tarea. Igual que hicimos antes, guarda el resultado
en la variable flowers e imprímela.
"""


states  = ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
flowers = ['Camellia', 'Forget-me-not', 'Saguaro cactus blossom', 'Apple blossom']
insects = ['Monarch butterfly', 'Four-spotted skimmer dragonfly', 'Two-tailed swallowtail', 'European honey bee']
index   = ['state 1', 'state 2', 'state 3', 'state 4']

df = pd.DataFrame({'state': states, 'flower': flowers, 'insect': insects}, index=index)
df = df.set_index('state')

flowers = df.iloc[0:3,0]
print(flowers)
print()



"""
Vamos a filtrar para que solo se seleccionen los juegos cuyas ventas en Japón
fueron superiores a un millón de dólares. 
Imprime solo las columnas 'name' y 'jp_sales' del DataFrame.
"""


df = read_file('vg_sales.csv')

print(df.query("jp_sales > 1")[['name', 'jp_sales']])
print()



"""
Filtra las filas del DataFrame donde las columnas 'publisher' y 'developer'
sean iguales con el método query(). Asigna el resultado a la variable
df_filtered y, finalmente, imprime las primeras 5 filas de df_filtered.

Imprime únicamente las columnas especificadas en la lista cols.
"""


df = read_file('vg_sales.csv')

cols = ['name', 'publisher', 'developer']

df_filtered = df.query("publisher == developer")[cols] 
print(df_filtered.head())
print()



"""
Filtra el dataframe df extrayendo solo las filas en las que los valores de la columna
'platform' no estén en la lista handhelds. Para ello deberás usar la palabra clave
not in .

Imprime solo las columnas 'name' y 'platform'.
"""


df = read_file('vg_sales.csv')

handhelds = ['3DS', 'DS', 'GB', 'GBA', 'PSP']
print(df.query("~(platform  in @handhelds)")[['name', 'platform']])# Otra forma de escribir el argumento de query sería "platform not in @handhelds"
print()



"""
Imprime una lista de todos los géneros únicos en el conjunto de datos llamando al
método unique() en la columna 'genre'.

Solamente imprime la columna 'genre'
"""


df = read_file('vg_sales.csv')

print(df['genre'].unique())
print()



"""
A partir del archivo vg_sales.csv, que contiene información sobre ventas de
videojuegos, filtra el conjunto de datos para excluir los juegos cuyos géneros
sean 'Shooter', 'Simulation', 'Sports' o 'Strategy'.

Luego, muestra una tabla que incluya solo las columnas 'name' y 'genre' del 
resto de los juegos.

Tenemos dos variables en el precódigo:
- cols, que contiene las columnas de nuestro interés: 'name' y 'genre'.
- s_genres, que es una lista de géneros que empiezan por la letra "S".

Tu objetivo es utilizar el método isin() con la lista proporcionada s_genres
para filtrar el DataFrame df de forma que solo se mantengan las filas en las
que el género del juego no empiece por la letra "S".

Cuando se filtran, utiliza la variable cols para seleccionar solo las columnas
'name' y 'genre' y asigna el resultado a una variable llamada df_filtered. 
Después muéstralo.
"""


df = read_file('vg_sales.csv')

cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

df_filtered = df[~df['genre'].isin(s_genres)][cols] # se podría escribir df_filtered = df.loc[~df['genre'].isin(s_genres), cols]
print(df_filtered)
print()



"""
Nuevamente, a partir del archivo vg_sales.csv, que contiene datos de
videojuegos, utiliza el método .query() de Pandas para excluir todos
los juegos cuyo género sea 'Shooter', 'Simulation', 'Sports' o 'Strategy'.

Muestra solo las columnas 'name' y 'genre' del resto de los videojuegos.

1. Vuelve a filtrar todos los géneros que no empiezan por "S", pero esta vez
   hazlo con el método query().
2. Para hacerlo, tendrás que utilizar la palabra clave not in en tu string de
   consulta.
3. Utiliza cols para seleccionar solo las columnas 'name' y 'genre' .
4. Asigna el resultado a una variable llamada df_filtered .
5. Imprime los resultados.
"""


df = read_file('vg_sales.csv')

cols = ['name', 'genre']
s_genres = ['Shooter', 'Simulation', 'Sports', 'Strategy']

# Filtra los géneros usando query() y not in
df_filtered = df.query("genre not in @s_genres")[cols]

# Imprime los resultados
print(df_filtered)
print()



"""
Añade una declaración print() en la que puedes llamar a query() en df y
pasarle un string de consulta que compruebe si la columna 'c' está en
our_series.index.
"""


our_series = pd.Series([10, 11, 12], index=['X', 'Y', 'T'])
df = pd.DataFrame(
        {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
        }
)

print(df.query("c in @our_series.index"))
print()



"""
Añade una declaración print() en la que puedes llamar a query() en df y
pasarle un string de consulta que compruebe si la columna 'a' está en 
our_df.b1.
"""


df = pd.DataFrame(
        {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
        }
)
our_df = pd.DataFrame(
        {
        'a1': [2, 4, 6],
        'b1': [3, 2, 2],
        'c1': ['A', 'B', 'C'],
        },
        index=['Z', 'X', 'P']
)

print(df.query("a in @our_df.b1"))
print()



"""
Verifica la presencia de los valores de la columna 'a' entre los valores del
diccionario our_dict (10, 11 y 12), usando el método query.

Puedes realizar la consulta con in, y deberás acceder a los valores del diccionario
usando .values().
"""


our_dict = {0: 10, 3: 11, 12: 12}
df = pd.DataFrame(
        {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
        }
)
print(df)
print()
print(our_dict)
print()
print(df.query("a in @our_dict.values()"))
print()



"""
Vamos a crear un DataFrame externo llamado our_df con valores de índice
establecidos por la lista ['Z', 'X', 'P']. A continuación, podemos comprobar
los valores de la columna 'c' para incluirlos en el índice de our_df.
"""


df = pd.DataFrame(
        {
        'a': [2, 3, 10, 11, 12],
        'b': [5, 4, 3, 2, 1],
        'c': ['X', 'Y', 'Y', 'Y', 'Z'],
        }
)
our_df = pd.DataFrame(
        {
        'a1': [2, 4, 6],
        'b1': [3, 2, 2],
        'c1': ['A', 'B', 'C'],
        },
        index=['Z', 'X', 'P']
)

print(df)
print()
print(our_df)
print()
print(df.query("c in @our_df.index"))
print()



"""
Tienes un DataFrame con información sobre productos en una tienda, incluyendo el
nombre del producto, la categoría y el precio. Quieres filtrar los productos que
pertenecen a una lista de categorías usando query().
"""


# Crear DataFrame de productos
datos = {
        'nombre': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet'],
        'categoría': ['Electrónica', 'Accesorios', 'Accesorios', 'Electrónica', 'Oficina', 'Electrónica'],
        'precio': [1000, 25, 50, 300, 150, 400]
}

productos = pd.DataFrame(datos)
print("Datos de productos:\n", productos)

categorias_deseadas = ['Electrónica', 'Oficina']

productos_filtrados = productos.query("categoría in @categorias_deseadas") # Otra forma podría ser productos[productos['categoría'].isin(categorias_deseadas)]

print("\nProductos filtrados por categoría:\n", productos_filtrados)
print()



"""
Tienes dos DataFrames de Pandas: uno llamado ventas con información de
productos vendidos y otro llamado stock con el inventario de productos.

Tu objetivo es filtrar el DataFrame ventas usando un Series externo para
seleccionar las ventas de productos más vendidos. Guarda el resultado en
ventas_filtradas y muéstralo.

Mantén el precódigo para evitar errores de revisión.
"""


# Crear DataFrame de ventas
datos_ventas = {
        'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet'],
        'ventas': [150, 500, 300, 120, 80, 200]
}
ventas = pd.DataFrame(datos_ventas)

# Crear DataFrame de stock
datos_stock = {
        'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora', 'Tablet', 'Cargador'],
        'stock': [50, 200, 150, 75, 30, 100, 60]
}
stock = pd.DataFrame(datos_stock)

print("Datos de ventas:\n", ventas)
print("\nDatos de stock:\n", stock)

# Series externo con los productos más vendidos
productos_más_vendidos = pd.Series(['Mouse', 'Tablet', 'Teclado'])

# Filtrar el DataFrame de ventas usando el Series externo
ventas_filtradas = ventas.query("producto in @productos_más_vendidos")
print("\nVentas filtradas (productos más vendidos):\n", ventas_filtradas)
print()



"""
Sigamos trabajando el vg_sales dataset. Tu objetivo es filtrar de tal forma la
información que solo te quedes con los juegos que fueron lanzados en la década
de los 80. Asigna el resultado a una variable llamada df_filtered y luego imprime
las primeras 5 filas.
"""


df = read_file('vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

df_filtered = df.query("year_of_release >= 1980 and year_of_release <1990")
print(df_filtered.head(5)) 
print()



"""
Recordemos otro tipo de filtrado que realizamos, en el que solo tomamos
las filas que superaban el millón de dólares en ventas en al menos una 
de las tres regiones. Realiza el mismo filtrado, pero en esta ocasión 
utiliza query(). 

Asigna tu string de consulta a una variable llamada q_string, luego imprime
las primeras 5 filas del resultado de llamar a query() en df con q_string 
como entrada.
"""


df = read_file('vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

q_string = "na_sales > 1 or eu_sales > 1 or jp_sales > 1"
print(df.query(q_string).head(5))
print()




df = read_file('vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

q_string = "na_sales > 1 or eu_sales > 1 or jp_sales > 1"
print(df.query(q_string).head(5)) 
print()



"""
El siguiente dataset, almacenado en la variable developers, contiene una lista de
empresas de desarrollo de videojuegos. 

El objetivo de este ejercicio es poner en practica tus habilidades para construir
una lógica que te permita filtrar información especifica contenida en el dataset,
sujeto a ciertos criterios. 

1. Comenzaremos por crear una lógica que nos permita filtrar todos aquellos
   videojuegos que se vendan en las siguientes regiones:
     a. América del Norte
     b. Europa
     c. Japón
     Notemos que, no hay ninguna columna que nos indique explícitamente si un 
     juego se vendió en las regiones antes mencionadas. Sin embargo, se puede
     inferir que un juego se vendió en una región si sus ventas son mayores a
     cero, para esa región.
2. Para realizar el filtrado, deberás crear un string de consulta y asignarlo
   a la variable q_string.
3. A continuación, utiliza esta variable para realizar el filtrado.
4. Adicionalmente, utiliza la variable cols para seleccionar solo las columnas
   'name', 'developer', 'na_sales', 'eu_sales' y 'jp_sales' del DataFrame
   filtrado.
5. Por ultimo, asigna el resultado a la variable df_filtered.

Muestra el DataFrame completo.
"""


df = read_file('vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# Selecciono las columnas solicitadas
cols = ['name', 'developer', 'na_sales', 'eu_sales', 'jp_sales']# Lista de columnas a seleccionar 

# Filtro por valores mayores a cero
q_string = "na_sales > 0 and eu_sales > 0 and jp_sales > 0"

# Filtro por las columnas y asigno el resultado a df_filtered
df_filtered = df.query(q_string)[cols]


# Imprimo el data frame completo
print(df_filtered)
print()



"""
Siguiendo con nuestro ejemplo anterior, vamos a complejizar el filtrado que
desarrollamos en el ejercicio anterior. La condición anterior exigía que los
juegos hubiesen tenido ventas en las tres regiones. En esta ocasión, incluiremos que:

- Las ventas en Japón sean mayores que las ventas combinadas de Norteamérica y Europa.
- Las empresas de desarrollo del juego deben estar contenidas en la lista developers.

Modifica el string de consulta, almacenado en la variable q_string, incorporando los
cambios mencionados. Luego, utilízala para realizar el filtrado. 

Muestra el resultado en pantalla.
"""


df = read_file('vg_sales.csv')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

developers = ['SquareSoft', 'Enix Corporation', 'Square Enix']
cols = ['name', 'developer', 'na_sales', 'eu_sales', 'jp_sales']


# Incopora los cambios necesario para reflejar las nuevas restricciones
q_string = "na_sales > 0 and eu_sales > 0 and jp_sales > 0 and jp_sales > (na_sales + eu_sales) and developer in @developers" 

df_filtered = df.query(q_string)[cols]
print(df_filtered ) 
print()



"""
Algunos géneros del dataset no están bien representados. Queremos combinar los
géneros menos representados en la categoría miscelánea, sustituyendo sus
valores por 'Misc'.

Para empezar, cuenta cuántas veces aparece cada valor de la columna 'genre'
llamando al método value_counts() e imprimiendo los resultados en orden ascendente.
"""


df = read_file('vg_sales.csv')

print(df['genre'].value_counts(ascending=True))
print()



"""
Crea una variable llamada genres que contenga una lista de las dos categorías
menos representadas del último ejercicio: 'Puzzle' y 'Strategy'. A continuación,
utiliza where() para modificar la columna 'genre' de df para que los valores de
la lista genres se sustituyan por 'Misc'. El precódigo contiene tu código del
último ejercicio que permite imprimir los valores únicos y comprobar el resultado.
"""


df = read_file('vg_sales.csv')

genres = ['Puzzle' , 'Strategy'] 
df['genre'] = df['genre'].where(~df['genre'].isin(genres), 'Misc')

print(df['genre'].value_counts(ascending=True))
print()



"""
La gestión del menú de un restaurante es clave para su éxito. El objetivo es
categorizar los platillos menos representados en la categoría de "Otros", 
sustituyendo sus nombres por 'Otros'. Vamos a hacerlo en el próximo ejercicio.

Para empezar, cuenta cuántas veces aparece cada valor de la columna 'platillo'
llamando al método value_counts() e imprimiendo los resultados en orden ascendente.
"""


df = read_file('menu_items.csv')

print(df['platillo'].value_counts(ascending=True))
print()



"""
Crea una variable llamada platillos que contenga una lista de las dos categorías
menos representadas del último ejercicio. A continuación, utiliza where() para
modificar la columna 'platillo' de df para que los valores de la lista platillos
se sustituyan por 'Otros'. El precódigo contiene tu código del último ejercicio
que permite imprimir los valores únicos y comprobar el resultado.
"""


df = read_file('menu_items.csv')

platillos = ['Ensalada' , 'Postre']
df['platillo'] = df['platillo'].where(~df['platillo'].isin(platillos), 'Otros')

print(df['platillo'].value_counts(ascending=True))
print()
