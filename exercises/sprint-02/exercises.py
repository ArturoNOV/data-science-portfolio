clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
]

elite_clients = [] # añade elite clients aquí

for client in clients:
		if client[3] > 200000:  # <escribe tu logica>
			elite_clients.append(client)  # escribe tu código aquí
print(elite_clients)

clients = [
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vacías para agregar clientes
neo = []
plus = []

for client in clients:
        if client[2] < 40:
            neo.append(client)
        else:
            plus.append(client)
# escribe tu código aquí

print(neo)


countries = ['France', 'Italy', 'New Zealand', 'Italy', 'France', 'USA']

# empieza a escribir tu bucle for aquí
for country in countries:
    if country == 'USA':
        print('The movie was released in the USA.')
    elif country == 'Italy':
        print('Il film e stato rilasciato in Italia.')
    elif country == 'France':
        print('Le film est sorti en France.')
    else:
        print('Country not defined.')

ratings = [91, 35, 65, 89, 78, 93]

for rate in ratings:
    if rate < 59:
        print('mala')
    else:
        print('buena')
        
clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vacías para agregar clientes
standard = [] # 1 - 100,000
plus = [] # 100,001 - 200,000
elite = [] # 200,001 - 300,000
executive = [] #>300,001

# escribe tu código aquí
for client in clients:
    if client[3] > 1 and client[3] <= 100000:
        standard.append(client)
    elif client[3] > 100000 and client[3] <= 200000:
        plus.append(client)
    elif client[3] > 200000 and client[3] < 300001:
        elite.append(client)
    else:
        executive.append(client)
print(executive)


""" Trabajas como analista de datos en una plataforma de streaming.
Has recibido un dataset con películas populares que será usado para análisis de tendencias.
Durante la revisión de calidad, detectas un error: aparece "The Lord of the Rings: The Return of the King" (2003)
, pero debe ser reemplazada por la primera entrega de la saga, "The Fellowship of the Ring" (2001).
"""

movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1993, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_to_change = "The Lord of the Rings: The Return of the King"
new_movie = "The Lord of the Rings: The Fellowship of the Ring"
new_year = 2001

for movie in movies:
    if movie[0] == movie_to_change:
        movie[0] = new_movie
        movie[1] = new_year

# no modifiques el código de abajo, ya que imprime el resultado
for movie in movies:
    print(movie)


"""Trabajaremos en una tabla con las siguientes columnas:
Name (Nombre), Salary(Salario), Position (Posición) y Seniority Level (Nivel de rango).
Aumentaremos el salario de un empleado en específico y, si el nuevo salario supera un determinado umbral especificado, actualizaremos su Seniority Level.

Por ejemplo, veremos lo siguiente: 

name_to_update = "Alicia" (empleado a analizar)
salary_increase = 10.000 (valor en el que se incrementará su salario)
salary_threshold = 80.000 (límite para cambiar de rango, si el salario actualizado supera ese tope se deberá actualizar su rango)
new_seniority = "Senior" (nuevo rango a implementar si supera el tope salarial)
Entonces, si al salario actual de Alicia le sumo $10.000 y el resultado supera los $80.000, entonces su rango se deberá cambiar a Senior."""


employees = [
    ['Alice', 75000, 'Desarrollador', 'Júnior'],
    ['Bob', 68000, 'Diseñador', 'Semi sénior'],
    ['Charlie', 78000, 'Desarrollador', 'Júnior'],
    ['David', 85000, 'Gerente', 'Sénior'],
    ['Eve', 80000, 'Desarrollador', 'Semi sénior']
]

# Define el nombre que actualizarás, el incremento de salario y el umbral especificado de salario para el cambio de antigüedad
name_to_update = "Alice"
salary_increase = 10000
salary_threshold = 80000
new_seniority = "Sénior"

## TU CÓDIGO ##
# Modifica la tabla
for employee in employees: #por cada empleado
    if employee[0] == name_to_update:
        employee[1] += salary_increase
        if employee[1] >= salary_threshold:
            employee[3] = new_seniority

# Mostrar la tabla actualizada
print(employees)


"""En este ejercicio, vamos a practicar cómo filtrar aquellas películas de origen estadounidense utilizando la lista anidada movies_info.
Es importante entender que cada elemento de movies_info, es una lista con la siguiente estructura: [Título, País, Año, Género, Duración, Puntuación].
Teniendo clara esta estructura:

1.Inicia una lista vacía llamada movies_filtered para almacenar las películas filtradas.
2.Utiliza un bucle for para recorrer cada sublista (película) en movies_info.
3.Dentro del bucle, utiliza una sentencia if para verificar si el elemento en el índice 1 de la sublista actual equivale a "USA".
4.Si la condición del paso 3 es verdadera, agrega la sublista completa (la película) a la lista movies_filtered con .append().
5.Una vez haya terminado el bucle, muestra en pantalla la lista movies_filteredpara ver las películas filtradas.
"""

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

movies_filtered = [] # lista vacía para almacenar el resultado


# escribe tu código aquí
for movie in movies_info:
    if movie[1] == 'USA':
        movies_filtered.append(movie)


# muestra el resultado
print(movies_filtered)


"""Sigamos filtrando nuestra movies_info. En esta ocasión, tu tarea será obtener la información
asociada al nombre, país, año, género, duración y puntuación para aquellas películas que excedan
los 180 minutos de duración. Utiliza una nueva lista para almacenar la información de aquellas
películas que cumplan este criterio (movies_filtered).

Sigue los mismos pasos del ejercicio anterior, iterando  a través de la lista y almacenando
aquella información que cumpla con el criterio de minutos de duración. Muestra esta lista
cuando hayas terminado.
"""

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

movies_filtered = [] # lista vacía para almacenar el resultado

# escribe tu código aquí
for movie in movies_info:
    if movie[4] > 180:
        movies_filtered.append(movie)

# muestra el resultado
print(movies_filtered)

"""
Siguiendo la misma linea con la que venimos trabajando en nuestros anteriores ejercicios,
tu tarea esta vez consistirá en obtener todas aquellas películas cuyo origen sea de USA y
de 1990 en adelante. En esta ocasión, conserva solo las columnas para el nombre y el año,
que debes almacenar en la variable usa_movies_filtered. Finalmente, muestra la tabla
resultante (lista de listas).
"""

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

usa_movies_filtered = [] # lista vacía para almacenar el resultado

# escribe tu código aquí
for movie in movies_info:
    if movie[1] == 'USA' and movie[2] >= 1990:
        usa_movies_filtered.append([movie[0], movie[2]])

# muestra el resultado
print(usa_movies_filtered )


"""
En esta tarea deberás:

-Crear una lista vacía llamada movies_filtered.
-Filtrar aquellas películas estrenadas en 1994 o que tienen un calificación menor a 8.5.
-Guardar esas películas filtradas en movies_filtered.

Es decir, deberás crear una lista vacía llamada movies_filtered y luego añadirle las películas
que fueron estrenadas en 1994 o que tienen una calificación inferior a 8.5. 
"""

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

# crear una lista vacía llamada movies_filtered
movies_filtered = []

for movie in movies_info:
    if movie[2] == 1994 or movie[5] < 8.5:
        movies_filtered.append(movie)

# no modifiques el código de abajo ya que imprime el resultado final
for movie in movies_filtered:
    print(movie) 



"""
Ejercicio 1
Es el Día de la Juventud, y el equipo de marketing quiere enviar un correo especial dirigido a nuestros clientes jóvenes.

Tu tarea es aplicar nuevos filtros combinados de ingresos y edad para clasificar a los clientes en dos nuevas categorías:

elite_young: Clientes con un ingreso anual entre $200.000 (exclusive) y $300.000 (inclusive) y edad menor a 35 años.
executive_young: Clientes con un ingreso anual superior a $300.000 (exclusive) y edad menor a 35 años.
Deberás actualizar el filtrado de los clientes utilizando estas reglas y asignarlos a la lista correspondiente.

Al final, imprime únicamente la lista executive_young.
"""

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"]
]

