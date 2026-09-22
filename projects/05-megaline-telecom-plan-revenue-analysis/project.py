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
¿Cuál es la mejor tarifa?

Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a
sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber
cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.

Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes
relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes,
de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de
texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar
qué tarifa de prepago genera más ingresos.

Propósito del proyecto: analizar el comportamiento de clientes de Megaline y determinar cuál
tarifa, Surf o Ultimate, genera más ingresos.

Plan general de trabajo: cargar los datos, revisar su estructura, corregir problemas, calcular
métricas mensuales por usuario, comparar ingresos por tarifa y probar hipótesis si el proyecto
lo solicita.


Inicialización
"""


# Cargar todas las librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st


"""
Cargar datos
"""


# Carga los archivos de datos en diferentes DataFrames
calls = read_file('megaline_calls.csv')
internet = read_file('megaline_internet.csv')
messages = read_file('megaline_messages.csv')
plans = read_file('megaline_plans.csv')
users = read_file('megaline_users.csv')


"""
Preparar los datos

En esta sección revisaré cada una de las tablas disponibles para comprender su estructura,
identificar tipos de datos, valores ausentes y posibles problemas. Después realizaré las
correcciones necesarias antes de calcular métricas mensuales por usuario y comparar el
comportamiento entre tarifas.

Tarifas
"""

# Imprime la información general/resumida sobre el DataFrame de las tarifas
plans.info()


# Imprime una muestra de los datos para las tarifas
plans.head()


"""
El DataFrame `plans` contiene dos filas, correspondientes a las tarifas Surf y Ultimate, y no
presenta valores ausentes. Los tipos de datos son adecuados para el análisis. Se observa que
la columna del pago mensual aparece como `usd_monthly_pay`, aunque en la descripción del
proyecto se menciona como `usd_monthly_fee`. Para mantener consistencia con el diccionario de
datos, más adelante se puede renombrar esta columna.


Corregir datos


Según lo observado, solo se requiere cambiar el nombre de la columna `usd_monthly_pay` por el
nombre correcto, `usd_monthly_fee`.
"""

# Renombrar la columna de pago mensual para que coincida con el diccionario de datos
plans = plans.rename(columns={'usd_monthly_pay': 'usd_monthly_fee'})


"""
Enriquecer los datos

Una columna que valdría la pena agregar para homologar las unidades sería la correspondiente a
los datos incluidos en cada tarifa expresados en gigabytes. Actualmente, la columna
`mb_per_month_included` muestra los datos incluidos en megabytes, mientras que el cobro por
excedente se calcula por gigabyte mediante la columna `usd_per_gb`. Por esta razón, se agregará
la columna `gb_per_month_included`, dividiendo los megabytes incluidos entre 1024.
"""

# Agregar una columna con los GB incluidos por mes
plans['gb_per_month_included'] = plans['mb_per_month_included'] / 1024


"""
Usuarios/as
"""

# Imprime la información general/resumida sobre el DataFrame de usuarios
users.info()

# Imprime una muestra de datos para usuarios
users.head()


"""
El DataFrame `users` contiene 500 registros y 8 columnas. No hay valores ausentes en `user_id`,
`first_name`, `last_name`, `age`, `city`, `reg_date` ni `plan`. La columna `churn_date` tiene
únicamente 34 valores no nulos, lo cual es esperado porque, según la descripción del proyecto,
los valores ausentes indican que el usuario seguía activo al momento de extraer los datos.

Se observa que las columnas `reg_date` y `churn_date` están almacenadas como tipo `object`,
aunque representan fechas. Para poder trabajar correctamente con ellas en el análisis, será
necesario convertirlas al tipo `datetime`.


Corregir los datos

El problema obvio a corregir sería convertir el formato de las fechas de texto a fecha.
"""

# Convertir las columnas de fechas al tipo datetime
users['reg_date'] = pd.to_datetime(users['reg_date'])
users['churn_date'] = pd.to_datetime(users['churn_date'])


users.info()


"""
Enriquecer los datos

No hay datos que enriquecer.



