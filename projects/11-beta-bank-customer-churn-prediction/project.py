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
Sprint 11 — Aprendizaje supervisado
Proyecto: Predicción de abandono de clientes — Beta Bank

1. Introducción

Beta Bank ha identificado que algunos de sus clientes están abandonando
la institución. Dado que conservar a los clientes actuales resulta más
económico que captar nuevos, el banco busca anticipar qué clientes
tienen mayor probabilidad de abandonar sus servicios para facilitar la
implementación de estrategias de retención.

El objetivo de este proyecto es **desarrollar un modelo de clasificación
que permita predecir el abandono de clientes**, utilizando información
histórica sobre sus características y comportamiento. La variable
objetivo será `Exited`, que indica si un cliente abandonó el banco (1) o
permaneció en él (0).

Para desarrollar el modelo, seguiremos las siguientes etapas:

1. **Exploración y preparación de los datos:** examinaremos la
   estructura y calidad del conjunto de datos, identificaremos posibles
   problemas y realizaremos las transformaciones necesarias para el
   entrenamiento.
2. **Análisis del equilibrio de clases:** estudiaremos la distribución
   de la variable objetivo y entrenaremos modelos iniciales sin aplicar
   técnicas para corregir un posible desequilibrio.
3. **Mejora y comparación de modelos:** aplicaremos al menos dos
   estrategias para tratar el desequilibrio de clases y compararemos
   diferentes modelos e hiperparámetros utilizando conjuntos de
   entrenamiento y validación.
4. **Evaluación final:** seleccionaremos el mejor modelo y evaluaremos
   su desempeño sobre un conjunto de prueba independiente, utilizando
   las métricas F1 y AUC-ROC.

El principal criterio de éxito será **alcanzar un valor F1 de al menos
0.59 en el conjunto de prueba**, buscando obtener el mejor desempeño
posible. Adicionalmente, analizaremos la métrica AUC-ROC para
complementar la evaluación de la capacidad del modelo para distinguir
entre clientes que abandonan el banco y aquellos que permanecen.
"""


"""
2. Importaciones

Para desarrollar el proyecto utilizaremos bibliotecas de Python que nos
permitirán cargar, explorar y preparar los datos, así como entrenar y
evaluar diferentes modelos de clasificación.

Las importaciones se organizarán siguiendo las recomendaciones de PEP 8,
agrupando las herramientas necesarias para el procesamiento de datos, la
construcción de modelos de Machine Learning y la evaluación de su
desempeño mediante las métricas F1 y AUC-ROC.

Centralizaremos las importaciones en esta sección para mantener el
código ordenado, facilitar su mantenimiento y evitar duplicaciones a lo
largo del notebook.
"""



import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


"""
3. Carga y exploración inicial de los datos

En esta sección cargaremos el conjunto de datos de Beta Bank, disponible
en el archivo `/datasets/Churn.csv`, y realizaremos una exploración
inicial para conocer su estructura, contenido y calidad.

Examinaremos las dimensiones del dataset, los tipos de datos y las
estadísticas descriptivas de sus variables. También identificaremos
posibles valores ausentes, registros duplicados y valores anómalos que
pudieran afectar el entrenamiento de los modelos.

Esta revisión nos permitirá comprender las características disponibles y
determinar qué operaciones de limpieza y preparación serán necesarias
antes de desarrollar los modelos de clasificación.

3.1. Carga del conjunto de datos

Comenzaremos leyendo el archivo CSV y visualizando sus primeras filas
para comprobar que los datos se hayan cargado correctamente e
identificar las columnas que contiene.
"""



# Cargar el conjunto de datos de Beta Bank.
data = read_file('Churn.csv')

# Mostrar las primeras cinco filas.
data.head()


"""
3.2. Dimensiones, estructura y tipos de datos

Después de comprobar la carga del archivo, examinaremos las dimensiones
y la estructura del conjunto de datos para conocer el número de
registros y características disponibles.

También revisaremos los tipos de datos asignados a cada columna, lo que
nos permitirá identificar las variables numéricas y categóricas, así
como posibles inconsistencias que debamos considerar durante el
preprocesamiento.

Esta revisión proporcionará una primera referencia sobre la calidad y
organización del dataset antes de investigar los valores ausentes,
duplicados y otras posibles anomalías.
"""



# Mostrar las dimensiones del conjunto de datos.
print('Dimensiones del DataFrame:', data.shape)

# Examinar la estructura y los tipos de datos.
data.info()


"""
**Resultados de la inspección estructural**

El conjunto de datos contiene 10,000 registros y 14 columnas, incluida
la variable objetivo `Exited`. Se identificaron ocho columnas de tipo
entero, tres de tipo decimal y tres de tipo objeto.

La revisión reveló que `Tenure` contiene 909 valores ausentes,
equivalentes al 9.09 % de los registros. Las demás columnas no presentan
valores nulos.

Estos resultados indican que será necesario investigar los valores
ausentes de `Tenure` y evaluar las transformaciones de las variables
categóricas antes del entrenamiento. Por el momento, conservaremos los
datos originales hasta determinar el tratamiento más adecuado.

3.3. Análisis de valores ausentes y duplicados

A continuación, cuantificaremos los valores ausentes por columna y
verificaremos si existen registros duplicados.

Esta comprobación permitirá confirmar los problemas de calidad
identificados durante la inspección estructural y detectar posibles
duplicaciones que pudieran afectar el análisis y el entrenamiento de los
modelos.
"""



# Contar los valores ausentes por columna.
print('Valores ausentes por columna:')
print(data.isna().sum())

# Comprobar registros completamente duplicados.
print('\nRegistros duplicados:', data.duplicated().sum())

# Comprobar identificadores de cliente duplicados.
print(
    'CustomerId duplicados:',
    data['CustomerId'].duplicated().sum()
)


"""
**Resultados del análisis de valores ausentes y duplicados**

La revisión confirmó que `Tenure` es la única variable con valores
ausentes, afectando al 9.09 % de los registros. No se identificaron
filas completamente duplicadas ni valores repetidos en `CustomerId`, por
lo que no es necesario eliminar registros por duplicación.

El tratamiento de los valores ausentes de `Tenure` se determinará
después de examinar sus características y distribución. Por ahora,
conservaremos los registros originales para evitar pérdidas de
información innecesarias.

3.4. Estadísticas descriptivas y revisión de valores anómalos

A continuación, examinaremos las estadísticas descriptivas de las
variables numéricas para conocer sus rangos, medidas de tendencia
central y dispersión.

Esta revisión permitirá identificar posibles valores extremos,
inconsistencias o características particulares de los datos que debamos
investigar antes del preprocesamiento.

Prestaremos especial atención a `Tenure`, debido a sus valores ausentes,
y a las variables que podrían influir en la predicción del abandono de
clientes. No consideraremos automáticamente que un valor extremo
representa un error sin analizar primero su significado.
"""



# Mostrar las estadísticas descriptivas de las variables numéricas.
data.describe()


"""
**Resultados del análisis descriptivo**

Las estadísticas descriptivas muestran que las variables numéricas
presentan rangos generalmente plausibles para el contexto bancario. Las
edades oscilan entre 18 y 92 años, mientras que las puntuaciones
crediticias se encuentran entre 350 y 850 puntos. No se identificaron
valores evidentemente imposibles que requieran una corrección inmediata.

La variable `Balance` presenta una proporción importante de saldos
iguales a cero, mientras que `EstimatedSalary` muestra un rango amplio
de valores. Estas características no representan necesariamente errores,
por lo que evitaremos modificar los registros sin evidencia adicional.

En el caso de `Tenure`, los valores disponibles se encuentran entre 0 y
10 años, con una media y una mediana cercanas a 5 años. Sin embargo,
antes de decidir cómo tratar sus valores ausentes, será necesario
examinar su distribución.

Por otra parte, la media de `Exited` indica que el 20.37 % de los
clientes abandonó el banco, lo que sugiere un desequilibrio entre las
clases. Este aspecto se estudiará con mayor detalle durante la
evaluación de los modelos de clasificación.

**Análisis adicional de `Tenure`**

A continuación, examinaremos la frecuencia de los valores de `Tenure`,
incluidos los registros ausentes. Esto nos permitirá comprender mejor su
distribución y evaluar posteriormente las alternativas de tratamiento,
sin modificar todavía el conjunto de datos.
"""



# Contar la frecuencia de cada valor, incluidos los ausentes.
tenure_counts = data['Tenure'].value_counts(
    dropna=False
).sort_index()

# Calcular las frecuencias y los porcentajes.
tenure_distribution = pd.DataFrame({
    'Frecuencia': tenure_counts,
    'Porcentaje (%)': (tenure_counts / len(data) * 100).round(2)
})

tenure_distribution


"""
**Resultados del análisis de `Tenure`**

La distribución de `Tenure` muestra frecuencias relativamente similares
para los períodos comprendidos entre 1 y 9 años, mientras que los
valores extremos de 0 y 10 años presentan una menor representación. No
se observa una concentración marcada en un período específico.

Los 909 valores ausentes representan el 9.09 % del conjunto de datos.
Aunque la media y la mediana se sitúan aproximadamente en 5 años, la
distribución observada no permite determinar por sí sola el tratamiento
más adecuado para estos registros.

Por lo tanto, evaluaremos las alternativas de imputación durante la
preparación de los datos, procurando conservar la información disponible
y evitar fugas de información entre los conjuntos de entrenamiento,
validación y prueba.

**Revisión de las variables categóricas**

Para completar la exploración inicial, examinaremos la distribución de
`Geography` y `Gender`. Esto nos permitirá identificar las categorías
presentes, verificar su consistencia y conocer su representación dentro
del conjunto de datos.

Los resultados servirán como referencia para determinar posteriormente
la codificación apropiada de estas características antes del
entrenamiento de los modelos.
"""



# Examinar las frecuencias de las variables categóricas.
for column in ['Geography', 'Gender']:
    counts = data[column].value_counts(dropna=False)
    percentages = counts / len(data) * 100

    distribution = pd.DataFrame({
        'Frecuencia': counts,
        'Porcentaje (%)': percentages.round(2)
    })

    print(f'\nDistribución de {column}:')
    print(distribution)


"""
3.5. Conclusiones de la exploración inicial

La exploración del conjunto de datos permitió conocer su estructura,
identificar las características disponibles y detectar los principales
aspectos que deberán considerarse antes del entrenamiento de los
modelos.

Los hallazgos más relevantes son los siguientes:

- **Calidad de los datos:** no se encontraron registros completamente
  duplicados ni identificadores de clientes repetidos. La única variable
  con valores ausentes es `Tenure`, cuyo tratamiento deberá justificarse
  durante el preprocesamiento.