elite_young = []
executive_young = []

for client in clients:
        if client[3] > 200000 and client[3] <= 300000 and client[2] < 35:
            elite_young.append(client)
        elif client[3] > 300000 and client[2] < 35:
            executive_young.append (client)
    # Completa tu código

# no modifiques nada por debajo de esta línea
print(executive_young)


"""
De nuevo, es hora de practicar un poco.

Crea un diccionario llamado movies que incluya las siguientes cuatro películas. 
El nombre de la película será la clave y el año de estreno será el valor:

Her, 2013
Big Eyes, 2014
Taxi Driver, 1976
The King of Comedy, 1982
Una vez creado, muestra el diccionario en la pantalla.
"""

movies = {
    'Her': 2013,
    'Big Eyes': 2014,
    'Taxi Driver': 1976,
    'The King of Comedy': 1982
}

print(movies)



"""
Ejercicio 1
Con el fin de facilitar el acceso a los datos de sus clientes, el equipo de gestión del Banco ABC
te ha pedido que reorganices la siguiente lista.

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"]
]
Reorganizaremos la información contenida en clients, una lista anidada donde cada sublista
representa un cliente que contiene la siguiente información en orden: [id, client_name, age, yearly_income, work_field].

Para ello:

1. Vamos utilizar un bucle for para recorrer cada sublista dentro de clients.
2. Dentro del bucle, crearemos un diccionario llamado client_info para almacenar la información de cada cliente.
3. Asignaremos los valores de cada sublista a las claves correspondientes en el diccionario client_info. Las claves serán: 1. "id". 2. "client_name". 3. "age". 4. "yearly_income". 5. "work_field".
4. Después de crear el diccionario, lo mostraremos en pantalla para verificar que la información se haya organizado correctamente.

En este ejercicio, solo debes completar dos líneas:

- Completar el valor de la clave "client_name" usando el dato correcto desde la sublista.
- Completar la línea de código para "work_field".
"""

clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"]
]

for client in clients:
    client_info = {
        "id": client[0],
        "client_name": client[1],  # completa usando el índice correcto
        "age": client[2],
        "yearly_income": client[3],
        "work_field": client[4]  # completa la línea para asignar el campo laboral
    }
    print(client_info)



"""
Recupera el precio de las acciones de 'Walmart' accediendo al valor correspondiente del diccionario usando la clave
y luego asígnalo a la variable walmart_price. Muestra walmart_price cuando se extraiga el precio.
"""

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

walmart_price = financial_info['Walmart']
print(walmart_price)



"""
Accede al precio de las acciones de 'Nike' del diccionario usando el método get(). Al llamar a get(),
None debe ser el valor devuelto si 'Nike' no se encuentra como clave.
"""

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

nike_price = financial_info.get('Nike')
print(nike_price)



"""
Ejercicio 1
Administras una pequeña tienda en línea y llevas un control del inventario en un diccionario anidado. Cada producto tiene:
- Un precio (price)
- Una cantidad disponible (quantity)
- Un descuento (discount), que en este ejercicio no usaremos

Tu objetivo es:
- Recorrer los productos
- Calcular el ingreso total sin aplicar descuentos, es decir: precio × cantidad
- Mostrar el resultado total con el formato: "Ingresos totales: $<total>"

Tu script debe mostrar en pantalla los ingresos totales de la venta de todos los productos.
"""

# Diccionario anidado con los productos en inventario
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Paso 1: Inicializa la variable para almacenar el total
total_cost = 0

# Paso 2: Recorre cada producto
for product in products:
    # Accede al precio y a la cantidad
    price = products[product]['price']
    quantity = products[product]['quantity']

    # Paso 3: Calcula el ingreso por producto y acumúlalo
    ### TU CÓDIGO AQUÍ ###
    total_cost += price * quantity

# Paso 4: Muestra el resultado final
print(f"Ingresos totales: ${total_cost}")



"""
Ejercicio 2
Continuemos trabajando con nuestra pequeña tienda online.
Ya sabemos que cada producto de tu tienda tiene un precio, una cantidad disponible en stock
y un descuento que puedes ofrecer a los clientes. Realizas un seguimiento de esta información
en un diccionario donde cada clave es el nombre del producto y el valor es otro diccionario
que contiene price (el precio), quantity (la cantidad) y discount (el descuento).

En esta ocasión deberás identificar el producto más caro en tu inventario. Para esto vamos
a reutilizar el código del ejercicio anterior, donde debes realizar dentro del bucle un
seguimiento del producto más caro. 

Tu script debe mostrar los ingresos totales de la venta de todos los productos
y mostrar el producto con el precio más alto.
"""

# Diccionario anidado que representa los productos
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Inicializa las variables
total_cost = 0
most_expensive_product = ""
highest_price = 0

