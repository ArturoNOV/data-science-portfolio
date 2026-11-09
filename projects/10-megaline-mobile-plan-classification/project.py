# Función para acceder a los datasets.
def read_file(file, **kwargs):
    from pathlib import Path

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
Sprint 10 — Introducción al Machine Learning
Proyecto: Recomendación de planes móviles — Megaline

1. Introducción

La compañía de telefonía móvil Megaline busca desarrollar un modelo de
aprendizaje automático que permita recomendar a sus clientes uno de sus
nuevos planes: Smart o Ultra, a partir de sus patrones de uso de los
servicios de telefonía, mensajería e Internet.

Para este proyecto se dispone de un conjunto de datos que contiene
información sobre el comportamiento mensual de clientes que ya utilizan
estos planes.

**Objetivo del proyecto**

Desarrollar y evaluar un modelo de clasificación capaz de identificar el
plan adecuado para cada cliente, utilizando sus características de
consumo y alcanzando una exactitud (*accuracy*) mínima de 0.75.

Para lograrlo, se explorarán los datos, se dividirán en conjuntos de
entrenamiento, validación y prueba, y se compararán distintos algoritmos
e hiperparámetros. Finalmente, se evaluará el modelo seleccionado y se
realizará una prueba de cordura para comprobar su desempeño frente a una
estrategia básica de clasificación.
"""


"""
2. Carga y exploración inicial de los datos

En esta etapa se importarán las librerías necesarias para el desarrollo
del proyecto y se cargará el conjunto de datos proporcionados.

Aunque los datos ya fueron procesados previamente, se verificará su
estructura, los tipos de datos, la presencia de valores ausentes o
duplicados y la existencia de posibles anomalías.

Esta revisión permitirá comprobar que el conjunto de datos es adecuado
para entrenar los modelos de clasificación y determinar si se requiere
alguna preparación adicional.
"""


import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Cargar el conjunto de datos
df = read_file('users_behavior.csv')

# Mostrar las primeras cinco filas
df.head()


# Examinar la estructura del conjunto de datos
df.info()


"""
**Resultados de la inspección inicial**

El conjunto de datos contiene 3,214 observaciones y cinco columnas:
cuatro características relacionadas con el consumo mensual de los
usuarios y una variable objetivo (`is_ultra`).

No se identificaron valores ausentes en ninguna columna. Las variables
`minutes` y `mb_used` son de tipo `float64`, mientras que `is_ultra` es
de tipo `int64`. Las columnas `calls` y `messages` también están
almacenadas como `float64`, aunque representan cantidades de llamadas y
mensajes.

A continuación, se examinarán las estadísticas descriptivas para
identificar posibles valores anómalos y determinar si es necesario
realizar alguna preparación adicional.
"""


# Obtener estadísticas descriptivas del conjunto de datos
df.describe()


"""
**Análisis de las estadísticas descriptivas**

Las estadísticas descriptivas muestran que las variables de consumo
(`calls`, `minutes`, `messages` y `mb_used`) tienen valores mínimos de
cero y no presentan valores negativos.

Los valores máximos son superiores a sus respectivas medias, lo que
podría indicar la presencia de usuarios con niveles de consumo elevados.
Sin embargo, estos valores no necesariamente representan errores, por lo
que no se considera justificado eliminarlos sin evidencia adicional.

La media de `is_ultra` es aproximadamente 0.3065. Al tratarse de una
variable binaria, esto indica que alrededor del 30.65 % de las
observaciones corresponden al plan Ultra y el 69.35 % al plan Smart.
Esta diferencia en la distribución de clases será relevante para la
evaluación de los modelos.

Por último, dado que `calls` y `messages` representan cantidades
discretas pero están almacenadas como `float64`, se comprobará si
contienen valores decimales antes de considerar su conversión a números
enteros.
"""


# Comprobar si existen valores no enteros
print(
    "Valores no enteros en calls:",
    (df['calls'] % 1 != 0).sum()
)

print(
    "Valores no enteros en messages:",
    (df['messages'] % 1 != 0).sum()
)


"""
**Verificación y conversión de tipos de datos**

