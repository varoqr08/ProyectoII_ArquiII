import numpy as np

def inter(Matrix):
    
    x=len(Matrix)
    y=len(Matrix[0])
    Salida = np.zeros(shape=(2*x,2*y))
    print(Salida)
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
    print(Salida)
    return Salida


a=[[1,2],[2,4]]
#print(a)
inter(a)
b=[[10,20,30],[40,50,60],[70,80,90]]
inter(b)
c=[[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]]
inter(c)