# Calcula el costo total y encuentra el producto más caro
for product in products:
    # Accede a los detalles del producto
    price = products[product]['price']
    quantity = products[product]['quantity']

    # Calcula el costo de cada producto
    cost = price * quantity
    total_cost += cost

    # Comprueba si el producto actual es el más caro
    ### AQUÍ VA TU CÓDIGO ###
    if price > highest_price:
        highest_price = price
        most_expensive_product = product
        
# Muestra los resultados
print(f"Ingresos totales: ${total_cost}")
print(f"Producto más caro: {most_expensive_product}")



"""
Ejercicio 3
Una vez más, seguiremos trabajando con tu tienda en línea.

Recuerda que cada producto tiene:
- un precio (price),
- una cantidad disponible (quantity)
- y un descuento (discount) que puedes ofrecer a los clientes.

Toda esta información se almacena en un diccionario anidado, donde cada clave
es el nombre del producto y el valor es otro diccionario con los tres atributos anteriores.

Anteriormente:
1. Identificaste el producto más caro del inventario (basado en su precio original).
2. Calculaste los ingresos totales.

Ahora, completarás el ejercicio. Tu objetivo es:
1. Reducir el precio del producto más caro en un 10%, es decir, multiplicarlo por 0.9.
2. Aplica y guarda este cambio directamente en el diccionario products.
3. Finalmente, muestra dos cosas:
    - Los ingresos totales.
    - El nombre del producto más caro, junto con su precio actualizado.
"""

# Diccionario anidado que representa los productos
products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

# Inicializa las variables
total_cost = 0
most_expensive_product = ""
highest_price = 0

# Calcula el costo total y encuentra el producto más caro
for product in products:
    # Accede a los detalles del producto
    price = products[product]['price']
    quantity = products[product]['quantity']

    # Calcula el costo de cada producto
    cost = price * quantity
    total_cost += cost

    # Comprueba si el producto actual es el más caro
    if price > highest_price:
        highest_price = price
        most_expensive_product = product

# Actualiza el precio del producto más caro (reducirlo en un 10%)
products[most_expensive_product]['price'] *= 0.9


# Muestra los resultados
print(f"Ingresos totales: ${total_cost}")
print(f"Producto más caro: {most_expensive_product} (Precio actualizado a ${products[most_expensive_product]['price']})")



"""
Añade un nuevo elemento al diccionario financial_info. Usa 'Microsoft' como clave y 208.35 como valor.
Cuando termines, muestra financial_info en la pantalla.
"""

financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

# agrega un nuevo par aquí
financial_info['Microsoft'] = 208.35

print(financial_info)



"""
Ejercicio 1
El departamento de marketing de ABC quiere conocer los ingresos de cada área donde trabajan sus clientes.
Te han solicitado recopilar esta información.

En el precódigo, de forma similar al ejercicio anterior, una lista de clients. Aquí tienes esta nueva versión:

clients = [
    [32456, "Jack Wilson", 31, 150000, "Healthcare"],
    [34591, "Nina Brown", 43, 250000, "Telecom"],
    [37512, "John Smith", 32, 210000, "IT"],
    [39591, "Brian Perez", 49, 340000, "Healthcare"],
    [45123, "Brian Lee", 48, 75000, "Telecom"],
    [47635, "David Chen", 56, 180000, "Telecom"],
    [49571, "Brian Chen", 52, 220000, "IT"],
    [50391, "David Rodriguez", 31, 120000, "IT"],
    [34556, "Lucas Hernandez", 37, 180000, "Healthcare"]
]

Además de eso, en el precódigo, inicializamos un diccionario llamado incomes_per_field. Tu objetivo es llenarlo. 
- Las claves serán las áreas en los que trabajan los clientes de ABC
- Los valores serán listas con los ingresos de todos los clientes de ABC que trabajan en cada área correspondiente

A continuación se muestra un ejemplo de un par clave-valor:
          'Healthcare': [150000, 340000, 180000]

La clave es el campo ("Healthcare") y los valores son los ingresos de clientes de la lista clients que trabajan
en "Healthcare" (Salud). En este caso 1 solo cliente trabaja en salud ( "Jack Wilson") y cobra 150000. 

Para llenar el diccionario incomes_per_field, itera sobre la lista clients y extrae el nombre del campo y 
los ingresos de cada cliente. A continuación, comprueba si el campo extraído existe en el diccionario incomes_per_field:

Si no es así, agrégalo como clave y establece una lista con un único ingreso como valor.
Si existe, añade el ingreso a la lista de ingresos.
"""

