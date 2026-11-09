# Sprint 11 — Prácticas de aprendizaje supervisado.
# Las variables llevan sufijos por etapa/modelo para evitar sobrescrituras
# accidentales al ejecutar todos los ejercicios en un mismo script.
# Los ejemplos de clases 0/1 utilizan sufijo _example.
# El modelo constante conserva la evaluación del dataset completo

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import (
    LinearRegression,
    LogisticRegression
)
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
    r2_score
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle


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
Carga los datos de travel_insurance_us.csv a la variable data. Muestra en la pantalla
los primeros diez elementos. Mira los datos.
"""

data_raw = read_file('travel_insurance_us.csv',
                keep_default_na=False
                )

print(data_raw.head(10))
print(data_raw.info())
print()

"""
Divide los datos en dos conjuntos:
 - conjunto de entrenamiento (train)
 - conjunto de validación (valid) — 25% de los datos de origen

Especifica random_state=12345. Declara cuatro variables y almacena las características y
el objetivo de la siguiente manera:
 - características: features_train, features_valid
 - objetivo: target_train, target_valid

Muestra en pantalla los tamaños de las tablas almacenadas en las variables:
features_train y features_valid.
"""

features_raw = data_raw.drop('Claim', axis=1)
target_raw = data_raw['Claim']

(
    features_train_raw,
    features_valid_raw,
    target_train_raw,
    target_valid_raw,
) = train_test_split(
    features_raw,
    target_raw,
    test_size=0.25,
    random_state=12345,
)

print(features_train_raw.shape)
print(features_valid_raw.shape)
print()



"""
Entrenamiento de pilotos

Verifica los tipos de características almacenadas en la tabla. Muéstralos. Luego muestra
en pantalla los primeros cinco valores de la columna Gender
"""

print(data_raw.dtypes)
print()
print(data_raw['Gender'].head())
print()

"""
Podemos mirar los valores de la columna Gender usando OHE. Llama a pd.get_dummies() y
muestra en pantalla las primeras cinco filas de la tabla transformada.
"""

print(pd.get_dummies(data_raw['Gender'], dtype=int).head())
print()



"""
Programa la variable Gender con OHE. Llama a pd.get_dummies() con el argumento
drop_first para evitar la trampa dummy. Muestra en pantalla las primeras cinco filas de
la tabla
modificada.
"""

gender = pd.get_dummies(data_raw['Gender'], drop_first=True, dtype=int)
print(gender.head())
print()



"""
Programa todo el DataFrame con One-Hot. Llama a pd.get_dummies() con el argumento
drop_first. Almacena la tabla en la variable data_ohe.

Muestra en pantalla las primeras tres filas de la tabla resultante.
"""

data_ohe = pd.get_dummies(data_raw, drop_first=True)

print((data_ohe).head(3))
print()



"""
Divide los datos de origen en dos conjuntos utilizando la proporción de 75:25 (%):
 - entrenamiento (train)
 - validación (valid)

Declara cuatro variables y almacena las características y el objetivo de la siguiente
manera:
 - características: features_train, features_valid
 - objetivo: target_train, target_valid

Vas a dominar una forma alternativa de usar la función train_test_split(): puede tomar
dos variables (características y objetivo). Consulta la documentación de este método en
particular.

Entrena una regresión logística. Muestra en pantalla el texto "¡Entrenado!" (ya en
precódigo) para asegurarte de que el código terminó de ejecutarse sin problemas.

Especifica random_state=12345 tanto para la división de datos como para el entrenamiento
del modelo.

Al entrenar una regresión logística, es posible que encuentres una advertencia de
sklearn.
Esta no te impedirá pasar la tarea, pero si no te gusta ver un montón de código en rojo
en tu pantalla, especifica el argumento solver='liblinear'; librería linear:

model = LogisticRegression(solver='liblinear')
"""

target_ohe = data_ohe['Claim']
features_ohe = data_ohe.drop('Claim', axis=1)

(
    features_train_ohe,
    features_valid_ohe,
    target_train_ohe,
    target_valid_ohe,
) = train_test_split(
    features_ohe,
    target_ohe,
    test_size=0.25,
    random_state=12345,
)

model_logistic_ohe = LogisticRegression(
    solver='liblinear', random_state=12345
)

model_logistic_ohe.fit(features_train_ohe, target_train_ohe)

print('¡Entrenado!')
print()



"""
Transforma las funciones utilizando codificación de etiquetas. Importa OrdinalEncoder
desde el módulo sklearn.preprocessing.

