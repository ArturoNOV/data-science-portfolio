import pandas as pd
from sklearn import set_config
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

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
Cambia la tarea original a una tarea de clasificación. Crea una nueva característica
llamada price_class. Para precios mayores a $113 000, asigna price_class a 1. Para
precios menores o iguales a $113 000, asigna 'price_class' a 0. Imprime las primeras
cinco filas de la tabla (que ya están en precodificación).
"""

df = read_file('train_data_us.csv')

df['price_class'] = (df['last_price'] > 113000).astype(int)

print(df.head())
print()



"""
Muchas librerías de machine learning requieren que las características se almacenen
en variables separadas. Declara dos variables:

features para características
target para objetivo
Imprime los tamaños de estas variables en pantalla.
"""

features = df.drop(['last_price','price_class'], axis=1)
target = df['price_class']

print(features.shape)
print(target.shape)
print()



"""
Comencemos con el entrenamiento del modelo. En la Lección anterior guardamos el
conjunto de datos de entrenamiento en las variables features y target. Para
iniciar el entrenamiento, llama al método fit() y pásale tus variables como argumento.

model.fit(features, target)

Finaliza el código e imprime la variable model en la pantalla.
"""

set_config(print_changed_only=False)

# crea un modelo vacío y se asigna a una variable
model = DecisionTreeClassifier()

print('Decision Tree Classifier', model)
print()

"""
 - class_weight=None — Cada clase tiene el mismo peso.
 - criterion='gini' — El índice de Gini mide la impureza en un nodo de un árbol de
   decisión. Un valor bajo indica nodos puros (datos de una clase), y un valor alto
   indica nodos impuros (datos mezclados de diferentes clases). Durante el
   entrenamiento, el árbol de decisión busca la división que más reduzca la
   impureza, según el índice de Gini, para crear nodos más homogéneos y mejorar la
   clasificación.
 - max_ depth=None — La profundidad del árbol es ilimitada.
"""



"""
Ahora tenemos un modelo entrenado en la variable model . Para predecir respuestas,
llama al método predict() y pásale la tabla con las características de las nuevas
observaciones.

answers = model.predict(new_features)
Crea dos nuevas observaciones y verifica los resultados de la predicción. Recuerda
que todo lo que está por encima y por debajo del precio mediano se etiqueta con las
clases de precio 1 y 0, respectivamente. Las observaciones en nuestra tarea son
apartamentos. Escribe los valores de las características para cada observación:
    1) El primer apartamento tiene 12 dormitorios con una superficie total de 900 m².
       La superficie de la sala de estar es de 409.7 m² y la superficie de la cocina
       es de 112 m².
    2) El segundo apartamento tiene 2 dormitorios con una superficie total de 109 m².
       La superficie de la sala de estar es de 32 m² y la de la cocina es de 40.5 m².

Casi no hay diferencia entre las características restantes. No proporcionamos precio
para estos dos casos experimentales, y se espera que nuestro clasificador entrenado
adivine la clase correcta usando las características que especificamos. Predice la
respuesta y muéstrala en la pantalla.
"""

model.fit(features, target)

new_features = pd.DataFrame(
    [
        [None, None, 2.8, 25, None, 25, 0, 0, 0, None, 0, 30706.0, 7877.0],
        [None, None, 2.75, 25, None, 25, 0, 0, 0, None, 0, 36421.0, 9176.0]
    ],
    columns=features.columns
)

# completa la tabla con las nuevas características
new_features.loc[0, 'total_area'] = 900.0
new_features.loc[0, 'bedrooms'] = 12
new_features.loc[0, 'living_area'] = 409.7
new_features.loc[0, 'kitchen_area'] = 112

new_features.loc[1, 'total_area'] = 109
new_features.loc[1, 'bedrooms'] = 2
new_features.loc[1, 'living_area'] = 32
new_features.loc[1, 'kitchen_area'] = 40.5

# predice respuestas y muestra el resultado en la pantalla
answers = model.predict(new_features)
print(answers, 'con Decision Tree Classifier')
print()



"""
Asigna las tres primeras observaciones del conjunto de prueba
(/datasets/test_data_us.csv) a la variable test_df. Guarda las funciones utilizadas
para la clasificación en la variable test_features. Haz una predicción de las
respuestas.

