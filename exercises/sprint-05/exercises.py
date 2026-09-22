import math as mt
from math import factorial

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats as st


"""
Supongamos que la empresa para la que trabajas actualizó la interfaz de la página del carrito
de compras en su sitio web. Tu equipo quiere saber qué tan complicada les parece a los usuarios,
así que decides estudiar el tiempo que tardan los clientes y las clientas en hacer sus pedidos,
es decir, el número de segundos que transcurren desde que un cliente inicia el proceso de compra
hasta que lo completa.

Solo un día después del lanzamiento de la nueva interfaz recibiste suficientes lecturas para
construir un histograma.

Te han proporcionado un dataset que contiene tiempos de pedido medidos en segundos y almacenados
en la variable pur_time. Tu objetivo es crear un histograma con los límites de contenedores en
los puntos [15, 30, 45, 60, 75, 90] y establecer la transparencia en 0.7.
"""


# el dataset pur_time (del inglés purchase_time que significa tiempo de compra)
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54,
                  58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38,
                  55, 53, 53, 43, 77, 44, 63, 63, 54])

pur_time.hist(bins = [15, 30, 45, 60, 75, 90], alpha = 0.7)
plt.show()



"""
Utiliza de nuevo los datos de tiempo de pedido del ejercicio 1 y construye dos histogramas con los
siguientes límites de intervalo:
- [15, 35, 55, 75, 90]
- [15, 45, 55, 90]

Establece la transparencia en 0.5 para ambos.
"""

# llamaremos al dataset `pur_time` (del inglés purchase_time que significa tiempo de compra)
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54,
                  58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38,
                  55, 53, 53, 43, 77, 44, 63, 63, 54])

pur_time.hist(bins = [15, 35, 55, 75, 90], alpha = 0.5) # escribe tu código aquí
pur_time.hist(bins = [15, 45, 55, 90], alpha = 0.5)
plt.show()

print()



"""
Tus objetivos actuales son:
1. Encontrar la media del dataset y almacenarla en la variable mean_value, utilizando un método
   apropiado.
2. Calcular la distancia entre cada valor y la media, y almacenar el valor resultante en la variable
   spacing_all. Para realizar este paso, puedes utilizar operaciones aritméticas sencillas con Series
   de pandas. Esto dará lugar a operaciones elemento por elemento, lo que significa que se realizará
   una operación en cada elemento de un Series, generando otro Series.
3. A continuación, calcula la distancia media y almacénala en la variable spacing_all_mean.
4. Imprime la variable spacing_all_mean.
"""

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Calcula la media de todos los valores
mean_value = data.mean()

# Calcula la distancia absoluta de cada valor respecto a la media
spacing_all = data - mean_value

# Calcula la media de todas las distancias
spacing_all_mean = spacing_all.mean()

print(spacing_all_mean)

print()



"""
Calcula la varianza del dataset data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]). Muestra los resultados.
"""


data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

variance = np.var(data) # calcula la varianza aquí
print(variance) # escribe tu código aquí)

print()



"""
Calcula la desviación estándar del dataset data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) y guárdala en
la variable standard_dev. Luego muestra los resultados.
"""


data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

standard_dev = np.std(data) # escribe tu código aquí
print(standard_dev) # escribe tu código aquí)

print()



"""
El usuario promedio tarda 3 segundos en leer un mensaje en un sitio web. Esta es la media del conjunto de datos.

Además, observamos que la varianza de los datos (que siguen la distribución normal) es de 0.25 segundos.

Utilizando la regla de las tres sigmas descrita anteriormente, tenemos que calcular cuánto tiempo debe mostrarse
un mensaje para que lo vea el 99.7% de los usuarios. Para ello, sigue estos pasos:
1. Calcula la desviación estándar a partir de la varianza y guarda el resultado en la variable adv_std.
2. Dadas la media y la desviación estándar, calcula el límite superior del intervalo que representa el 99.7% de
   los usuarios. Almacena el valor resultante en la variable adv_time.

Muestra tus resultados con el mensaje El tiempo de visualización del mensaje es.
"""


adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var) # calcula la desviación estándar

adv_time = adv_mean + 3 * adv_std # calcula el tiempo de visualización del mensaje
print('El tiempo de visualización del mensaje es' , adv_time) # escribe tu código aquí)

print()