Llamadas
"""

# Imprime la información general/resumida sobre el DataFrame de las llamadas
calls.info()


# Imprime una muestra de datos para las llamadas
calls.head()


"""
El DataFrame `calls` contiene 137,735 registros y 4 columnas. No se observan valores ausentes
en ninguna columna. La columna `call_date` está almacenada como tipo `object`, aunque representa
fechas, por lo que debe convertirse al tipo `datetime`. La columna `duration` está en formato
decimal, lo cual representa la duración original de cada llamada en minutos. Más adelante será
necesario redondear cada llamada hacia arriba, ya que Megaline cobra cada llamada individual
redondeada al minuto completo.



Corregir los datos

El cambio importante que se debe realizar en este punto es corregir el formato de las fechas,
de `object` a `datetime`.
"""

# Convertir la columna de fecha de llamada al tipo datetime

calls['call_date'] = pd.to_datetime(calls['call_date'])

calls.info()


"""
Enriquecer los datos

Se agrega la columna `duration_rounded` para representar los minutos facturables de cada llamada.
Esta columna redondea hacia arriba la duración original registrada en `duration`, de acuerdo con
la regla de facturación indicada en la descripción del proyecto.
"""

# Redondear cada llamada hacia arriba según la regla de facturación de Megaline

calls['duration_rounded'] = np.ceil(calls['duration'])

calls.head()


"""
Mensajes
"""

# Imprime la información general/resumida sobre el DataFrame de los mensajes

messages.info()


# Imprime una muestra de datos para los mensajes

messages.head()


"""
El DataFrame `messages` contiene 76,051 registros y 3 columnas. No se observan valores ausentes.
La columna `message_date` está almacenada como tipo `object`, aunque representa fechas, por lo
que debe convertirse al tipo `datetime` para poder trabajar correctamente con periodos mensuales
más adelante.



Corregir los datos

Corregimos el formato de las fechas.
"""

# Convertir la columna de fecha del mensaje al tipo datetime

messages['message_date'] = pd.to_datetime(messages['message_date'])

messages.info()


"""
Enriquecer los datos

No hay datos que enriquecer.



Internet
"""

# Imprime la información general/resumida sobre el DataFrame de internet
internet.info()


# Imprime una muestra de datos para el tráfico de internet
internet.head()


"""
El DataFrame `internet` contiene 104,825 registros y 4 columnas. No se observan valores ausentes.
La columna `session_date` está almacenada como tipo `object`, aunque representa fechas, por lo que
debe convertirse al tipo `datetime`. La columna `mb_used` está en formato numérico decimal y
representa el consumo de datos de cada sesión en megabytes.

También se observan sesiones con `mb_used` igual a 0.00. Por ahora no se eliminarán, ya que pueden
representar sesiones registradas sin consumo de datos. Además, según la descripción del proyecto,
las sesiones individuales de internet no se redondean; primero se suma el consumo mensual por usuario
y después el total mensual se redondea hacia arriba a gigabytes.



Corregir los datos

De igual forma, se corrige el formato de las fechas de `object` a `datetime`.
"""

# Convertir la columna de fecha de sesión al tipo datetime
internet['session_date'] = pd.to_datetime(internet['session_date'])

internet.info()


"""
Enriquecer los datos

No hay datos que enriquecer.



Estudiar las condiciones de las tarifas
"""

# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras
plans


"""
Las condiciones de las tarifas muestran que `surf` tiene una cuota mensual menor, pero también
incluye menos minutos, mensajes y datos. En cambio, `ultimate` tiene una cuota mensual más alta,
pero ofrece límites incluidos mucho mayores y cargos menores por excedente. Esta diferencia será
importante al calcular los ingresos mensuales por usuario, ya que los usuarios de `surf` podrían
generar cargos adicionales con mayor frecuencia.



