from PIL import Image
from matplotlib import pyplot
import numpy as np
import os

#Se le pide la imagen al usuario
def Generador():
    try:
        imagen = input('Favor escribir el nombre de la imagen a procesar: ')

        img = Image.open(str(imagen)).convert('LA')
        global width
        global height
        width, height = img.size
        img.save('images/greyScale.png')
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
    fh = open('images/image.txt', 'w')
    listToStr = ''.join([value for value in str(Data)]) 
    fh.write(listToStr)
    fh.close


    
    return Inter(Data)



def Inter(Matrix):
    
    x=len(Matrix)
    y=len(Matrix[0])
    Salida = np.zeros(shape=(2*x,2*y))
    R=2*x
    W=2*y
    i=0
    j=0
    contador=0
    Vsync=0
    while i < len(Matrix):
        j=0
        contador=0
        while j < len(Matrix[0]):
            if i==0 and j==0:
                Salida[i][j]=Matrix[i][j]
                Salida[i+1][j]=Matrix[i][j]
                Salida[i][j+1]=Matrix[i][j]
                Salida[i+1][j+1]=Matrix[i][j]
            elif i==0 and j==(y-1):
                Salida[i][R-1]=Matrix[i][j]
                Salida[i][R-2]=Matrix[i][j]
                Salida[i+1][R-1]=Matrix[i][j]
                Salida[i+1][R-2]=Matrix[i][j]
            elif i==(x-1) and j==0:
                Salida[W-1][j]=Matrix[i][j]
                Salida[W-2][j]=Matrix[i][j]
                Salida[W-1][j+1]=Matrix[i][j]
                Salida[W-2][j+1]=Matrix[i][j]
            elif i==(x-1) and j==(y-1):
                Salida[W-1][R-1]=Matrix[i][j]
                Salida[W-1][R-2]=Matrix[i][j]
                Salida[W-2][R-1]=Matrix[i][j]
                Salida[W-2][R-2]=Matrix[i][j]
            elif i==0:
                Salida[i][contador]=Matrix[i][j]
                Salida[i][contador+1]=Matrix[i][j]
                Salida[i+1][contador]=Matrix[i][j]
                Salida[i+1][contador+1]=Matrix[i][j]
            elif j==0:
                Salida[Vsync][j]=Matrix[i][j]
                Salida[Vsync][j+1]=Matrix[i][j]
                Salida[Vsync+1][j]=Matrix[i][j]
                Salida[Vsync+1][j+1]=Matrix[i][j]
            else:
                Salida[Vsync][contador]=Matrix[i][j]
                Salida[Vsync][contador+1]=Matrix[i][j]
                Salida[Vsync+1][contador]=Matrix[i][j]
                Salida[Vsync+1][contador+1]=Matrix[i][j]
            j=j+1
            contador=contador+2
        Vsync=Vsync+2    
        i=i+1
    #print(Salida)
    return NewImage(Salida)

def NewImage(Salida):    
    #Creamos imagen Sharpening y la mostramos
    data = np.array(Salida)
    data = data.reshape((width*2, height*2))
    image = Image.fromarray(data.astype(np.uint8), 'L')
    #image = image.resize((width,height))
    image.save("images/Interpolation.jpg")
    print("Listo! Imagen guardada bajo el nombre Interpolation.jpg")


Generador()