"""
Tu empresa organiza un concurso tipo trivia en un centro comercial.

Por su experiencia en concursos similares, sabes que, por término medio, el 3% de los participantes responden
correctamente a las preguntas, y que la desviación estándar es del 0.4%.

Esperas que 6000 personas se presenten al concurso. Tienes que calcular cuántas personas podrían ganar para
preparar una cantidad suficiente de premios. En concreto, hay que determinar un intervalo para el número de
ganadores tal que, con un 99.7% de probabilidad, el número real esté dentro de ese intervalo (es decir, entre
x y y). Vamos a utilizar la regla de las tres sigmas para calcular dicho intervalo.

Una vez que lo hayas calculado, deberás imprimir los resultados de la siguiente manera: Intervalo: ... - ...
(¡fíjate en los espacios alrededor del guion!)

Para que esta tarea no sea tan abrumadora, vamos a desglosarla en pasos más sencillos:
1. Para empezar, calcula el promedio esperado de respuestas correctas de los participantes. Teniendo en cuenta
   el porcentaje medio de participantes que, como se espera, responderán correctamente (3% o 0.03) y el número
   previsto de participantes (6000), calcula la media y almacena el valor resultante en la variable quiz_mean.
2. A continuación, a partir del número total de participantes previstos (6000) y de un porcentaje dado para la
   desviación estándar (0.4% o 0.004), calcula la desviación estándar para el número de personas que participarán
   en el concurso. Este valor, σ, debe almacenarse en la variable quiz_std.
3. Por último, se nos pide que determinemos un intervalo para el número de ganadores. Según la regla de las tres
   sigmas, este intervalo comprende tres desviaciones estándar a la izquierda y 3 a la derecha de la media. 
   Calcula los límites de dicho intervalo y guarda el límite inferior en la variable quiz_bottom_line y el límite
   superior en la variable quiz_top_line.
4. Muestra los resultados en el formato requerido.
"""

quiz_mean = 6000 * 0.03 # calcula el número promedio de personas que responden correctamente
quiz_std = 6000 * 0.004 # calcula la desviación estándar del número total de participantes

quiz_bottom_line = quiz_mean - 3 * quiz_std # calcula el límite inferior del intervalo
quiz_top_line = quiz_mean + 3 * quiz_std # calcula el límite superior del intervalo

print('Intervalo:', quiz_bottom_line,'-', quiz_top_line) # escribe tu código aquí)

print()



"""
Después de barajar la lista, tienes que calcular la probabilidad de que la primera canción sea del grupo 'Queen'.
Escribe el código para calcularlo.

Utiliza la variable desired_outcomes para almacenar el número de resultados deseados, total_outcomes para almacenar
el número total de resultados, y probability para el resultado final. Tras hacer esto, muestra probability.
"""


cool_rock = pd.DataFrame(
   {
      'Artist': [
            'Queen',
            'Queen',
            'Queen',
            'Pink Floyd',
            'Nirvana',
            'AC/DC',
            'AC/DC',
            'Scorpions',
            'Scorpions',
            'Scorpions',
      ],
      'Song': [
            'The Show Must Go On',
            'Another One Bites The Dust',
            'We Will Rock You',
            'Wish You Were Here',
            'Smells Like Teen Spirit',
            'Highway To Hell',
            'Back in Black',
            'Wind Of Change',
            'Still Loving You',
            'Send Me An Angel',
      ],
   }
)

desired_artist = 'Queen'

desired_outcomes = len(cool_rock[cool_rock['Artist'] == desired_artist])
total_outcomes = len(cool_rock)
probability = desired_outcomes / total_outcomes
print(probability)

print()



"""
Se seleccionaron cinco candidatos para el proyecto. La responsable de RRHH quiere entrevistar a cada uno de ellos,
pero no puede decidir en qué orden va a llamar a los candidatos. Completa el siguiente código que calculará cuántas
opciones de listas se pueden hacer, en las que cinco candidatos están ordenados en un orden diferente.

Guarda el resultado de los cálculos en la variable lists_amount. Muestra la variable.
"""


candidates_amount = 5

lists_amount = factorial(candidates_amount) # agrega aquí tu código
print(lists_amount)

print()




"""
Completa el siguiente código para determinar el número de maneras para formar equipos de tres personas
seleccionándolas entre cinco candidatos.
Guarda el resultado de los cálculos en la variable combinations e imprímela.
"""