Agregar datos por usuario
"""

# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.
calls['month'] = calls['call_date'].dt.month
calls_per_month = calls.groupby(['user_id', 'month'])['id'].count().reset_index()
calls_per_month = calls_per_month.rename(columns={'id': 'calls_count'})
calls_per_month.head()


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.
minutes_per_month = calls.groupby(['user_id', 'month'])['duration_rounded'].sum().reset_index()
minutes_per_month = minutes_per_month.rename(columns={'duration_rounded': 'minutes_used'})
minutes_per_month.head()


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.
messages['month'] = messages['message_date'].dt.month
messages_per_month = messages.groupby(['user_id', 'month'])['id'].count().reset_index()
messages_per_month = messages_per_month.rename(columns={'id': 'messages_count'})
messages_per_month.head()


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.
internet['month'] = internet['session_date'].dt.month
internet_per_month = internet.groupby(['user_id', 'month'])['mb_used'].sum().reset_index()
internet_per_month['gb_used'] = np.ceil(internet_per_month['mb_used'] / 1024)
internet_per_month.head()


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month
user_monthly_usage = calls_per_month.merge(
    minutes_per_month,
    on=['user_id', 'month'],
    how='outer'
)

user_monthly_usage = user_monthly_usage.merge(
    messages_per_month,
    on=['user_id', 'month'],
    how='outer'
)

user_monthly_usage = user_monthly_usage.merge(
    internet_per_month,
    on=['user_id', 'month'],
    how='outer'
)

user_monthly_usage[['calls_count', 'minutes_used', 'messages_count', 'mb_used', 'gb_used']] = user_monthly_usage[
    ['calls_count', 'minutes_used', 'messages_count', 'mb_used', 'gb_used']
].fillna(0)

user_monthly_usage.head()


# Añade la información de la tarifa
user_monthly_usage = user_monthly_usage.merge(
    users[['user_id', 'plan', 'city']],
    on='user_id',
    how='left'
)

user_monthly_usage = user_monthly_usage.merge(
    plans,
    left_on='plan',
    right_on='plan_name',
    how='left'
)

user_monthly_usage.head()


# Calcula el ingreso mensual para cada usuario
user_monthly_usage['extra_minutes'] = np.maximum(
    user_monthly_usage['minutes_used'] - user_monthly_usage['minutes_included'],
    0
)

user_monthly_usage['extra_messages'] = np.maximum(
    user_monthly_usage['messages_count'] - user_monthly_usage['messages_included'],
    0
)

user_monthly_usage['extra_gb'] = np.maximum(
    user_monthly_usage['gb_used'] - user_monthly_usage['gb_per_month_included'],
    0
)

user_monthly_usage['monthly_revenue'] = (
    user_monthly_usage['usd_monthly_fee']
    + user_monthly_usage['extra_minutes'] * user_monthly_usage['usd_per_minute']
    + user_monthly_usage['extra_messages'] * user_monthly_usage['usd_per_message']
    + user_monthly_usage['extra_gb'] * user_monthly_usage['usd_per_gb']
)

user_monthly_usage[
    ['user_id', 'month', 'plan', 'minutes_used', 'messages_count', 'gb_used',
    'extra_minutes', 'extra_messages', 'extra_gb', 'monthly_revenue']
].head()



"""
Estudia el comportamiento de usuario



