from random import randint

filas = 5
columnas = 12
ventasxanio = [] #Para guardar las ventas por año

Lista = []                #Creamos una lista vacía [[6,8,67],[4,7,12]]
for i in range(filas):        #Número de filas que tendrá la matriz (4)
    Lista.append([])      #Agregamos una fila vacía a la matriz
    for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
        n = randint(0, 30)  #Generamos un número aleatorio entre 0 y 100
        Lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente

for i in range(filas):
    for j in range(columnas):
        print(f"{Lista[i][j]:4}", end=" ") #le guarda espacio a 4 enteros para que todos queden alineados
    print()

for f in range (filas):
    suma = sum(Lista[f]) #Sumamos las ventas de cada año
    ventasxanio.append(suma) #Agregamos la suma a la lista de ventas por año
print(ventasxanio)

mayor = max(ventasxanio) #Buscamos el mayor valor de la lista
print(mayor)

indice = ventasxanio.index(mayor) #Buscamos el índice del mayor valor
print(indice)
print(f"El año con más ventas fue el año {2020+indice} con {mayor} ventas.")