n = 5 # define aquí el número de candidatos
k = 3 # define aquí el número necesario de compañeros de equipo

combinations = factorial (n) / (factorial(k) * factorial(n-k)) # realiza aquí los cálculos principales
print(combinations)

print()



"""
Estás desarrollando con tus amigos un juego de búsqueda que consta de 10 tareas diferentes. Las tareas pueden
realizarse en cualquier orden, pero solo una secuencia de todas las existentes permite a los jugadores ganar
el superpremio. ¿Cuál es la probabilidad de ganar el superpremio, suponiendo que la probabilidad de elegir
cada tarea en cualquier fase de la búsqueda es la misma?

Completa el código siguiente para calcular la probabilidad. Utiliza las siguientes variables:

- tasks: para almacenar el número de tareas.
- permutations: para almacenar el número de permutaciones.
- probability: para almacenar la probabilidad de elegir la única secuencia de tareas que permite a los
  jugadores ganar el superpremio.
"""


tasks = 10 # introduce aquí el número de tareas
permutations = factorial(tasks) # calcula aquí el número total de secuencias de tareas posibles
probability = 1 / permutations # calcula aquí la probabilidad de seleccionar la única combinación ganadora

print(probability)

print()



"""
Como los clientes no estaban satisfechos con la dificultad de ganar el superpremio, cambiaste las reglas.
Ahora, los jugadores pueden elegir las tres tareas con las que quieren empezar el juego. El orden de las
tareas no importa, lo importante es la combinación. Si los jugadores consiguen adivinar la "combinación
secreta", recibirán un código promocional de descuento.

Para garantizar la equidad, debes calcular la probabilidad de obtener el código promocional utilizando
las siguientes variables:
- tasks: número total de tareas disponibles.
- chosen: número de tareas elegidas al principio del juego.
- combinations: número total de combinaciones posibles de 3 tareas de las 10 disponibles.
- probability: probabilidad final de obtener el código promocional.

Implementa un programa que calcule la probabilidad de obtener el código promocional utilizando las
variables anteriores.
"""


tasks = 10 # introduce aquí el número total de tareas
chosen = 3 # introduce aquí el número de tareas a elegir

combinations = factorial(tasks) / (factorial(chosen) * factorial(tasks - chosen)) # calcula el número de combinaciones disponibles
probability = 1 / combinations # calcula aquí el resultado final

print(probability)

print()



"""
Tenemos a 30 estudiantes que realizaron un examen. Sus puntuaciones se almacenan en la variable exam_results.
Si un estudiante obtuvo menos de 20 puntos, reprobó el examen. Escribe un programa que cuente cuántos
estudiantes reprobaron el examen y almacena el resultado en la variable failed_students. Muestra el resultado.
"""


exam_results = np.array(
   [
      42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
      66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
      34,  47,  64,  58,  61,  12,  30,  63,  20,  68
   ]
)


failed_students = 0 # valor inicial

# código para los cálculos
for grade in exam_results:
   if grade < 20:
      failed_students += 1

print('Número de estudiantes reprobados:', failed_students)

print()



"""
Vamos a seguir con los resultados del examen. Ahora tenemos que contar no solo a los estudiantes que reprobaron,
sino también a los que obtuvieron otros resultados: excelente (90 puntos o más), notable (70-89 puntos),
satisfactorio (50-69) y aprobado (20-49).

Crea un diccionario summarized_data y escribe código para rellenarlo con los datos necesarios.
"""


exam_results = np.array(
   [
      42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
      66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
      34,  47,  64,  58,  61,  12,  30,  63,  20,  68
   ]
)

summarized_data = {
   'excellent': 0,
   'good': 0,
   'average': 0,
   'passable': 0,
   'failed': 0
}

# Recorremos cada resultado del examen
for score in exam_results:
   if score >= 90:
      summarized_data['excellent'] += 1
   elif score >= 70:
      summarized_data['good'] += 1
   elif score >= 50:
      summarized_data['average'] += 1
   elif score >= 20:
      summarized_data['passable'] += 1
   else:
      summarized_data['failed'] += 1

# código para mostrar los resultados en pantalla. No lo cambies.
for result in summarized_data:
   print(result, '-', summarized_data[result])

print()



