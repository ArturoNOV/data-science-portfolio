
usuario_nombre = ' mike_reed '

# 1. Limpia el dato eliminando los espacios innecesarios en la variable user_name
usuario_nombre = usuario_nombre.strip()

# 2. Reemplaza el guion bajo por un espacio.
usuario_nombre = usuario_nombre.replace('_',' ')

print(usuario_nombre)

# 1. Divide el usuario en dos partes: nombre y apellido
usuario_sep = usuario_nombre.split(' ')

print(usuario_sep)


usuario_edad = 32.0

# 1. Convierte el valor al tipo de dato correcto
usuario_edad = int(usuario_edad)

print(usuario_edad)


usuario_edad = 'treinta y dos'

# 1. Intenta convertir usuario_edad a entero y guárdalo en usuario_edad_int
# 2. Si falla, muestra el mensaje correspondiente
# escribe tu código aquí
try:
    usuario_edad_int = int(usuario_edad)
    print(usuario_edad_int)
except ValueError:
    print("Proporcione su edad como un valor numérico.")


usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['ROPA', 'ELECTRÓNICA', 'BELLEZA'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['LIBROS', 'HOGAR', 'DEPORTE'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BELLEZA', 'HOGAR', 'COMIDA'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['ROPA', 'COMIDA', 'BELLEZA'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['DEPORTE', 'ELECTRÓNICA', 'HOGAR'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOGAR', 'LIBROS', 'ROPA'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BELLEZA', 'ROPA', 'ELECTRÓNICA'], [189, 299, 579]],
]

# 1. Ordena la lista por el ID de usuario en orden ascendente
usuarios.sort()

print(usuarios)


categorias_fav_low = ['electrónica', 'deporte', 'libros']
gasto_por_categoria = [894, 213, 173]

# 1. Calcula la suma de los gastos del usuario
suma_total = sum(gasto_por_categoria)

print(suma_total)


usuario_id = '32415'
usuario_nombre = ['mike', 'reed']
usuario_edad = 32

# 1. Crea la cadena de resumen del cliente
usuario_info = f"El usuario {usuario_id} es {usuario_nombre[0].capitalize()}, quien tiene {usuario_edad} años."

print(usuario_info)


usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['ROPA', 'ELECTRÓNICA', 'BELLEZA'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['LIBROS', 'HOGAR', 'DEPORTE'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BELLEZA', 'HOGAR', 'COMIDA'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['ROPA', 'COMIDA', 'BELLEZA'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['DEPORTE', 'ELECTRÓNICA', 'HOGAR'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOGAR', 'LIBROS', 'ROPA'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BELLEZA', 'ROPA', 'ELECTRÓNICA'], [189, 299, 579]],
]

# 1. Cuenta el número de clientes registrados
usuarios_info = f"Hemos registrado datos de {len(usuarios)} clientes."

print(usuarios_info)


usuarios = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
]

usuarios_limpio = []


# Procesa al primer usuario
# 1. Limpia espacios y reemplaza guión bajo
usuario_nombre_1 = usuarios[0][1].strip().replace('_', ' ')
# 2. Convierte edad a entero
usuario_edad_1 = int(usuarios[0][2])
# 3. Separa el nombre
usuario_nombre_1 = usuario_nombre_1.split()
# 4. Agrega el usuario limpio a la lista
usuarios_limpio.append([usuarios[0][0],usuario_nombre_1,usuario_edad_1,usuarios[0][3],usuarios[0][4]])

# Procesa al segundo usuario
usuario_nombre_2 = usuarios[1][1].strip().replace('_', ' ')
usuario_edad_2 = int(usuarios[1][2])
usuario_nombre_2 = usuario_nombre_2.split()
usuarios_limpio.append([usuarios[1][0],usuario_nombre_2,usuario_edad_2,usuarios[1][3],usuarios[1][4]])

# Procesa al tercer usuario
usuario_nombre_3 = usuarios[2][1].strip().replace('_', ' ')
usuario_edad_3 = int(usuarios[2][2])
usuario_nombre_3 = usuario_nombre_3.split()
usuarios_limpio.append([usuarios[2][0],usuario_nombre_3,usuario_edad_3,usuarios[2][3],usuarios[2][4]])

print(usuarios_limpio)