- **Variables numéricas:** presentan rangos generalmente plausibles para
  el contexto del proyecto. Algunas características, como los saldos
  bancarios iguales a cero, requieren una interpretación cuidadosa, pero
  no justifican modificaciones automáticas.
- **Variables categóricas:** `Geography` contiene tres países, con una
  mayor representación de Francia, mientras que `Gender` presenta dos
  categorías con proporciones relativamente equilibradas. No se
  identificaron inconsistencias aparentes en sus valores.
- **Variable objetivo:** se identificó una menor representación de los
  clientes que abandonaron el banco. Este desequilibrio se investigará
  formalmente antes de entrenar los modelos y evaluar las estrategias
  para mejorar su desempeño.

En conjunto, los datos presentan una estructura adecuada para continuar
con el proyecto, aunque será necesario realizar algunas operaciones de
preparación.

La siguiente etapa se enfocará en seleccionar las características
relevantes, tratar los valores ausentes y transformar las variables
categóricas. Estas decisiones se tomarán considerando las
características de los datos y la necesidad de evitar fugas de
información entre los conjuntos de entrenamiento, validación y prueba.
"""


"""
4. Preparación y preprocesamiento de los datos

Después de explorar el conjunto de datos e identificar sus principales
características, procederemos a preparar la información para el
entrenamiento de los modelos de clasificación.

El objetivo de esta etapa es asegurar que las variables utilizadas sean
pertinentes, que los valores ausentes reciban un tratamiento adecuado y
que las características categóricas puedan ser procesadas por los
algoritmos de Machine Learning.

Para ello, evaluaremos las columnas que deben conservarse como
características predictoras, las alternativas para tratar los valores
ausentes de `Tenure` y la codificación de las variables categóricas.

También consideraremos la prevención de fugas de información (*data
leakage*). Por esta razón, las transformaciones que requieran obtener
parámetros de los datos, como el cálculo de valores para imputación, se
ajustarán utilizando únicamente el conjunto de entrenamiento, después de
realizar la división correspondiente.

4.1. Selección de características relevantes

Comenzaremos examinando las columnas que contienen información
identificadora, como `RowNumber`, `CustomerId` y `Surname`, para
determinar si aportan información útil para predecir el abandono de
clientes.

La selección de características permitirá evitar la incorporación de
variables que no representen características relevantes del
comportamiento de los clientes, conservando aquellas que puedan
contribuir al desempeño predictivo del modelo.
"""



# Examinar la cantidad de valores únicos en las columnas identificadoras.
identifier_columns = ['RowNumber', 'CustomerId', 'Surname']

print('Valores únicos por columna:')
print(data[identifier_columns].nunique())

# Examinar los apellidos más frecuentes.
print('\nLos 10 apellidos más frecuentes:')
print(data['Surname'].value_counts().head(10))


"""
**Resultados del análisis de las columnas identificadoras**

La revisión mostró que `RowNumber` y `CustomerId` contienen 10,000
valores únicos, uno por registro. Ambas columnas cumplen funciones de
identificación y no aportan, por su significado, información
directamente relacionada con las características o el comportamiento
bancario de los clientes.

Por su parte, `Surname` presenta 2,932 valores distintos, lo que
representa una cardinalidad elevada. Su codificación podría incrementar
considerablemente el número de características y la complejidad de los
modelos, con un posible riesgo de sobreajuste.

Por lo tanto, **se excluirán `RowNumber`, `CustomerId` y `Surname` del
conjunto de características predictoras**, ya que no existe una
justificación suficiente para incorporarlas en esta etapa del proyecto.

Conservaremos las demás variables para su preparación posterior,
mientras que `Exited` permanecerá como la variable objetivo del problema
de clasificación.

La exclusión se realizará sobre una copia del conjunto de datos,
conservando el DataFrame original para facilitar futuras comprobaciones.
"""



# Excluir las columnas identificadoras del conjunto de datos.
data_model = data.drop(columns=identifier_columns)

# Verificar las dimensiones de ambos DataFrames.
print('Dimensiones del conjunto original:', data.shape)
print('Dimensiones del conjunto preparado:', data_model.shape)

# Mostrar las primeras cinco filas del conjunto preparado.
data_model.head()


"""
4.2. Tratamiento de valores ausentes

Durante la exploración inicial identificamos 909 valores ausentes en
`Tenure`, equivalentes al 9.09 % de los registros. Esta variable
representa el período de maduración del depósito a plazo fijo del
cliente, expresado en años.

El análisis de su distribución mostró valores comprendidos entre 0 y 10
años, con una media y una mediana cercanas a 5 años y frecuencias
relativamente uniformes entre los períodos intermedios.

Para tratar los valores ausentes, consideraremos alternativas como la
eliminación de registros o la imputación mediante una medida de
tendencia central. Dado que eliminar los registros implicaría perder una
proporción considerable de la información, la imputación mediante la
mediana constituye una opción razonable que evaluaremos para conservar
los datos disponibles.

Sin embargo, para evitar fugas de información (*data leakage*),
cualquier estadístico utilizado para la imputación deberá calcularse
exclusivamente a partir del conjunto de entrenamiento y aplicarse
posteriormente a los conjuntos de validación y prueba.

Por lo tanto, antes de ejecutar la transformación, será necesario
dividir los datos. De esta manera, garantizaremos que la información
reservada para evaluar los modelos no influya en su preparación.
"""


"""
4.3. Codificación de variables categóricas

El conjunto de datos contiene dos características categóricas que
utilizaremos para el entrenamiento: `Geography`, con tres países de
residencia, y `Gender`, con dos categorías.

Dado que los modelos de clasificación seleccionados requieren
características numéricas, transformaremos estas variables mediante
*One-Hot Encoding* (OHE), utilizando la función `pd.get_dummies()` de
pandas.

Esta técnica permite representar las categorías mediante columnas
indicadoras, sin establecer un orden numérico artificial entre ellas.
Utilizaremos el argumento `drop_first=True` para evitar columnas
redundantes, especialmente en modelos como la regresión logística.

Para prevenir fugas de información, realizaremos primero la división de
los datos en conjuntos de entrenamiento, validación y prueba.
Posteriormente, aplicaremos la codificación asegurando que los tres
conjuntos conserven las mismas columnas predictoras.

Esta transformación permitirá incorporar la información categórica al
entrenamiento sin alterar las variables numéricas originales.
"""


"""
5. Preparación de los conjuntos para Machine Learning

Para entrenar y evaluar correctamente los modelos de clasificación,
dividiremos el conjunto de datos en tres subconjuntos independientes:
entrenamiento, validación y prueba.

Cada conjunto tendrá una función específica:

- **Entrenamiento:** se utilizará para que los modelos aprendan las
  relaciones entre las características de los clientes y su abandono del
  banco.
- **Validación:** permitirá comparar modelos, evaluar hiperparámetros y
  seleccionar la configuración con mejor desempeño.
- **Prueba:** se reservará para evaluar el modelo definitivo sobre datos
  que no hayan intervenido en el entrenamiento ni en la selección de
  hiperparámetros.

Debido al desequilibrio identificado en la variable objetivo,
procuraremos conservar proporciones similares de ambas clases en los
tres conjuntos mediante una división estratificada.

Una vez realizada la división, aplicaremos las transformaciones de
preprocesamiento definidas anteriormente, evitando que la información de
validación y prueba influya en los parámetros aprendidos durante la
preparación de los datos.

5.1. Separación de características y variable objetivo

Comenzaremos separando las diez características predictoras de la
variable objetivo `Exited`, utilizando el DataFrame `data_model`, del
que previamente excluimos las columnas identificadoras.

Esta separación permitirá preparar los datos para su posterior división
y entrenamiento, manteniendo claramente diferenciada la información
utilizada para realizar las predicciones de los resultados que buscamos
predecir.
"""



# Separar las características predictoras.
features = data_model.drop(columns=['Exited'])

# Separar la variable objetivo.
target = data_model['Exited']

# Verificar las dimensiones de ambos conjuntos.
print('Dimensiones de features:', features.shape)
print('Dimensiones de target:', target.shape)


"""
5.2. División en conjuntos de entrenamiento, validación y prueba

Para desarrollar y evaluar los modelos de clasificación, dividiremos los
datos en tres conjuntos independientes, utilizando las siguientes
proporciones:

- **Entrenamiento (60 %):** 6,000 registros destinados al aprendizaje de
  los modelos.
- **Validación (20 %):** 2,000 registros que utilizaremos para comparar
  modelos, ajustar hiperparámetros y seleccionar la mejor configuración.
- **Prueba (20 %):** 2,000 registros reservados exclusivamente para
  evaluar el desempeño final del modelo seleccionado.

Esta distribución permite disponer de una cantidad considerable de datos
para el entrenamiento y mantener conjuntos independientes para la
selección y evaluación de los modelos.

Debido al desequilibrio identificado en `Exited`, utilizaremos una
división estratificada mediante el parámetro `stratify`, con el objetivo
de conservar aproximadamente la proporción original de ambas clases en
cada conjunto.

También estableceremos `random_state=12345` para garantizar que la
división pueda reproducirse.

La separación se realizará mediante `train_test_split()` de
scikit-learn, en dos etapas: primero reservaremos el conjunto de prueba
y después dividiremos los datos restantes en entrenamiento y validación.

Una vez completada la división, verificaremos las dimensiones de los
conjuntos y la distribución de sus clases antes de continuar con las
transformaciones de preprocesamiento.
"""



# Separar el 20 % de los datos para el conjunto de prueba.
(
    features_train_valid,
    features_test,
    target_train_valid,
    target_test
) = train_test_split(
    features,
    target,
    test_size=0.20,
    random_state=12345,
    stratify=target
)

# Separar el 25 % de los datos restantes para validación.
(
    features_train,
    features_valid,
    target_train,
    target_valid
) = train_test_split(
    features_train_valid,
    target_train_valid,
    test_size=0.25,
    random_state=12345,
    stratify=target_train_valid
)

# Verificar las dimensiones de los conjuntos.
print('Conjunto de entrenamiento:')
print('Features:', features_train.shape)
print('Target:', target_train.shape)

print('\nConjunto de validación:')
print('Features:', features_valid.shape)
print('Target:', target_valid.shape)

print('\nConjunto de prueba:')
print('Features:', features_test.shape)
print('Target:', target_test.shape)


"""
5.3. Verificación de los conjuntos y distribución de clases

La división generó tres conjuntos con las proporciones previstas: 60 %
para entrenamiento, 20 % para validación y 20 % para prueba. Se
conservaron los 10,000 registros originales y las diez características
predictoras.

