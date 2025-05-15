from random import randint

lista = []
for i in range(1000):
    lista.append(randint(50,90))
conjunto = set(lista)
no_repetidos = list(conjunto)

print(no_repetidos)
print(f"Hay {len(no_repetidos)} números no repetidos")  


