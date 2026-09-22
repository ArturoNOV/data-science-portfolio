from pathlib import Path
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

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
Realiza la operación de conversión utilizando el método astype(). 

Convierte la columna StockCode de Object a int.
Verifica los resultados llamando el método info() en el DataFrame.
"""

data = {
    'StockCode': ['10001', '10002', '10003', '10004', '10005', '10006'],
    'Description': ['Mug', 'T-shirt', 'Notebook', 'Invalid Code', 'Float code', 'Pen'],
    'Quantity': [10, 5, 8, 1, 3, 6],
    'UnitPrice': [2.5, 15.0, 4.2, 1.0, 6.75, 1.5]
}

df = pd.DataFrame(data) #Convierte la lista en DataFreame

#1. Convierte 'StockCode' a tipo de dato entero 'int'
df['StockCode'] = df['StockCode'].astype('int')

#2. Valida el cambio ejecutando el metodo info() sobre el dataframe
df.info()

print()


"""
Ahora, utiliza  la funcion to_numeric() para los datos de la columna 'UnitPrice' 

1. Convierte la columna 'UnitPrice' de object a float
 a. Usa la función to_numeric().
 b. Usa el parámetro errors= que remplaza valores inválidos con NaN.
2. Verifica los resultados llamando al método info() en el DataFrame.
"""

df = read_file('OnlineRetail.csv', encoding='latin1')

#1. Convierte la columna `'UnitPrice'` de `object` a `float`
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors = 'coerce')

#2. Verifica los resultados llamando al método `info()` en el DataFrame.
df.info()

print()

"""
Ahora, probemos con los datos de la columna 'Quantity' 

1. En el primer paso usa numpy para comprobar si no hay problema con convertir
   la columna 'Quantity' de float a int sin modificar los valores. Muestra la
   expresión que evalúa si es True o False.
"""

df = read_file('OnlineRetail.csv', encoding='latin1')

resultado = np.array_equal(df['Quantity'], df['Quantity'].astype('float'))

print(resultado)

print()


"""
Ahora realiza la operación de conversión utilizando el método astype().
Convierte la columna 'Quantity' de float a int, después verifica los resultados
llamando el método info() en el DataFrame.
"""

df = read_file('OnlineRetail.csv', encoding='latin1')

#convierte los valores de la columna a enteros
df['Quantity'] = df['Quantity'].astype('int')

#Valida el resultado con el metodod info() 
df.info()

print()


"""
Una clienta reporta que su pedido no llegó y asegura haberlo hecho “el 13 de mayo
de 2013 a mediodía”.

Buscas en el sistema un registro con esa fecha exacta. El campo 'InvoiceDate'
de la tabla llega como texto:

'5/13/13 12:04:00'
Sabes que está en formato estadounidense, así que usas to_datetime() para
convertirlo.
"""

string_date = '5/13/13 12:04:00'
fecha = pd.to_datetime(string_date, format='%m/%d/%y %H:%M:%S')
print(fecha)

print()


"""
Trabajas con el equipo de ventas globales y estás revisando registros de una
sucursal en Europa del Este.
Recibes este string como fecha de una operación financiera:

'20-12-2002Z04:31:00'
Necesitas convertirlo a datetime para agregarlo al informe.

Escribe el string de formato adecuado que coincida con la estructura de esta fecha.
"""

raw_date = '20-12-2002Z04:31:00'
clean_date = pd.to_datetime(raw_date, format='%d-%m-%YZ%H:%M:%S')
print(clean_date)

print()


"""
Tu equipo trabaja para SkyFlow, una empresa que desarrolla sistemas inteligentes
para ascensores en edificios corporativos. Recientemente, un cliente se ha quejado
de que su ascensor hace demasiadas paradas innecesarias y no responde
eficientemente en horas pico.

El equipo técnico ha recolectado datos durante los últimos tres meses. El archivo
se llama position.csv y contiene un registro cada vez que el ascensor cambia de piso.
Tu misión es ayudar a preparar los datos para que el equipo de análisis pueda
identificar patrones de uso y momentos críticos de congestión.

Ruta de archivo: /datasets/position.csv