Crea la nueva columna con las respuestas correctas (price_class) y calcula sus
valores de la misma manera que lo hiciste para el conjunto de datos principal.
Copia esta columna en la variable test_target.
Imprime las predicciones y las respuestas correctas en la pantalla de la siguiente
manera:

Predicciones: [... ... ...]
Respuestas correctas: [... ... ...]

Las matrices de salida tienen que ser numpy.ndarray. El modelo genera este formato
de manera predeterminada, así que deja test_predictions como está. Usa el atributo
values para tomar los valores de numpy.ndarray desde el objeto serie test_target.

Averigüa cuántos errores ha cometido el modelo.
"""

model = DecisionTreeClassifier(random_state=12345)

model.fit(features, target)

# el conjunto de prueba está en el archivo test_data_us.csv 
test_df = read_file('test_data_us.csv').head(3)

# seleccionamos las características que usará el modelo para predecir
test_features = test_df.drop('last_price', axis=1)

# creamos las predicciones
test_predictions = model.predict(test_features)

# creamos la clase de precio correcta a partir del precio real
test_df['price_class'] = (test_df['last_price'] > 113000).astype(float)

# guardamos las respuestas correctas del conjunto de prueba
test_target = test_df['price_class']

# mostramos las predicciones y las respuestas correctas para compararlas
print('Utilizando Decision Tree Classifier:')
print('Predicciones:', test_predictions)
print('Respuestas correctas:', test_target.values)
print()



"""
Tres ejemplos no son suficientes para saber si el modelo funciona bien o no.
Cuenta el número de errores para todo el conjunto de prueba.

Escribe la función error_count(). El modelo toma las respuestas y predicciones
correctas y devuelve el número de discrepancias. Muestra el resultado en pantalla
de la siguiente manera:

Errores: ...
"""

# se crea el dataframe con el total de los datos
test_df = read_file('test_data_us.csv')

test_df['price_class'] = (test_df['last_price'] > 113000).astype(float)

test_features = test_df.drop(['last_price', 'price_class'], axis=1)

# pruebas para comprobar los nombres de columnas entre los dos DataFrames
print(features.columns.tolist())
print(test_features.columns.tolist())
print(features.columns.equals(test_features.columns))

test_target = test_df['price_class']
test_predictions = model.predict(test_features)
print()

def error_count(answers, predictions):
    return (answers.values != predictions).sum()

print('Errores con Decision Tree Classifier:', error_count(
    test_target, test_predictions))
print()



"""
7. Escribe la función accuracy(). Esta divide el número de respuestas correctas
entre el número total de predicciones realizadas y devuelve la puntuación de
exactitud.

Muestra la exactitud en la pantalla de la siguiente manera:

Exactitud: ...
"""

model = DecisionTreeClassifier(random_state=12345, class_weight='balanced')

model.fit(features, target)

test_predictions = model.predict(test_features)

def accuracy(answers, predictions):
    return (len(answers) - error_count(answers, predictions))/ len(answers) 

print('Accuracy (Decision Tree Classifier):', accuracy
      (test_target, test_predictions))
print()



"""
¿La puntuación de exactitud difiere entre el conjunto de entrenamiento y el
conjunto de prueba? Calcula los valores y muéstralos en la pantalla de la siguiente
manera:

Exactitud
Training set: ...
Test set: ...

Guarda las predicciones en las variables train_predictions (para el conjunto de
entrenamiento) y test_predictions (para el conjunto de prueba).
"""

model = DecisionTreeClassifier(random_state=12345)

model.fit(features, target)

train_predictions = model.predict(features) 
test_predictions = model.predict(test_features)

print('Exactitud (Decision Tree Classifier)')
print('Training set:', accuracy_score(target, train_predictions))
print('Test set:', accuracy_score(test_target, test_predictions))
print()



"""
Haz que el programa de entrenamiento del árbol de decisión pruebe varias
configuraciones del parámetro de profundidad máxima del árbol max_depth. El
programa tiene que:
 - Iterar sobre los valores del 1 al 10.
 - Entrenar modelos en el conjunto de entrenamiento. No olvides especificar
   random_state=54321 al inicializar el constructor del modelo.
 - Imprimir la puntuación de exactitud de cada modelo en los conjuntos de
   entrenamiento y de prueba.