Llamadas
"""

# Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.
avg_minutes_by_plan_month = user_monthly_usage.groupby(['month', 'plan'])['minutes_used'].mean().reset_index()

avg_minutes_by_plan_month_pivot = avg_minutes_by_plan_month.pivot(
    index='month',
    columns='plan',
    values='minutes_used'
)

avg_minutes_by_plan_month_pivot.plot(
    kind='bar',
    figsize=(10, 6)
)

plt.title('Promedio mensual de minutos usados por plan')
plt.xlabel('Mes')
plt.ylabel('Minutos promedio')
plt.legend(title='Plan')
plt.show()


"""
La duración promedio mensual de llamadas muestra un comportamiento relativamente similar entre
los usuarios de los planes `surf` y `ultimate`. Aunque en algunos meses uno de los planes supera 
l otro, no se observa una diferencia constante y marcada a favor de un solo plan. También se 
precia que el promedio de minutos tiende a ser mayor en los últimos meses del año.
"""


# Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.
surf_minutes = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['minutes_used']
ultimate_minutes = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['minutes_used']

surf_minutes.plot(
    kind='hist',
    bins=30,
    alpha=0.7,
    figsize=(10, 6),
    label='surf'
)

ultimate_minutes.plot(
    kind='hist',
    bins=30,
    alpha=0.7,
    label='ultimate'
)

plt.title('Distribución de minutos mensuales usados por plan')
plt.xlabel('Minutos mensuales')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()


"""
El histograma muestra que la distribución de minutos mensuales usados por los usuarios de `surf`
y `ultimate` es similar. En ambos planes, la mayoría de los registros se concentra aproximadamente
entre 200 y 650 minutos mensuales. También se observan algunos valores altos por encima de 1000
minutos, lo que indica usuarios con consumo considerablemente mayor al promedio. Las frecuencias
del plan `surf` son más altas, pero esto puede deberse a que hay más usuarios o registros mensuales
de ese plan, no necesariamente a un mayor consumo individual.
"""


# Calcula la media y la varianza de la duración mensual de llamadas.
surf_minutes_mean = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['minutes_used'].mean()
ultimate_minutes_mean = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['minutes_used'].mean()

surf_minutes_var = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['minutes_used'].var()
ultimate_minutes_var = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['minutes_used'].var()

call_duration_stats = pd.DataFrame({
    'plan': ['surf', 'ultimate'],
    'mean_minutes': [surf_minutes_mean, ultimate_minutes_mean],
    'variance_minutes': [surf_minutes_var, ultimate_minutes_var]
})

call_duration_stats


"""
La media mensual de minutos usados es muy similar entre los usuarios de `surf` y `ultimate`: ambos
planes están alrededor de 429 a 430 minutos mensuales. La varianza también es parecida, aunque
ligeramente mayor en `ultimate`, lo que indica que el consumo de minutos de ese plan tiene una
dispersión un poco más alta. En general, no se observa una diferencia marcada en el comportamiento
de llamadas entre ambos planes.
"""

# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas
user_monthly_usage.boxplot(
    column='minutes_used',
    by='plan',
    figsize=(8, 6)
)

plt.title('Distribución de minutos mensuales usados por plan')
plt.suptitle('')
plt.xlabel('Plan')
plt.ylabel('Minutos mensuales')
plt.show()



"""
En general, el comportamiento de llamadas de los usuarios de `surf` y `ultimate` es muy similar.
Las medias mensuales son casi iguales, alrededor de 429 a 430 minutos, y el diagrama de caja muestra
medianas y rangos intercuartílicos muy parecidos. Ambos planes presentan algunos valores atípicos
altos, con usuarios que superan los 1000 minutos mensuales. Con base en estos resultados, no se
observa una diferencia marcada en el comportamiento de llamadas entre los usuarios de ambos planes.
"""


"""
Mensajes
"""

# Compara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan
avg_messages_by_plan_month = user_monthly_usage.groupby(['month', 'plan'])['messages_count'].mean().reset_index()

avg_messages_by_plan_month_pivot = avg_messages_by_plan_month.pivot(
    index='month',
    columns='plan',
    values='messages_count'
)

avg_messages_by_plan_month_pivot.plot(
    kind='bar',
    figsize=(10, 6)
)

plt.title('Promedio mensual de mensajes enviados por plan')
plt.xlabel('Mes')
plt.ylabel('Mensajes promedio')
plt.legend(title='Plan')
plt.show()



"""
El promedio mensual de mensajes enviados tiende a ser mayor en el plan `ultimate` que en el plan
`surf` durante prácticamente todos los meses. En ambos planes se observa un aumento gradual en el
número promedio de mensajes enviados conforme avanza el año. A diferencia del comportamiento de
llamadas, aquí sí parece haber una diferencia más consistente entre los planes.
"""


# Calcula la media y la varianza de los mensajes mensuales enviados.

surf_messages_mean = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['messages_count'].mean()
ultimate_messages_mean = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['messages_count'].mean()

surf_messages_var = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['messages_count'].var()
ultimate_messages_var = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['messages_count'].var()

message_stats = pd.DataFrame({
    'plan': ['surf', 'ultimate'],
    'mean_messages': [surf_messages_mean, ultimate_messages_mean],
    'variance_messages': [surf_messages_var, ultimate_messages_var]
})

message_stats


# Traza un diagrama de caja para visualizar la distribución de mensajes mensuales por plan

user_monthly_usage.boxplot(
    column='messages_count',
    by='plan',
    figsize=(8, 6)
)

plt.title('Distribución de mensajes mensuales enviados por plan')
plt.suptitle('')
plt.xlabel('Plan')
plt.ylabel('Mensajes mensuales')
plt.show()


"""
Los usuarios del plan `ultimate` tienden a enviar más mensajes mensuales que los usuarios del plan
`surf`. Esto se observa tanto en el promedio mensual por mes como en la media general: `ultimate`
tiene una media aproximada de 37.55 mensajes mensuales, mientras que `surf` tiene una media aproximada
de 31.16. El diagrama de caja también muestra una mediana ligeramente mayor para `ultimate`. Aunque
ambos planes presentan valores atípicos, en general sí parece haber una diferencia moderada en el
comportamiento de mensajes entre los usuarios de ambos planes.
"""


"""
Internet
"""

# Compara la cantidad de tráfico de Internet consumido por usuarios por plan y por mes
avg_internet_by_plan_month = user_monthly_usage.groupby(['month', 'plan'])['gb_used'].mean().reset_index()

avg_internet_by_plan_month_pivot = avg_internet_by_plan_month.pivot(
    index='month',
    columns='plan',
    values='gb_used'
)

avg_internet_by_plan_month_pivot.plot(
    kind='bar',
    figsize=(10, 6)
)

plt.title('Promedio mensual de GB usados por plan')
plt.xlabel('Mes')
plt.ylabel('GB promedio')
plt.legend(title='Plan')
plt.show()


"""
El consumo promedio mensual de internet tiende a ser mayor en el plan `ultimate` que en el plan
`surf`, especialmente durante los primeros meses del año. Sin embargo, en los meses posteriores
la diferencia entre ambos planes se reduce y los consumos promedio se vuelven más similares. En
ambos planes se observa una tendencia general de aumento en el consumo de datos conforme avanza
el año.
"""


# Calcula la media y la varianza del consumo mensual de internet.

surf_internet_mean = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['gb_used'].mean()
ultimate_internet_mean = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['gb_used'].mean()

surf_internet_var = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['gb_used'].var()
ultimate_internet_var = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['gb_used'].var()

internet_stats = pd.DataFrame({
    'plan': ['surf', 'ultimate'],
    'mean_gb': [surf_internet_mean, ultimate_internet_mean],
    'variance_gb': [surf_internet_var, ultimate_internet_var]
})

internet_stats


# Traza un diagrama de caja para visualizar la distribución del consumo mensual de internet por plan

user_monthly_usage.boxplot(
    column='gb_used',
    by='plan',
    figsize=(8, 6)
)

plt.title('Distribución de GB mensuales usados por plan')
plt.suptitle('')
plt.xlabel('Plan')
plt.ylabel('GB mensuales')
plt.show()


"""
El consumo mensual de internet es bastante similar entre los usuarios de `surf` y `ultimate`. Las
medias son cercanas: aproximadamente 16.67 GB para `surf` y 17.31 GB para `ultimate`. El diagrama
de caja también muestra medianas y rangos intercuartílicos parecidos. Aunque `surf` presenta algunos
valores atípicos más extremos, en general no se observa una diferencia marcada en el consumo de
internet entre ambos planes. Sin embargo, esta variable puede ser importante para los ingresos, ya
que `surf` incluye solo 15 GB mensuales, mientras que `ultimate` incluye 30 GB.