Almacena el resultado en la variable data_ordinal. Utiliza el constructor DataFrame().

Muestra en pantalla las primeras cinco filas.
"""

encoder = OrdinalEncoder()
encoder.fit(data_raw)
data_ordinal = pd.DataFrame(
    encoder.transform(data_raw),
    columns=data_raw.columns
)

print(data_ordinal.head())
print()



"""
Utiliza los datos transformados para entrenar un árbol de decisión. Muestra en pantalla
el texto "¡Entrenado!" (en precódigo) para asegurarte de que el código completó su
ejecución.
"""

target_ordinal = data_ordinal['Claim']
features_ordinal = data_ordinal.drop('Claim', axis=1)
(
    features_train_ordinal,
    features_valid_ordinal,
    target_train_ordinal,
    target_valid_ordinal,
) = train_test_split(
    features_ordinal,
    target_ordinal,
    test_size=0.25,
    random_state=12345,
)

model_tree_ordinal = DecisionTreeClassifier(random_state=12345)
model_tree_ordinal.fit(features_train_ordinal, target_train_ordinal)

print('¡Entrenado!')
print()



"""
Estandariza las características numéricas. Importa StandardScaler desde el módulo
sklearn.preprocessing.

Crea una instancia de la clase StandardScaler() y ajústala usando los datos de
entrenamiento. (La variable numeric ya contiene la lista de todas las características
numéricas).

Almacena los conjuntos de entrenamiento y validación modificados en variables de la
siguiente manera: features_train y features_valid.

Muestra en pantalla las primeras cinco filas.

Cuando estandarices las funciones, es posible que te encuentres con
SettingWithCopyWarning. Esta no te impedirá pasar la tarea, pero si lo deseas, puedes
silenciarla con la siguiente declaración:
pd.options.mode.chained_assignment = None
"""

numeric = ['Duration', 'Net Sales', 'Commission (in value)', 'Age']

scaler = StandardScaler()

# Aprender los parámetros del conjunto de entrenamiento
scaler.fit(features_train_ordinal[numeric])

# Estandarizar las características numéricas de entrenamiento
features_train_ordinal[numeric] = scaler.transform(
    features_train_ordinal[numeric]
)

# Estandarizar las características numéricas de validación
features_valid_ordinal[numeric] = scaler.transform(
    features_valid_ordinal[numeric]
)

# Mostrar las primeras cinco filas
print(features_train_ordinal.head())
print()



"""
Exactitud para el árbol de decisión.

Entrena el modelo de árbol de decisión calculando el valor de exactitud en el
conjunto de validación. Para hacerlo, declara la variable predicted_valid, luego guarda
el resultado
en la variable accuracy_valid.Especifica random_state=12345. Muéstrala en la pantalla.

Se han guardado el conjunto de datos con las funciones preparadas en el archivo
travel_insurance_us_preprocessed.csv.
"""

data_preprocessed = read_file('travel_insurance_us_preprocessed.csv')

target_preprocessed = data_preprocessed['Claim']
features_preprocessed = data_preprocessed.drop('Claim', axis=1)
(
    features_train_preprocessed,
    features_valid_preprocessed,
    target_train_preprocessed,
    target_valid_preprocessed,
) = train_test_split(
    features_preprocessed,
    target_preprocessed,
    test_size=0.25,
    random_state=12345,
)

model_tree_baseline = DecisionTreeClassifier(random_state=12345)
model_tree_baseline.fit(features_train_preprocessed, target_train_preprocessed)

predicted_tree_baseline = model_tree_baseline.predict(
    features_valid_preprocessed
)

accuracy_tree_baseline = accuracy_score(
    target_valid_preprocessed,
    predicted_tree_baseline,
)

print(accuracy_tree_baseline)
print()



"""
Prueba de consistencia

Para contar clases en la característica objetivo, utiliza el método value_counts(). Haz
las frecuencias relativas (de 0 a 1). La documentación de Pandas te ayudará a hacerlo.

Guarda los valores en la variable class_frequency. Muéstralos en pantalla