Para comprobar que la estratificación se realizó correctamente,
examinaremos la distribución de la variable objetivo `Exited` en cada
conjunto y la compararemos con la distribución original.

Esta verificación permitirá confirmar que los conjuntos mantienen
proporciones similares de clientes que abandonaron el banco y de
aquellos que permanecieron, evitando diferencias importantes en su
composición.

También servirá como referencia para el posterior análisis del
desequilibrio de clases y la comparación de los modelos de
clasificación.

Una vez comprobada la división, retomaremos las transformaciones de
preprocesamiento pendientes, utilizando exclusivamente los datos de
entrenamiento para calcular los parámetros necesarios y evitando fugas
de información hacia los conjuntos de validación y prueba.
"""



# Comparar la distribución de clases entre los conjuntos.
class_distribution = pd.DataFrame({
    'Original': target.value_counts(normalize=True),
    'Entrenamiento': target_train.value_counts(normalize=True),
    'Validación': target_valid.value_counts(normalize=True),
    'Prueba': target_test.value_counts(normalize=True)
})

# Convertir las proporciones a porcentajes.
class_distribution = (class_distribution * 100).round(2)

# Ordenar las clases e identificar la variable objetivo.
class_distribution.index.name = 'Exited'
class_distribution.sort_index()


"""
**Resultados de la verificación de la división estratificada**

La distribución de `Exited` se mantuvo prácticamente constante en los
tres conjuntos. La clase mayoritaria, correspondiente a los clientes que
permanecieron en el banco, representa aproximadamente el 79.6 % de los
registros, mientras que la clase minoritaria concentra el 20.4 %
restante.

Las diferencias respecto a la distribución original son mínimas, por lo
que podemos considerar que la estratificación se realizó correctamente.

Esta comprobación confirma que los conjuntos conservan una composición
comparable respecto a la variable objetivo. El desequilibrio de clases
se estudiará posteriormente, sin modificar las distribuciones de
validación y prueba.

5.4. Aplicación del preprocesamiento a los conjuntos

Una vez realizada y verificada la división de los datos, retomaremos las
transformaciones identificadas durante la exploración inicial.

5.4.1. Imputación de valores ausentes en `Tenure`

Para conservar los registros que presentan valores ausentes en `Tenure`,
utilizaremos la imputación mediante la mediana.

Esta alternativa permite sustituir los valores faltantes sin eliminar
observaciones y resulta menos sensible a los valores extremos que la
media. Aunque no garantiza recuperar los valores originales, constituye
una solución sencilla y adecuada para establecer una primera estrategia
de preprocesamiento.

La mediana se calculará exclusivamente con los valores disponibles en el
conjunto de entrenamiento y se utilizará para completar los valores
ausentes de los tres conjuntos.

De esta manera, evitaremos que la información de validación o prueba
influya en el tratamiento de los datos utilizados para entrenar los
modelos.

Después de aplicar la imputación, verificaremos que no permanezcan
valores ausentes y que las dimensiones de los conjuntos se hayan
conservado.
"""



# Comprobar los valores ausentes antes de la imputación.
print('Valores ausentes antes de la imputación:')
print('Entrenamiento:', features_train['Tenure'].isna().sum())
print('Validación:', features_valid['Tenure'].isna().sum())
print('Prueba:', features_test['Tenure'].isna().sum())

# Calcular la mediana exclusivamente con los datos de entrenamiento.
tenure_median = features_train['Tenure'].median()
print('\nMediana de Tenure:', tenure_median)

# Crear copias para aplicar la imputación.
features_train = features_train.copy()
features_valid = features_valid.copy()
features_test = features_test.copy()

# Imputar los valores ausentes utilizando la mediana de entrenamiento.
features_train['Tenure'] = features_train['Tenure'].fillna(tenure_median)
features_valid['Tenure'] = features_valid['Tenure'].fillna(tenure_median)
features_test['Tenure'] = features_test['Tenure'].fillna(tenure_median)

# Verificar los valores ausentes después de la imputación.
print('\nValores ausentes después de la imputación:')
print('Entrenamiento:', features_train.isna().sum().sum())
print('Validación:', features_valid.isna().sum().sum())
print('Prueba:', features_test.isna().sum().sum())

# Comprobar que se conservaron las dimensiones.
print('\nDimensiones después de la imputación:')
print('Entrenamiento:', features_train.shape)
print('Validación:', features_valid.shape)
print('Prueba:', features_test.shape)


"""

**Resultados de la imputación de `Tenure`**

La mediana de `Tenure`, calculada exclusivamente con el conjunto de
entrenamiento, fue de 5 años. Este valor se utilizó para sustituir los
registros ausentes en los tres conjuntos, conservando todas las
observaciones originales.

La verificación posterior confirmó que no permanecen valores ausentes y
que las dimensiones de entrenamiento, validación y prueba no se
modificaron.

Aunque esta estrategia permite conservar la información disponible,
debemos considerar que la imputación incrementa artificialmente la
frecuencia del valor 5. Esta limitación se tendrá presente al
interpretar los resultados de los modelos.

5.4.2. Codificación de variables categóricas

Una vez completada la imputación, transformaremos las variables
categóricas `Geography` y `Gender` mediante *One-Hot Encoding*,
utilizando `pd.get_dummies()`.

Aplicaremos `drop_first=True` para evitar categorías redundantes y
mantendremos una representación numérica consistente entre los tres
conjuntos.

Para ello, utilizaremos las categorías del conjunto de entrenamiento
como referencia, asegurando que validación y prueba tengan las mismas
columnas y codificación. De esta manera, los modelos podrán procesar las
características sin incorporar información de los conjuntos reservados
durante el preprocesamiento.

Finalmente, verificaremos las dimensiones, los tipos de datos y la
correspondencia de las columnas antes de iniciar el entrenamiento.
"""



# Identificar las variables categóricas.
categorical_columns = ['Geography', 'Gender']

# Establecer las mismas categorías en los tres conjuntos.
for column in categorical_columns:
    categories = sorted(features_train[column].unique())

    for dataset in (features_train, features_valid, features_test):
        dataset[column] = pd.Categorical(
            dataset[column],
            categories=categories
        )

# Aplicar One-Hot Encoding a los tres conjuntos.
features_train_ohe = pd.get_dummies(
    features_train, drop_first=True, dtype=int
)
features_valid_ohe = pd.get_dummies(
    features_valid, drop_first=True, dtype=int
)
features_test_ohe = pd.get_dummies(
    features_test, drop_first=True, dtype=int
)

# Verificar las dimensiones después de la codificación.
print('Dimensiones después de One-Hot Encoding:')
print('Entrenamiento:', features_train_ohe.shape)
print('Validación:', features_valid_ohe.shape)
print('Prueba:', features_test_ohe.shape)

# Verificar que los tres conjuntos tengan las mismas columnas.
print('\nColumnas coincidentes:')
print(
    features_train_ohe.columns.equals(features_valid_ohe.columns)
    and features_train_ohe.columns.equals(features_test_ohe.columns)
)

# Mostrar las primeras cinco filas del conjunto de entrenamiento.
features_train_ohe.head()


"""
**Resultados de la codificación categórica**

La transformación mediante *One-Hot Encoding* generó tres columnas
indicadoras: `Geography_Germany`, `Geography_Spain` y `Gender_Male`,
utilizando Francia y el género femenino como categorías de referencia.

Después de la codificación, los conjuntos de entrenamiento, validación y
prueba contienen 11 características predictoras. La verificación
confirmó que los tres conjuntos conservan las mismas columnas y el mismo
orden, sin modificar la cantidad de registros.

Esta transformación permite incorporar las características categóricas a
los modelos de clasificación mediante representaciones numéricas, sin
introducir relaciones ordinales artificiales entre las categorías.

5.5. Verificación final del preprocesamiento

Antes de iniciar el entrenamiento, realizaremos una comprobación final
de los conjuntos preparados.

Verificaremos que todas las características sean numéricas, que no
existan valores ausentes y que las columnas mantengan una estructura
consistente entre entrenamiento, validación y prueba.

También comprobaremos que las categorías presentes en los conjuntos de
validación y prueba estén contempladas en las categorías utilizadas para
la codificación, evitando interpretaciones incorrectas de valores
desconocidos.

Estas comprobaciones permitirán confirmar que los datos están preparados
para comenzar el entrenamiento y la evaluación de los modelos de
clasificación.
"""



# Agrupar los conjuntos preparados para su verificación.
prepared_sets = {
    'Entrenamiento': features_train_ohe,
    'Validación': features_valid_ohe,
    'Prueba': features_test_ohe
}

# Comprobar valores ausentes y columnas no numéricas.
for name, dataset in prepared_sets.items():
    missing_values = dataset.isna().sum().sum()
    non_numeric = dataset.select_dtypes(
        exclude='number'
    ).columns.tolist()

    print(f'\n{name}:')
    print('Valores ausentes:', missing_values)
    print('Columnas no numéricas:', non_numeric)

# Comprobar categorías desconocidas en validación y prueba.
for column in categorical_columns:
    training_categories = set(
        data_model.loc[features_train.index, column]
    )

    print(f'\nCategorías desconocidas en {column}:')

    for name, dataset in [
        ('Validación', features_valid),
        ('Prueba', features_test)
    ]:
        observed_categories = set(
            data_model.loc[dataset.index, column]
        )

        unknown_categories = observed_categories - training_categories
        print(f'{name}: {sorted(unknown_categories)}')


"""
**Conclusiones del preprocesamiento**

La preparación de los datos se completó satisfactoriamente. Se
excluyeron las columnas identificadoras, se imputaron los valores
ausentes de `Tenure` utilizando la mediana del conjunto de entrenamiento
y se codificaron las variables categóricas mediante *One-Hot Encoding*.

Las verificaciones finales confirmaron que los tres conjuntos contienen
únicamente características numéricas, no presentan valores ausentes y
mantienen las mismas 11 columnas predictoras.

Asimismo, se conservaron las proporciones originales de entrenamiento,
validación y prueba, evitando utilizar información de los conjuntos
reservados para calcular los parámetros del preprocesamiento.

Con estas comprobaciones, los datos están preparados para comenzar el
entrenamiento de los modelos de clasificación.

6. Análisis del equilibrio de clases y modelos iniciales

En esta sección investigaremos el efecto del desequilibrio de clases
sobre el desempeño de los modelos de clasificación.

Comenzaremos entrenando modelos sin aplicar técnicas de balanceo, con el
propósito de establecer una referencia inicial que permita evaluar
posteriormente las mejoras obtenidas mediante diferentes estrategias de
tratamiento del desequilibrio.

