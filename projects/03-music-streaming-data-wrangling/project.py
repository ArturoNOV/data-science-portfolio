# function created to read csv and excel files for each exercise.
def read_file(file, **kwargs):
    from pathlib import Path
    import pandas as pd

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
Como analista de datos, tu trabajo consiste en analizar datos para extraer
información valiosa y tomar decisiones basadas en ellos. Esto implica
diferentes etapas, como la descripción general de los datos y el preprocesamiento.

Descripción del proyecto
En este proyecto, trabajarás con datos reales de transmisión de música online
para explorar y procesar información sobre los hábitos de escucha de los usuarios
y las usuarias en dos ciudades: Springfield y Shelbyville.

1. Etapa 1. Descripción de los datos 
Abre los datos y examínalos.

Etapa 1.1. Necesitarás pandas, así que impórtalo.
"""
import pandas as pd


"""
Etapa 1.2. Lee el archivo music_project_en.csv de la carpeta C:/GITHUB/TripleTen/Proyectos/Sprint3
y guárdalo en la variable df:
"""
# df = pd.read_csv('/datasets/music_project_en.csv') se reemplaza con la siguiente linea debido a mi estructura de archivos
df = read_file('music_project_en.csv')

"""
Etapa 1.3. Muestra las 10 primeras filas de la tabla:
"""
print(df.head(10))


"""
Etapa 1.4. Obtén la información general sobre la tabla con el método info()
"""
print(df.info())


"""
Estas son nuestras observaciones sobre la tabla. Contiene siete columnas que
almacenan los mismos tipos de datos:
object .

Según la documentación:

' userID' : identificador del usuario;
'Track' : titulo de la canción;
'artist' : nombre del artista;
· 'genre' : género de la canción;
. 'City' : ciudad del usuario;
'time' : la hora exacta en la que se reprodujo la canción;
. 'Day' : dia de la semana.

Podemos ver dos problemas con el estilo en los encabezados de la tabla:

1. Algunos encabezados están en mayúsculas, otros en minúsculas.
2. Identifica tu mismo el segundo problema y escríbelo aquí.
    -Algunos nombres de columnas tienen espacios innecesarios al inicio o al final.
    -Hay inconsistencia de estilo: userID, Track, City, Day, artist, genre, time.
    Lo ideal sería usar un formato uniforme, por ejemplo todo en minúsculas y
    sin espacios.


1.1. Escribe algunas observaciones por tu parte. Contesta a las siguientes preguntas: 
1.   ¿Qué tipo de datos hay en las filas? ¿Cómo podemos saber qué almacenan las columnas?
        -Cada fila representa una reproducción de una canción por un usuario. Las columnas
        almacenan información sobre el usuario, la canción, el artista, el género, la ciudad,
        la hora y el día de reproducción. Podemos saber qué almacena cada columna revisando
        la información devuelta por info(), en este caso vemos que todas las columnas son 
        tipo 'object'.
2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos
    más información?
        -Sí parece haber suficientes datos para analizar patrones de reproducción por ciudad,
        día, hora, artista o género. Sin embargo, seguramente, es necesario limpiar los datos
        y revisar los valores ausentes.
3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos
    incorrectos?
        -Sí. Hay valores ausentes en las columnas Track, artist y genre. También hay problemas
        en los nombres de las columnas: algunas tienen mayúsculas, otras minúsculas y algunas
        parecen tener espacios innecesarios. Por ahora no sabemos si hay duplicados; habría 
        que comprobarlo con df.duplicated().sum().
"""

"""
Etapa 2. Preprocesamiento de los datos 
Tu objetivo aquí es preparar los datos para analizarlos. El primer paso es resolver los problemas
con los encabezados. Después podemos avanzar a los valores ausentes y duplicados. ¡Empecemos!

Vamos a corregir el formato en los encabezados de la tabla.

2.1. Estilo del encabezado 
Etapa 2.1. Muestra los encabezados de la tabla (los nombres de las columnas):
"""
print(df.columns)

"""
Vamos cambiar los encabezados de la tabla siguiendo las reglas estilísticas convencionales:

- Todos los caracteres deben ser minúsculas.
- Elimina los espacios.
- Si el nombre tiene varias palabras, utiliza snake_case, es decir, añade un guion bajo ( _ ) 
  entre las palabras en lugar de un espacio.

Etapa 2.2. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos
los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:
"""
col_names_lower = []

for old_name in df.columns:
    name_lower = old_name.lower()
    col_names_lower.append(name_lower)

df.columns = col_names_lower

print(df.columns)


"""
Etapa 2.3. Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los
nombres de las columnas y muestra los nombres de las columnas de nuevo:
"""
col_names_stripped = []

for old_name in df.columns:
    name_stripped = old_name.strip()
    col_names_stripped.append(name_stripped)

df.columns = col_names_stripped

print(df.columns)


"""
Etapa 2.4. Necesitamos aplicar la regla de snake_case en la columna userid. Debe ser user_id.
Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.
"""
df.rename(columns={'userid': 'user_id'}, inplace=True)

print(df.columns)


"""
2.2 Valores Ausentes

Etapa 2.5. Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos
para obteren el número de valores ausentes.
"""
print(df.isna().sum())
print(df.isnull().sum())


"""
Etapa 2.6. Sustituye los valores ausentes en las columnas 'track', 'artist' y 'genre' con el string 'unknown'.