Usa el método plot() con el argumento kind='bar'' para trazar un diagrama.
"""

class_frequency = data_preprocessed['Claim'].value_counts(normalize=True)

print(class_frequency)
class_frequency.plot(kind='bar')
plt.show()
print()



"""
Analiza las frecuencias de clase de las predicciones del árbol de decisión (la variable
predicted_valid).

De manera similar:

Aplica el método value_counts(). Relativiza las frecuencias.
Guarda los valores en la variable class_frequency. Muéstralos en pantalla.
Usa el método plot() con el argumento kind='bar' para trazar un diagrama.
"""

# Calcular las frecuencias relativas de las predicciones
class_frequency = pd.Series(predicted_tree_baseline).value_counts(
    normalize=True
)

# Mostrar las frecuencias
print(class_frequency)

# Graficar las frecuencias
class_frequency.plot(kind='bar')
plt.show()
print()



"""
Crea un modelo constante: predice la clase "0" para cualquier observación. Guarda sus
predicciones en la variable target_pred_constant. Muestra en pantalla el valor de
accuracy.
"""

target_preprocessed = data_preprocessed['Claim']
features_preprocessed = data_preprocessed.drop('Claim', axis=1)

target_pred_constant = pd.Series(0, index=target_preprocessed.index)

accuracy_constant = accuracy_score(target_preprocessed, target_pred_constant)

print(accuracy_constant)
print()



"""
Aquí hay un ejemplo de predicciones frente a respuestas correctas. Cuenta el número de
respuestas VP y muestra el resultado en la pantalla.
"""

target_example = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions_example = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])

true_positives = ((target_example == 1) & (predictions_example == 1)).sum()

print('True Positives:', true_positives)
print()



"""
Cuenta el número de respuestas VN tal como lo hiciste en el ejercicio anterior. Muestra
los resultados en la pantalla.
"""

true_negatives = ((target_example == 0) & (predictions_example == 0)).sum()

print('True Negatives:', true_negatives)
print()



"""
Encuentra el número de respuestas FP de la misma manera que encontraste las respuestas
VN en la tarea anterior. Muestra los resultados en la pantalla.
"""

false_positives = ((target_example == 0) & (predictions_example == 1)).sum()

print('False Positives:', false_positives)
print()



"""
Cuenta el número de respuestas FN. Muestra los resultados en la pantalla.
"""

false_negatives = ((target_example == 1) & (predictions_example == 0)).sum()

print('False Negatives:', false_negatives)
print()



"""
Calcula la matriz de confusión utilizando la función confusion_matrix().  Impórtala
desde el módulo sklearn.metrics. Muestra los resultados en la pantalla.
"""

cm = confusion_matrix(target_example, predictions_example)
print(f"Confusion Matrix:\n", cm)
print()



"""
Calcula una matriz de confusión para el árbol de decisión y llama a la función
confusion_matrix(). Muéstrala en pantalla. Muéstrala en pantalla.
"""

model_tree_metrics = DecisionTreeClassifier(random_state=12345)
model_tree_metrics.fit(features_train_preprocessed, target_train_preprocessed)
predicted_tree_metrics = model_tree_metrics.predict(
    features_valid_preprocessed
)

cm_tree = confusion_matrix(target_valid_preprocessed, predicted_tree_metrics)
print(f"Confusion Matrix:\n", cm_tree)
print()



"""
Recall

En el módulo sklearn.metrics, encuentra la función que se encarga de calcular recall.
Impórtala.

La función toma respuestas y predicciones correctas y devuelve la proporción de
respuestas correctas encontradas por el modelo. Muestra los resultados en la pantalla.
"""

recall = recall_score(target_valid_preprocessed, predicted_tree_metrics)
print(f"Recall: {recall}")
print()



"""
Precisión

En el módulo sklearn.metrics, encuentra la función que calcula la precisión. Impórtala.

Esta función toma respuestas y predicciones correctas. Devuelve observaciones marcadas
como positivas por el modelo que en realidad son positivas. Muestra los resultados en la
pantalla.
"""

precision = precision_score(target_valid_preprocessed, predicted_tree_metrics)
print(f"Precision: {precision}")
print()



"""
Valor F1

Calcula lo siguiente:
 - precisión, usando la función precision_score()
 - recall, usando la función recall_score()
 - Valor F1, utilizando la fórmula de la lección.