Utilizaremos principalmente la métrica F1 para evaluar los modelos, ya
que combina la precisión y la exhaustividad (*recall*) y resulta
especialmente relevante cuando la clase positiva tiene menor
representación. También calcularemos AUC-ROC para complementar el
análisis de su capacidad de discriminación.

Los resultados iniciales se compararán posteriormente con los modelos
entrenados mediante técnicas de ajuste del desequilibrio.

6.1. Análisis del desequilibrio de clases

Durante la verificación de la división estratificada comprobamos que
aproximadamente el 79.6 % de los clientes permaneció en el banco,
mientras que el 20.4 % lo abandonó.

Esta diferencia indica un desequilibrio en la variable objetivo
`Exited`, cuya clase minoritaria es precisamente la que buscamos
identificar.

Para establecer una referencia antes del entrenamiento, examinaremos la
cantidad de registros de cada clase en el conjunto de entrenamiento y su
relación de frecuencia.

Esto permitirá dimensionar el desequilibrio y comprender por qué una
exactitud (*accuracy*) elevada no necesariamente implica un buen
desempeño para identificar clientes que podrían abandonar el banco.
"""



# Calcular las frecuencias de las clases en entrenamiento.
class_counts = target_train.value_counts().sort_index()

# Construir una tabla con frecuencias y porcentajes.
class_balance = pd.DataFrame({
    'Frecuencia': class_counts,
    'Porcentaje (%)': (
        class_counts / len(target_train) * 100
    ).round(2)
})

class_balance.index.name = 'Exited'

print('Distribución de clases en entrenamiento:')
print(class_balance)

# Calcular la relación entre las clases.
class_ratio = class_counts.max() / class_counts.min()

print(f'\nRelación entre clases: {class_ratio:.2f}:1')


"""
**Resultados del análisis del desequilibrio de clases**

El conjunto de entrenamiento contiene 4,777 registros de clientes que
permanecieron en el banco y 1,223 de clientes que lo abandonaron,
equivalentes al 79.62 % y 20.38 %, respectivamente.

La relación entre ambas clases es de aproximadamente 3.91:1, lo que
confirma un desequilibrio que podría afectar la capacidad de los modelos
para identificar correctamente a los clientes que abandonan el banco.

Debido a esta distribución, la exactitud por sí sola no será suficiente
para evaluar el desempeño predictivo. Utilizaremos principalmente F1
para medir el equilibrio entre precisión y exhaustividad de la clase
positiva, complementando el análisis con AUC-ROC.

6.2. Entrenamiento de modelos iniciales sin corrección del desequilibrio

Para establecer una referencia de desempeño, comenzaremos entrenando
modelos de clasificación sin aplicar técnicas de balanceo ni modificar
los pesos de las clases.

Evaluaremos diferentes algoritmos estudiados durante el sprint,
utilizando los conjuntos de entrenamiento y validación. Compararemos sus
resultados para identificar sus fortalezas y limitaciones frente al
desequilibrio original.

Comenzaremos con un árbol de decisión, que permite trabajar directamente
con las características numéricas preparadas y no requiere escalado
previo.

Posteriormente, evaluaremos otros modelos y sus parámetros, documentando
los resultados relevantes. Esta primera etapa servirá como punto de
comparación para determinar si las técnicas de corrección del
desequilibrio permiten mejorar el valor F1.
"""



# Inicializar el árbol de decisión sin balanceo de clases.
model_tree = DecisionTreeClassifier(random_state=12345)

# Entrenar el modelo.
model_tree.fit(features_train_ohe, target_train)

# Obtener las predicciones de entrenamiento y validación.
predictions_train_tree = model_tree.predict(features_train_ohe)
predictions_valid_tree = model_tree.predict(features_valid_ohe)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_tree = model_tree.predict_proba(
    features_valid_ohe
)[:, 1]

# Calcular las métricas de evaluación.
f1_train_tree = f1_score(target_train, predictions_train_tree)
f1_valid_tree = f1_score(target_valid, predictions_valid_tree)
auc_roc_valid_tree = roc_auc_score(
    target_valid, probabilities_valid_tree
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_tree:.4f}')
print(f'F1 en validación: {f1_valid_tree:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_tree:.4f}')


"""
**Resultados del árbol de decisión sin corrección del desequilibrio**

El árbol de decisión obtuvo un F1 de 1.0000 en entrenamiento y de 0.4982
en validación. Esta diferencia evidencia un sobreajuste considerable, ya
que el modelo logró clasificar perfectamente los registros utilizados
para entrenarlo, pero presentó dificultades para generalizar a datos no
vistos.

Por su parte, el AUC-ROC de 0.6868 indica una capacidad de
discriminación superior a la de una clasificación aleatoria, aunque
todavía limitada.

Estos resultados muestran que el árbol sin restricciones no constituye
una solución adecuada en su configuración inicial. El ajuste de
hiperparámetros, especialmente la profundidad máxima (`max_depth`),
podría ayudar a reducir el sobreajuste.

Sin embargo, antes de realizar ajustes, compararemos su desempeño con
otros algoritmos entrenados sin corregir el desequilibrio de clases,
para establecer una referencia más completa.

**Evaluación inicial del bosque aleatorio**

A continuación, entrenaremos un modelo `RandomForestClassifier`
utilizando los mismos conjuntos de entrenamiento y validación.

El bosque aleatorio combina múltiples árboles de decisión y sus
predicciones, lo que puede reducir el sobreajuste respecto a un árbol
individual y mejorar la capacidad de generalización.

Evaluaremos nuevamente F1 en entrenamiento y validación, así como
AUC-ROC, para determinar si este enfoque ofrece mejores resultados sin
aplicar todavía técnicas de balanceo.
"""



# Inicializar el bosque aleatorio sin balanceo de clases.
model_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=12345
)

# Entrenar el modelo.
model_forest.fit(features_train_ohe, target_train)

# Obtener las predicciones de entrenamiento y validación.
predictions_train_forest = model_forest.predict(features_train_ohe)
predictions_valid_forest = model_forest.predict(features_valid_ohe)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_forest = model_forest.predict_proba(
    features_valid_ohe
)[:, 1]

# Calcular las métricas de evaluación.
f1_train_forest = f1_score(target_train, predictions_train_forest)
f1_valid_forest = f1_score(target_valid, predictions_valid_forest)
auc_roc_valid_forest = roc_auc_score(
    target_valid, probabilities_valid_forest
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_forest:.4f}')
print(f'F1 en validación: {f1_valid_forest:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_forest:.4f}')


"""
**Resultados del bosque aleatorio sin corrección del desequilibrio**

El bosque aleatorio obtuvo un F1 de 0.9996 en entrenamiento y de 0.5556
en validación, superando el desempeño del árbol de decisión individual
en este último conjunto.

La métrica AUC-ROC también presentó una mejora considerable, alcanzando
0.8536 frente al 0.6868 obtenido anteriormente. Este resultado indica
una mayor capacidad del bosque aleatorio para distinguir entre ambas
clases.

Sin embargo, la diferencia entre los valores F1 de entrenamiento y
validación sigue siendo considerable, lo que evidencia que el modelo
todavía presenta sobreajuste.

En conjunto, los resultados muestran que el bosque aleatorio constituye
una alternativa más prometedora que el árbol individual, aunque será
necesario investigar ajustes de hiperparámetros y estrategias para
tratar el desequilibrio de clases.

**Evaluación inicial de la regresión logística**

Para completar la comparación inicial, entrenaremos un modelo
`LogisticRegression` sin aplicar técnicas de balanceo.

A diferencia de los modelos basados en árboles, la regresión logística
estima la probabilidad de pertenecer a una clase mediante una relación
lineal entre las características y los logaritmos de las probabilidades
relativas (*log-odds*).

Dado que las variables numéricas presentan escalas muy diferentes,
evaluaremos la necesidad de estandarizarlas antes del entrenamiento para
favorecer la convergencia del algoritmo.

Al igual que en los modelos anteriores, calcularemos F1 en entrenamiento
y validación, así como AUC-ROC en validación, para establecer una
comparación consistente entre los tres algoritmos.
"""



# Seleccionar las características numéricas que serán estandarizadas.
numeric_columns = [
    'CreditScore',
    'Age',
    'Tenure',
    'Balance',
    'NumOfProducts',
    'EstimatedSalary'
]

# Inicializar y ajustar el escalador con entrenamiento.
scaler = StandardScaler()
scaler.fit(features_train_ohe[numeric_columns])

# Crear conjuntos independientes para la regresión logística.
features_train_scaled = features_train_ohe.astype(float)
features_valid_scaled = features_valid_ohe.astype(float)
features_test_scaled = features_test_ohe.astype(float)

# Aplicar la misma transformación a los tres conjuntos.
features_train_scaled[numeric_columns] = scaler.transform(
    features_train_ohe[numeric_columns]
)
features_valid_scaled[numeric_columns] = scaler.transform(
    features_valid_ohe[numeric_columns]
)
features_test_scaled[numeric_columns] = scaler.transform(
    features_test_ohe[numeric_columns]
)

# Verificar las dimensiones.
print('Dimensiones después de la estandarización:')
print('Entrenamiento:', features_train_scaled.shape)
print('Validación:', features_valid_scaled.shape)
print('Prueba:', features_test_scaled.shape)

# Verificar la media y desviación estándar en entrenamiento.
print('\nMedias de las características estandarizadas:')
print(features_train_scaled[numeric_columns].mean().round(3))

print('\nDesviaciones estándar:')
print(features_train_scaled[numeric_columns].std(ddof=0).round(3))


"""
**Resultados de la estandarización**

La estandarización de las seis características numéricas seleccionadas
se realizó correctamente. Las variables transformadas presentan medias
cercanas a cero y desviaciones estándar cercanas a uno en el conjunto de
entrenamiento.

Las dimensiones de los tres conjuntos permanecieron sin modificaciones,
conservando las 11 características predictoras. Además, los indicadores
binarios mantuvieron sus valores originales de 0 y 1.

El escalador se ajustó exclusivamente con los datos de entrenamiento y
sus parámetros se aplicaron posteriormente a validación y prueba,
evitando fugas de información.

**Entrenamiento y evaluación inicial de la regresión logística**

Una vez preparadas las características, entrenaremos un modelo de
regresión logística sin aplicar técnicas para corregir el desequilibrio
de clases.

Utilizaremos los conjuntos estandarizados de entrenamiento y validación
para evaluar su desempeño mediante F1 y AUC-ROC, manteniendo las mismas
condiciones generales de evaluación que en los modelos anteriores.

Compararemos los resultados de entrenamiento y validación para
identificar posibles dificultades de generalización, así como su
capacidad para reconocer a los clientes que abandonan el banco.