La comprobación de las columnas `calls` y `messages` confirmó que
ninguna de las 3,214 observaciones contiene valores con parte decimal.

Dado que ambas variables representan cantidades discretas, se considera
apropiado convertirlas de `float64` a `int64` para que sus tipos de
datos correspondan con la información que representan.

Esta conversión no implica pérdida de información y, aunque no es
indispensable para entrenar los modelos de clasificación, permite
mantener una estructura de datos más coherente.

A continuación, se realizará la conversión y se verificarán los tipos de
datos resultantes.
"""


# Convertir las columnas de conteo a números enteros
df['calls'] = df['calls'].astype('int64')
df['messages'] = df['messages'].astype('int64')

# Verificar los tipos de datos
df.dtypes


# Comprobar la existencia de filas duplicadas
print('Número de filas duplicadas:', df.duplicated().sum())


# Comprobar los valores y la distribución de la variable objetivo
df['is_ultra'].value_counts()


"""
Conclusiones de la exploración inicial

La revisión del conjunto de datos permitió comprobar lo siguiente:

- No se encontraron valores ausentes ni filas completamente duplicadas.
- No se identificaron valores negativos en las variables de consumo.
- Las columnas `calls` y `messages` se convirtieron de `float64` a
  `int64` después de verificar que todos sus valores eran enteros.
- No se encontraron evidencias suficientes para considerar incorrectos
  los valores máximos de consumo, por lo que se conservaron todas las
  observaciones.
- Se confirmó que la variable objetivo `is_ultra` contiene
  exclusivamente las clases `0` (Smart) y `1` (Ultra).

El desequilibrio entre las clases, identificado durante el análisis
descriptivo, será considerado al preparar los conjuntos de
entrenamiento, validación y prueba.

Con base en las verificaciones realizadas, no se requieren
modificaciones adicionales antes de comenzar el modelado.
"""


"""
3. Preparación de los datos para el modelado

Para desarrollar y evaluar los modelos de clasificación, dividiremos el
conjunto de datos en tres partes:

- **Entrenamiento (60 %):** utilizado para que los modelos aprendan las
  relaciones entre las características de consumo y el plan contratado.
- **Validación (20 %):** utilizado para comparar los modelos y
  seleccionar los hiperparámetros que ofrecen mejores resultados.
- **Prueba (20 %):** reservado para evaluar el desempeño del modelo
  seleccionado sobre datos que no participaron en el entrenamiento ni en
  la selección de hiperparámetros.

Debido al desequilibrio identificado en la variable objetivo, se
utilizará una división estratificada para mantener aproximadamente la
misma proporción de clientes Smart y Ultra en los tres conjuntos.

También se establecerá un valor fijo de `random_state` para garantizar
la reproducibilidad de los resultados.

Antes de realizar la división, separaremos las variables predictoras de
la variable objetivo (`is_ultra`).
"""


# Separar las características y la variable objetivo
features = df.drop('is_ultra', axis=1)
target = df['is_ultra']

# Comprobar las dimensiones de ambas variables
print('Dimensiones de features:', features.shape)
print('Dimensiones de target:', target.shape)


# Separar el conjunto de prueba (20 %)
features_temp, features_test, target_temp, target_test = train_test_split(
    features,
    target,
    test_size=0.20,
    random_state=12345,
    stratify=target
)

# Comprobar las dimensiones de los conjuntos
print('Dimensiones de features_temp:', features_temp.shape)
print('Dimensiones de features_test:', features_test.shape)
print('Dimensiones de target_temp:', target_temp.shape)
print('Dimensiones de target_test:', target_test.shape)


# Dividir el conjunto temporal en entrenamiento y validación
features_train, features_valid, target_train, target_valid = train_test_split(
    features_temp,
    target_temp,
    test_size=0.25,
    random_state=12345,
    stratify=target_temp
)

# Comprobar las dimensiones de los tres conjuntos
print('Entrenamiento:', features_train.shape, target_train.shape)
print('Validación:', features_valid.shape, target_valid.shape)
print('Prueba:', features_test.shape, target_test.shape)


# Comprobar la distribución de clases en los tres conjuntos
print('Distribución en entrenamiento:')
print(target_train.value_counts(normalize=True))

print('\nDistribución en validación:')
print(target_valid.value_counts(normalize=True))

print('\nDistribución en prueba:')
print(target_test.value_counts(normalize=True))


"""
Conclusiones de la preparación de datos

