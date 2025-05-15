from random import randint

lista = []
for i in range(20): 
    n = randint(100, 200)
    lista.append(n)
 
print(lista)
mayor = max(lista)
menor = min(lista)

ind_mayor = lista.index(mayor)
ind_menor = lista.index(menor)  

print(f"El mayor es {mayor} y su índice es {ind_mayor}")
print(f"El menor es {menor} y su índice es {ind_menor}")