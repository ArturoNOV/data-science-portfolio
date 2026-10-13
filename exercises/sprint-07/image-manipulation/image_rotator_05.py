from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('angle', help='rotación deseada', type=int)
parser.add_argument(
    '-i',
    '--info',
    help='muestra el tamaño de la imagen',
    action='store_true',
)
args = parser.parse_args()

angle = args.angle

try:
    im = Image.open(args.input_file)
    
except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto')

else:
    rotated = im.rotate(angle)

    if args.info:
        print('dimensiones de la imagen de entrada:', im.size)

    im.close()
    rotated.save(args.output_file)
    print('Ejecución fluida')