"""
Los portátiles de Pineapple son caros, pero siguen siendo populares entre los geeks de la informática: el 60%
de los clientes están dispuestos a comprarse una computadora portátil de esta marca si acuden a la tienda.
Los portátiles de Banana son más baratos, pero no tan populares: solo el 20% de los visitantes de la tienda
están dispuestos a comprarlos.
Supongamos que la tienda solo tiene a la venta equipos de Pineapple. ¿Cuál es la probabilidad de que 50 de cada
80 clientes realicen una compra en un día?

Guarda el resultado en la variable probability y muéstralo.

No olvides que en Python se utiliza el signo ** para la exponenciación.
"""


p = 0.6  # la probabilidad de que un cliente realice una compra
q = 0.4  # la probabilidad de que un cliente NO realice una compra
n = 80   # el número total de visitantes
k = 50   # el número de visitantes que esperamos que realicen una compra

# Calculamos el número de combinaciones posibles de k compras entre n visitantes
combinations = factorial(n) / (factorial(k) * factorial(n - k))

# Calculamos la probabilidad binomial
probability = combinations * (p ** k) * (q ** (n - k))

print(probability)

print()



"""
Supongamos que, al lado de una tienda de hardware Pineapple, hay un gran centro comercial con otra tienda que
vende computadoras Banana. 160 clientes visitan esa tienda durante el día. ¿Cuál es la probabilidad de que 50
de esos visitantes se compren una computadora portátil?

Recuerda que solo el 20% de los usuarios están dispuestos a comprar un portátil de la marca Banana.

Guarda el resultado en la variable probability y muéstralo.
"""


p = 0.2 # la probabilidad de que un cliente realice una compra
q = 0.8 # la probabilidad de que un cliente NO realice una compra
n = 160 # el número total de visitantes
k = 50 # el número de visitantes que esperamos que realicen una compra

probability = (factorial(n) / (factorial(k) * factorial(n - k))) * (p ** k) * (q ** (n - k))# escribe aquí el
# código para realizar los cálculos

print(probability)

print()



"""
El número de visitantes mensuales de una tienda virtual tiene una distribución normal con una media de 100 500
y una desviación estándar de 3 500.

Encuentra la probabilidad de que en el próximo mes el sitio web del outlet tenga:
- menos de 92 000 visitantes;
- más de 111 000 visitantes.

Completa el código siguiendo los comentarios y utiliza las sentencias print() del precódigo para mostrar tus
resultados.
"""


mu = 100500 # ¿cuál es la media de la distribución?
sigma =3500 # ¿cuál es la desviación estándar de la distribución?

more_threshold = 111000 # ¿Cuál es el límite superior del número de visitantes?
fewer_threshold = 92000 # ¿Cuál es el límite inferior del número de visitantes?

p_more_visitors = 1- st.norm(100500, 3500).cdf(more_threshold) # calcula la probabilidad de que el número de
#visitantes sea superior al umbral superior
p_fewer_visitors = st.norm(100500, 3500).cdf(fewer_threshold)# calcula la probabilidad de que el número de
#visitantes sea inferior al umbral inferior

print(f'Probabilidad de que el número de visitantes sea superior a {more_threshold}: {p_more_visitors}')
print(f'Probabilidad de que el número de visitantes sea inferior a {fewer_threshold}: {p_fewer_visitors}')

print()



"""
Otra tienda online, Fancy Pants, vende productos de regalo a un público muy limitado de clientes corporativos.
Las ventas semanales en la tienda de conjuntos de ajedrez de lujo fabricados con colmillo de mamut tienen una
distribución normal con una media de 420 y una desviación estándar de 65.

El equipo de inventario está decidiendo cuántos conjuntos pedir. Quieren que la posibilidad de venderlos todos
la próxima semana sea del 90%. ¿Cuántos deben pedir?
"""


mu = 420 # escribe tu código aquí: ¿cuál es la media?
sigma = 65 # escribe tu código aquí: ¿cuál es la desviación estándar?
prob = .9 # escribe tu código aquí: ¿cuál es la probabilidad requerida de vender todos los artículos?

n_shipment = st.norm(mu, sigma).ppf(prob) # escribe tu código aquí: ¿cuántos artículos se deben pedir?

print('Cantidad de artículos a pedir:', int(n_shipment))

print()