Asigna los valores de las métricas a las variables precision, recall y f1.

Finalmente, muéstralos en pantalla.
"""

target_example = pd.Series([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])
predictions_example = pd.Series([1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1])

precision = precision_score(target_example, predictions_example)
recall = recall_score(target_example, predictions_example)
f1 = f1_score(target_example, predictions_example)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1: {f1}")
print()



"""
Utiliza la función que calcula el valor F1.

Esta función toma las respuestas y predicciones correctas y devuelve la media armónica
de recall y precisión. Muestra los resultados en la pantalla.
"""

target_preprocessed = data_preprocessed['Claim']
features_preprocessed = data_preprocessed.drop('Claim', axis=1)
(
    features_train_preprocessed,
    features_valid_preprocessed,
    target_train_preprocessed,
    target_valid_preprocessed,
) = train_test_split(
    features_preprocessed,
    target_preprocessed,
    test_size=0.25,
    random_state=12345,
)

model_tree_f1 = DecisionTreeClassifier(random_state=12345)
model_tree_f1.fit(features_train_preprocessed, target_train_preprocessed)
predicted_tree_f1 = model_tree_f1.predict(features_valid_preprocessed)

f1 = f1_score(target_valid_preprocessed, predicted_tree_f1)
print(f"F1: {f1}")
print()



"""
Ajuste de peso de clase

Aquí hay un código de entrenamiento para un modelo de regresión logística con clases
igualmente ponderadas de las lecciones anteriores. Equilibra los pesos de clase
pasando el
valor de argumento adecuado para class_weight. Observa cómo cambia el valor F1.
"""

for weight in [None, 'balanced']:
    model_logistic_weighted = LogisticRegression(
        random_state=12345,
        solver='liblinear',
        class_weight=weight
    )

    model_logistic_weighted.fit(
        features_train_preprocessed,
        target_train_preprocessed,
    )

    predicted_logistic_weighted = model_logistic_weighted.predict(
        features_valid_preprocessed
    )

    print(
        f"Class weight: {weight}, "
        f"F1: {f1_score(
            target_valid_preprocessed,
            predicted_logistic_weighted,
        ):.4f}"
    )
print()



"""
Sobremuestreo

Hemos dividido los datos en datos de entrenamiento y datos de prueba. Tu tarea
consistirá en dividir el dataset de entrenamiento en cuatro variables del siguiente
modo:
 - features_zeros — características de las observaciones de la respuesta "0"
 - features_ones — características de las observaciones de la respuesta "1"
 - target_zeros — objetivo de las observaciones de la respuesta "0"
 - target_ones — objetivo de las observaciones de la respuesta "1"

Muestra en la pantalla los tamaños de las cuatro tablas almacenadas en las variables.
"""

features_zeros = features_train_preprocessed[target_train_preprocessed == 0]
features_ones = features_train_preprocessed[target_train_preprocessed == 1]
target_zeros = target_train_preprocessed[target_train_preprocessed == 0]
target_ones = target_train_preprocessed[target_train_preprocessed == 1]

print(features_zeros.shape)
print(features_ones.shape)
print(target_zeros.shape)
print(target_ones.shape)
print()



"""
Se pueden duplicar observaciones "n" número de veces utilizando la sintaxis de
multiplicación de listas de Python. Para repetir los elementos de la lista, la lista se
multiplica por un número entero (el número requerido de repeticiones). Aquí tienes un
ejemplo:

 | answers = [0, 1, 0]
 | print(answers)
 | answers_x3 = answers * 3
 | print(answers_x3)

 | [0, 1, 0]
 | [0, 1, 0, 0, 1, 0, 0, 1, 0]

Tu tarea es abordar el desequilibrio de clases al:
 1. Identicar la clase subrepresentada (clase positiva).
  2. Duplicar estas observaciones de clase positivas. El número de repeticiones se
     almacena en la variable repeat.
  3. Combinar las observaciones de clase positivas duplicadas con las observaciones de
     clase negativas.
 4. Utiliza la función pd.concat() para realizar esta combinación.
  5. Consultar la documentación de pd.concat() para conocer los detalles sobre cómo
     utilizar la función.
 6. Almacenar las características combinadas en la variable features_upsampled.
  7. Repetir el proceso de duplicación para el objetivo y almacena el resultado en la
     variable target_upsampled.
 8. Muestra los tamaños de las nuevas variables.