Esta evaluación completará la comparación inicial entre el árbol de
decisión, el bosque aleatorio y la regresión logística, antes de
investigar ajustes de hiperparámetros y estrategias para tratar el
desequilibrio de clases.
"""



# Inicializar la regresión logística sin balanceo de clases.
model_logistic = LogisticRegression(
    random_state=12345,
    solver='liblinear'
)

# Entrenar el modelo con las características estandarizadas.
model_logistic.fit(features_train_scaled, target_train)

# Obtener las predicciones de entrenamiento y validación.
predictions_train_logistic = model_logistic.predict(
    features_train_scaled
)
predictions_valid_logistic = model_logistic.predict(
    features_valid_scaled
)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_logistic = model_logistic.predict_proba(
    features_valid_scaled
)[:, 1]

# Calcular las métricas de evaluación.
f1_train_logistic = f1_score(
    target_train, predictions_train_logistic
)
f1_valid_logistic = f1_score(
    target_valid, predictions_valid_logistic
)
auc_roc_valid_logistic = roc_auc_score(
    target_valid, probabilities_valid_logistic
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_logistic:.4f}')
print(f'F1 en validación: {f1_valid_logistic:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_logistic:.4f}')


"""
**Resultados de la regresión logística sin corrección del
desequilibrio**

La regresión logística obtuvo un F1 de 0.3036 en entrenamiento y de
0.3215 en validación. La similitud entre ambos resultados no muestra
indicios importantes de sobreajuste, aunque el desempeño general es
inferior al de los modelos basados en árboles.

Por otra parte, el AUC-ROC de 0.7876 indica una capacidad de
discriminación superior a la del árbol de decisión, a pesar de presentar
un F1 menor. Esta diferencia sugiere que podría resultar conveniente
investigar posteriormente el efecto del umbral de clasificación sobre
las predicciones.

En conjunto, los resultados muestran que la regresión logística, con su
configuración inicial y sin corregir el desequilibrio, tiene
dificultades para identificar adecuadamente a los clientes que abandonan
el banco.

6.3. Comparación de los modelos iniciales

Después de entrenar el árbol de decisión, el bosque aleatorio y la
regresión logística, compararemos sus resultados para identificar las
principales diferencias de desempeño.

Organizaremos las métricas F1 de entrenamiento y validación, así como
AUC-ROC de validación, en una tabla que facilite la comparación entre
los tres algoritmos.

Esta revisión permitirá establecer una referencia del desempeño de los
modelos sin corregir el desequilibrio de clases y determinar qué
aspectos necesitan mejorar.

Posteriormente investigaremos ajustes de hiperparámetros y aplicaremos
al menos dos estrategias para tratar el desequilibrio, evaluando si
estas modificaciones mejoran la capacidad de los modelos para
identificar a los clientes que abandonan el banco.
"""



# Organizar los resultados de los modelos iniciales.
baseline_results = pd.DataFrame({
    'Modelo': [
        'Árbol de decisión',
        'Bosque aleatorio',
        'Regresión logística'
    ],
    'F1 entrenamiento': [
        f1_train_tree,
        f1_train_forest,
        f1_train_logistic
    ],
    'F1 validación': [
        f1_valid_tree,
        f1_valid_forest,
        f1_valid_logistic
    ],
    'AUC-ROC validación': [
        auc_roc_valid_tree,
        auc_roc_valid_forest,
        auc_roc_valid_logistic
    ]
})

# Calcular la diferencia entre F1 de entrenamiento y validación.
baseline_results['Diferencia F1'] = (
    baseline_results['F1 entrenamiento']
    - baseline_results['F1 validación']
)

# Ordenar los modelos según su F1 en validación.
baseline_results = baseline_results.sort_values(
    by='F1 validación',
    ascending=False
).reset_index(drop=True)

# Mostrar los resultados con cuatro decimales.
baseline_results.round(4)


"""
**Conclusiones de la comparación inicial**

La comparación de los tres algoritmos mostró diferencias importantes en
su capacidad de clasificación y generalización.

El bosque aleatorio obtuvo los mejores resultados en validación, con un
F1 de 0.5556 y un AUC-ROC de 0.8536. Sin embargo, al igual que el árbol
de decisión, presentó una diferencia considerable entre el desempeño de
entrenamiento y validación, lo que evidencia sobreajuste.

La regresión logística mostró resultados más similares entre ambos
conjuntos, aunque con un F1 inferior. Su AUC-ROC sugiere que conserva
cierta capacidad para distinguir entre las clases, a pesar de las
limitaciones observadas en sus predicciones iniciales.

Estos resultados establecen una referencia para evaluar las mejoras
posteriores. Ninguno de los modelos alcanzó un F1 de 0.59 en validación,
por lo que investigaremos estrategias para mejorar la identificación de
clientes que abandonan el banco.

7. Mejora del modelo y tratamiento del desequilibrio de clases

En esta sección buscaremos mejorar el desempeño de los modelos mediante
técnicas para tratar el desequilibrio de clases y el ajuste de
hiperparámetros.

Evaluaremos dos estrategias principales:

1. **Ajuste de pesos de las clases (`class_weight`):** modificaremos la
   importancia relativa de los errores de clasificación durante el
   entrenamiento, asignando mayor peso a la clase minoritaria.
2. **Sobremuestreo (*upsampling*):** aumentaremos la representación de
   la clase minoritaria en el conjunto de entrenamiento, con el
   propósito de mejorar su identificación.

Compararemos los resultados obtenidos mediante F1 y AUC-ROC, utilizando
el conjunto de validación para seleccionar las configuraciones más
prometedoras.

También investigaremos distintos hiperparámetros para controlar la
complejidad de los modelos y reducir posibles problemas de sobreajuste.

7.1. Ajuste de pesos de las clases

Comenzaremos utilizando el parámetro `class_weight='balanced'`,
disponible en los modelos de clasificación seleccionados.

Este parámetro asigna pesos inversamente proporcionales a las
frecuencias de las clases, aumentando la importancia de los errores
cometidos sobre los clientes que abandonaron el banco.

Inicialmente mantendremos los demás hiperparámetros de los modelos de
referencia para observar el efecto del balanceo. Posteriormente
investigaremos configuraciones alternativas para mejorar su desempeño.

Esta estrategia no modifica la cantidad de registros ni las proporciones
originales del conjunto de entrenamiento, sino la importancia que el
algoritmo asigna a cada clase durante el aprendizaje.
"""



# Inicializar el bosque aleatorio con pesos balanceados.
model_forest_balanced = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=12345
)

# Entrenar el modelo con el conjunto original de entrenamiento.
model_forest_balanced.fit(features_train_ohe, target_train)

# Obtener las predicciones de entrenamiento y validación.
predictions_train_forest_balanced = model_forest_balanced.predict(
    features_train_ohe
)
predictions_valid_forest_balanced = model_forest_balanced.predict(
    features_valid_ohe
)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_forest_balanced = (
    model_forest_balanced.predict_proba(features_valid_ohe)[:, 1]
)

# Calcular las métricas de evaluación.
f1_train_forest_balanced = f1_score(
    target_train, predictions_train_forest_balanced
)
f1_valid_forest_balanced = f1_score(
    target_valid, predictions_valid_forest_balanced
)
auc_roc_valid_forest_balanced = roc_auc_score(
    target_valid, probabilities_valid_forest_balanced
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_forest_balanced:.4f}')
print(f'F1 en validación: {f1_valid_forest_balanced:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_forest_balanced:.4f}')


"""
**Resultados del bosque aleatorio con pesos de clases balanceados**

La incorporación de `class_weight='balanced'` no produjo una mejora
respecto al bosque aleatorio inicial. El F1 en validación disminuyó
ligeramente de 0.5556 a 0.5545, mientras que AUC-ROC pasó de 0.8536 a
0.8490.

Además, el F1 de entrenamiento alcanzó 1.0000, lo que confirma que el
modelo continúa presentando un sobreajuste considerable.

Estos resultados indican que modificar los pesos de las clases,
manteniendo los demás hiperparámetros, no fue suficiente para mejorar el
desempeño del bosque aleatorio.

Sin embargo, esto no implica que la técnica sea ineficaz en general. Su
efecto puede variar según el algoritmo y la configuración utilizada.

**Evaluación de la regresión logística con pesos balanceados**

A continuación, aplicaremos `class_weight='balanced'` a la regresión
logística, conservando los hiperparámetros y las características
estandarizadas del modelo inicial.

Este experimento permitirá evaluar si el ajuste de pesos mejora la
identificación de clientes que abandonan el banco en un algoritmo
diferente, comparando nuevamente F1 y AUC-ROC sobre el conjunto de
validación.
"""



# Inicializar la regresión logística con pesos balanceados.
model_logistic_balanced = LogisticRegression(
    random_state=12345,
    solver='liblinear',
    class_weight='balanced'
)

# Entrenar el modelo con las características estandarizadas.
model_logistic_balanced.fit(features_train_scaled, target_train)

# Obtener las predicciones de entrenamiento y validación.
predictions_train_logistic_balanced = model_logistic_balanced.predict(
    features_train_scaled
)
predictions_valid_logistic_balanced = model_logistic_balanced.predict(
    features_valid_scaled
)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_logistic_balanced = (
    model_logistic_balanced.predict_proba(features_valid_scaled)[:, 1]
)

# Calcular las métricas de evaluación.
f1_train_logistic_balanced = f1_score(
    target_train, predictions_train_logistic_balanced
)
f1_valid_logistic_balanced = f1_score(
    target_valid, predictions_valid_logistic_balanced
)
auc_roc_valid_logistic_balanced = roc_auc_score(
    target_valid, probabilities_valid_logistic_balanced
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_logistic_balanced:.4f}')
print(f'F1 en validación: {f1_valid_logistic_balanced:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_logistic_balanced:.4f}')


"""
**Resultados de la regresión logística con pesos balanceados**

La incorporación de `class_weight='balanced'` mejoró considerablemente
el desempeño de la regresión logística. El F1 en validación aumentó de
0.3215 a 0.5113, mientras que AUC-ROC presentó una ligera mejora,
pasando de 0.7876 a 0.7918.

El F1 en entrenamiento alcanzó 0.4796, un resultado relativamente
cercano al obtenido en validación, sin evidencias importantes de
sobreajuste.

Estos resultados indican que el ajuste de pesos permitió mejorar el
equilibrio entre precisión y exhaustividad al clasificar a los clientes
que abandonan el banco. Sin embargo, el F1 de validación todavía es
inferior al obtenido por el bosque aleatorio sin balanceo.