Ingreso
"""

# Traza un histograma para visualizar la distribución de ingresos mensuales por plan
surf_revenue = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['monthly_revenue']
ultimate_revenue = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['monthly_revenue']

surf_revenue.plot(
    kind='hist',
    bins=30,
    alpha=0.7,
    figsize=(10, 6),
    label='surf'
)

ultimate_revenue.plot(
    kind='hist',
    bins=30,
    alpha=0.7,
    label='ultimate'
)

plt.title('Distribución de ingresos mensuales por plan')
plt.xlabel('Ingreso mensual')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()


# Describe estadísticamente los ingresos mensuales por plan.
surf_revenue_mean = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['monthly_revenue'].mean()
ultimate_revenue_mean = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['monthly_revenue'].mean()

surf_revenue_var = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['monthly_revenue'].var()
ultimate_revenue_var = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['monthly_revenue'].var()

revenue_stats = pd.DataFrame({
    'plan': ['surf', 'ultimate'],
    'mean_revenue': [surf_revenue_mean, ultimate_revenue_mean],
    'variance_revenue': [surf_revenue_var, ultimate_revenue_var]
})

revenue_stats

# Revisar los ingresos mensuales más frecuentes en el plan ultimate
user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['monthly_revenue'].value_counts().head(10)


"""
La distribución de ingresos del plan `ultimate` está fuertemente concentrada en 70 USD, que
corresponde a la cuota mensual base. Esto confirma que la mayoría de los usuarios de este plan no
generan cargos adicionales, ya que los límites incluidos son suficientemente altos para cubrir su
consumo mensual. Los pocos valores superiores a 70 representan casos con excedentes.
"""


# Traza un diagrama de caja para visualizar la distribución de ingresos mensuales por plan
user_monthly_usage.boxplot(
    column='monthly_revenue',
    by='plan',
    figsize=(8, 6)
)

plt.title('Distribución de ingresos mensuales por plan')
plt.suptitle('')
plt.xlabel('Plan')
plt.ylabel('Ingreso mensual')
plt.show()


"""
El plan `ultimate` genera un ingreso mensual promedio mayor que `surf`: aproximadamente 72.31 USD
frente a 60.71 USD. Sin embargo, la distribución de ingresos es muy diferente entre ambos planes.
En `ultimate`, la mayoría de los usuarios paga cerca de 70 USD, que corresponde a la cuota mensual
base, por lo que los ingresos son más estables y tienen una varianza baja. En cambio, `surf` tiene
una cuota base menor, pero muchos usuarios generan cargos adicionales, especialmente por excedentes
de internet. Esto produce una distribución mucho más dispersa y con valores atípicos altos. En
resumen, `ultimate` genera más ingreso promedio y es más estable, mientras que `surf` depende más
de los cargos por excedente.