Ejercicio 1: Cargando y explorando los datos
Abre el archivo position.csv, que contiene los movimientos del ascensor. Guarda los
datos en una variable llamada position y muestra las primeras 15 filas para entender
la estructura general del dataset.
"""

position = read_file('position.csv')

print(position.head(15))

print()


"""
Ejercicio 2: Revisando los tipos de datos
El equipo de analítica necesita trabajar con los datos de tiempo, pero antes
debemos verificar si pandas los reconoce como fechas o como strings. Usa el
método .info() para revisar los tipos de datos del dataframe position
"""

position = read_file('position.csv')

position.info()

print()


"""
Ejercicio 3: Transformando el tiempo
Para poder responder preguntas como "¿A qué hora hay más tráfico en el elevador?"
o "¿Cuánto tarda entre pisos?", necesitamos convertir los valores de 'timestamp' a
un tipo de datos datetime.

Usa pd.to_datetime() para hacer la conversión, y luego revisa las primeras filas de
nuevo:

Procesa los datos de hora en la columna 'timestamp' convirtiéndolos de string a
datetime. Después, muestra las primeras filas en la tabla position usando el
método head(). 

Aquí tienes un ejemplo de formato fecha que puedes usar como una plantilla: 2019-02-04T13:22:34.
"""

position = read_file('position.csv')

position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')
print(position.head())

print()


"""
El equipo de ventas quiere analizar qué días del mes tienen más movimiento para
lanzar promociones estratégicas. Pero primero, necesitan extraer esa información
del dataset.

🔧 Tu tarea:

1. Extrae el día del mes y guárdalo en una nueva columna 'Day'.
2. Muestra las primeras 10 filas de las columnas 'InvoiceDate' y 'Day'.
"""

# 1. Leer datos
df = read_file('OnlineRetail.csv', encoding='latin1')

# 2. Convertir columna a datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')# %Y-%m-%dT%H:%M:%SZ')

# 3. Extraer el día del mes
df['Day'] = df['InvoiceDate'].dt.day

# 4. Verifica el resultado
print(df[['InvoiceDate', 'Day']].head(10))

print()


"""
Análisis mensual de operaciones para Skyflow

Contexto

El equipo de operaciones quiere entender cómo ha evolucionado la actividad de los
elevadores mes a mes. Para empezar, necesitas extraer el mes de cada registro en
la columna 'timestamp', que representa cuándo ocurrió un evento del sistema
(por ejemplo, un ascensor detenido o en movimiento).

Tu objetivo

Extrae el mes de cada marca de tiempo y guarda el resultado en la variable
dt_months. Luego muestra las primeras cinco filas con head().
"""

position = read_file('position.csv')

position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

dt_months = position['timestamp'].dt.month
print(dt_months.head(5))

print()


"""
Asignar zona horaria local a los registros.

Contexto

Tu equipo ha confirmado que todas las marcas de tiempo fueron registradas desde
sensores ubicados en Toronto, pero actualmente no tienen zona horaria asignada.
Esto podría causar errores en el análisis temporal, especialmente cuando se
comparan registros con datos de otras ciudades.

Tu objetivo

Localiza correctamente las marcas de tiempo asignándoles la zona horaria
'America/Toronto', y guarda el resultado en una nueva variable llamada
dt_toronto. Muestra las primeras cinco filas.
"""


position = read_file('position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

dt_toronto = position['timestamp'].dt.tz_localize('America/Toronto')

print(dt_toronto.head(5))

print()


"""
Te han encargado comprobar cuál es el juego más vendido (en promedio) en todos los mercados.

Necesitas:

Tomar el promedio de las columnas 'jp_sales', 'na_sales' y 'eu_sales' y guardarlo en una nueva
columna llamada 'average_sales'.
Ordenar los valores del DataFrame por average_sales en orden descendente. Utiliza el método
sort_values, pasando los argumentos correctos a los parámetros by= y ascending=.

Después muestra los primeros cinco valores del dataframe con la nueva columna.
"""

df = read_file('vg_sales.csv')

df['average_sales'] = df[['jp_sales', 'na_sales', 'eu_sales']].mean(axis=1)

df = df.sort_values(by='average_sales', ascending=False)

print(df.head(5))

print()


"""
1. Comienza por escribir una función llamada score_group() que organice los juegos por categorías
de acuerdo con las puntuaciones de las críticas. Categoriza las puntuaciones con base en estas
características:

- Devuelve 'low' (bajo) si el valor de score es menor a 60.
- Devuelve 'medium' (medio) si el valor de score está entre 60 y 79 inclusive.
- Devuelve 'high' (alto) si el valor de score es 80 o mayor.
- Devuelve 'no score' (sin puntuación) en cualquier otro caso (por ejemplo, si score no
  contiene un valor numérico válido o está ausente).

La función score_group() debe tener un input numérico llamado score. La salida debe ser una
cadena que designe la categoría de la puntuación.

Asegúrate de que tu función produzca el output correcto cuando se le pasen los valores 10, 65,
99 y np.nan. Escribimos una declaración print() distinta para llamar a cada función.

2. Agrega una columna 'score_categorized' a la tabla df aplicando la función score_group() a
la columna 'critic_score', con el método apply(). Imprime las primeras 5 filas para asegurarte
de que se creó la nueva columna correctamente.

3. Ahora calcula el total de ventas de Norteamérica para cada categoría de critic score
(puntuación de crítica).

Para hacerlo, es necesario:
- Agrupar por la nueva columna 'score_categorized' utilizando el método groupby().
- Calcular la suma de la columna 'na_sales' del DataFrame agrupado utilizando sum().
- Mostrar el resultado.
"""

df = read_file('vg_sales.csv')

def score_group(score):
    """
    La funcion devielve el grupo de acuerdo con las puntuaciones de las críticas.

    - 'low' (bajo) si es menor a 60.
    - 'medium' (medio) si entre 60 y 79 inclusive.
    - 'high' (alto) si es 80 o mayor.
    - 'no score' (sin puntuación) en cualquier otro caso.
    """
    if score < 60:
        return 'low'
    elif score <= 79:
        return 'medium'
    elif score >= 80:
        return 'high'
    else:
        return 'no score'

print(score_group(10))
print(score_group(65))
print(score_group(99))
print(score_group(np.nan))

df['score_categorized'] = df['critic_score'].apply(score_group)
print(df.head())

df_grouped = df.groupby('score_categorized')
df_sum = df_grouped['na_sales'].sum()

print(df_sum)

print()


"""
Escribe una función que se llame avg_score_group() (grupo puntuación promedio) que tenga un parámetro
llamado row. El parámetro row debe ser un objeto tipo Series de pandas. La función debe calcular la
calificación promedio de cada juego, luego devolver una cadena que coloque cada uno en una de estas
categorías:
- valor 'low' para promedios menores de 60.
- valor 'medium' para promedios de 60 a 79.
- valor 'high' (alto) para puntuaciones mayores a 80.

Para calcular la puntuación promedio, avg_score_group() debe tomar los valores de row con los nombres
de columna 'critic_score' y 'user_score'. La fórmula para calcularlo es avg_score = (critic_score +
user_score * 10) / 2.

Te dejamos las pruebas hechas, se debe imprimir low, medium y high, en ese orden.

2. Ahora es momento de poner a prueba tu nueva función. Crea tres filas personalizadas con estos
nombres de variables y valores:
- row_1: puntuación de la crítica de 66 y puntuación de los usuarios de 3.6.
- row_2: puntuación de la crítica de 72 y puntuación de los usuarios de 8.1.
- row_3: puntuación de la crítica de 99 y puntuación de los usuarios de 9.4.

Cada una de las variables de fila debe ser un objeto tipo Series con valores de índice 'critic_score'
y 'user_score' para que avg_score_group() pueda extraer los valores correctos.
"""

df = read_file('vg_sales.csv')
df.dropna(inplace=True)

def avg_score_group(row):
    """
    La función devuelve una categoría de juegos según la
    calificación promedio de cada juego según las reglar:
    —'low'   para promedios <60
    —'medium'  para promedios de 60 a 79
    —'high'  para promedios mayores a 80
    """
    critic_score = row['critic_score']
    user_score = row['user_score']
    avg_score = (critic_score + user_score * 10) / 2
    if avg_score < 60:
        return 'low'
    elif avg_score < 79:
        return 'medium'
    else:
        return 'high'


# parte de prueba a continuación.
col_names = ['critic_score', 'user_score']
test_low  = pd.Series([10, 1.0], index=col_names)
test_med  = pd.Series([65, 6.5], index=col_names)
test_high = pd.Series([99, 9.9], index=col_names)

rows = [test_low, test_med, test_high]

for row in rows:
    print(avg_score_group(row))

# crea las filas de input de prueba aquí
cols = ['critic_score', 'user_score']
row_1 = pd.Series([66, 3.6], index=cols)
row_2 = pd.Series([72, 8.1], index=cols)
row_3 = pd.Series([99, 9.4], index=cols)
    
# imprime los resultados de llamar a la función con los input de prueba en orden
print(avg_score_group(row_1))
print(avg_score_group(row_2))
print(avg_score_group(row_3))

print()


"""
¡Es hora de que analicemos en detalle las ventas de videojuegos de cada género!