La comparación también demuestra que el efecto de `class_weight` depende
del algoritmo utilizado, por lo que resulta importante evaluar esta
técnica en diferentes modelos antes de establecer conclusiones
generales.

**Evaluación del árbol de decisión con pesos balanceados**

Para completar esta primera investigación, aplicaremos
`class_weight='balanced'` al árbol de decisión, conservando inicialmente
sus hiperparámetros predeterminados.

Compararemos los resultados con los obtenidos anteriormente sin
balanceo, utilizando F1 en entrenamiento y validación, así como AUC-ROC
en validación.

Este experimento permitirá determinar si el ajuste de pesos mejora la
identificación de la clase minoritaria y si tiene algún efecto sobre el
sobreajuste observado en el árbol original.

Posteriormente investigaremos los hiperparámetros de los modelos para
mejorar su capacidad de generalización.
"""



# Inicializar el árbol de decisión con pesos balanceados.
model_tree_balanced = DecisionTreeClassifier(
    class_weight='balanced',
    random_state=12345
)

# Entrenar el modelo.
model_tree_balanced.fit(features_train_ohe, target_train)

# Obtener las predicciones de entrenamiento y validación.
predictions_train_tree_balanced = model_tree_balanced.predict(
    features_train_ohe
)
predictions_valid_tree_balanced = model_tree_balanced.predict(
    features_valid_ohe
)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_tree_balanced = (
    model_tree_balanced.predict_proba(features_valid_ohe)[:, 1]
)

# Calcular las métricas de evaluación.
f1_train_tree_balanced = f1_score(
    target_train, predictions_train_tree_balanced
)
f1_valid_tree_balanced = f1_score(
    target_valid, predictions_valid_tree_balanced
)
auc_roc_valid_tree_balanced = roc_auc_score(
    target_valid, probabilities_valid_tree_balanced
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_tree_balanced:.4f}')
print(f'F1 en validación: {f1_valid_tree_balanced:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_tree_balanced:.4f}')


"""
**Resultados del árbol de decisión con pesos balanceados**

El árbol de decisión con `class_weight='balanced'` obtuvo un F1 de
1.0000 en entrenamiento y de 0.5074 en validación. En comparación con el
modelo original, el F1 de validación aumentó ligeramente, mientras que
AUC-ROC pasó de 0.6868 a 0.6906.

A pesar de estas mejoras, la diferencia entre entrenamiento y validación
sigue siendo considerable, lo que confirma que el modelo continúa
presentando sobreajuste. Por lo tanto, será necesario investigar
hiperparámetros que permitan controlar su complejidad.

7.1.1. Comparación de modelos con y sin balanceo de clases

Después de evaluar los tres algoritmos utilizando
`class_weight='balanced'`, compararemos sus resultados con los modelos
iniciales para determinar el efecto de esta técnica sobre F1 y AUC-ROC.

Esta comparación permitirá identificar qué modelos se beneficiaron del
ajuste de pesos y cuáles requieren otras modificaciones para mejorar su
desempeño.

Los resultados también servirán como referencia para la siguiente etapa,
en la que investigaremos diferentes configuraciones de hiperparámetros,
particularmente la profundidad máxima de los árboles y el número de
estimadores del bosque aleatorio.

El objetivo será mejorar la capacidad de generalización y aumentar F1 en
validación, manteniendo reservado el conjunto de prueba para la
evaluación final.
"""



# Reunir los resultados de los modelos con y sin balanceo.
class_weight_results = pd.DataFrame({
    'Modelo': [
        'Árbol de decisión',
        'Árbol de decisión',
        'Bosque aleatorio',
        'Bosque aleatorio',
        'Regresión logística',
        'Regresión logística'
    ],
    'Balanceo': [
        'Sin balanceo',
        'class_weight',
        'Sin balanceo',
        'class_weight',
        'Sin balanceo',
        'class_weight'
    ],
    'F1 entrenamiento': [
        f1_train_tree,
        f1_train_tree_balanced,
        f1_train_forest,
        f1_train_forest_balanced,
        f1_train_logistic,
        f1_train_logistic_balanced
    ],
    'F1 validación': [
        f1_valid_tree,
        f1_valid_tree_balanced,
        f1_valid_forest,
        f1_valid_forest_balanced,
        f1_valid_logistic,
        f1_valid_logistic_balanced
    ],
    'AUC-ROC validación': [
        auc_roc_valid_tree,
        auc_roc_valid_tree_balanced,
        auc_roc_valid_forest,
        auc_roc_valid_forest_balanced,
        auc_roc_valid_logistic,
        auc_roc_valid_logistic_balanced
    ]
})

# Calcular la diferencia de F1 entre entrenamiento y validación.
class_weight_results['Diferencia F1'] = (
    class_weight_results['F1 entrenamiento']
    - class_weight_results['F1 validación']
)

# Mostrar la comparación con cuatro decimales.
class_weight_results.round(4)


"""
**Resultados de la comparación de modelos con y sin balanceo**

La comparación de los seis experimentos mostró que el efecto de
`class_weight='balanced'` varía considerablemente según el algoritmo
utilizado.

La regresión logística presentó la mejora más significativa en F1 de
validación, mientras que el árbol de decisión registró un incremento
moderado y el bosque aleatorio experimentó una ligera disminución.

A pesar de estas diferencias, el bosque aleatorio sin balanceo continúa
siendo el modelo con mejor desempeño en validación, alcanzando un F1 de
0.5556 y un AUC-ROC de 0.8536.

Los resultados también muestran que los modelos basados en árboles
presentan diferencias considerables entre entrenamiento y validación, lo
que sugiere la necesidad de controlar su complejidad.

En consecuencia, el ajuste de pesos por sí solo no fue suficiente para
resolver las limitaciones identificadas. Será necesario investigar los
hiperparámetros de los modelos antes de seleccionar la configuración más
adecuada.

7.1.2. Ajuste de hiperparámetros de los modelos basados en árboles

A continuación, investigaremos diferentes configuraciones del árbol de
decisión y del bosque aleatorio para mejorar su capacidad de
generalización.

En el árbol de decisión evaluaremos distintas profundidades máximas
(`max_depth`), mientras que en el bosque aleatorio analizaremos
combinaciones de profundidad máxima y número de árboles
(`n_estimators`).

Compararemos configuraciones con y sin pesos de clases balanceados para
identificar cómo interactúan la complejidad de los modelos y el
tratamiento del desequilibrio.

Utilizaremos el conjunto de entrenamiento para ajustar los modelos y el
conjunto de validación para seleccionar los hiperparámetros que
produzcan el mejor F1, complementando el análisis con AUC-ROC.

También examinaremos las diferencias entre entrenamiento y validación
para identificar posibles problemas de sobreajuste o subajuste.

El conjunto de prueba permanecerá reservado para la evaluación final del
modelo seleccionado.
"""



# Almacenar los resultados de los experimentos.
tree_tuning = []

best_tree_f1 = -1
best_tree_model = None
best_tree_params = {}

# Evaluar diferentes profundidades con y sin balanceo.
for weight in [None, 'balanced']:
    for depth in range(1, 16):
        model = DecisionTreeClassifier(
            max_depth=depth,
            class_weight=weight,
            random_state=12345
        )

        model.fit(features_train_ohe, target_train)

        # Obtener las predicciones y probabilidades.
        predictions_train = model.predict(features_train_ohe)
        predictions_valid = model.predict(features_valid_ohe)
        probabilities_valid = model.predict_proba(
            features_valid_ohe
        )[:, 1]

        # Calcular las métricas.
        train_f1 = f1_score(target_train, predictions_train)
        valid_f1 = f1_score(target_valid, predictions_valid)
        valid_auc = roc_auc_score(
            target_valid, probabilities_valid
        )

        # Conservar los resultados del experimento.
        tree_tuning.append({
            'max_depth': depth,
            'Balanceo': (
                'Sin balanceo' if weight is None else 'class_weight'
            ),
            'F1 entrenamiento': train_f1,
            'F1 validación': valid_f1,
            'AUC-ROC validación': valid_auc
        })

        # Identificar y almacenar el mejor modelo.
        if valid_f1 > best_tree_f1:
            best_tree_f1 = valid_f1
            best_tree_model = model
            best_tree_params = {
                'max_depth': depth,
                'class_weight': weight
            }

# Crear una tabla con los resultados.
tree_tuning_results = pd.DataFrame(tree_tuning)

tree_tuning_results['Diferencia F1'] = (
    tree_tuning_results['F1 entrenamiento']
    - tree_tuning_results['F1 validación']
)

tree_tuning_results = tree_tuning_results.sort_values(
    by='F1 validación',
    ascending=False
).reset_index(drop=True)

# Mostrar la mejor configuración encontrada.
print('Mejor configuración del árbol de decisión:')
print('max_depth:', best_tree_params['max_depth'])
print('class_weight:', best_tree_params['class_weight'])
print(f'Mejor F1 en validación: {best_tree_f1:.4f}')

# Mostrar los diez mejores experimentos.
tree_tuning_results.head(10).round(4)


"""
**Resultados del ajuste de hiperparámetros del árbol de decisión**

La investigación de distintas profundidades permitió mejorar
considerablemente el desempeño del árbol de decisión y reducir su
sobreajuste.

La mejor configuración encontrada utilizó `max_depth=8` y
`class_weight=None`, alcanzando un F1 de 0.5796 en validación y un
AUC-ROC de 0.8074. En comparación con el árbol inicial sin
restricciones, la mejora de F1 fue de 0.0814 puntos.

Además, la diferencia entre F1 de entrenamiento y validación disminuyó
de 0.5018 a 0.0880, lo que evidencia una mejora importante en la
capacidad de generalización del modelo.

También se identificaron configuraciones con pesos balanceados que
obtuvieron resultados competitivos. En particular, el árbol de
profundidad 6 con `class_weight='balanced'` alcanzó un F1 de 0.5747 y un
AUC-ROC de 0.8353, mostrando que el balanceo puede beneficiar algunas
métricas sin necesariamente producir el mayor F1.

Estos resultados confirman que controlar la complejidad del modelo es
fundamental y que la mejor configuración debe seleccionarse considerando
las métricas obtenidas en validación.

**Ajuste de hiperparámetros del bosque aleatorio**

A continuación, investigaremos diferentes combinaciones de `max_depth` y
`n_estimators` en `RandomForestClassifier`, tanto con pesos balanceados
como sin ellos.

El objetivo será identificar una configuración que mejore el F1 de
validación y reduzca el sobreajuste observado en el bosque aleatorio
inicial.

Para ello, utilizaremos ciclos que permitan entrenar y evaluar
sistemáticamente diferentes configuraciones, conservando sus resultados
en una tabla comparativa y almacenando automáticamente el mejor modelo
encontrado.

