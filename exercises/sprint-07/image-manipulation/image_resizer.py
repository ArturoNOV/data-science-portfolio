from PIL import Image
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('width', help='ancho de la imagen', type=int)
parser.add_argument('height', help='alto de la imagen', type=int)

args = parser.parse_args()

new_size = (args.width, args.height)

try:
    im = Image.open(args.input_file)

except FileNotFoundError:
    raise SystemExit(
        'Archivo de entrada no encontrado. '
        'Introduce una ruta de archivo válida.'
    )

resized = im.resize(new_size)
resized.save(args.output_file)
im.close()
