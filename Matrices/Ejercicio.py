Matriz = [[1,4,6,8,3],[8,9,12,54,47],[98,45,78,3,10]]
print(Matriz)

filas = len(Matriz) #3
columnas = len(Matriz[0]) #4

for i in range(filas): #índice de filas
    for j in range(columnas): #índice de columnas
        print(f"{Matriz[i][j]:3}", end=" ")
    print()
