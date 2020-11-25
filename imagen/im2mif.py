import sys
import cv2
import numpy as np
import os.path
from matplotlib import pyplot as plt

# Arguments
args = sys.argv

if len(args) == 1:
    sys.exit("El uso del script es: python im2mif.py <imagen>")

if os.path.exists(args[1]) == False:
    sys.exit("La imagen no existe, verifique el nombre escrito")

# Carga de la image
A = cv2.imread(args[1], 0)
m, n = A.shape

A_flat = A.flatten()

print(type(A[1][1]))

pixelesPorVector = 32
width = pixelesPorVector * 8
depth = int((n / pixelesPorVector) * m)


with open("imageIn.mif", "w") as f:
    f.write("WIDTH=" + str(width) + ";\r")
    f.write("DEPTH=" + str(depth) + ";\r\r")
    f.write("ADDRESS_RADIX=UNS;\r")
    f.write("DATA_RADIX=HEX;\r\r")
    f.write("CONTENT BEGIN\r")

    index = 0
    line = "\t"+str(index)+" : "

    while index < depth:
        slice = A_flat[index*32:][:32]
        line += "".join('{:02x}'.format(x) for x in slice)
        line += "\r"
        f.write(line)
        index += 1
        line = "\t"+str(index)+" : "

    f.write("END")