Se separaron las cuatro características predictoras (`calls`, `minutes`,
`messages` y `mb_used`) de la variable objetivo (`is_ultra`).

Posteriormente, se dividieron las 3,214 observaciones en tres conjuntos
independientes:

- **Entrenamiento:** 1,928 observaciones (aproximadamente 60 %).
- **Validación:** 643 observaciones (aproximadamente 20 %).
- **Prueba:** 643 observaciones (aproximadamente 20 %).

Se utilizó `random_state=12345` para garantizar la reproducibilidad de
las divisiones y el parámetro `stratify` para conservar la distribución
de las clases.

La verificación confirmó que las proporciones de clientes Smart y Ultra
se mantienen prácticamente iguales en los tres conjuntos, por lo que la
estratificación fue satisfactoria.

Con los datos preparados, podemos comenzar el entrenamiento y la
comparación de los modelos de clasificación, utilizando el conjunto de
validación para seleccionar el modelo más adecuado y reservando el
conjunto de prueba para la evaluación final.
"""


"""
4. Entrenamiento y comparación de modelos

En esta etapa se entrenarán y evaluarán diferentes modelos de
clasificación para identificar cuál ofrece la mayor exactitud al
predecir el plan de los clientes de Megaline.

Se investigarán tres algoritmos:

- **Árbol de decisión (DecisionTreeClassifier):** clasifica las
  observaciones mediante una secuencia de decisiones basadas en sus
  características.
- **Bosque aleatorio (RandomForestClassifier):** combina múltiples
  árboles de decisión para obtener predicciones más estables.
- **Regresión logística (LogisticRegression):** estima la probabilidad
  de pertenecer a cada clase a partir de las características
  predictoras.

Los modelos se entrenarán con el conjunto de entrenamiento y se
evaluarán utilizando el conjunto de validación. Se modificarán los
hiperparámetros relevantes para estudiar su influencia en la exactitud y
detectar posibles indicios de sobreajuste.

El criterio principal de comparación será la exactitud (*accuracy*), de
acuerdo con los requisitos del proyecto, cuyo umbral mínimo es 0.75.

4.1. Árbol de decisión

Comenzaremos con un árbol de decisión, evaluando diferentes valores del
hiperparámetro `max_depth`, que controla la profundidad máxima del
árbol.

Una profundidad reducida puede limitar la capacidad del modelo para
identificar patrones complejos, mientras que una profundidad excesiva
puede provocar sobreajuste.

Compararemos la exactitud obtenida en los conjuntos de entrenamiento y
validación para identificar una profundidad apropiada.
"""


# Inicializar las variables para identificar el mejor modelo
best_tree_model = None
best_tree_depth = 0
best_tree_score = 0

# Evaluar diferentes profundidades del árbol de decisión
for depth in range(1, 11):
    model = DecisionTreeClassifier(
        random_state=12345,
        max_depth=depth
    )

    # Entrenar el modelo
    model.fit(features_train, target_train)

    # Calcular la exactitud en entrenamiento y validación
    train_accuracy = accuracy_score(
        target_train,
        model.predict(features_train)
    )
    valid_accuracy = accuracy_score(
        target_valid,
        model.predict(features_valid)
    )

    print(
        f'Profundidad: {depth} | '
        f'Entrenamiento: {train_accuracy:.4f} | '
        f'Validación: {valid_accuracy:.4f}'
    )

    # Guardar el modelo con mayor exactitud en validación
    if valid_accuracy > best_tree_score:
        best_tree_score = valid_accuracy
        best_tree_depth = depth
        best_tree_model = model

# Mostrar los resultados del mejor modelo
print(
    f'\nMejor profundidad: {best_tree_depth} | '
    f'Exactitud en validación: {best_tree_score:.4f}'
)


"""
**Resultados del árbol de decisión**