"""

for depth in range(1, 11):  # selecciona el rango del hiperparámetro
    model = DecisionTreeClassifier(random_state=54321, max_depth=depth)
    model.fit(features, target)
    print("Exactitud de max_depth igual a", depth)
    # calcula e imprime la puntuación de accuracy en el conjunto de
    # entrenamiento
    print("Conjunto de entrenamiento:", accuracy_score
          (target, model.predict(features)))
    
    # calcula e imprime la puntuación de accuracy en el conjunto de prueba
    print("Conjunto de prueba (Decision Tree Classifier):", accuracy_score
          (test_target, model.predict(test_features))) 
print()



"""
Separa el dataset en dos conjuntos:
 - conjunto de entrenamiento (df_train);
 - conjunto de validación (df_valid) — 25 % de los datos fuente

Declara cuatro variables y pásalas de la siguiente manera:
 - características: features_train y features_valid;
 - objetivo: target_train y target_valid

Imprime los tamaños de las tablas que están almacenadas en cuatro variables.
"""

# segmenta el 25% de los datos para hacer el conjunto de validación.
df_train, df_valid = train_test_split(df, test_size=0.25, random_state=12345)

# se declaran variables para las características y para la
# característica objetivo.
features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

print(features_train.shape)
print(target_train.shape)
print(features_valid.shape)
print(target_valid.shape)
print()



"""
Cambia el hiperparámetro max_depthen el bucle de 1 a 5. Por cada valor, imprime
la calidad para el conjunto de validación. Imprime esto en la pantalla:

max_depth = 1 : ...
max_depth = 2 : ...
...
max_depth = 5 : ...

Aún no necesitamos probar nuestros modelos con el dataset de prueba. Primero
seleccionaremos el mejor modelo.
"""

for depth in range(1, 6):
    model = DecisionTreeClassifier(max_depth=depth, random_state=12345)
    model.fit(features_train, target_train)
    print("max_depth =", depth, ":", accuracy_score
        (target_valid, model.predict(features_valid)),
        '(Decision Tree Classifier)'
        )
print()



"""
Realiza un bucle que pruebe modelos de bosque aleatorio con varios números de
estimadores (árboles).

1. Divide los datos en conjuntos de entrenamiento y validación.
2. Elige el rango para que sea lo suficientemente grande para obtener una
   puntuación lo suficientemente buena, pero lo suficientemente pequeño para que
   tu programa no sea innecesariamente lento.
3. Configura el número de árboles para que sea igual a la variable de bucle est
   en el constructor del modelo.
4. Entrena modelos en el conjunto de entrenamiento. Calcula accuracy en el
   conjunto de validación para cada modelo.
5. Imprime la mejor puntuación de accuracy junto con el número correspondiente
   de estimadores.
"""

best_score = 0
best_est = 0

for est in range(1, 11): # selecciona el rango del hiperparámetro
    # configura el número de árboles
    model = RandomForestClassifier(random_state=54321, n_estimators=est)
    # entrena el modelo en el conjunto de entrenamiento
    model.fit(features_train, target_train)
    # calcula la puntuación de accuracy en el conjunto de validación
    score = model.score(features_valid, target_valid)
    if score > best_score:
        # guarda la mejor puntuación de accuracy en el conjunto de validación
        best_score = score
        # guarda el número de estimadores que corresponden a la mejor puntuación
        # de exactitud
        best_est = est

print(
    "La exactitud del mejor modelo en el conjunto de validación "
    "utilizando Random Forest Classifier "
    "(n_estimators = {}): {}".format(best_est, best_score)
    )
print()



"""
Entrena un modelo de regresión logística en el conjunto de entrenamiento, luego
calcula el valor de accuracy tanto en el conjunto de entrenamiento como en el
conjunto de validación.
"""

# segmenta el 25% de los datos para hacer el conjunto de validación
df_train, df_valid = train_test_split(df, test_size=0.25, random_state=54321)

# asignamos nuevamente los valores correspondientes a las variables porque
# cambiamos el random_state
features_train = df_train.drop(['last_price', 'price_class'], axis=1)
target_train = df_train['price_class']
features_valid = df_valid.drop(['last_price', 'price_class'], axis=1)
target_valid = df_valid['price_class']

# inicializa el constructor de regresión logística con los parámetros
# random_state=54321 y solver='liblinear'
model = LogisticRegression(random_state=54321, solver='liblinear')
# entrena el modelo en el conjunto de entrenamiento
model.fit(features_train, target_train)
# calcula la puntuación de accuracy en el conjunto de entrenamiento
score_train = model.score(features_train, target_train)
# calcula la puntuación de accuracy en el conjunto de validación
score_valid = model.score(features_valid, target_valid)

print(
    "Accuracy del modelo de regresión logística en el conjunto de "
    "entrenamiento:", score_train
    )
print(
    "Accuracy del modelo de regresión logística en el conjunto de "
    "validación:", score_valid
    )
print()



"""
Escribe una función mse(). Debe tomar respuestas correctas y predicciones y
devolver el valor del error cuadrático medio.

