from PIL import Image
from matplotlib import pyplot
import numpy as np
import os
# load image
#im = Image.open("pokeball.png").convert('LA')

#Se le pide la imagen al usuario
def Generador():
    try:
        #imagen = input('Favor escribir el nombre de la imagen a procesar: ')
        imagen="pokeball.png"

        img = Image.open(str(imagen)).convert('LA')
        global width
        global height
        width, height = img.size
        img.save('greyScale.png')
    except:
        print("Imagen no encontrada, favor intente de nuevo.")
        return Generador()

    #pixeles en pares ordenados ej: (#,255)
    pix_val = list(img.getdata())

    #pixeles en lista ej: [#, #, #, ...]
    imageData = [x for sets in pix_val for x in sets]
    del imageData[1::2]

    #pixeles como matriz de tamano width x height
    Data = np.array(imageData)
    Data = Data.reshape((width, height))

    #Crea el archivo txt con los valores de los pixeles de la imagen
    fh = open('image.txt', 'w')
    listToStr = ''.join([value for value in str(Data)]) 
    fh.write(listToStr)
    fh.close


    Fragmentos=biFrag(Data)
    
    Parallel=Filter(Fragmentos)

    output= Build(Parallel)
    
    NewImage(output)

 #Crea la imagen   
def NewImage(Salida):    
    #Creamos imagen Sharpening y la mostramos
    data = np.array(Salida)
    data = data.reshape((840, 840))
    image = Image.fromarray(data.astype(np.uint8), 'L')
    image = image.resize((840,840))
    image.save("Parallelized.jpg")
    print("Listo! Imagen guardada bajo el nombre Parallelized.jpg")

def Prueba(Salida, name):    #Función de Debug
    #Creamos imagen Sharpening y la mostramos
    data = np.array(Salida)
    data = data.reshape((105, 105))
    image = Image.fromarray(data.astype(np.uint8), 'L')
    #image = image.resize((width,height))
    imgName = "salida/" + name + ".jpg";
    image.save(imgName)
    print("Listo! Imagen guardada bajo el nombre Test.jpg")


#Fragmenta la matriz
def biFrag(Matriz):
    secciones = np.zeros(shape=(16,105,105),  dtype=int)
    #print(secciones)
    index = 0
    x=105
    for i in range(4):
        for j in range(4):
            secciones[index][0:105][0:105] = Matriz[i*x:i*x+105,j*x:j*x+105]
            index += 1
 
    return secciones

#Ensambla la imagen
def Build(Secciones):
    Salida = np.zeros(shape=(840,840), dtype=int)
    x=210
    index = 0

    for i in range(4):
        for j in range(4):
            Salida[i*x:i*x+210,j*x:j*x+210] = Secciones[index]
            index += 1
    
    return Salida

#Interpolacion
def Interpolation(Matrix):
    x,y = np.shape(Matrix)
    Salida = np.zeros(shape=(2*x,2*y), dtype=int)
    p=q=0 #iteradores ded la matriz de entrada
    for i in range(0,2*x,2):
        for j in range(0,2*y,2):
            Salida[i][j] = Matrix[p][q]
            Salida[i][j+1] = Matrix[p][q]
            Salida[i+1][j] = Matrix[p][q]
            Salida[i+1][j+1] = Matrix[p][q]
            q += 1
        p += 1
        q = 0
    return Salida

#Aplica las interpolaciones
def Filter(secciones):
    MegaPic = np.zeros(shape=(16, 210, 210), dtype=int)
    print(np.shape(MegaPic))

    for i in range (16):

        if i%2==0:
            MegaPic[i] = Interpolation(secciones[i])
        else:
            MegaPic[i] = Interpolation(secciones[i])
    return MegaPic

Generador()