"""

n_repeats = 10

features_upsampled = pd.concat(
    [features_zeros] + [features_ones] * n_repeats
)
target_upsampled = pd.concat(
    [target_zeros] + [target_ones] * n_repeats
)

print(features_upsampled.shape)
print(target_upsampled.shape)
print()



"""
Utilizaremos lo que hemos programado en los ejercicios anteriores y lo implementaremos
dentro de la función upsample(). La función tiene que:
 1. Manejar tres parámetros: features, target y repeat .
  2.Dividir features y target en dataframes/series para la clase 0 y la clase 1.
     (Ejercicio 1)
 3. Duplicar: Repetir los datos de la clase 1 repeat veces (Ejercicio 2).
  4. Concatenar: Combinar los datos de la clase 0 con los datos repetidos de la clase 1
     utilizando pd.concat() (Ejercicio 2).
 5. Mezclar los datos combinados con shuffle() con un random_state de tu elección.
 6. Devolver las características mezcladas y el objetivo.

Por último, llamarás a la función de los datos entrenados y mostrarás los tamaños de las
muestras.
"""

def upsample(features, target, repeat):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_upsampled = pd.concat(
        [features_zeros] + [features_ones] * repeat
    )

    target_upsampled = pd.concat(
        [target_zeros] + [target_ones] * repeat
    )
    features_upsampled, target_upsampled = shuffle(
        features_upsampled,
        target_upsampled,
        random_state=12345
    )
    return features_upsampled, target_upsampled

features_upsampled, target_upsampled = upsample(
    features_train_preprocessed, target_train_preprocessed, 10
)

print(features_upsampled.shape)
print(target_upsampled.shape)
print()



"""
Entrena el modelo LogisticRegression con los nuevos datos. Encuentra el valor F1 y
muéstralo en la pantalla
"""

model_logistic_upsampled = LogisticRegression(
    solver='liblinear', random_state=12345
)
model_logistic_upsampled.fit(features_upsampled, target_upsampled)
predicted_logistic_upsampled = model_logistic_upsampled.predict(
    features_valid_preprocessed
)

print('F1:', f1_score(target_valid_preprocessed, predicted_logistic_upsampled))
print()



"""
Submuestreo

Para realizar el submuestreo, escribe una función downsample() y pásale tres argumentos:
 - features
 - target
 - fraction (fracción de observaciones negativas a mantener)

La función debe realizar el submuestreo y devolver tanto las características
modificadas como las etiquetas. Antes de devolver estos datos, asegúrate de mezclarlos
para evitar sesgos en el proceso de aprendizaje del modelo.

Llama a la función para los datos de entrenamiento con una fracción de 0.1. Muestra
en la pantalla los tamaños de las muestras.
"""

def downsample(features, target, fraction):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_downsampled = pd.concat([
        features_zeros.sample(
            frac=fraction,
            random_state=12345),
        features_ones
    ])
    target_downsampled = pd.concat([
        target_zeros.sample(
            frac=fraction,
            random_state=12345),
        target_ones
    ])
    features_downsampled, target_downsampled = shuffle(
    features_downsampled,
    target_downsampled,
    random_state=12345
    )

    return features_downsampled, target_downsampled


features_downsampled, target_downsampled = downsample(
    features_train_preprocessed, target_train_preprocessed, 0.1
)

print(features_downsampled.shape)
print(target_downsampled.shape)
print()



"""
Entrena el modelo LogisticRegression con los nuevos datos. Encuentra el valor F1 y
muéstralo en la pantalla
"""

model_logistic_downsampled = LogisticRegression(
    solver='liblinear', random_state=12345
)
model_logistic_downsampled.fit(features_downsampled, target_downsampled)
predicted_logistic_downsampled = model_logistic_downsampled.predict(
    features_valid_preprocessed
)

print(
    'F1:',
    f1_score(target_valid_preprocessed, predicted_logistic_downsampled),
)
print()



"""
Ajuste de umbral