""""
Los precios de los pedidos realizados en una tienda virtual tienen una distribución normal con una media de 24
dólares y una desviación estándar de 3.20 dólares.

Algunos clientes eligen la entrega rápida por mensajería, que tiene un precio fijo independientemente del valor
del pedido.

Los clientes tienden a molestarse cuando el costo de la entrega es igual al costo del pedido. ¿Cuánto debería
costar el envío por mensajería para que no supere el precio del pedido en el 75% de los casos?
"""


mu = 24 # coloca tu código aquí: ¿cuál es la media de la distribución?
sigma = 3.20 # coloca tu código aquí: ¿cuál es la desviación estándar de la distribución?
threshold = .75 # coloca tu código aquí: ¿qué porcentaje de pedidos debería costar más del doble del costo de envío?

max_delivery_price = st.norm(mu, sigma).ppf(1 - threshold) # coloca tu código aquí: el costo máximo de envío

print('Costo máximo de envío por mensajería:', max_delivery_price)

print()



"""
Una empresa envía a sus clientes un boletín electrónico mensual con novedades y ofertas de los socios. Sabemos
que el 40% de los clientes abre el boletín.

Uno de los socios está planeando una campaña publicitaria y espera llegar a unos 9000 clientes. Calcula la
probabilidad de que se cumplan las expectativas del socio si el boletín se envía a 23 000 personas.

En el ejemplo anterior, hemos creado una variable llamada clicks. Aquí, crea otra llamada threshold y guarda
el valor 9000 en ella. Que el tamaño de la población sea binom_n y que la probabilidad de que se abra el
boletín sea binom_p.

Guarda la probabilidad de que se cumplan las expectativas del socio como p_threshold y muéstrala.
"""


# escribe tu código aquí
binom_n = 23000
binom_p = 0.40
threshold = 9000

# calculamos el valor esperado de éxitos y sigma
mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

# calculamos la probabilidad de cumplir expectativas
p_threshold = 1- st.norm(mu, sigma).cdf(threshold)
print(p_threshold)

print()



"""
Eres el dueño de una cadena de estaciones de alquiler de patinetes llamada Scooters Get You There. Hay 20
locales en el centro de la ciudad y cada uno tiene un máximo de 50 patinetes eléctricos. Quieres probar la
hipótesis de que en el último mes hubo un promedio de 30 patinetes disponibles en cualquier estación durante
el día. Un grupo urbano llamado 'Squirrel' destacó la importancia de este número en su estudio de la movilidad
de los residentes. Si hay menos patinetes en la estación, los usuarios pensarán que no podrán alquilar uno
cuando lo necesiten, pero cuando haya más, la gente pensará que no podrán aparcar su patinete después de un
viaje porque no habrá aparcamiento.

Cada hora, cada estación envía el número de patinetes disponibles al servidor. Has descargado los números de
13:00 a 16:00 durante los últimos 30 días. Prueba tu hipótesis usando esta muestra. Establece un umbral de 5%
para la significación estadística.
"""


scooters = pd.Series([15, 31, 10, 21, 21, 32, 30, 25, 21,
28, 25, 32, 38, 18, 33, 24, 26, 40, 24, 37, 20, 36, 28, 38,
24, 35, 33, 21, 29, 26, 13, 25, 34, 38, 23, 37, 31, 28, 32,
24, 25, 13, 38, 34, 48, 19, 20, 22, 38, 28, 31, 18, 21, 24,
31, 21, 28, 29, 33, 40, 26, 33, 33,  6, 27, 24, 17, 28,  7,
33, 25, 25, 29, 19, 30, 29, 22, 15, 28, 36, 25, 36, 25, 29,
33, 19, 32, 32, 28, 26, 18, 48, 15, 27, 27, 27,  0, 28, 39,
27, 25, 39, 28, 22, 33, 30, 35, 19, 20, 18, 31, 44, 20, 18,
17, 28, 17, 44, 40, 33,])

optimal_value = 30 # escribe tu código aquí

alpha = 0.05 # establece la significación estadística crítica

results = st.ttest_1samp(
   scooters,
   optimal_value
) # realiza la prueba t

print('valor p: ', results.pvalue) # extrae el valor p de los resultados de la prueba

if (results.pvalue < alpha): # compara el valor p con el umbral alpha
   print('Rechazamos la hipótesis nula')
else:
   print("No podemos rechazar la hipótesis nula")

print()