Prueba las hipótesis estadísticas


Hipótesis nula: el ingreso promedio mensual de los usuarios de `ultimate` es igual al ingreso promedio
mensual de los usuarios de `surf`.
Hipótesis alternativa: el ingreso promedio mensual de los usuarios de `ultimate` es diferente al
ingreso promedio mensual de los usuarios de `surf`.

Se utilizará una prueba t bilateral para dos muestras independientes, ya que se comparan los ingresos
de dos grupos distintos de usuarios. Como las varianzas de ingresos entre los planes son diferentes,
se utilizará la versión de Welch mediante `equal_var=False`. El nivel de significancia será de 0.05.
"""

# Prueba las hipótesis
alpha = 0.05

surf_revenue = user_monthly_usage[user_monthly_usage['plan'] == 'surf']['monthly_revenue']
ultimate_revenue = user_monthly_usage[user_monthly_usage['plan'] == 'ultimate']['monthly_revenue']

results = st.ttest_ind(
    surf_revenue,
    ultimate_revenue,
    equal_var=False
)

print('p-value:', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print('No podemos rechazar la hipótesis nula')


"""
El valor p obtenido fue mucho menor que el nivel de significancia de 0.05, por lo que se rechaza
la hipótesis nula. Esto indica que existe evidencia estadística suficiente para concluir que el
ingreso promedio mensual de los usuarios de `surf` y `ultimate` es diferente. Además, de acuerdo
con las medias calculadas previamente, el plan `ultimate` genera un ingreso promedio mensual
mayor que el plan `surf`.
"""

# Crear una columna para identificar si el usuario pertenece al área NY-NJ
user_monthly_usage['region_group'] = np.where(
    user_monthly_usage['city'].str.contains('NY-NJ', regex=False),
    'NY-NJ',
    'Other'
)

user_monthly_usage[['user_id', 'month', 'city', 'region_group', 'monthly_revenue']].head()


# Revisar cuántos registros hay en cada grupo regional
user_monthly_usage['region_group'].value_counts()


"""
Se utilizará una prueba t bilateral para dos muestras independientes, ya que se comparan los ingresos
de dos grupos regionales distintos. Como no se asume igualdad de varianzas entre los grupos y los
tamaños de muestra son diferentes, se utilizará la versión de Welch mediante `equal_var=False`. El
nivel de significancia será de 0.05.


Hipótesis nula: el ingreso promedio mensual de los usuarios del área NY-NJ es igual al ingreso promedio
mensual de los usuarios de otras regiones.
Hipótesis alternativa: el ingreso promedio mensual de los usuarios del área NY-NJ es diferente al ingreso
promedio mensual de los usuarios de otras regiones.