Al igual que en los experimentos anteriores, seleccionaremos la
configuración con mayor F1 en validación y utilizaremos AUC-ROC como
métrica complementaria, sin consultar todavía el conjunto de prueba.
"""



# Almacenar los resultados de los experimentos.
forest_tuning = []

best_forest_f1 = -1
best_forest_model = None
best_forest_params = {}

# Evaluar combinaciones de hiperparámetros.
for weight in [None, 'balanced']:
    for depth in [4, 6, 8, 10, 12]:
        for est in [50, 100, 150]:
            model = RandomForestClassifier(
                n_estimators=est,
                max_depth=depth,
                class_weight=weight,
                random_state=12345
            )

            model.fit(features_train_ohe, target_train)

            # Obtener las predicciones y probabilidades.
            predictions_train = model.predict(features_train_ohe)
            predictions_valid = model.predict(features_valid_ohe)
            probabilities_valid = model.predict_proba(
                features_valid_ohe
            )[:, 1]

            # Calcular las métricas.
            train_f1 = f1_score(target_train, predictions_train)
            valid_f1 = f1_score(target_valid, predictions_valid)
            valid_auc = roc_auc_score(
                target_valid, probabilities_valid
            )

            # Conservar los resultados del experimento.
            forest_tuning.append({
                'n_estimators': est,
                'max_depth': depth,
                'Balanceo': (
                    'Sin balanceo' if weight is None else 'class_weight'
                ),
                'F1 entrenamiento': train_f1,
                'F1 validación': valid_f1,
                'AUC-ROC validación': valid_auc
            })

            # Identificar y almacenar el mejor modelo.
            if valid_f1 > best_forest_f1:
                best_forest_f1 = valid_f1
                best_forest_model = model
                best_forest_params = {
                    'n_estimators': est,
                    'max_depth': depth,
                    'class_weight': weight
                }

# Crear una tabla con los resultados.
forest_tuning_results = pd.DataFrame(forest_tuning)

forest_tuning_results['Diferencia F1'] = (
    forest_tuning_results['F1 entrenamiento']
    - forest_tuning_results['F1 validación']
)

forest_tuning_results = forest_tuning_results.sort_values(
    by='F1 validación',
    ascending=False
).reset_index(drop=True)

# Mostrar la mejor configuración encontrada.
print('Mejor configuración del bosque aleatorio:')
print('n_estimators:', best_forest_params['n_estimators'])
print('max_depth:', best_forest_params['max_depth'])
print('class_weight:', best_forest_params['class_weight'])
print(f'Mejor F1 en validación: {best_forest_f1:.4f}')

# Mostrar los diez mejores experimentos.
forest_tuning_results.head(10).round(4)


"""
**Resultados del ajuste de hiperparámetros del bosque aleatorio**

La investigación de diferentes combinaciones de profundidad máxima,
número de árboles y pesos de clases permitió mejorar considerablemente
el desempeño del bosque aleatorio.

La mejor configuración encontrada utilizó `n_estimators=100`,
`max_depth=10` y `class_weight='balanced'`, alcanzando un F1 de 0.6376 y
un AUC-ROC de 0.8656 en validación.

En comparación con el bosque aleatorio inicial, el F1 aumentó 0.0820
puntos, mientras que la diferencia entre entrenamiento y validación
disminuyó de 0.4440 a 0.1725. Estos resultados indican una mejora
importante en la capacidad de generalización, aunque todavía existe
cierta diferencia de desempeño entre ambos conjuntos.

También observamos que las configuraciones balanceadas ocuparon los
primeros lugares de la comparación, a diferencia del experimento inicial
con `class_weight`, en el que no se obtuvo una mejora. Esto demuestra
que el efecto del balanceo puede depender de la complejidad del modelo y
de sus hiperparámetros.

Aunque algunas configuraciones consiguieron valores superiores de
AUC-ROC y menores diferencias entre entrenamiento y validación,
seleccionamos el modelo con mayor F1 por tratarse de la métrica
principal del proyecto.

El resultado supera el valor de referencia de 0.59 en validación; sin
embargo, el cumplimiento del requisito de TripleTen deberá comprobarse
posteriormente en el conjunto de prueba.

7.2. Tratamiento del desequilibrio mediante sobremuestreo (Upsampling)

Después de investigar el ajuste de pesos de las clases, evaluaremos una
segunda estrategia para tratar el desequilibrio: el sobremuestreo o
*upsampling*.

Esta técnica consiste en aumentar la representación de la clase
minoritaria mediante la repetición aleatoria de sus registros, con el
propósito de reducir la diferencia de frecuencias entre ambas clases
durante el entrenamiento.

A diferencia de `class_weight`, el sobremuestreo modifica la composición
del conjunto utilizado para entrenar, sin cambiar directamente los pesos
asignados por el algoritmo.

Aplicaremos esta transformación exclusivamente al conjunto de
entrenamiento, manteniendo intactos los conjuntos de validación y prueba
para obtener evaluaciones comparables.

Posteriormente, entrenaremos y evaluaremos los modelos con los datos
sobremuestreados, utilizando F1 y AUC-ROC para determinar si esta
estrategia ofrece ventajas frente al ajuste de pesos.

También consideraremos el posible sobreajuste asociado a la repetición
de observaciones, evitando asumir que aumentar la cantidad de registros
de la clase minoritaria produce necesariamente mejores resultados.
"""



# Crear una función para aumentar la representación de la clase minoritaria.
def upsample(features, target, repeat):
    data_train = features.copy()
    data_train['Exited'] = target

    # Separar los registros según su clase.
    majority = data_train[data_train['Exited'] == 0]
    minority = data_train[data_train['Exited'] == 1]

    # Repetir la clase minoritaria y mezclar los registros.
    data_upsampled = pd.concat(
        [majority] + [minority] * repeat,
        ignore_index=True
    ).sample(frac=1, random_state=12345).reset_index(drop=True)

    # Separar nuevamente las características y la variable objetivo.
    features_upsampled = data_upsampled.drop(columns=['Exited'])
    target_upsampled = data_upsampled['Exited']

    return features_upsampled, target_upsampled


# Aplicar upsampling exclusivamente al conjunto de entrenamiento.
features_train_upsampled, target_train_upsampled = upsample(
    features_train_ohe,
    target_train,
    repeat=4
)

# Verificar las dimensiones y la nueva distribución de clases.
print('Dimensiones después de Upsampling:')
print('Features:', features_train_upsampled.shape)
print('Target:', target_train_upsampled.shape)

print('\nDistribución de clases:')
print(target_train_upsampled.value_counts().sort_index())

print('\nProporciones de clases:')
print(
    target_train_upsampled.value_counts(
        normalize=True
    ).sort_index().round(4)
)


"""
**Resultados del sobremuestreo**

La aplicación de *upsampling* permitió equilibrar prácticamente las
clases del conjunto de entrenamiento. Mediante la repetición de los
registros de la clase minoritaria, su representación aumentó del 20.38 %
al 50.59 %, mientras que la clase mayoritaria pasó a representar el
49.41 %.

El conjunto resultante contiene 9,669 observaciones, conservando todos
los registros originales y agregando copias de los clientes que
abandonaron el banco.

Esta transformación se aplicó exclusivamente al conjunto de
entrenamiento, por lo que validación y prueba mantienen sus
distribuciones originales. Esto permitirá evaluar los modelos sobre
datos no sobremuestreados y comparar sus resultados con los experimentos
anteriores.

Aunque el balance entre clases mejoró considerablemente, todavía debemos
comprobar si esta modificación se traduce en un mejor desempeño
predictivo.

7.2.1. Entrenamiento del bosque aleatorio con Upsampling

Para evaluar el efecto del sobremuestreo, entrenaremos un modelo
`RandomForestClassifier` utilizando el conjunto de entrenamiento
balanceado mediante *upsampling*.

Comenzaremos con `n_estimators=100` y `max_depth=10`, correspondientes a
la mejor combinación de profundidad y número de árboles encontrada
anteriormente.

No utilizaremos `class_weight='balanced'`, ya que buscamos investigar el
efecto del sobremuestreo sin combinar ambas técnicas de corrección del
desequilibrio.

Evaluaremos F1 en entrenamiento y validación, así como AUC-ROC en
validación. Prestaremos especial atención a los resultados sobre este
último conjunto, dado que las métricas de entrenamiento pueden verse
favorecidas por la repetición de registros.

Posteriormente compararemos estos resultados con las configuraciones
anteriores para determinar si el sobremuestreo constituye una
alternativa competitiva frente al ajuste de pesos de las clases.
"""



# Inicializar el bosque aleatorio sin ajuste de pesos.
model_forest_upsampled = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=12345
)

# Entrenar el modelo con los datos sobremuestreados.
model_forest_upsampled.fit(
    features_train_upsampled,
    target_train_upsampled
)

# Obtener las predicciones en entrenamiento original y validación.
predictions_train_forest_upsampled = model_forest_upsampled.predict(
    features_train_ohe
)
predictions_valid_forest_upsampled = model_forest_upsampled.predict(
    features_valid_ohe
)

# Obtener las probabilidades de la clase positiva en validación.
probabilities_valid_forest_upsampled = (
    model_forest_upsampled.predict_proba(features_valid_ohe)[:, 1]
)

# Calcular las métricas de evaluación.
f1_train_forest_upsampled = f1_score(
    target_train, predictions_train_forest_upsampled
)
f1_valid_forest_upsampled = f1_score(
    target_valid, predictions_valid_forest_upsampled
)
auc_roc_valid_forest_upsampled = roc_auc_score(
    target_valid, probabilities_valid_forest_upsampled
)

# Mostrar los resultados.
print(f'F1 en entrenamiento: {f1_train_forest_upsampled:.4f}')
print(f'F1 en validación: {f1_valid_forest_upsampled:.4f}')
print(f'AUC-ROC en validación: {auc_roc_valid_forest_upsampled:.4f}')


"""
**Resultados del bosque aleatorio con Upsampling**

El bosque aleatorio entrenado mediante *upsampling*, utilizando
`n_estimators=100` y `max_depth=10`, obtuvo un F1 de 0.8004 en
entrenamiento y de 0.6384 en validación, así como un AUC-ROC de 0.8647.

En comparación con el bosque optimizado mediante
`class_weight='balanced'`, el sobremuestreo produjo una mejora mínima de
0.0008 puntos en F1 de validación, acompañada de una ligera disminución
en AUC-ROC.

La diferencia entre F1 de entrenamiento y validación fue de 0.1620, lo
que indica que todavía existe cierto sobreajuste, aunque
considerablemente menor que en los modelos iniciales sin restricciones
de profundidad.

