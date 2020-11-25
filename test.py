from PIL import Image
from matplotlib import pyplot
import numpy as np
import os



# load image
#im = Image.open("pokeball.png").convert('LA')

#width_2 = im.width * 2
#height_2 = im.height *2
#im2 = (np.array(im))
#print(im2)
#im.show()

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
    # pix_val = img.getdata() //

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
    print(len(Fragmentos[0]))
    if len(Fragmentos[0])==105:
        print("OK")
    
    Parallel=Filter(Fragmentos)

    output= Build(Parallel)
    if len(output)==840:
       print("TRUE")
    
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

def Prueba(Salida):    #Función de Debug
    #Creamos imagen Sharpening y la mostramos
    data = np.array(Salida)
    data = data.reshape((105, 105))
    image = Image.fromarray(data.astype(int), 'L')
    #image = image.resize((width,height))
    image.save("test.jpg")
    print("Listo! Imagen guardada bajo el nombre Parallelized.jpg")

   # else:
    #    print("F")

    #print(Fragments[0])
    #return Inter(Data)





#Fragmenta la matriz
def biFrag(Matriz):
    secciones=[]
    MiniMatriz= np.zeros(shape=(105,105))
    i=0
    while i<16:
        secciones.append(MiniMatriz)
        i+=1
    #print(secciones)

    x=0
    y=0

    while x < 420:
        y=0
        while y < 420:
            if x >= 0 and x <= 104:
                if y >= 0 and y <= 104:
                    secciones[0][x][y]=Matriz[x][y]
                   # secciones[0].append(Matriz[x][y])
                elif y >= 105 and y <= 209:
                    secciones[4][x][y-105]=Matriz[x][y]
                elif y >= 210 and y <= 314:
                    secciones[8][x][y-210]=Matriz[x][y]
                elif y >= 315 and y <= 419:
                    secciones[12][x][y-315]=Matriz[x][y]
            elif x >= 105 and x <= 209:
                if y >= 0 and y <= 104:
                    secciones[1][x-105][y]=Matriz[x][y]
                elif y >= 105 and y <= 209:
                    secciones[5][x-105][y-105]=Matriz[x][y]
                elif y >= 210 and y <= 314:
                    secciones[9][x-105][y-210]=Matriz[x][y]
                elif y >= 315 and y <= 419:
                    secciones[13][x-105][y-315]=Matriz[x][y]
            elif x >= 210 and x <= 314:
                if y >= 0 and y <= 104:
                    secciones[2][x-210][y]=Matriz[x][y]
                elif y >= 105 and y <= 209:
                    secciones[6][x-210][y-105]=Matriz[x][y]
                elif y >= 210 and y <= 314:
                    secciones[10][x-210][y-210]=Matriz[x][y]
                elif y >= 315 and y <= 419:
                    secciones[14][x-210][y-315]=Matriz[x][y]
            else:
                if y >= 0 and y <= 104:
                    secciones[3][x-315][y]=Matriz[x][y]
                elif y >= 105 and y <= 209:
                    secciones[7][x-315][y-105]=Matriz[x][y]
                elif y >= 210 and y <= 314:
                    secciones[11][x-315][y-210]=Matriz[x][y]
                elif y >= 315 and y <= 419:
                    secciones[15][x-315][y-315]=Matriz[x][y]
            y=y+1
        x=x+1
    if len(secciones)==16:
        print("OK")
    if len(secciones[12])==105:
        print("Nice")
    fh = open('test.txt', 'w')
    listToStr = ''.join([value for value in str(secciones[12])]) 
    fh.write(listToStr)
    fh.close
    Prueba(secciones[3])
    return secciones

#Ensambla la imagen
def Build(Secciones):
    Salida = np.zeros(shape=(840,840), dtype=int)
    x=0
    y=0
    i=0
    M1= Secciones[0]
    M2=Secciones[1]
    M3=Secciones[2]
    M4=Secciones[3]
    M5=Secciones[4]
    M6=Secciones[5]
    M7=Secciones[6]
    M8=Secciones[7]
    M9=Secciones[8]
    M10=Secciones[9]
    M11=Secciones[10]
    M12=Secciones[11]
    M13=Secciones[12]
    M14=Secciones[13]
    M15=Secciones[14]
    M16=Secciones[15]
    while x < 840:
        y=0
        while y < 840:
            if x >= 0 and x <= 209:
                if y >= 0 and y <= 209:
                    Salida[x][y]=M1[x][y]
                elif y >= 210 and y <= 419:
                    Salida[x][y]= M5[x][y-210]
                elif y >= 420 and y <= 629:
                    Salida[x][y]= M9[x][y-420]
                elif y >= 630 and y <= 829:
                    Salida[x][y]= M13[x][y-630]
            elif x >= 210 and x <= 419:
                if y >= 0 and y <= 209:
                    Salida[x][y]=M2[x-210][y]
                elif y >= 210 and y <= 419:
                    Salida[x][y]=M6[x-210][y-210]
                elif y >= 420 and y <= 629:
                    Salida[x][y]=M10[x-210][y-420]
                elif y >= 630 and y <= 829:
                    Salida[x][y]=M14[x-210][y-630]
            elif x >= 420 and x <= 629:
                if y >= 0 and y <= 209:
                    Salida[x][y]=M3[x-420][y]
                elif y >= 210 and y <= 419:
                    Salida[x][y]=M7[x-420][y-210]
                elif y >= 420 and y <= 629:
                    Salida[x][y]=M11[x-420][y-420]
                elif y >= 630 and y <= 829:
                    Salida[x][y]=M15[x-420][y-630]
            else:
                if y >= 0 and y <= 209:
                    Salida[x][y]=M4[x-630][y]
                elif y >= 210 and y <= 419:
                    Salida[x][y]=M8[x-630][y-210]
                elif y >= 420 and y <= 629:
                    Salida[x][y]=M12[x-630][y-420]
                elif y >= 630 and y <= 829:
                    Salida[x][y]=M16[x-630][y-630]
            y+=1
        x+=1
    return Salida

#Interpolacion
def Inter(Matrix):
    
    x=len(Matrix)
    y=len(Matrix[0])
    Salida = np.zeros(shape=(2*x,2*y), dtype=int)
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
    return Salida

#Aplica las interpolaciones
def Filter(secciones):
    MegaPic=[]
    i=0
    while i < 16:
        if i%2==0:
            tmp = Inter(secciones[i])
            MegaPic.append(tmp)
        else:
            tmp = Inter(secciones[i])
            MegaPic.append(tmp)
        i+=1
    if len(MegaPic)==16:
        print("OC")
    if len(MegaPic[0])==210:
        print("420")
    return MegaPic

Generador()