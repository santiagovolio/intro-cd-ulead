#TRABAJO #1 SANTIAGO VOLIO

print("PRIMER EJERCICIO DE INTRODUCCIÓN A CIENCIAS DE DATOS")
print(" ") #Añadí espacio para que el titulo no se enrede


# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
numero = int(input("Ingresa tu número favorito: "))


# Determinar si es mayor o menor de edad
if edad >= 18:
    print(nombre, "usted es mayor de edad")
else:
    print(nombre, "usted es menor de edad")

# Determinar si el numero ingresado por el usuario es par o impar
if numero % 2 == 0:
    print("Tu número favorito es par")
else:
    print("tu número favorito es impar")

# Ciclo de while para secuencia del número ingresado por el ususario
print(f"Secuencia desde 1 hasta {numero}:")
sumatoria = 0
contador = 1

while contador <= numero:
    sumatoria = contador + sumatoria
    contador += 1
    print(sumatoria)


# Mensaje final para el usuario

print(nombre, ": ")
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

if numero % 2 == 0:
    print("Tu número favorito es par.")
else:
    print("Tu número favorito es impar.")

print(f"La suma de todos los números desde 1 hasta el {numero} es: {sumatoria}")