Encuentra las probabilidades de clase para la muestra de validación. Almacena los
valores para las probabilidades de clase "1" en la variable probabilities_one_valid.
Muestra en la pantalla los primeros cinco elementos de la variable.
"""

target_preprocessed = data_preprocessed['Claim']
features_preprocessed = data_preprocessed.drop('Claim', axis=1)
(
    features_train_preprocessed,
    features_valid_preprocessed,
    target_train_preprocessed,
    target_valid_preprocessed,
) = train_test_split(
    features_preprocessed,
    target_preprocessed,
    test_size=0.25,
    random_state=12345,
)

model_logistic_probabilities = LogisticRegression(
    random_state=12345,
    solver='liblinear',
)
model_logistic_probabilities.fit(
    features_train_preprocessed,
    target_train_preprocessed,
)

probabilities_valid_baseline = model_logistic_probabilities.predict_proba(
    features_valid_preprocessed
)
probabilities_one_valid_baseline = probabilities_valid_baseline[:, 1]

print(probabilities_one_valid_baseline[:5])
print()



"""
Pasa por los valores de umbral de 0 a 0.3 en intervalos de 0.02. Encuentra precisión y
recall para cada valor del umbral. Muestra en pantalla los resultados.

Para crear un bucle con el rango deseado, usamos la función arange() de la librería
numpy.
Al igual que la función range(), ésta itera sobre los elementos especificados del rango,
pero es diferente porque funciona con números fraccionarios además de enteros.

Más adelante aprenderemos más sobre las herramientas de la librería numpy.
"""

target_preprocessed = data_preprocessed['Claim']
features_preprocessed = data_preprocessed.drop('Claim', axis=1)
(
    features_train_preprocessed,
    features_valid_preprocessed,
    target_train_preprocessed,
    target_valid_preprocessed,
) = train_test_split(
    features_preprocessed,
    target_preprocessed,
    test_size=0.25,
    random_state=12345,
)

model_logistic_threshold = LogisticRegression(
    random_state=12345,
    solver='liblinear',
)
model_logistic_threshold.fit(
    features_train_preprocessed,
    target_train_preprocessed,
)

probabilities_valid_threshold = model_logistic_threshold.predict_proba(
    features_valid_preprocessed
)
probabilities_one_valid_threshold = probabilities_valid_threshold[:, 1]

for threshold in np.arange(0, 0.3, 0.02):
    predicted_valid_threshold = (
        probabilities_one_valid_threshold >= threshold
    ).astype(int)

    precision = precision_score(
        target_valid_preprocessed,
        predicted_valid_threshold,
    )
    recall = recall_score(
        target_valid_preprocessed,
        predicted_valid_threshold,
    )

    print(
        'Threshold = {:.2f} | Precision = {:.3f}, Recall = {:.3f}'.format(
            threshold, precision, recall
        )
    )
print()

"""
Curva ROC

Haz una curva ROC para la regresión logística y trázala en la gráfica.
"""

fpr, tpr, thresholds = roc_curve(
    target_valid_preprocessed,
    probabilities_one_valid_threshold,
)

plt.figure()

# Dibujar la curva ROC
plt.plot(fpr, tpr)

# Línea de referencia del modelo aleatorio
plt.plot([0, 1], [0, 1], linestyle='--')

# Establecer los límites de los ejes
plt.xlim(0, 1)
plt.ylim(0, 1)

# Nombrar los ejes
plt.xlabel('Tasa de falsos positivos')
plt.ylabel('Tasa de verdaderos positivos')

# Agregar el título
plt.title('Curva ROC')

# Mostrar la gráfica
plt.show()



"""
Calcula el AUC-ROC para la regresión logística. Encuentra la función adecuada en la
documentación de sklearn, así como la descripción de cómo funciona. Importa la función.
Muestra en la pantalla el valor AUC-ROC.
"""

auc_roc = roc_auc_score(
    target_valid_preprocessed,
    probabilities_one_valid_threshold,
)

print('AUC-ROC:', auc_roc)
print()



"""
Carga los datos de flights.csv. Se debe mostrar lo siguiente:

Tamaño de la tabla
Primeras cinco filas de la tabla
Mira los datos.
"""

data_flights = read_file('flights.csv')

print('Flights Shape:', data_flights.shape)
print("Flight first 5 rows\n", data_flights.head())
print()



"""
Codifica la característica categórica utilizando OHE. Estandariza las características
numéricas. Muestra los tamaños de la tabla (en precódigo).