clients = [
    [32456, "Jack Wilson", 31, 150000, "Healthcare"],
    [34591, "Nina Brown", 43, 250000, "Telecom"],
    [37512, "John Smith", 32, 210000, "IT"],
    [39591, "Brian Perez", 49, 340000, "Healthcare"],
    [45123, "Brian Lee", 48, 75000, "Telecom"],
    [47635, "David Chen", 56, 180000, "Telecom"],
    [49571, "Brian Chen", 52, 220000, "IT"],
    [50391, "David Rodriguez", 31, 120000, "IT"],
    [34556, "Lucas Hernandez", 37, 180000, "Healthcare"]
]

incomes_per_field = {} # aquí colocarás los ingresos para cada campo

for client in clients:
    field = client[4]
    income = client[3]
    if incomes_per_field.get(field) == None:
        incomes_per_field[field] = [income]
    else:
        incomes_per_field[field] += [income]

# no modifiques el código de abajo, ya que imprime el resultado
print(incomes_per_field)



"""
Tu objetivo es crear una función que reciba un único parámetro, el nombre y apellido de un tenista.
Con esta información, tu función debe ser capaz de agregarle, a dicho texto, el siguiente string: es un tenista. 
"""

def tenis_players(fname):
    result = str(fname) + " es un tenista"
    return result # escribe tu código aquí

print(tenis_players('Rafael Nadal'))
print(tenis_players('Novak Djokovic'))
print(tenis_players('Roger Federer'))



"""
Ejercicio 1
Imagina que tienes la siguiente lista anidada de clientes del banco ABC, con la siguiente estructura [id, client_name, age, yearly_income, work_field]:

clients_list = [
        [47635, "David Kim", 36, 180000, "Finance"],
        [49571, "Samantha Chen", 42, 220000, "Retail"],
        [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
        [34556, "Lucas Hernandez", 37, 75000, "Education"],
        [64291, "Jessica Li", 25, 125000, "IT"],
        [104556, "William Brown", 38, 289000, "Finance"],
        [105491, "Emily Smith", 29, 193000, "Healthcare"],
        [107512, "Michael Perez", 53, 415000, "Transportation"]]
Programa una función, llamada filter_clients, que permita filtrar una lista de clientes según el área de trabajo del cliente. Por ejemplo, “IT”. 

Para ello, tu función deberá:

Recibir dos parámetros: la lista de clientes con la que deberá trabajar y el work_field que estoy buscando filtrar.
Definir dentro de la función una variable llamada field, la cual almacenará el área de trabajo por el que se busca filtrar a los clientes.
Utiliza el valor "Finance".
Recorrer cada cliente de la lista. Si se encuentra uno que coincida con el campo a filtrar, la información de este cliente se debe añadir
a una nueva lista.
Esta nueva lista se devolverá como resultado de ejecutar la función cuando se termine de recorrer la lista completa de clientes.
"""