"""
El 1 de junio de 2019 tomaste un curso del famoso coach y empresario llamado Robby Tobbinson. Si aplicas sus
exclusivas técnicas conscientes de negocio se garantiza que tu proyecto online generará al menos $800 por día,
quizás más, en solo un mes. Él te lo promete.

Las promesas están bien pero las pruebas estadísticas son mejores. Vamos a ver qué nos dicen los números.

Utiliza un dataset con los ingresos diarios del último mes para probar tu hipótesis. La hipótesis es que tus
ingresos diarios promedio igualaron o superaron los $800.

Recuerda: la hipótesis que contiene el signo de igualdad suele ser la hipótesis nula. Por lo tanto, "Todo saldrá
como lo predijo el coach" es tu hipótesis nula y "Los ingresos serán menores de lo que se predijo" es la hipótesis
alternativa. Las desviaciones aleatorias siempre son posibles. Solo puedes decir "¡La metodología de Tobbinson no
funcionó!" si tus ingresos son significativamente inferiores a la cantidad propuesta.
"""


revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

interested_value = 800 # ¿cuánto prometió Robby Tobbinson?

alpha = 0.05 # indica el nivel de significación estadística

results = st.ttest_1samp(revenue, interested_value) # utiliza la función st.ttest_1samp()

print('valor p:', results.pvalue/2) # imprime el valor p para una prueba unilateral)

if (results.pvalue / 2 < alpha) and (revenue.mean() < interested_value): # compara el valor obtenido y el nivel crítico de significación estadística
   # y verifica si la media muestral está en el lado correcto del interested_value):
   print(
      "Rechazamos la hipótesis nula: los ingresos fueron significativamente inferiores a 800 dólares"
   )
else:
   print(
      "No podemos rechazar la hipótesis nula: los ingresos no fueron significativamente inferiores"
   )

print()



"""
1. Hay dos conjuntos de datos: el tiempo promedio que pasan en un sitio web 1) los usuarios que inician sesión
con nombre de usuario y contraseña, y 2) los usuarios que inician sesión a través de las redes sociales. Prueba
la hipótesis de que ambos grupos de usuarios pasan la misma cantidad de tiempo en el sitio web.
"""


# tiempo pasado en el sitio web por usuarios con un nombre de usuario y contraseña
time_on_site_logpass = [368, 113, 328, 447, 1, 156, 335, 233, 
                     308, 181, 271, 239, 411, 293, 303, 
                     206, 196, 203, 311, 205, 297, 529, 
                     373, 217, 416, 206, 1, 128, 16, 214]

# tiempo pasado en el sitio web por los usuarios que inician sesión a través de las redes sociales
time_on_site_social  = [451, 182, 469, 546, 396, 630, 206, 
                        130, 45, 569, 434, 321, 374, 149, 
                        721, 350, 347, 446, 406, 365, 203, 
                        405, 631, 545, 584, 248, 171, 309, 
                        338, 505]


# tu código va debajo

alpha = 0.05 # tu código: establece un nivel crítico de significación estadística

results = st.ttest_ind(time_on_site_logpass,time_on_site_social) # tu código: prueba la hipótesis de que las medias de las dos poblaciones independientes son iguales

print('valor p:', results.pvalue) # tu código: imprime el valor p obtenido

if results.pvalue < alpha: # tu código: compara los valores p obtenidos con el nivel de significación estadística):
   print("Rechazamos la hipótesis nula")
else:
   print("No podemos rechazar la hipótesis nula")

print()



"""
2. Tenemos dos datasets: la profundidad de la visita al sitio web de diferentes grupos de usuarios para los meses
de verano y otoño. Prueba la hipótesis de que las profundidades de visita de los sitios web son iguales. Por
ejemplo, puede ser que en verano los visitantes no se sumerjan tanto en el contenido, lo que sería algo a tener
en cuenta al planificar una campaña publicitaria para los meses de verano. Vamos a establecer el nivel de
significación en 0.05.

No esperamos que las varianzas sean las mismas así que establece el parámetro equal_var en False.  Puedes ejecutar
np.var(pages_per_session_autumn) etcétera para verificar la varianza del conjunto.
"""


pages_per_session_autumn = [7.1, 7.3, 9.8, 7.3, 6.4, 10.5, 8.7, 
                           17.5, 3.3, 15.5, 16.2, 0.4, 8.3, 
                           8.1, 3.0, 6.1, 4.4, 18.8, 14.7, 16.4, 
                           13.6, 4.4, 7.4, 12.4, 3.9, 13.6, 
                           8.8, 8.1, 13.6, 12.2]
