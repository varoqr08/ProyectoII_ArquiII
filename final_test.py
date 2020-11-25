from PIL import Image
from matplotlib import pyplot
import numpy as np
import os



#Se le pide la imagen al usuario
def Generador():
    try:
        #imagen = input('Favor escribir el nombre de la imagen a procesar: ')
        imagen="pokeball.png"

        img = Image.open(str(imagen)).convert('LA')
        global width
        global height
        width, height = img.size
        #image = image.resize((width,height))
        img.save('greyScale.png')
    except:
        print("Imagen no encontrada, favor intente de nuevo.")
        return Generador()

    #pixeles en pares ordenados ej: (#,255)
    pix_val = list(img.getdata())

    #pixeles en lista ej: [#, #, #, ...]
    imageData = [x for sets in pix_val for x in sets]
    #print(len(imageData))
    del imageData[1::2]
    #print(len(imageData))

    #pixeles como matriz de tamano width x height
    Data = np.array(imageData)
    Data = Data.reshape((width, height))

    #Crea el archivo txt con los valores de los pixeles de la imagen
    fh = open('image.txt', 'w')
    listToStr = ''.join([value for value in str(Data)])
    #print(len(listToStr))
    fh.write(listToStr)
    fh.close


    global M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, M16, SupremeList
    M1 = []
    M2 = []
    M3 = []
    M4 = []
    M5 = []
    M6 = []
    M7 = []
    M8 = []
    M9 = []
    M10 = []
    M11 = []
    M12 = []
    M13 = []
    M14 = []
    M15 = []
    M16 =[]
    SupremeList = []


#################################################
    Fragmentos=biFrag(Data)    
    Parallel=Filter(Fragmentos)
    output= Build(Parallel)
    NewImage(output)
#################################################


 #Crea la imagen   
def NewImage(Salida):    
    
    data = np.array(Salida)
    data = data.reshape((840, 840))
    image = Image.fromarray(data.astype(np.uint8), 'L')
    image = image.resize((840,840))
    image.save("Parallelized.jpg")
    print("Listo! Imagen guardada bajo el nombre Parallelized.jpg")

def Prueba(Salida):    #Función de Debug
    
    data = np.array(Salida)
    data = data.reshape((105, 105))
    image = Image.fromarray(data.astype(np.uint8), 'L')
    image.save("test.jpg")
    print("Listo! Imagen guardada bajo el nombre test.jpg")



#Fragmenta la matriz
def biFrag(Matriz):
    secciones=[]
    MiniMatriz= np.zeros(shape=(105,105))
    i=0
    while i<16:
        secciones.append(MiniMatriz)
        i+=1

    x=0
    y=0
    while x < 420:
        y=0
        while y < 420:
            if x >= 0 and x <= 104:
                if y >= 0 and y <= 104:
                    M1.append(Matriz[x][y])
                    
                elif y >= 105 and y <= 209:
                    M5.append(Matriz[x][y])
                    
                elif y >= 210 and y <= 314:
                    M9.append(Matriz[x][y])
                    
                elif y >= 315 and y <= 419:
                    M13.append(Matriz[x][y])
                    
            elif x >= 105 and x <= 209:
                if y >= 0 and y <= 104:
                    M2.append(Matriz[x][y])
                    
                elif y >= 105 and y <= 209:
                    M6.append(Matriz[x][y])
                    
                elif y >= 210 and y <= 314:
                    M10.append(Matriz[x][y])
                    
                elif y >= 315 and y <= 419:
                    M14.append(Matriz[x][y])
                    
            elif x >= 210 and x <= 314:
                if y >= 0 and y <= 104:
                    M3.append(Matriz[x][y])
                    
                elif y >= 105 and y <= 209:
                    M7.append(Matriz[x][y])
                    
                elif y >= 210 and y <= 314:
                    M11.append(Matriz[x][y])
                    
                elif y >= 315 and y <= 419:
                    M15.append(Matriz[x][y])
                    
            else:
                if y >= 0 and y <= 104:
                    M4.append(Matriz[x][y])
                    
                elif y >= 105 and y <= 209:
                    M8.append(Matriz[x][y])
                    
                elif y >= 210 and y <= 314:
                    M12.append(Matriz[x][y])
                    
                elif y >= 315 and y <= 419:
                    M16.append(Matriz[x][y])
                    
            y=y+1
        x=x+1
        
    m1 = ListToMat(M1)
    m2 = ListToMat(M2)
    m3 = ListToMat(M3)
    m4 = ListToMat(M4)
    m5 = ListToMat(M5)
    m6 = ListToMat(M6)
    m7 = ListToMat(M7)
    m8 = ListToMat(M8)
    m9 = ListToMat(M9)
    m10 = ListToMat(M10)
    m11 = ListToMat(M11)
    m12 = ListToMat(M12)
    m13 = ListToMat(M13)
    m14 = ListToMat(M14)
    m15 = ListToMat(M15)
    m16 = ListToMat(M16)
    
    fh = open('test.txt', 'w')
    listToStr = ''.join([value for value in str(secciones)]) 
    fh.write(listToStr)
    fh.close
    
#############################################    
    Prueba(M7)
#############################################

    secciones = SupremeList
    return secciones


def ListToMat(matrix):
    m = np.array(matrix)
    m = m.reshape((105, 105))
    SupremeList.append(m)
    return m

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
    return Salida



def bilinear(matrix, width_in, height_in, array_out, width_out, height_out):
    array_in = np.array(matrix)
    for i in range(height_out):
        for j in range(width_out):
            
            # Relative coordinates of the pixel in output space
            x_out = j / width_out
            y_out = i / height_out
 
            # Corresponding absolute coordinates of the pixel in input space
            x_in = (x_out * width_in)
            y_in = (y_out * height_in)
 
            # Nearest neighbours coordinates in input space
            x_prev = int(x_in)
            x_next = x_prev + 1
            y_prev = int(y_in)
            y_next = y_prev + 1
 
            # Sanitize bounds - no need to check for < 0
            x_prev = min(x_prev, width_in - 1)
            x_next = min(x_next, width_in - 1)
            y_prev = min(y_prev, height_in - 1)
            y_next = min(y_next, height_in - 1)
            
            # Distances between neighbour nodes in input space
            Dy_next = y_next - y_in
            Dy_prev = 1. - Dy_next
            Dx_next = x_next - x_in
            Dx_prev = 1. - Dx_next
            
            # Aplica algoritmo bilinear
            array_out[i][j] = Dy_prev * (array_in[y_next][x_prev] * Dx_next + array_in[y_next][x_next] * Dx_prev) + Dy_next * (array_in[y_prev][x_prev] * Dx_next + array_in[y_prev][x_next] * Dx_prev)
    array_out = array_out.reshape((210, 210))
    return array_out


#Aplica las interpolaciones
def Filter(secciones):
    MegaPic=[]

    #Se define el filtro a aplicar por secciones
    i=0
    while i < 16:
        if i%2==0:
            tmp = Inter(secciones[i])
            MegaPic.append(tmp)
        else:
            out = np.zeros((210, 210, 1))
            tmp = bilinear(secciones[i], 105, 105, out, 210, 210)
            MegaPic.append(tmp)
        i+=1
    return MegaPic

Generador()