1. Crea una lista llamada columns_to_replace que contenga los nombres de las columnas 'track', 'artist' y 'genre'.
2. Usa un bucle for para iterar sobre cada columna en columns_to_replace.
3. Dentro del bucle, sustituye los valores ausentes en cada columna con el string 'unknown'.
"""
columns_to_replace = ['track', 'artist', 'genre']

for column in columns_to_replace:
    df[column] = df[column].fillna('unknown')


"""
Etapa 2.7. Ahora comprueba el resultado para asegurarte de que no falten valores ausentes por reemplazar
en el conjunto de datos. Para ello, cuenta los valores ausentes una vez más.
"""
print(df.isna().sum())

"""
2.3. Duplicados 
Etapa 2.8. Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos
para obtener la cantidad de duplicados explícitos.
"""
print(df.duplicated().sum())
print(len(df[df.duplicated()]))


"""
Etapa 2.9. Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.
"""
df = df.drop_duplicates().reset_index(drop=True)


"""
Etapa 2.10. Comprobemos ahora si conseguimos eliminar todos los duplicados. Cuenta los duplicados 
explícitos una vez más para asegurarte de haberlos eliminado todos:
"""
print(df.duplicated().sum())


"""
Ahora queremos deshacernos de los duplicados implícitos en la columna genre. Por ejemplo, el nombre de un
género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

Etapa 2.11. Primero debemos mostrar una lista de nombres de géneros únicos, por orden alfabético. Para ello:

1. Extrae la columna genre del DataFrame.
2. Llama al método que devolverá todos los valores únicos en la columna extraída.
"""
print(df['genre'].sort_values().unique())


"""
Etapa 2.12. Vamos a examinar la lista para identificar duplicados implícitos del género hiphop, es decir,
nombres mal escritos o variantes que hacen referencia al mismo género musical.

Los duplicados que encontrarás son:
- hip
- hop
- hip-hop

Para solucionarlo, vamos a crear una función llamada replace_wrong_values().

1. Define una función llamada replace_wrong_values() que reciba los siguientes parámetros:
- df: el DataFrame a modificar
- column: el nombre de la columna a trabajar
- wrong_values: una lista con los valores incorrectos
- correct_value: el valor correcto para reemplazar
- Dentro de la función, usa un bucle for para iterar sobre cada valor incorrecto y aplicar .replace().
"""
def replace_wrong_values(df, column, wrong_values, correct_value):
    for wrong_value in wrong_values:
        df[column] = df[column].replace(wrong_value, correct_value)
    return df


"""
Etapa 2.13. Ahora, llama a la función pasando:
- df como el DataFrame
- 'genre' como nombre de columna
- ['hip', 'hop', 'hip-hop'] como lista de valores incorrectos
- 'hiphop' como valor correcto
"""
replace_wrong_values(df, 'genre', ['hip', 'hop', 'hip-hop'], 'hiphop')


"""
Etapa 2.14. Asegúrate de que los nombres duplicados se hayan eliminado. Muestra la lista de valores
únicos de la columna 'genre' una vez más:
"""
print(df['genre'].sort_values().unique())


"""
3. Etapa 3. Análisis

3.1. Tarea: Comparar el comportamiento de los usuarios en las dos ciudades 

Queremos analizar si hay diferencias en la cantidad de canciones reproducidas en Springfield y
Shelbyville. Para ello, usaremos los datos de dos días de la semana: lunes y viernes.

Compararemos cuántas canciones se escucharon en cada ciudad durante esos días para identificar
posibles patrones de comportamiento.

Sigue estos tres pasos para organizar tu análisis:
- Dividir: agrupa los datos por ciudad.
- Aplicar: cuenta cuántas canciones se reproducen en cada grupo.
- Combinar: presenta los resultados de forma que se puedan comparar fácilmente ambas ciudades.

Repite este proceso por separado para cada uno de los dos días.

Etapa 3.1. Cuenta cuántas canciones se reprodujeron en cada ciudad utilizando la columna 'track' como referencia.
"""
print(df.groupby('city')['track'].count())
print(df[df['day'] == 'Monday'].groupby('city')['track'].count())
print(df[df['day'] == 'Friday'].groupby('city')['track'].count())

"""
Etapa 3.3. Agrupa los datos por día de la semana y cuenta cuántas canciones se reprodujeron los lunes y viernes.
"""
print(df[df['day'].isin(['Monday', 'Friday'])].groupby('day')['track'].count())
print(df[df['day'].isin(['Monday', 'Friday'])]['track'].count())


"""
Etapa 3.5

Ahora vamos a combinar dos criterios: día y ciudad.

Crea una función llamada number_tracks() que reciba dos parámetros:
- day: un día de la semana (por ejemplo, 'Monday')
- city: el nombre de una ciudad (por ejemplo, 'Springfield')

Dentro de la función:
1. Filtra el DataFrame por el día.
2. Luego, filtra por la ciudad.
3. Cuenta cuántas veces aparece 'user_id' en ese filtro.
4. Devuelve ese número como resultado.
"""
def number_tracks(day, city):
    df_by_day = df[df['day'] == day]
    df_by_city = df_by_day[df_by_day['city'] == city]
    track_count = df_by_city['user_id'].count()
    return track_count


"""
Etapa 3.6. Llama a number_tracks() cuatro veces: una por ciudad en cada uno de los dos días.
"""
# El número de canciones reproducidas en Springfield el lunes
print(number_tracks('Monday', 'Springfield'))
# El número de canciones reproducidas en Shelbyville el lunes
print(number_tracks('Monday', 'Shelbyville'))
# El número de canciones reproducidas en Springfield el viernes
print(number_tracks('Friday', 'Springfield'))
# El número de canciones reproducidas en Shelbyville el viernes
print(number_tracks('Friday', 'Shelbyville'))

