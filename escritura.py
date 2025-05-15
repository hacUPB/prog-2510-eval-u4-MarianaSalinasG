nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
cedula = input("Ingrese su cédula: ")


var_archivo = open("Texto1.txt", "a")
var_archivo.write(f"{nombre} con cédula {cedula} tiene {edad} años.\n")

var_archivo.close()

#w si el archivo no existe, lo crea.
#r si el archivo existe, lo abre para lectura.
#a si el archivo existe, escritura sin sobreescribir.