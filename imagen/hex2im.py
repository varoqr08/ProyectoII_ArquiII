import sys
import cv2
import numpy as np
import os.path
from matplotlib import pyplot as plt

# Arguments
args = sys.argv

if len(args) != 5:
    sys.exit("El uso del script es: python im2mif.py <imagen> <m> <n> <grises?>")

if os.path.exists(args[1]) == False:
    sys.exit("La imagen no existe, verifique el nombre escrito")


# Carga de la image
file = args[1]
m = int(args[2])
n = int(args[3])

mode = int(args[4])

image = np.uint8(np.zeros((m, n, 3)))

pixelesPorVector = 32
width = pixelesPorVector * 8
depth = int((n / pixelesPorVector) * m)

if n % pixelesPorVector != 0:
    sys.exit("El numero de columnas de la imagen debe ser multiplo de " +
             str(pixelesPorVector))

with open(file, "r") as f:
    lines = f.readlines()
    linea = 0
    EOF = 0
    x = y = 0
    for line in lines:
        for p in range(0, 48, 6):
            for q in range(3):
                image[x][y][q] = int(line[p+2*q:p+2*q+2], 16)
            y += 1
            if y == n:
                y = 0
                x += 1


if mode != 1:
    numBins = 300
# TODO
else:
    numBins = 300
    plt.subplot(1, 2, 1), plt.imshow(image)
    plt.title("Imagen reconstruida")

    plt.subplot(1, 2, 2),
    plt.hist(image[:, :, 0].ravel(), numBins)
    plt.title("Histograma")
    plt.xlim([0, 256])

plt.show()