Cuando muestres los resultados en pantalla, no prestes atención al texto en color rojo.
Está bien.
"""

# Codificación One-Hot Encoding
data_flights_ohe = pd.get_dummies(
    data_flights,
    drop_first=True
)

# Separación de características y objetivo
target_flights = data_flights_ohe['Arrival Delay']
features_flights = data_flights_ohe.drop(
    'Arrival Delay',
    axis=1
)

# División en entrenamiento y validación
features_train_flights, features_valid_flights, \
target_train_flights, target_valid_flights = train_test_split(
    features_flights,
    target_flights,
    test_size=0.25,
    random_state=12345
)

# Características numéricas
numeric_flights = [
    'Day',
    'Day Of Week',
    'Origin Airport Delay Rate',
    'Destination Airport Delay Rate',
    'Scheduled Time',
    'Distance',
    'Scheduled Departure Hour',
    'Scheduled Departure Minute'
]

# Estandarización
scaler_flights = StandardScaler()

scaler_flights.fit(features_train_flights[numeric_flights])

features_train_flights[numeric_flights] = scaler_flights.transform(
    features_train_flights[numeric_flights]
)

features_valid_flights[numeric_flights] = scaler_flights.transform(
    features_valid_flights[numeric_flights]
)

# Resultados
print('Features Tain Shape:', features_train_flights.shape)
print('Features Valid Shape:', features_valid_flights.shape)
print()



"""
EMC en una tarea de regresión

Carga los datos de flights_preprocessed.csv. Genera y almacena las predicciones de ambos
modelos sobre el conjunto de validación.

Entrena un modelo de regresión lineal y calcula su ECM y RECM sobre el conjunto de
validación.

Después, crea un modelo constante que prediga para todas las observaciones de validación
el valor medio de `target_train`. Calcula también su ECM y RECM.

Muestra los resultados de ambos modelos para comparar su desempeño y determinar si la
regresión lineal supera al modelo constante.
"""

data_flights_preprocessed = read_file('flights_preprocessed.csv')

target_flights_preprocessed = data_flights_preprocessed['Arrival Delay']
features_flights_preprocessed = data_flights_preprocessed.drop(
    'Arrival Delay',
    axis=1
)

(
    features_train_flights_preprocessed,
    features_valid_flights_preprocessed,
    target_train_flights_preprocessed,
    target_valid_flights_preprocessed
) = train_test_split(
    features_flights_preprocessed,
    target_flights_preprocessed,
    test_size=0.25,
    random_state=12345
)

model_linear_flights = LinearRegression()
model_linear_flights.fit(
    features_train_flights_preprocessed,
    target_train_flights_preprocessed
)

predicted_valid_linear_flights = model_linear_flights.predict(
    features_valid_flights_preprocessed
)

mse_linear_flights = mean_squared_error(
    target_valid_flights_preprocessed,
    predicted_valid_linear_flights
)

print('Linear Regression')
print("MSE =", mse_linear_flights)
print("RMSE =", mse_linear_flights ** 0.5)
print()

mean_target_flights = target_train_flights_preprocessed.mean()

predicted_valid_mean_flights = (
    [mean_target_flights] * len(target_valid_flights_preprocessed)
)

mse_mean_flights = mean_squared_error(
    target_valid_flights_preprocessed,
    predicted_valid_mean_flights
)

print('Mean')
print('MSE =', mse_mean_flights)
print('RMSE =', mse_mean_flights ** 0.5)
print()

print(
    'RMSE Difference:',
    mse_mean_flights ** 0.5 - mse_linear_flights ** 0.5
)
print()



"""
Coeficiente de dererminación

Calcula el valor R2 para la regresión lineal. Busca la función adecuada en la
documentación de sklearn.metrics.  Impórtala.

Muestra el resultado
"""

r2_linear_flights = r2_score(
    target_valid_flights_preprocessed,
    predicted_valid_linear_flights
)

print('R2 =', r2_linear_flights)
print()



"""
Maximización de R2

Entrena un modelo `RandomForestRegressor` con el dataset `flights_preprocessed.csv`, sin
escalar las características.

Evalúa profundidades de 1 a 15 utilizando 20 árboles y selecciona la que obtenga el
mayor R² en validación.