Se evaluaron diez modelos de árbol de decisión, variando `max_depth`
entre 1 y 10 y manteniendo `random_state=12345`.

Todos los modelos superaron el umbral mínimo de exactitud de 0.75 en
validación. Mediante la comparación automática de los resultados, se
identificó `max_depth=5` como la mejor profundidad entre las evaluadas,
con una exactitud de 0.8165 en validación y 0.8200 en entrenamiento.

Se observó que, al aumentar la profundidad, la exactitud de
entrenamiento continuó mejorando, mientras que la exactitud de
validación dejó de presentar mejoras sostenidas. Este comportamiento
sugiere posibles indicios de sobreajuste en los árboles más profundos.

El modelo seleccionado se almacenó en `best_tree_model` para su
posterior comparación con los demás algoritmos. La evaluación definitiva
se realizará únicamente después de seleccionar el mejor modelo global,
utilizando el conjunto de prueba reservado.
"""


"""
4.2. Bosque aleatorio

El algoritmo de bosque aleatorio (`RandomForestClassifier`) combina las
predicciones de múltiples árboles de decisión para realizar una
clasificación.

En esta etapa se evaluarán diferentes combinaciones de dos
hiperparámetros:

- **`n_estimators`:** cantidad de árboles que componen el bosque.
- **`max_depth`:** profundidad máxima permitida para cada árbol.

Se entrenarán los modelos utilizando el conjunto de entrenamiento y se
comparará su exactitud sobre el conjunto de validación.

También se analizará la diferencia entre las exactitudes de
entrenamiento y validación para identificar posibles indicios de
sobreajuste.

El objetivo será seleccionar automáticamente la combinación de
hiperparámetros que alcance la mayor exactitud en validación y comparar
su desempeño con el árbol de decisión evaluado anteriormente.
"""


# Inicializar las variables para identificar el mejor modelo
best_forest_model = None
best_forest_est = 0
best_forest_depth = 0
best_forest_score = 0

# Evaluar diferentes combinaciones de hiperparámetros
for est in [10, 20, 50, 100]:
    for depth in range(1, 11):
        model = RandomForestClassifier(
            random_state=12345,
            n_estimators=est,
            max_depth=depth
        )

        # Entrenar el modelo
        model.fit(features_train, target_train)

        # Calcular la exactitud en entrenamiento y validación
        train_accuracy = accuracy_score(
            target_train,
            model.predict(features_train)
        )
        valid_accuracy = accuracy_score(
            target_valid,
            model.predict(features_valid)
        )

        print(
            f'Árboles: {est:3} | '
            f'Profundidad: {depth:2} | '
            f'Entrenamiento: {train_accuracy:.4f} | '
            f'Validación: {valid_accuracy:.4f}'
        )

        # Guardar la mejor combinación de hiperparámetros
        if valid_accuracy > best_forest_score:
            best_forest_score = valid_accuracy
            best_forest_est = est
            best_forest_depth = depth
            best_forest_model = model

# Mostrar los resultados del mejor modelo
print(
    f'\nMejor número de árboles: {best_forest_est} | '
    f'Mejor profundidad: {best_forest_depth} | '
    f'Exactitud en validación: {best_forest_score:.4f}'
)


"""
**Resultados del bosque aleatorio**

