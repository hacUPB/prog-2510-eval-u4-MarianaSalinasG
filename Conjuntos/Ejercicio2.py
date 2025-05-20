from random import randint

lista1 = []
lista2 = []
for i in range(1000):
    lista1.append(randint(0,100))
    lista2.append(randint(50,150))

#Encontrar los elementos comunes
#Encontrar los elementos no comunes

conjunto1 = set(lista1)
conjunto2 = set(lista2)

elementos_comunes = conjunto1.intersection(conjunto2)  
print(f"Los elementos comunes son: {elementos_comunes}")

elementos_no_comunes = conjunto1.symmetric_difference(conjunto2)
print(f"Los elementos no comunes son: {elementos_no_comunes}")