clients_list = [
        [47635, "David Kim", 36, 180000, "Finance"],
        [49571, "Samantha Chen", 42, 220000, "Retail"],
        [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
        [34556, "Lucas Hernandez", 37, 75000, "Education"],
        [64291, "Jessica Li", 25, 125000, "IT"],
        [104556, "William Brown", 38, 289000, "Finance"],
        [105491, "Emily Smith", 29, 193000, "Healthcare"],
        [107512, "Michael Perez", 53, 415000, "Transportation"]]


# crea aquí tu función filter_clients. Usar la lista de clientes y el field como parámetros
def filter_clients(clients, field):
    result = []
    for client in clients:
        if client[4] == field:
            result.append(client)
    return result

filtered_list = filter_clients(clients_list, "Finance")

# muestra el resultado
print(filtered_list)



"""
El siguiente fragmento de código contiene operaciones repetitivas. 
Tu trabajo en esta tarea simplemente consiste en calcular el precio total multiplicando el número de artículos por su precio.

En esta primera instancia, debes escribir una función llamada calculate_total_price que calcule el precio total por artículo. 

item_price_1 = 20.0
item_quantity_1 = 20

item_price_2 = 30.0
item_quantity_2 = 1

item_price_3 = 10.0
item_quantity_3 = 6

# Calcula el total para el primer artículo
item_total_1 = item_price_1 * item_quantity_1

# Calcula el total para el segundo artículo
item_total_2 = item_price_2 * item_quantity_2

# Calcula el total para el tercer artículo
item_total_3 = item_price_3 * item_quantity_3

print(item_total_1)
print(item_total_2)
print(item_total_3)
"""

# escribe aquí tu código para definir una función
def calculate_total_price(price, quantity):
    total = price * quantity
    return total


# Define los precios y la cantidad de los tres artículos
item_price_1 = 20.0
item_quantity_1 = 20

item_price_2 = 30.0
item_quantity_2 = 1

item_price_3 = 10.0
item_quantity_3 = 6


# Llama a la función para cada artículo y almacena el resultado en una variable
item_total_1 = calculate_total_price(item_price_1, item_quantity_1)
item_total_2 = calculate_total_price(item_price_2, item_quantity_2)
item_total_3 = calculate_total_price(item_price_3, item_quantity_3)


# Imprime el precio total de cada artículo del carrito
print(item_total_1)
print(item_total_2)
print(item_total_3)



"""
Siguiendo con el ejemplo anterior, en esta ocasión podemos hacer un 10% de descuento si la cantidad de ítems
es superior a 5. Para ello, multiplicamos el total por 0.9. Tu objetivo es actualizar la función llamada 
calculate_total_price para que pueda calcular los precios con el descuento. 

El resultado esperado es este: 
"""

# Define una función que tome dos parámetros: precio y cantidad
def calculate_total_price(price, quantity):
    # Calcula el precio total de un artículo concreto del carrito
    total = price * quantity
		## COMPLETA AQUI EL CODIGO
    if quantity > 5:
        total *= 0.9
    # Devuelve el precio total de ese artículo del carrito
    return total


# Define los precios y la cantidad de los tres artículos
item_price_1 = 20.0
item_quantity_1 = 20

item_price_2 = 30.0
item_quantity_2 = 1

item_price_3 = 10.0
item_quantity_3 = 6


# Llama a la función para cada artículo y almacena el resultado en una variable
item_total_1 = calculate_total_price(item_price_1, item_quantity_1)
item_total_2 = calculate_total_price(item_price_2, item_quantity_2)
item_total_3 = calculate_total_price(item_price_3, item_quantity_3)


# Imprime el precio total de cada artículo del carrito
print(item_total_1)
print(item_total_2)
print(item_total_3)



"""
Ejercicio
Eres responsable de una pequeña biblioteca. Tienes un inventario de libros almacenado como una lista de diccionarios. 
Cada libro tiene un titulo, un autor y un estado de disponible  (True si está disponible, False si está prestado).

Antes de comenzar, observa la estructura del inventario:

[
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": False}
]
Cada entrada representa un libro con su título, autor y disponibilidad.

Objetivo:
Tu tarea es construir una función que permita verificar si un libro específico está disponible en el inventario.

Debes implementar la función check_availability(titulo), que:

Recorra el inventario (inventory).
Busque el libro por su titulo.
Muestre si está disponible.
Si el libro no existe, debe mostrar que no está en el inventario.
Descomposición de la tarea:

Definir la función check_availability(titulo).
Usar un bucle for para recorrer cada libro en el inventario.
Comparar el titulo proporcionado con el título de cada libro en el inventario y comprobar su estado de disponibilidad (disponible).
Mostrar el estado de disponibilidad si se encuentra, usando la frase "'{titulo}' está disponible.".
Si no se encuentra, imprimir el mensaje "'{titulo}' no está en el inventario.".
"""

# Inventario inicial
inventory = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": False},
]

#1 Definir la función para verificar disponibilidad
def check_availability(titulo):
    for book in inventory:  #2 Crear un bucle para recorrer cada libro
        if book["titulo"] == titulo:  #3 Revisar si el libro está en el inventario y su estado es "disponible"
            if book["disponible"]:
                print(f"'{titulo}' está disponible.")
            else:
                print(f"'{titulo}' no está disponible.")
            return
    print(f"'{titulo}' no está en el inventario.")


# Uso de la función
check_availability("Cien años de soledad")
check_availability("Pedro Páramo")



