import os
import csv
import matplotlib.pyplot as plt

print('-' * 40)
print("Análisis de datos en .CSV y .TXT")
print('-' * 40)

# Solicitar la ruta de la carpeta
ruta = input("\nIngrese la ruta de la carpeta: ")
if not ruta.endswith('/'):
    ruta += '/'

# Menú principal
print("1. Listar archivos en la ruta actual")
print("2. Procesar archivo de texto (.txt)")
print("3. Procesar archivo separado por comas (.csv)")
print("4. Salir")
menu = input("Escoja la opción que quiere (1, 2, 3, 4): ")

if menu == '1':
    ruta_completa = os.path.abspath(ruta)
    print(f"\nArchivos en la ruta: {ruta_completa}")
    print('-' * 40)
    for archivo in os.listdir(ruta):
        print(archivo)

elif menu == '2':
    print("\n")
    print('-' * 40)
    print("Submenú de archivos de texto")
    print('-' * 40)

    archivo = input("Ingrese el nombre del archivo de texto: ")
    if not archivo.endswith('.txt'):
        archivo += '.txt'
    archivo = ruta + archivo

    print("1. Contar palabras y caracteres")
    print("2. Reemplazar palabras")
    print("3. Histograma de vocales")
    sub_menu = input("Escoja la opción que quiere (1, 2, 3): ")
    print('\n' + '-' * 40)

    if sub_menu == '1':
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()
        palabras = texto.split()
        total_palabras = len(palabras)
        total_caracteres = len(texto)
        sin_espacios = len(texto.replace(" ", "").replace("\n", ""))
        print(f"El archivo tiene {total_palabras} palabras.")
        print(f"Caracteres (con espacios): {total_caracteres}")
        print(f"Caracteres (sin espacios): {sin_espacios}")

    elif sub_menu == '2':
        palabra_ant = input("Ingrese la palabra a reemplazar: ")
        palabra_nueva = input("Ingrese la nueva palabra: ")
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read()
        nuevo_texto = texto.replace(palabra_ant, palabra_nueva)
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_texto)
        print(f"Se ha reemplazado '{palabra_ant}' por '{palabra_nueva}' en el archivo.")

    elif sub_menu == '3':
        with open(archivo, "r", encoding="utf-8") as f:
            texto = f.read().lower()
        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for letra in texto:
            if letra in vocales:
                vocales[letra] += 1
        plt.bar(vocales.keys(), vocales.values(), color='skyblue')
        plt.title("Histograma de vocales")
        plt.xlabel("Vocal")
        plt.ylabel("Cantidad")
        plt.grid(True)
        plt.show()

    else:
        print("Opción no válida.")

elif menu == '3':
    print("\n")
    print('-' * 40)
    print("Submenú de archivos separados por comas")
    print('-' * 40)

    archivo = input("Ingrese el nombre del archivo CSV (sin .csv): ")
    if not archivo.endswith('.csv'):
        archivo += '.csv'
    archivo = ruta + archivo

    print("1. Mostrar las 15 primeras filas")
    print("2. Calcular estadísticas de una columna")
    print("3. Graficar una columna")
    sub_menu = input("Escoja la opción que quiere (1, 2, 3): ")
    print('\n' + '-' * 40)

    if sub_menu == '1':
        with open(archivo, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            for i, fila in enumerate(lector):
                print(fila)
                if i == 14:
                    break

    elif sub_menu == '2':
        columna = int(input("Ingrese el número de la columna (empezando desde 1): ")) - 1
        datos = []
        with open(archivo, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)
            for fila in lector:
                try:
                    valor = float(fila[columna])
                    datos.append(valor)
                except:
                    continue
        if datos:
            datos.sort()
            n = len(datos)
            promedio = sum(datos) / n
            mediana = datos[n//2] if n % 2 != 0 else (datos[n//2 - 1] + datos[n//2]) / 2
            print(f"Número de datos: {n}")
            print(f"Promedio: {promedio}")
            print(f"Mediana: {mediana}")
            print(f"Mínimo: {min(datos)}")
            print(f"Máximo: {max(datos)}")
        else:
            print("No se pudieron leer datos numéricos de esa columna.")

    elif sub_menu == '3':
        columna = int(input("Ingrese el número de la columna (empezando desde 1): ")) - 1
        datos = []
        with open(archivo, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)
            for fila in lector:
                try:
                    datos.append(float(fila[columna]))
                except:
                    continue
        if datos:
            plt.plot(datos)
            plt.title("Gráfico de la columna")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.grid(True)
            plt.show()
        else:
            print("No se encontraron datos numéricos en la columna.")

    else:
        print("Opción no válida.")

elif menu == '4':
    print("Saliendo del programa...")

else:
    print("Opción no válida. Saliendo...")