Se evaluaron 40 combinaciones de hiperparámetros, utilizando 10, 20, 50
y 100 árboles, con profundidades entre 1 y 10.

La selección automática identificó como mejor combinación
`n_estimators=10` y `max_depth=8`, con una exactitud de 0.8320 en
validación y 0.8646 en entrenamiento.

Se observó que aumentar la cantidad de árboles no produjo necesariamente
mejores resultados. Asimismo, las mayores profundidades tendieron a
incrementar la exactitud de entrenamiento sin generar mejoras sostenidas
en validación, lo que sugiere posibles indicios de sobreajuste.

El bosque aleatorio superó la mejor exactitud obtenida anteriormente con
el árbol de decisión (0.8165). Por lo tanto, se conserva como el mejor
candidato hasta este momento, aunque todavía será necesario compararlo
con la regresión logística.

El modelo seleccionado quedó almacenado en `best_forest_model` para su
evaluación posterior.
"""


"""
4.3. Regresión logística

La regresión logística (`LogisticRegression`) es un algoritmo de
clasificación que estima la probabilidad de que una observación
pertenezca a una determinada clase.

A diferencia de los árboles de decisión y los bosques aleatorios, este
modelo establece una relación lineal entre las características
predictoras y el logaritmo de las probabilidades relativas de las
clases.

En este proyecto se utilizará para predecir si un cliente pertenece al
plan Smart o Ultra a partir de sus patrones de consumo.

Se comprobará que el algoritmo complete correctamente su entrenamiento y
se calculará su exactitud en los conjuntos de entrenamiento y
validación.

Finalmente, se comparará su desempeño con los resultados obtenidos
mediante el árbol de decisión y el bosque aleatorio para determinar cuál
ofrece la mayor exactitud.
"""


# Inicializar el modelo de regresión logística
logistic_model = LogisticRegression(random_state=12345)

# Entrenar el modelo
logistic_model.fit(features_train, target_train)

# Calcular la exactitud en entrenamiento y validación
logistic_train_accuracy = accuracy_score(
    target_train,
    logistic_model.predict(features_train)
)

logistic_valid_accuracy = accuracy_score(
    target_valid,
    logistic_model.predict(features_valid)
)

# Mostrar los resultados
print(
    f'Exactitud en entrenamiento: {logistic_train_accuracy:.4f}'
)

print(
    f'Exactitud en validación: {logistic_valid_accuracy:.4f}'
)


"""
**Resultados de la regresión logística**

El modelo de regresión logística se entrenó utilizando las
características originales del conjunto de entrenamiento, sin aplicar
estandarización.

Se obtuvo una exactitud de 0.7464 en entrenamiento y 0.7558 en
validación, superando ligeramente el umbral mínimo de 0.75 establecido
para el proyecto.

La diferencia entre ambas exactitudes es pequeña y no muestra indicios
evidentes de sobreajuste. Sin embargo, el desempeño en validación fue
inferior al obtenido con el árbol de decisión y el bosque aleatorio.

Por lo tanto, entre los modelos y configuraciones evaluados hasta ahora,
la regresión logística presentó la menor exactitud de validación.
"""


# Crear una tabla comparativa de los modelos
model_comparison = pd.DataFrame({
    'Modelo': [
        'Árbol de decisión',
        'Bosque aleatorio',
        'Regresión logística'
    ],
    'Exactitud en validación': [
        best_tree_score,
        best_forest_score,
        logistic_valid_accuracy
    ]
})

# Ordenar los modelos por exactitud, de mayor a menor
model_comparison = model_comparison.sort_values(
    by='Exactitud en validación',
    ascending=False
).reset_index(drop=True)

# Mostrar la tabla comparativa
model_comparison


"""
Conclusiones de la comparación de modelos

Se entrenaron y evaluaron tres algoritmos de clasificación: árbol de
decisión, bosque aleatorio y regresión logística.

