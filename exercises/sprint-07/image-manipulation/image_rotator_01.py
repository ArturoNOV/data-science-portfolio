from pathlib import Path
from PIL import Image # importa el módulo Image de la librería PIL


script_folder = Path(__file__).resolve().parent

input_path = script_folder / 'tripleten_logo.jpeg'
output_path = script_folder / 'rotated.png'

# carga una imagen llamada 'tripleten_logo.jpeg'.
im = Image.open(input_path)

# obtén el tamaño de la imagen mediante el atributo .size y muéstralo
print(im.size)

# gira la imagen 90 grados en sentido contrario a las agujas del reloj
rotated = im.rotate(90)

# guarda la imagen girada
rotated.save(output_path)

im.close()