Se utilizará una prueba t para dos muestras independientes, ya que se comparan los ingresos de dos grupos
regionales distintos. El nivel de significancia será de 0.05.
"""

# Prueba las hipótesis
alpha = 0.05

ny_nj_revenue = user_monthly_usage[user_monthly_usage['region_group'] == 'NY-NJ']['monthly_revenue']
other_revenue = user_monthly_usage[user_monthly_usage['region_group'] == 'Other']['monthly_revenue']

results = st.ttest_ind(
    ny_nj_revenue,
    other_revenue,
    equal_var=False
)

print('Ingreso promedio NY-NJ:', ny_nj_revenue.mean())
print('Ingreso promedio otras regiones:', other_revenue.mean())
print('p-value:', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print('No podemos rechazar la hipótesis nula')


"""
El valor p obtenido fue 0.0335, menor que el nivel de significancia de 0.05. Por lo tanto, se rechaza la
hipótesis nula. Esto indica que existe evidencia estadística suficiente para concluir que el ingreso
promedio mensual de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones. Además,
las medias calculadas muestran que el ingreso promedio mensual de otras regiones es mayor que el de NY-NJ
en esta muestra.



Conclusión general

En este proyecto se analizaron los datos de usuarios de Megaline para comparar el comportamiento de consumo
y los ingresos generados por los planes `surf` y `ultimate`.

Primero se prepararon los datos corrigiendo los tipos de fecha en las tablas de usuarios, llamadas, mensajes
e internet. Los valores ausentes en `churn_date` se conservaron, ya que representan usuarios que seguían
activos. Para las llamadas, se creó una columna de minutos facturables redondeando cada duración hacia arriba,
de acuerdo con la regla de facturación de Megaline. Para internet, primero se sumó el consumo mensual en MB
por usuario y después se convirtió a GB redondeados hacia arriba, ya que la facturación se realiza sobre el
consumo mensual total. También se fusionaron los datos mensuales de llamadas, mensajes e internet con la
información del plan y la ciudad de cada usuario. Los valores ausentes de consumo mensual se sustituyeron
por 0, ya que indican meses en los que el usuario no utilizó ese servicio.

En cuanto al comportamiento de los usuarios, el consumo de llamadas fue muy similar entre ambos planes. Los
usuarios de `surf` y `ultimate` tuvieron promedios mensuales cercanos a 429 y 430 minutos, respectivamente.
En mensajes, los usuarios de `ultimate` enviaron ligeramente más mensajes en promedio que los usuarios de
`surf`. En internet, el consumo promedio mensual también fue parecido: aproximadamente 16.67 GB para `surf`
y 17.31 GB para `ultimate`.

La diferencia más importante apareció en los ingresos. El plan `ultimate` generó un ingreso promedio mensual
mayor, con aproximadamente 72.31 USD frente a 60.71 USD de `surf`. Además, los ingresos de `ultimate` fueron
mucho más estables, ya que la mayoría de sus usuarios pagó únicamente la cuota mensual base de 70 USD. En
cambio, `surf` tuvo una varianza mucho mayor porque, aunque su cuota base es menor, muchos usuarios generaron
cargos adicionales, especialmente por excedentes de internet. Esto provocó una distribución más dispersa y con
valores atípicos altos.

La primera prueba de hipótesis mostró que el ingreso promedio mensual de los usuarios de `surf` y `ultimate`
es diferente. El valor p fue mucho menor que 0.05, por lo que se rechazó la hipótesis nula. Además, las medias
calculadas indican que `ultimate` genera mayor ingreso promedio mensual.

La segunda prueba de hipótesis comparó el ingreso promedio de los usuarios del área NY-NJ contra el de otras
regiones. El valor p fue 0.0335, menor que el nivel de significancia de 0.05, por lo que también se rechazó la
hipótesis nula. En esta muestra, el ingreso promedio mensual de otras regiones fue mayor que el de NY-NJ:
aproximadamente 65.22 USD frente a 59.92 USD.

En conclusión, si el objetivo es identificar qué plan genera mayor ingreso promedio mensual, `ultimate` es la
mejor tarifa, ya que produce ingresos promedio más altos y más estables. Sin embargo, `surf` también es
relevante para el negocio porque puede generar ingresos elevados en usuarios con mucho consumo adicional,
aunque de manera menos predecible.
"""