Los tres superaron el umbral mínimo de exactitud de 0.75 en el conjunto
de validación. Sin embargo, el bosque aleatorio obtuvo el mejor
desempeño, alcanzando una exactitud de 0.8320, seguido del árbol de
decisión con 0.8165 y la regresión logística con 0.7558.

El mejor bosque aleatorio utilizó los hiperparámetros `n_estimators=10`
y `max_depth=8`, seleccionados automáticamente entre las 40
combinaciones evaluadas.

Con base en estos resultados, se selecciona el bosque aleatorio como el
modelo más adecuado entre los candidatos estudiados.

La siguiente etapa consistirá en entrenar el modelo seleccionado
utilizando conjuntamente los datos de entrenamiento y validación, para
posteriormente evaluar su capacidad de generalización sobre el conjunto
de prueba, que hasta ahora ha permanecido reservado.
"""


"""
5. Evaluación del modelo seleccionado

Después de comparar los tres algoritmos, se seleccionó el bosque
aleatorio por haber obtenido la mayor exactitud en el conjunto de
validación.

Para la evaluación final, se entrenará un nuevo modelo utilizando los
hiperparámetros seleccionados (`n_estimators=10` y `max_depth=8`) y
combinando los conjuntos de entrenamiento y validación.

Esto permitirá aprovechar aproximadamente el 80 % de las observaciones
para el entrenamiento definitivo, manteniendo reservado el 20 % restante
para la prueba.

Una vez entrenado, se evaluará el modelo utilizando el conjunto de
prueba, que no ha participado en el entrenamiento ni en la selección de
hiperparámetros.

La exactitud obtenida se comparará con el umbral mínimo de 0.75
establecido para determinar si el modelo cumple el objetivo del
proyecto.
"""


# Combinar los conjuntos de entrenamiento y validación
features_final = pd.concat(
    [features_train, features_valid]
)

target_final = pd.concat(
    [target_train, target_valid]
)

# Verificar las dimensiones de los conjuntos combinados
print('Dimensiones de features_final:', features_final.shape)
print('Dimensiones de target_final:', target_final.shape)


# Inicializar el modelo definitivo con los mejores hiperparámetros
final_model = RandomForestClassifier(
    random_state=12345,
    n_estimators=best_forest_est,
    max_depth=best_forest_depth
)

# Entrenar el modelo con los datos combinados
final_model.fit(features_final, target_final)

# Comprobar la exactitud en el conjunto de entrenamiento definitivo
final_train_accuracy = accuracy_score(
    target_final,
    final_model.predict(features_final)
)

print(
    f'Exactitud en entrenamiento definitivo: '
    f'{final_train_accuracy:.4f}'
)


# Obtener las predicciones del conjunto de prueba
test_predictions = final_model.predict(features_test)

# Calcular la exactitud en el conjunto de prueba
test_accuracy = accuracy_score(
    target_test,
    test_predictions
)

# Mostrar la exactitud obtenida
print(f'Exactitud en prueba: {test_accuracy:.4f}')


"""
Resultados de la evaluación final

El modelo definitivo de bosque aleatorio se entrenó utilizando 2,571
observaciones, correspondientes a la combinación de los conjuntos de
entrenamiento y validación, y conservando los hiperparámetros
seleccionados previamente (`n_estimators=10` y `max_depth=8`).

Se obtuvo una exactitud de 0.8608 en entrenamiento y de 0.8149 en el
conjunto de prueba.

La exactitud de prueba supera el umbral mínimo de 0.75 establecido, por
lo que el modelo cumple el objetivo principal de desempeño.

Aunque la exactitud de prueba es inferior a la de entrenamiento, el
modelo conserva un desempeño superior al requerido al clasificar
observaciones que no participaron en su entrenamiento.

Finalmente, se realizará una prueba de cordura para comprobar si el
desempeño obtenido representa una mejora respecto de una estrategia
básica de clasificación.
"""


"""
6. Prueba de cordura (Sanity Check)