Entrena el modelo final con 100 árboles y la profundidad seleccionada. Muestra los
valores R² de entrenamiento y validación, buscando alcanzar al menos 0.14 en validación.
"""

# Buscar la mejor profundidad del bosque aleatorio
best_r2_flights = float('-inf')
best_depth_flights = None

for depth in range(1, 16):
    model_candidate_flights = RandomForestRegressor(
        n_estimators=20,
        max_depth=depth,
        random_state=12345
    )

    model_candidate_flights.fit(
        features_train_flights_preprocessed,
        target_train_flights_preprocessed
    )

    r2_valid_flights = model_candidate_flights.score(
        features_valid_flights_preprocessed,
        target_valid_flights_preprocessed
    )

    if r2_valid_flights > best_r2_flights:
        best_r2_flights = r2_valid_flights
        best_depth_flights = depth

# Entrenar el modelo final con la mejor profundidad encontrada
model_forest_flights = RandomForestRegressor(
    n_estimators=100,
    max_depth=best_depth_flights,
    random_state=12345
)

model_forest_flights.fit(
    features_train_flights_preprocessed,
    target_train_flights_preprocessed
)

# Mostrar resultados
print("Mejor profundidad encontrada:", best_depth_flights)
print("Configuración del modelo actual lograda:")
print(
    "Valor R2 en un conjunto de entrenamiento",
    model_forest_flights.score(
        features_train_flights_preprocessed,
        target_train_flights_preprocessed
    )
)
print(
    "Valor R2 en un conjunto de validación:",
    model_forest_flights.score(
        features_valid_flights_preprocessed,
        target_valid_flights_preprocessed
    )
)
print()



"""
Error absoluto medio

Codifica la función mae() según la fórmula. Esta función las respuestas y predicciones
correctas y devuelve el valor de error absoluto medio.

Considera que en Python el valor absoluto se calcula usando la función abs().

Prueba la función en el ejemplo. Muestra el resultado en la pantalla.
"""

def mae(target, predictions):
    differences = target - predictions
    absolute_errors = differences.abs()
    return absolute_errors.mean()


target_mae_example = pd.Series([-0.5, 2.1, 1.5, 0.3])
predictions_mae_example = pd.Series([-0.6, 1.7, 1.6, 0.2])

print('MAE:', mae(target_mae_example, predictions_mae_example))
print()



"""
Calcula EAM para la regresión lineal. Encuentra la función apropiada en la documentación
de sklearn. Impórtala. Muéstrala en la pantalla.
"""

mae_linear_flights = mean_absolute_error(
    target_valid_flights_preprocessed,
    predicted_valid_linear_flights
)

print('MAE Linear Regression =\n', mae_linear_flights)
print()



"""
Interpretación de EAM

Calcula el EAM utilizando la mediana como valor constante. El cálculo EAM para la
regresión lineal se encuentra en el precódigo. Compara los valores.

Muestra el resultado en la pantalla.
"""

median_target_flights = target_train_flights_preprocessed.median()

predicted_valid_median_flights = (
    [median_target_flights] * len(target_valid_flights_preprocessed)
)

mae_median_flights = mean_absolute_error(
    target_valid_flights_preprocessed,
    predicted_valid_median_flights
)

print('MAE Median =\n', mae_median_flights)
print()



"""
Minimizción de EAM

Construye un modelo con un valor EAM menor o igual a 26.2.

En la quinta lección de este capítulo ya aprendimos que RandomForestRegressor es una
buena alternativa para la regresión lineal. Emplea la configuración de modelo que usaste
en la lección 5 y verifica a cuál EAM puede llevar.
"""

# Calcular las predicciones del bosque aleatorio
predicted_train_forest_flights = model_forest_flights.predict(
    features_train_flights_preprocessed
)

predicted_valid_forest_flights = model_forest_flights.predict(
    features_valid_flights_preprocessed
)

# Calcular el EAM en entrenamiento y validación
mae_train_forest_flights = mean_absolute_error(
    target_train_flights_preprocessed,
    predicted_train_forest_flights
)

mae_valid_forest_flights = mean_absolute_error(
    target_valid_flights_preprocessed,
    predicted_valid_forest_flights
)

# Mostrar los resultados
print("Configuración del modelo actual lograda:")
print(
    "Valor EAM en un conjunto de entrenamiento:",
    mae_train_forest_flights
)
print(
    "Valor EAM en un conjunto de validación:",
    mae_valid_forest_flights
)
print()