pages_per_session_summer = [12.1, 24.3, 6.4, 19.9, 19.7, 12.5, 17.6, 
                           5.0, 22.4, 13.5, 10.8, 23.4, 9.4, 3.7, 
                           2.5, 19.8, 4.8, 29.0, 1.7, 28.6, 16.7, 
                           14.2, 10.6, 18.2, 14.7, 23.8, 15.9, 16.2, 
                           12.1, 14.5]

alpha = 0.05 # tu código: establece un nivel crítico de significación estadística

results = st.ttest_ind(pages_per_session_autumn, pages_per_session_summer, equal_var = False) # tu código: prueba la hipótesis de que las medias de las dos poblaciones independientes son iguales

print('valor p:', results.pvalue) # tu código: imprime el valor p obtenido

if results.pvalue < alpha:# su código: compara los valores p obtenidos con el nivel de significación estadística):
   print("Rechazamos la hipótesis nula")
else:
   print("No podemos rechazar la hipótesis nula")

print()



"""
1. Tenemos dos datasets: el tiempo que un grupo de usuarios pasó en sus páginas personales en un sitio web, registrado
antes y después de que se rediseñó la página personal. Prueba la hipótesis de que el tiempo que pasan allí cambió
(aumentó o disminuyó) después del rediseño.

Piensa en la frase "el tiempo que pasan allí cambió" de la hipótesis anterior. ¿Sugiere la necesidad de una prueba
unilateral o bilateral?
"""


time_before = [1732, 1301, 1540, 2247, 1632, 1550, 754, 1946, 1889, 
         2748, 1349, 1648, 1665, 2416, 1470, 1681, 1868, 1629, 
         1271, 1633, 2131, 942, 1599, 1127, 2200, 661, 1207, 
         1737, 2410, 1486]

time_after = [955, 2577, 360, 139, 1618, 990, 644, 1796, 1487, 949, 472, 
         1906, 1758, 1258, 2554, 612, 309, 1864, 1294, 1487, 1164, 1559, 
         491, 2286, 1270, 2069, 1553, 1629, 1704, 1623]

alpha = 0.05 # tu código: establece un nivel crítico de significación estadística

results = st.ttest_rel(time_before, time_after) # tu código: realiza la prueba y calcula el valor p

print('valor p:', results.pvalue) # tu código: imprime el valor p obtenido

if results.pvalue < alpha: #tu código: compara el valor p con el nivel de la significación estadística):
   print("Rechazamos la hipótesis nula")
else:
   print("No podemos rechazar la hipótesis nula")

print()



"""
2. Tenemos dos datasets: la cantidad de balas compradas por jugadores apasionados de un juego online, antes y
después de introducir una mecánica que proporcionó incentivos para disparar en ráfagas. Prueba la hipótesis de
que los jugadores empezaron a usar más balas después de que se introdujo la nueva característica.

Piensa en la palabra "más" de la hipótesis anterior. ¿Sugiere la necesidad de una prueba unilateral o bilateral?
"""


bullets_before = [821, 1164, 598, 854, 455, 1220, 161, 1400, 479, 215, 
         564, 159, 920, 173, 276, 444, 273, 711, 291, 880, 
         892, 712, 16, 476, 498, 9, 1251, 938, 389, 513]

bullets_after = [904, 220, 676, 459, 299, 659, 1698, 1120, 514, 1086, 1499, 
         1262, 829, 476, 1149, 996, 1247, 1117, 1324, 532, 1458, 898, 
         1837, 455, 1667, 898, 474, 558, 639, 1012]

print('media anterior:', pd.Series(bullets_before).mean())
print('media posterior:', pd.Series(bullets_after).mean())

alpha = 0.05 # tu código: establece un nivel crítico de significación estadística

results = st.ttest_rel(
   bullets_before, 
   bullets_after)

print('valor-p:', results.pvalue / 2) # tu código: imprime el valor p obtenido)

if (results.pvalue / 2 < alpha) and (pd.Series(bullets_after).mean() > pd.Series(bullets_before).mean()): #tu código: compara el valor p con la significación estadística):
   print("Rechazamos la hipótesis nula")
else:
   print("No podemos rechazar la hipótesis nula")

print()