Para comprobar que el modelo desarrollado aporta valor frente a una
estrategia básica de clasificación, se realizará una prueba de cordura
(*sanity check*).

Esta prueba consiste en comparar la exactitud del bosque aleatorio con
la de un clasificador de referencia (*baseline*) que siempre predice la
clase más frecuente, sin considerar las características de consumo de
los clientes.

Dado que el plan Smart (`0`) representa la clase mayoritaria,
utilizaremos esta estrategia como referencia.

La clase mayoritaria se determinará utilizando los datos de
entrenamiento del modelo definitivo, y la exactitud de referencia se
calculará sobre el mismo conjunto de prueba utilizado para evaluar el
bosque aleatorio.

Finalmente, se compararán ambas exactitudes para determinar si el modelo
desarrollado mejora la predicción respecto de esta estrategia básica.
"""


# Identificar la clase mayoritaria en el entrenamiento definitivo
majority_class = target_final.value_counts().idxmax()

# Calcular la exactitud del clasificador de referencia
baseline_accuracy = (target_test == majority_class).mean()

# Comparar los resultados
print(f'Clase mayoritaria: {majority_class}')
print(f'Exactitud del modelo de referencia: {baseline_accuracy:.4f}')
print(f'Exactitud del bosque aleatorio: {test_accuracy:.4f}')


"""
**Resultados de la prueba de cordura**

Se identificó el plan Smart (`0`) como la clase mayoritaria y se utilizó
como referencia una estrategia que siempre predice esa clase.

El clasificador de referencia obtuvo una exactitud de 0.6936 en el
conjunto de prueba, mientras que el bosque aleatorio alcanzó 0.8149.

La diferencia de 0.1213, equivalente a 12.13 puntos porcentuales,
demuestra que el modelo desarrollado mejora la exactitud de la
estrategia básica de clasificación.

Por lo tanto, el bosque aleatorio supera la prueba de cordura y cumple
también con el umbral mínimo de exactitud de 0.75 establecido para el
proyecto.
"""


"""
7. Conclusiones generales

El objetivo de este proyecto fue desarrollar un modelo de clasificación
capaz de predecir el plan Smart o Ultra de los clientes de Megaline a
partir de sus patrones de consumo, alcanzando una exactitud mínima de
0.75.

Durante el desarrollo se obtuvieron los siguientes resultados:

1. **Preparación de los datos:** se analizaron 3,214 observaciones, sin
   identificar valores ausentes ni filas duplicadas. Se verificaron y
   ajustaron los tipos de datos necesarios antes de dividir el dataset
   en entrenamiento (60 %), validación (20 %) y prueba (20 %),
   conservando la distribución de las clases mediante estratificación.

2. **Comparación de modelos:** se evaluaron árboles de decisión, bosques
   aleatorios y regresión logística. El bosque aleatorio obtuvo la mayor
   exactitud de validación (0.8320), utilizando 10 árboles y una
   profundidad máxima de 8.

3. **Evaluación final:** el modelo seleccionado se entrenó nuevamente
   con los conjuntos de entrenamiento y validación combinados,
   alcanzando una exactitud de 0.8149 sobre el conjunto de prueba. Este
   resultado supera el umbral mínimo solicitado.

4. **Prueba de cordura:** el bosque aleatorio superó la exactitud de
   0.6936 obtenida por un clasificador que siempre predice la clase
   mayoritaria, con una mejora de 12.13 puntos porcentuales.

**Conclusión final**

El modelo de bosque aleatorio seleccionado cumple el objetivo del
proyecto y demuestra una mejor capacidad de clasificación que la
estrategia básica de referencia.

Estos resultados indican que las características de consumo contienen
información útil para predecir el plan de los clientes. Sin embargo, la
exactitud global no permite determinar por sí sola qué tan bien se
identifica cada plan individualmente ni garantiza que el plan predicho
sea el más conveniente para cada usuario.
"""