El precódigo crea una columna 'total_sales' como ya has hecho antes. Utilizarás estas columnas,
así que apunta sus nombres.

A continuación, el precódigo agrupa el DataFrame df por la columna 'genre' y asigna el objeto
agrupado resultante a la variable grp.

Y ahora vas a hacer lo siguiente:
- Crear un diccionario para calcular los resultados por cada género:
    - Suma del total de ventas.
    - Ventas promedio NA (Norteamérica).
    - Ventas promedio EU (Europa).
    -Ventas promedio JP (Japón).
- Asignar el diccionario a una variable llamada agg_dict con las tuplas descritas anteriormente.
- Asignar el resultado de agg() a una variable llamada genre.
- Imprimir genre.
"""

df = read_file('vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

grp = df.groupby('genre')

agg_dict = {'total_sales' : 'sum', 'na_sales' : 'mean', 'eu_sales' : 'mean', 'jp_sales' : 'mean'}

genre = grp.agg(agg_dict)

# muestra los resultados
print(genre)

print()


"""
Hemos filtrado el conjunto de datos de videojuegos para que solo contenga juegos que se lanzaron 
n el 2000 o después. Crea una tabla dinámica a partir del conjunto de datos filtrados que contenga
el valor promedio para las ventas en Japón para cada combinación de género y año de lanzamiento.

- Los géneros servirán de índice.
- Las columnas de la tabla dinámica serán los años de lanzamiento.
- Utiliza la columna correspondiente como valores a ser agregados.
- Utiliza la función de agregación apropiada.

Asigna el resultado a una variable llamada df_pivot y luego muéstralo.
"""

df = read_file('vg_sales.csv')
df = df[df['year_of_release'] >= 2000]

df_pivot = df.pivot_table(index='genre',
                        columns='year_of_release',
                        values='jp_sales',
                        aggfunc='mean')

print(df_pivot)

print()


"""
1. eímos los datos, creamos una columna 'total_sales' y calculamos las ventas totales para cada
plataforma en la variable total_sales.

Tienes que calcular el número total de distribuidoras que crearon un juego en cada plataforma,
utilizando nunique(). Asigna el resultado a una variable llamada num_pubs y luego muéstralo.
"""

df = read_file('vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()

num_pubs = df.groupby('platform')['publisher'].nunique()

print(num_pubs)

print()


"""
2. Combina total_sales y num_pubs por columnas en un DataFrame llamado platforms usando concat().
Cambia los nombres de las columnas en platforms a 'total_sales' y 'num_publishers', respectivamente,
luego imprime platforms.
"""

df = read_file('vg_sales.csv')
df['total_sales'] = df['na_sales'] + df['eu_sales'] + df['jp_sales']

total_sales = df.groupby('platform')['total_sales'].sum()
num_pubs = df.groupby('platform')['publisher'].nunique()

platforms = pd.concat([total_sales, num_pubs], axis=1)

# cambia los nombres de las columnas
platforms.columns = ['total_sales', 'num_publishers']

# muestra tu resultado
print(platforms)

print()


"""
1. Tenemos dos DataFrames, df_orders y df_members, los cuales ya se han incluido en el precódigo.

df_orders:
Cada fila representa un único pedido.
Contiene una columna llamada 'user_id' que indica qué cliente realizó el pedido.
Contiene una columna 'id' que identifica cada uno de los pedidos.
df_members:
Cada fila representa un único cliente.
Contiene una columna 'id' que identifica cada uno de los clientes.
Tu tarea:

Fusionar estos dos DataFrames para que en el DataFrame resultante incluyas solo a aquellos clientes
que hayan realizado un pedido. Sigue estos pasos:

1. Tipo de fusión:
    - Elige una fusión que conserve solo a los clientes con pedidos coincidentes (por ejemplo, una
      fusión interna).
2. Detalles de la fusión:
    - Utiliza df_members como el DataFrame izquierdo y haz coincidir el id del cliente.
    - Utiliza df_orders como el DataFrame derecho y haz coincidir la columna 'user_id' (no la id
      del pedido).
3. Sufijos de columna:
    - Aplica sufijos a los nombres de las columnas solapadas: pon '_member' a las columnas de df_members
      y '_order' a las columnas de df_orders.
4. Almacenar y mostrar:
    - Asigna el DataFrame fusionado a la variable llamada df_merged.
    - Muestra en pantalla df_merged para revisar los resultados.
5. Nota:
    - No elimines ninguna columna durante la fusión.
"""

df_members = read_file('new_members.csv')
df_orders = read_file('recent_orders.csv')

df_merged = df_members.merge(df_orders,
                            left_on='id',
                            right_on='user_id',
                            suffixes=('_member', '_order')
                            )

print(df_merged)

print()


"""
Vamos a arreglarlo un poco.
- Elimina la columna duplicada (en este caso, 'user_id').
- Asigna el resultado de vuelta al DataFrame 'df_merged'.
- Muestra el DataFrame fusionado.
"""

df_members = read_file('new_members.csv')
df_orders = read_file('recent_orders.csv')

df_merged = df_members.merge(df_orders,
                            left_on='id',
                            right_on='user_id',
                            suffixes=('_member', '_order'))

df_merged = df_merged.drop('user_id', axis='columns')
print(df_merged)

print()


"""
Hemos importado pandas y las librerías pyplot de Matplotlib en el precódigo proporcionado, y creamos
un DataFrame llamado df. 

Tu tarea es crear un gráfico con forma de estrellas rosas utilizando los datos en df. Para tu
comodidad, todos los atributos necesarios se enumeran a continuación. Sigue las instrucciones para
lograr el resultado deseado. Si lo necesitas, consulta la sección de repaso para recordar los nombres
de los parámetros.

Usando el método plot() de pandas, crea un trazo de columna 'a' frente a la columna 'c' del df que
tenga los siguientes argumentos:

1. El título "A vs C" (el uso de mayúsculas y minúsculas es importante, así que puedes copiarlo
y pegarlo).
2. Un estilo de marcador de estrella (puedes usar un asterisco '*' para lograrlo).
3. Marcadores de color rosa fuerte (utiliza el nuevo y obvio parámetro color= para hacerlo, con el
argumento 'hotpink')
4. Tamaño de la gráfica de 5 por 5 pulgadas.
5. Rango del eje X de 0 a 12.
6. Rango del eje Y de 1 a 6.
7. Eje X con la leyenda "C".
8. Eje Y con la leyenda "A".
"""

df = pd.DataFrame({'a':[2, 3, 4, 5], 'b':[4, 9, 16, 25], 'c':[1, 3, 6, 10]})

df.plot(x='c',
        y='a',
        title='A vs C',
        style='*',
        color='hotpink',
        figsize=[5,5],
        xlim=[0,12],
        ylim=[1,6],
        xlabel="C",
        ylabel="A")
        

plt.show()

print()


"""
Para hacer el análisis más interesante y fácil de entender, usaremos el mismo conjunto de datos de antes,
pero esta vez analizaremos height frente a age en lugar de weight. Vas a crear un gráfico de dispersión
que muestre la relación entre estas dos variables.

Los datos de altura y peso del adulto se han leído en la variable df para ti en el precódigo. Utiliza el
argumento kind='scatter' para crear el gráfico de dispersión deseado. Da al gráfico los siguientes
argumentos:

1. El título “Adult heights” ("Altura de adultos" en Espanol) (el uso de mayúsculas y minúsculas es
importante).
2. Valor alfa de 0.36.
3. Tamaño de la gráfica de 8 por 6 pulgadas.
4. Eje X etiquetado “Age / years” (“Edad / anos“ en Espanol).
5. Eje Y etiquetado “Height / inches” ("Altura / pulgadas" en Espanol).
"""

df = read_file('height_weight.csv')

df.plot(x='age',
        y='height',
        title="Adult heights",
        kind='scatter',
        alpha= 0.36,
        figsize=[8,6],
        xlabel='Age / years',
        ylabel='Height / inches',
)

plt.show()

print()


"""
¿Recuerdas el gráfico de dispersión que hiciste en la última lección para las columnas 'height' y 'age'?
Ahora vas a calcular el coeficiente de correlación de Pearson para aquellas columnas y asigna el
resultado a una variable llamada ah_corr. Después muéstralo. ¿El resultado se alinea con el gráfico
de dispersión?
"""

df = read_file('height_weight.csv')

ah_corr = df['height'].corr(df['age'])

print(ah_corr)

print()


"""
Intenta llamar al método corr() en todo el DataFrame. Para ello, sigue el mismo proceso que antes,
pero no pases ninguna variable al DataFrame df o al método corr(). ¿Qué pasa? Imprime el resultado.
"""

df = read_file('height_weight.csv')

print(df.corr())

print()


"""
Obtén los coeficientes de correlación para la columna 'male' con cada una de las otras tres columnas.
Pero en lugar de llamar corr() en la columna 'male' tres veces por separado, crea una matriz de
correlación y extrae los tres coeficientes que deseas. El resultado debería ser un objeto Series con
tres elementos, uno para cada coeficiente.

Asigna la matriz de correlación a una variable llamada corr_mat y asigna el Series de coeficientes a
una variable llamada male_corr. Luego, muestra male_corr.

Usa loc[] con 'male' como el primer argumento, y una lista de los otros datos como el segundo argumento
para extraer aquellos valores para la variable male_corr.
"""

df = read_file('height_weight.csv')

corr_mat = df.corr() 
male_corr = corr_mat.loc['male', ['height', 'weight', 'age']]
print(male_corr)

print()



"""
Ejercicio 1
Crea un gráfico de líneas para el volumen comercial del conjunto de datos de acciones de Starbucks.
Haz que tu gráfico se adhiera a lo siguiente:

1. Titulado "Historic SBUX volume" ("Volumen histórico de SBUX”) (la distinción entre mayúsculas y
minúsculas es importante).
2. Eje X con la leyenda “Date” ("Fecha").
3. Eje Y con la leyenda “Volume” ("Volumen").
4. Leyendas de marca del eje X rotadas 50 grados.
5. El límite del eje Y de 1 millón a 70 millones (puedes usar 1e6 y 7e7 como los límites inferior y
superior, respectivamente, para evitar escribir tantos ceros. 1e6 significa "1 por 10 a la sexta
potencia", es decir, 1 000 000, y 7e7 significa "7 por 10 a la séptima potencia", es decir, 70 000 000).
6. Sin leyenda.
"""

df = read_file('sbux.csv')

df.plot(x='date',
        y='volume',
        xlabel='Date',
        ylabel='Volume',
        title='Historic SBUX volume',
        ylim=[1e6,7e7],
        legend=False,
        rot=50)

plt.show()

print()



"""
Crea un gráfico de líneas que incluya tanto el precio de apertura como el de cierre. Para hacer esto,
puedes pasar la lista de nombres de columna, cols, proporcionada en el precódigo como tu argumento
para y=. Dado que tendrás dos variables diferentes en el mismo gráfico, asegúrate de incluir una leyenda
esta vez. Haz que tu gráfico también cumpla con lo siguiente:

1. Titulado “Historic SBUX price” ("Precio histórico de SBUX") (la distinción entre mayúsculas y minúsculas
   es importante).
2. Eje X con la leyenda “Date” ("Fecha").
3. Eje Y con la leyenda “Share price / USD” ("Precio de la acción / USD"). Deja un espacio antes y después
   de la /, por claridad y para evitar errores.
4. Leyendas de marca del eje X rotadas 50 grados.

No olvides incluir plt.show().
"""

df = read_file('sbux.csv')
cols = ['open', 'close']

df.plot(x = 'date',
        y = cols,
        title = 'Historic SBUX price',
        xlabel = 'Date',
        ylabel = 'Share price / USD',
        rot = 50)

plt.show()

print ()



'''
La población de California es mucho mayor que la de Oregón y Washington, por lo que es difícil hacerse
una idea de los datos de esos dos estados a partir del gráfico que hicimos. Crea un gráfico de barras
que muestre solo las poblaciones de Oregón y Washington para cada año en el conjunto de datos. Hazlo
llamando a plot() en df con argumentos que le den a tu gráfica las siguientes propiedades:

1. Incluye solo datos para Oregón y Washington especificando nuestro eje Y, tal como hicimos en
   lalección anterior.
2. Título: “Pacific Northwest population growth” (“Crecimiento de la población del noroeste del
   Pacífico“). La distinción entre mayúsculas y minúsculas es importante.
3. El eje X etiquetado: “Year” ("Año").
4. El eje Y etiquetado: “Population (millions)” ("Población (millones)").
5. Leyenda con etiquetas "OR" y "WA" para las poblaciones de Oregón y Washington, respectivamente.
'''

df = read_file('west_coast_pop.csv')
cols = ['or_pop', 'wa_pop']
df.plot(x = 'year',
        y = cols,
        kind = 'bar',
        title = 'Pacific Northwest population growth',
        xlabel = 'Year',
        ylabel = 'Population (millions)')

plt.legend(['OR','WA'])
plt.show()

print()



"""
1.
Investiga la distribución del peso para diferentes grupos de edad. Haremos esto en dos pasos.
Para comenzar, divide el conjunto de datos en tres DataFrames filtrando df y asígnalos a las
siguientes variables:

1. df_20s: solo las filas donde 'age' es menor a 30.
2. df_30s: solo las filas donde 'age' es mayor o igual a 30 y menor a 40.
3. df_40s: solo las filas donde 'age' es mayor o igual a 40.
   - En este último, no excluyas 50 años. Con una sola condición para la edad de 40 es suficiente.

Para verificar que filtraste correctamente, muestra los siguientes resultados:
1. La suma de las longitudes de los tres DataFrames (debe haber 10 000 filas en total).
2. El valor mínimo y máximo en la columna 'age' de df_20s
3. El valor mínimo y máximo en la columna 'age' de df_30s
4. El valor mínimo y máximo en la columna 'age' de df_40s

El precódigo ya contiene una plantilla para que muestres tus resultados, solo completa el código.

2.
Y, para el segundo paso, vas a crear un histograma para cada grupo de edad, todos en la misma
gráfica. Para esto, haz lo siguiente:

- Llama plot() en la columna 'weight' de df_20s
  - Establece el número de contenedores a 20.
  - Título de la gráfica “Weight / lbs” ("Peso / lbs").
  - Etiqueta el eje Y “Frequency” ("Frecuencia").
- Llama plot() en la columna 'weight' de df_30s
  - Establece el número de contenedores a 20.
  - Establece el valor de alpha a 0.6.
- Llama plot() en la columna 'weight' de df_40s
  - Establece el número de contenedores a 20.
  - Establece el valor de alpha a 0.3.

Finalmente, usa la función legend() de matplotlib para etiquetar cada histograma como "20s", "30s"
y "40s", respectivamente.
"""

df = read_file('height_weight.csv')

# separa df en dataframes separados según la edad
df_20s = df[df['age'] < 30]
df_30s = df[(df['age'] >= 30) & (df['age'] < 40)]
df_40s = df[df['age'] >= 40]

print("La suma de las longitudes del dataframe:", len(df_20s) + len(df_30s) + len(df_40s))
print("Edad mínima y máxima para df_20s:", df_20s['age'].min() , df_20s['age'].max())
print("Edad mínima y máxima para df_30s:", df_30s['age'].min() , df_30s['age'].max())
print("Edad mínima y máxima para df_40s:", df_40s['age'].min() , df_40s['age'].max())

df_20s['weight'].plot(kind = 'hist',
                    title = 'Weight / lbs',
                    ylabel = 'Frequency',
                    bins = 20)

df_30s['weight'].plot(kind = 'hist',
                    bins = 20,
                    alpha = 0.6)

df_40s['weight'].plot(kind = 'hist',
                    bins = 20,
                    alpha = 0.3)

plt.legend(["20s", "30s", "40s"])

plt.show()