Tomamos las respuestas (costos reales) y las predicciones de la tabla. Imprime en
la pantalla el valor del EMC.
"""

def mse_manual(answers, predictions):
    err_obs = 0
    for i in range(len(answers)):
        err_obs += (answers[i] - predictions[i]) ** 2
    mse = err_obs / len(answers)
    return mse
    
answers = [623, 253, 150, 237]
predictions = [649, 253, 370, 148]

print(mse_manual(answers, predictions))
print()



"""
Utiliza la función de sklearn para calcular el Error Cuadrático Medio (EMC).

Busca en la documentación de sklearn la función correspondiente, impórtala y
calcula el EMC usando las mismas respuestas correctas y predicciones del ejercicio
anterior.

Imprime el resultado en pantalla.
"""

answers = [623, 253, 150, 237]
predictions = [649, 253, 370, 148]

result = mean_squared_error(answers, predictions)
print(result)
print()



"""
Prepara los datos y encuentra el precio promedio.

 - Declara la variable features con todas las características excepto last_price.
 - Declara la variable target con last_price como objetivo.
 - Calcula el valor promedio para los elementos de la variable target.

Imprime el resultado como se muestra:

Average price: ...
"""

features = df.drop('last_price', axis=1)
target = df['last_price']

average = target.mean()

print('Average price:', average)
print()



"""
Calcula el ECM para el conjunto de entrenamiento usando el precio promedio como
valor de predicción.

Imprime el resultado como se muestra:

MSE: ...

La función mean_squared_error() en scikit-learn tiene su maña. Tendrás que pasar
unos minutos leyendo la documentación o consultar Stack Overflow.

Divide los precios entre 100 000 con el propósito de evitar números grandes.
"""

features = df.drop(['last_price'], axis=1)
target = df['last_price'] / 1000000

predictions = pd.Series(target.mean(), index=target.index)

mse = mean_squared_error(target, predictions)

print('MSE:', mse)
print()



"""
No necesitamos "dólares cuadrados". Para obtener dólares normales encuentra la
RECM sacando la raíz cuadrada del ECM. Imprime en la pantalla los resultados como
se muestra:

RMSE: ...
Para encontrar la raíz cuadrada de un número usa el operador de exponente **. Eleva
el número a la potencia 0.5. Por ejemplo:

print(25 ** 0.5)
5
"""

rmse = mse ** 0.5

print('RMSE:', rmse)
print()



"""
Árbol de decisión de regresión
1. Destina 25% de los datos al conjunto de validación y el resto para el de
   entrenamiento.
2. Entrena modelos de árbol de decisión para un problema de regresión con
   diferentes valores de profundidad entre 1 y 5.
3. Calcula el valor de RECM en el conjunto de validación para cada modelo.
4. Almacena en la variable best_model el modelo con el mejor valor de RECM en el
   conjunto de validación. Para calcular la métrica RECM, toma el valor de la raíz
   cuadrada del ECM:

¿Es un buen resultado? Comparémoslo con otros modelos. Por lo menos podemos tener
la certeza de que nuestro modelo pasó la prueba de cordura.
"""

features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345
) # segmenta el 25% de los datos para hacer el conjunto de validación

best_model = None
best_result = 10000
best_depth = 0

# selecciona el rango del hiperparámetro, el límite superior no se incluye
for depth in range(1, 6):
    # entrena el modelo en el conjunto de entrenamiento
    model = DecisionTreeRegressor(random_state=12345, max_depth=depth)
    # entrena el modelo en el conjunto de entrenamiento
    model.fit(features_train, target_train)
    # obtiene las predicciones del modelo en el conjunto de validación
    predictions_valid = model.predict(features_valid)
    # calcula la RECM en el conjunto de validación
    result = mean_squared_error(target_valid, predictions_valid) ** 0.5
    if result < best_result:
        best_model = model
        best_result = result
        best_depth = depth

print(
    f"RECM del mejor modelo en el conjunto de validación usando Decision Tree "
    "Regressor (max_depth = {best_depth}): {best_result}"
    )
print()



"""
Bosque aleatorio de regresión

1. Selecciona 25% de los datos para la muestra de validación (prueba), lo demás
   será para el entrenamiento.
2. Extrae características y objetivos para el entrenamiento y la validación.
   Para conseguir objetivos, selecciona la columna 'last_price' y divídela entre
   100000. La característica son todas las columnas excepto por la columna
   'last_price'.
3. Entrena modelos de bosque aleatorio para el problema de regresión:
 - con el número de árboles: de 10 a 50, en intervalos de 10,
 - con una profundidad máxima de 1 a 10.
4. Para cada modelo, calcula la RECM en el conjunto de validación y guárdalo en
   la variable error.

Para calcular la métrica RECM, toma el valor de la raíz cuadrada del ECM:

    mean_squared_error(target_valid, predictions_valid)**0.5
"""

# Se hace división de datos para el entrenamiento y la validación
df_train, df_valid = train_test_split(df, random_state=54321, test_size = 0.25)

# se extraen las características de entrenamiento
features_train = df_train.drop(['last_price'], axis=1)
# se extraen los objetivos de entrenamiento
target_train = df_train['last_price'] / 100000
# se extraen las características para la validación
features_valid = df_valid.drop(['last_price'], axis=1)
# se extraen los objetivos de validación
target_valid = df_valid['last_price'] / 100000

best_error = 10000 # configura el inicio de RECM
best_est = 0
best_depth = 0
for est in range(10, 51, 10):
    for depth in range (1, 11):
        # inicializa el constructor de modelos con los parámetros
        # random_state=54321, n_estimators=est y max_depth=depth
        model = RandomForestRegressor(
            random_state=54321, n_estimators=est, max_depth=depth)
        # entrena el modelo en el conjunto de entrenamiento
        model.fit(features_train, target_train)
        # se obtienen las predicciones del modelo en el conjunto de validación
        predictions_valid = model.predict(features_valid)
        # calcula la RECM en el conjunto de validación
        error =mean_squared_error(target_valid, predictions_valid) ** 0.5
        print(
            f"RECM de validación para n_estimators={est}, "
            f"max_depth={depth}: {error}"
        )
        # se guarda la configuración del modelo si se logra el error más bajo
        if error < best_error:
            best_error = error
            best_est = est
            best_depth = depth

print()
print(
    "RECM del mejor modelo en el conjunto de validación usando Random Forest"
    "Regressor:", best_error, "n_estimators:", best_est, "best_depth:", best_depth)
print()



"""
Regresión lineal

Lleva las características de entrenamiento a la variable features y la
característica last_price del objetivo a la variable target. Divide el valor de la
característica target entre 1000000.

Inicializa un modelo de regresión lineal y entrénalo. Calcula el valor de la
métrica RECM en el conjunto de validación y almacénalo en la variable result.
"""

features = df.drop(['last_price'], axis=1) # extrae las características
target = df['last_price'] / 1000000 # extrae los objetivos

# segmenta el 25% de los datos para hacer el conjunto de validación
features_train, features_valid, target_train, target_valid = train_test_split(
    features, target, test_size=0.25, random_state=12345)

# se inicializa el constructor de modelos
model = LinearRegression()
# se entrena el modelo en el conjunto de entrenamiento
model.fit(features_train, target_train)
# se obtiene las predicciones del modelo en el conjunto de validación
predictions_valid = model.predict(features_valid)

# se calcula la RECM en el conjunto de validación
result = mean_squared_error(target_valid, predictions_valid) ** 0.5
print("RECM del modelo de regresión lineal en el conjunto de validación:", result)
print()