"""
Ahora, tu objetivo es permitir que los usuarios agreguen nuevos libros al inventario de la biblioteca.

Recuérdate la estructura del inventario:

[
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": False}
]
Cada entrada representa un libro con su título, autor y disponibilidad.

Objetivo:
Debes implementar la función add_book(titulo, autor, disponible), que:

Cree un diccionario con las claves 'titulo', 'autor' y 'disponible'.
Agregue ese diccionario a la lista inventory.
Descomposición de la tarea:

Definir la función add_book.
Crear un nuevo diccionario para representar el libro.
Usar el método .append() para añadirlo a inventory.
Verificar agregando un libro y mostrando el inventario.
"""

# Inventario inicial
inventory = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "disponible": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "disponible": False},
]

#1 Definir la función para agregar un libro
def add_book(titulo, autor, disponible):
    #2 Crear un diccionario que contenga los datos del libro
    new_book = {"titulo": titulo, "autor": autor, "disponible": disponible}
    #3 Agregar el nuevo libro al inventario con append()
    inventory.append(new_book)

#4 Definir la función para verificar disponibilidad
def check_availability(titulo):
    for book in inventory:
        #5 Revisar si el libro está en el inventario y disponible
        if book["titulo"] == titulo and book["disponible"]:
            print(f"'{titulo}' está disponible.")
            return
    #6 Si no se encuentra, imprimir el mensaje de no disponibilidad
    print(f"'{titulo}' no está en el inventario.")

# Uso de las funciones
add_book("Pedro Páramo", "Juan Rulfo", disponible=True)
check_availability("Pedro Páramo")



"""
En el precódigo, encontrarás las funciones que hemos creado en esta lección para filtrar y mostrar el resultado.
Utiliza estas funciones para filtrar las películas de más de 140 minutos de duración e imprimir el resultado.
"""

def filter_by_timing(data, target_duration): 
    filtered_result = []
    for row in data:
        if row[4] > target_duration:
            filtered_result.append(row)
    return filtered_result 

def print_movie_info(data):
    for movie in data:
        print(movie)

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

# llama aquí a la función de filtrado
filtered_movies = filter_by_timing(movies_info, 140)
# llama a la función para mostrar los resultados aquí
print_movie_info(filtered_movies)



"""
Ejercicio 1
Basándote en la función anterior, escribe una nueva función que filtre aquellas películas por año de estreno ( filter_by_year()).
Para ello, la nueva función debe tener dos parámetros:
- data: una lista de listas con la información de diferentes películas.
- year: criterio de filtrado, basado en el año.

Con esta información, itera a través de data, filtrando aquellas películas estrenadas después de year.
Almacena aquellos elementos en una nueva lista, los cuales debes retornar como resultado al finalizar la función.
Utiliza el año "1990" como argumento de filtrado.
"""
# esta función muestra la tabla filtrada. No modificar
def print_movie_info(data):
    for movie in data:
        print(movie)

# Utiliza como referencia la función que definiste en el ejercicio anterior.
# Renombra la funcion y realiza los ajustes necesarios para crear filter_by_year() 
def filter_by_year(data, year):
    filtered_result = []
    for row in data:
        if row[2] > year: # Pista: aquí debes cambiar el elemento de la fila que comparas
            filtered_result.append(row)
    return filtered_result 

    
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

# A continuación tienes dos llamadas a funciones: una para filtrar y otra para mostrar el resultado en pantalla
movies_filtered = filter_by_year(movies_info, 1990)
print_movie_info(movies_filtered)



"""
Imagina que estás administrando un sistema de cuentas bancarias en el que múltiples operaciones, como depósitos y retiros,
necesitan actualizar el saldo de la cuenta. Para mantener el código organizado y fácil de mantener, es esencial comprender
cómo interactúan las variables locales y globales, particularmente cuando se modifican datos compartidos como el saldo de la cuenta.
El manejo incorrecto de estas variables puede generar discrepancias en los saldos de los clientes.

Tienes una variable global que representa el saldo bancario total. Debes crear una función que realice operaciones de depósito,
actualizando el saldo cada vez que se realiza un depósito.

Utiliza una variable global para representar el saldo general y variables locales dentro de la función para manejar los cálculos,
demostrando la interacción entre las variables globales y locales.
"""

