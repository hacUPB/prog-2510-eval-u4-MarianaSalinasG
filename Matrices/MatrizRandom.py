filas = 2
columnas = 3
Lista = []                #Creamos una lista vacía [[6,8,67],[4,7,12]]
for i in range(filas):        #Número de filas que tendrá la matriz (4)
    Lista.append([])      #Agregamos una fila vacía a la matriz
    for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
        n = int(input("Ingrese un valor: "))
        Lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente
print(Lista)