Los resultados muestran que ambas estrategias de balanceo alcanzaron
desempeños muy similares con esta configuración. Por lo tanto, no existe
evidencia suficiente para afirmar que una técnica sea claramente
superior a la otra.

Con estos experimentos hemos completado la evaluación de los dos
enfoques de corrección del desequilibrio establecidos para el proyecto.

8. Comparación y selección del mejor modelo

Una vez evaluados los modelos iniciales, investigados sus
hiperparámetros y aplicadas las dos estrategias de balanceo,
compararemos los resultados más relevantes para seleccionar el modelo
definitivo.

Utilizaremos F1 de validación como criterio principal de selección y
AUC-ROC como métrica complementaria. También consideraremos las
diferencias entre entrenamiento y validación para identificar posibles
limitaciones de generalización.

La comparación incluirá los mejores modelos basados en árboles y las
configuraciones del bosque aleatorio con y sin tratamiento del
desequilibrio, conservando los resultados de los experimentos anteriores
como referencia.

Esta revisión permitirá justificar la selección de la configuración
definitiva antes de realizar la evaluación final sobre el conjunto de
prueba, que permanecerá reservado hasta completar la selección.
"""



# Recuperar los mejores resultados de los modelos optimizados.
best_tree_result = tree_tuning_results.iloc[0]
best_forest_result = forest_tuning_results.iloc[0]

# Recuperar el bosque sin balanceo con 100 árboles y profundidad 10.
forest_unbalanced = forest_tuning_results.loc[
    (forest_tuning_results['n_estimators'] == 100)
    & (forest_tuning_results['max_depth'] == 10)
    & (forest_tuning_results['Balanceo'] == 'Sin balanceo')
].iloc[0]

# Reunir los resultados más relevantes.
model_comparison = pd.DataFrame({
    'Modelo': [
        'Árbol optimizado',
        'Bosque inicial',
        'Bosque ajustado',
        'Bosque ajustado',
        'Bosque ajustado',
        'Regresión logística'
    ],
    'Balanceo': [
        best_tree_result['Balanceo'],
        'Sin balanceo',
        'Sin balanceo',
        best_forest_result['Balanceo'],
        'Upsampling',
        'class_weight'
    ],
    'F1 entrenamiento': [
        best_tree_result['F1 entrenamiento'],
        f1_train_forest,
        forest_unbalanced['F1 entrenamiento'],
        best_forest_result['F1 entrenamiento'],
        f1_train_forest_upsampled,
        f1_train_logistic_balanced
    ],
    'F1 validación': [
        best_tree_result['F1 validación'],
        f1_valid_forest,
        forest_unbalanced['F1 validación'],
        best_forest_result['F1 validación'],
        f1_valid_forest_upsampled,
        f1_valid_logistic_balanced
    ],
    'AUC-ROC validación': [
        best_tree_result['AUC-ROC validación'],
        auc_roc_valid_forest,
        forest_unbalanced['AUC-ROC validación'],
        best_forest_result['AUC-ROC validación'],
        auc_roc_valid_forest_upsampled,
        auc_roc_valid_logistic_balanced
    ]
})

# Calcular la diferencia entre entrenamiento y validación.
model_comparison['Diferencia F1'] = (
    model_comparison['F1 entrenamiento']
    - model_comparison['F1 validación']
)

# Ordenar según el F1 de validación.
model_comparison = model_comparison.sort_values(
    by='F1 validación',
    ascending=False
).reset_index(drop=True)

# Mostrar la comparación.
model_comparison.round(4)


"""
**Resultados de la comparación y selección del mejor modelo**

La comparación de las configuraciones evaluadas permitió identificar al
bosque aleatorio entrenado mediante *upsampling* como el modelo con
mayor F1 en validación.

La configuración seleccionada utiliza `n_estimators=100`, `max_depth=10`
y `class_weight=None`, con un conjunto de entrenamiento previamente
balanceado mediante sobremuestreo.

Este modelo alcanzó un F1 de 0.6384 y un AUC-ROC de 0.8647 en
validación. Además, presentó una diferencia de 0.1620 entre F1 de
entrenamiento y validación, considerablemente menor que la observada en
el bosque aleatorio inicial.

El bosque optimizado mediante `class_weight='balanced'` obtuvo
resultados prácticamente equivalentes, con un F1 de 0.6376 y un AUC-ROC
de 0.8656. La diferencia mínima entre ambas configuraciones no permite
establecer una superioridad concluyente del sobremuestreo, aunque este
último obtuvo el mayor F1 en los experimentos realizados.

Por lo tanto, **seleccionamos el bosque aleatorio entrenado mediante
*upsampling* como candidato definitivo**, siguiendo el criterio
principal de maximizar F1 en validación.

9. Evaluación final del modelo

Una vez seleccionado el modelo, realizaremos su evaluación sobre el
conjunto de prueba, compuesto por 2,000 registros que no han intervenido
en el entrenamiento ni en la selección de hiperparámetros.

Utilizaremos el modelo seleccionado y las transformaciones de
preprocesamiento previamente establecidas, evitando introducir nuevos
ajustes basados en los resultados de prueba.

Calcularemos las siguientes métricas:

- **F1:** para comprobar si el modelo alcanza el valor mínimo de 0.59
  establecido por TripleTen.
- **AUC-ROC:** para evaluar su capacidad de distinguir entre clientes
  que abandonan el banco y aquellos que permanecen.

Compararemos los resultados de prueba con los obtenidos en validación,
con el propósito de identificar posibles diferencias de generalización.

Esta evaluación permitirá determinar si el modelo cumple el objetivo del
proyecto y establecer las conclusiones finales sobre su desempeño y
limitaciones.
"""



# Obtener las predicciones del modelo definitivo.
predictions_test_final = model_forest_upsampled.predict(
    features_test_ohe
)

# Obtener las probabilidades de la clase positiva.
probabilities_test_final = model_forest_upsampled.predict_proba(
    features_test_ohe
)[:, 1]

# Calcular las métricas sobre el conjunto de prueba.
f1_test_final = f1_score(
    target_test, predictions_test_final
)
auc_roc_test_final = roc_auc_score(
    target_test, probabilities_test_final
)

# Mostrar los resultados de la evaluación final.
print(f'F1 en prueba: {f1_test_final:.4f}')
print(f'AUC-ROC en prueba: {auc_roc_test_final:.4f}')

# Verificar el cumplimiento del requisito de TripleTen.
print(f'\nCumple F1 >= 0.59: {f1_test_final >= 0.59}')


"""
**Resultados de la evaluación final**

El bosque aleatorio seleccionado, entrenado mediante *upsampling* con
`n_estimators=100` y `max_depth=10`, obtuvo un F1 de 0.6250 y un AUC-ROC
de 0.8655 en el conjunto de prueba.

El resultado de F1 supera el mínimo de 0.59 establecido por TripleTen,
por lo que **se cumplió el objetivo principal de desempeño del
proyecto**.

En comparación con la validación, donde se obtuvo un F1 de 0.6384, la
disminución fue de 0.0134 puntos. Esta diferencia relativamente pequeña
indica que el modelo mantuvo un desempeño similar sobre datos que no
participaron en el entrenamiento ni en la selección de hiperparámetros.

Por su parte, AUC-ROC se mantuvo prácticamente constante entre
validación y prueba, lo que respalda la capacidad del modelo para
distinguir entre clientes que abandonan el banco y aquellos que
permanecen.

Es importante considerar que ambas métricas evalúan aspectos diferentes.
F1 refleja el equilibrio entre precisión y exhaustividad al utilizar un
umbral de clasificación determinado, mientras que AUC-ROC evalúa la
capacidad de discriminación considerando diferentes umbrales. Por lo
tanto, el valor de AUC-ROC complementa la evaluación, pero no sustituye
el análisis de F1 ni garantiza una clasificación correcta de todos los
clientes.

Aunque los resultados son satisfactorios respecto a los criterios
establecidos, el modelo todavía puede cometer errores de clasificación.
Sus predicciones deben interpretarse como estimaciones de riesgo y no
como certezas sobre el comportamiento futuro de cada cliente.

La evaluación final se realizó sin modificar los hiperparámetros
seleccionados ni utilizar el conjunto de prueba para realizar ajustes
adicionales, preservando la independencia de esta etapa.

10. Conclusiones generales

El proyecto permitió desarrollar y evaluar un modelo de clasificación
para predecir el abandono de clientes de Beta Bank, utilizando
información histórica sobre sus características personales, financieras
y su relación con la institución.

Durante la preparación de los datos se identificaron y trataron valores
ausentes, se excluyeron columnas identificadoras y se codificaron las
variables categóricas. Asimismo, se dividió el conjunto de datos en
entrenamiento, validación y prueba, aplicando las transformaciones
correspondientes sin utilizar información de los conjuntos reservados
para ajustar los parámetros del preprocesamiento.

El análisis de la variable objetivo reveló un desequilibrio importante
entre los clientes que permanecieron y aquellos que abandonaron el
banco. Los modelos iniciales mostraron diferentes limitaciones,
especialmente el sobreajuste de los algoritmos basados en árboles y el
bajo F1 de la regresión logística sin balanceo.

La investigación de hiperparámetros permitió mejorar la generalización
de los modelos. Además, se evaluaron dos estrategias para tratar el
desequilibrio de clases: el ajuste de pesos mediante `class_weight` y el
sobremuestreo (*upsampling*). Ambas produjeron resultados competitivos
al combinarse con una configuración adecuada del bosque aleatorio.

El modelo seleccionado fue un `RandomForestClassifier` entrenado
mediante *upsampling*, que alcanzó el mayor F1 de validación entre las
configuraciones evaluadas. Su desempeño en el conjunto de prueba
confirmó el cumplimiento del objetivo establecido, mientras que AUC-ROC
mostró una capacidad de discriminación consistente con la observada
durante la validación.

Como principales limitaciones, debemos considerar que la imputación de
valores ausentes y la repetición de registros durante el sobremuestreo
pueden influir en el aprendizaje del modelo. Asimismo, los resultados
obtenidos no garantizan que su desempeño se mantenga sin cambios al
utilizar datos de nuevos clientes.

En conclusión, **el proyecto cumplió los requisitos de desempeño y
permitió identificar un modelo con capacidad para apoyar la detección de
clientes con mayor riesgo de abandono**. Sus predicciones podrían servir
como herramienta de apoyo para orientar estrategias de retención de Beta
Bank, considerando siempre las limitaciones identificadas y la necesidad
de evaluar su funcionamiento con datos futuros.
"""
