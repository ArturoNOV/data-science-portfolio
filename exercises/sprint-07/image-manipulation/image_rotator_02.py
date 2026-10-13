from PIL import Image
import argparse # importa el módulo argparse

# inicializa el analizador sintáctico
parser = argparse.ArgumentParser()

# agrega argumentos con sus nombres correspondientes
parser.add_argument('input_file')      # primer argumento: archivo de entrada
parser.add_argument('output_file')     # segundo argumento: archivo de salida
parser.add_argument('angle', type=int) # tercer argumento: ángulo

# analiza los argumentos
args = parser.parse_args()

# carga una imagen del argumento input_file
im = Image.open(args.input_file)

# muestra el tamaño de la imagen
print(im.size)

# gira la imagen en un ángulo proporcionado como argumento
rotated = im.rotate(args.angle, expand=True)

# guarda la imagen girada usando la ruta de salida de un argumento output_file
rotated.save(args.output_file)

# muestra el tamaño de la imagen rotada
print(rotated.size)