# Variable global que representa el saldo bancario inicial
balance = 1000

# Muestra el saldo inicial
print(f"Saldo inicial: {balance}")

# Función para realizar una operación de depósito
def deposit_money(amount):
    global balance  # Accede a la variable global 'balance'
    local_balance = balance  # Variable local para realizar un seguimiento del saldo temporal
    
    #Completa el código aquí actualizando local_balance
    ## ESCRIBE TU CODIGO AQUI
    local_balance += amount  # Actualiza el saldo local con el monto del depósito
    
    # Actualiza el saldo global
    balance = local_balance

# Realiza operaciones de depósito
deposit_money(200)  # Depositar 200
print(f"Saldo global actualizado: {balance}")

deposit_money(150)  # Depositar 150
print(f"Saldo global actualizado: {balance}")



"""
Ejercicio 1
En un sistema de inventario, es clave llevar un control preciso del stock. Para ello:

- Se utiliza un diccionario global para almacenar el inventario.
- Se emplean variables locales dentro de las funciones para agregar o quitar stock.
Se utiliza la función agregar stock, que suma unidades o añade nuevos productos.

En este ejercicio deberás crear la función agregar stock. Presta atención al entorno de cada variable. 
"""

# Diccionario global que representa los niveles de inventario actuales
inventory = {
    'manzana': 50,
    'plátano': 30,
    'naranja': 20
}

# Muestra el inventario inicial
print("Inventario inicial:", inventory)

# Función para agregar stock
def add_stock(product, quantity):
    """
    Agrega un producto al inventario o actualiza la cantidad si ya existe.
    
    Parámetros:
    - product (str): Nombre del producto.
    - quantity (int): Cantidad a agregar.
    """
		### AQUÍ VA TU CÓDIGO ###
    if product in inventory:
        inventory[product] += quantity  # Actualiza la cantidad existente
        print(f"Se agrega(n) {quantity} {product}(s). Nuevo inventario: {inventory[product]}")
    else:
        inventory[product] = quantity  # Agrega un nuevo producto al inventario
        print(f"Se agrega el nuevo producto {product} con {quantity} unidades. Nuevo inventario: {inventory[product]}")


# Realiza operaciones de stock
add_stock('manzana', 20)   # Agregar 20 manzanas
add_stock('kiwi', 30)      # Agregar 30 kiwis



"""
Ejercicio 2
Seguimos trabajando con el sistema de inventario de nuestra tienda. Hasta ahora, ya diseñamos una función para agregar productos al stock.
Repasemos algunos puntos clave del código:
- El inventario se almacena en un diccionario global llamado inventory.
- Dentro de las funciones, se utilizan variables locales para manejar cantidades específicas y realizar operaciones.

Para mantener este ejercicio claro y enfocado, no volveremos a escribir la función add_stock.

Ahora tu tarea será crear una función para remover productos del inventario, por ejemplo, cuando un cliente realiza una compra.

Tu función debe:
1. Verificar si el producto existe en el inventario.
2. Validar si hay suficiente stock disponible para quitar la cantidad indicada.
3. Actualizar el inventario si la operación es válida, o mostrar un mensaje si no es posible.
    El mensaje es: El producto X no existe en el inventario. No se puede quitar el stock.

Además, recuerda prestar atención al uso de variables globales y locales.
"""

# Diccionario global que representa los niveles de inventario actuales
inventory = {
    'manzana': 50,
    'plátano': 30,
    'naranja': 20
}

# Muestra el inventario inicial
print("Inventario inicial:", inventory)


# Función para quitar stock
def remove_stock(product, quantity):
	### AQUÍ VA TU CÓDIGO ###
    if product not in inventory:
            print(f"El producto {product} no existe en el inventario. No se puede quitar el stock.")
    else:
        if inventory[product] >= quantity:
            inventory[product] -= quantity
            print(f"Se quita(n) {quantity} {product}(s). Nuevo inventario: {inventory[product]}")
        else:
            print(f"Stock insuficiente de {product}. No se puede(n) quitar {quantity} {product}(s).")


# Realiza operaciones de stock
remove_stock('plátano', 10)    # Quitar 20 plátanos
remove_stock('naranja', 25)    # Intentar quitar 25 naranjas
remove_stock('uva', 50)        # Quitar 50 uvas

