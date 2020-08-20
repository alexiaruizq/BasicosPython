#Esto es un comentario
print("Hola mundo")
print("Adiós mundo")


#Operadores artimeticos
5+1
print(4+6)
print (5-2)
print(3*4)
print(20/4)


#Precedencia de operaciones
print(5+8*(3+2))


#Tipos de datos
print(type(2))
print(type(8.62))
print(type("Texto"))
print(type('Texto'))
print(type("5"))


#Variables
mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "Mensaje modificado"
print (mensaje)
print(type(mensaje))
mensaje = 100
print(mensaje)
print(type(mensaje))

tresanimales = "Gallo, perico, lombriz"
print(tresanimales)


TextoUno = "Mi texto"
TextoDos = "Mi segundo texto"

print(TextoUno + TextoDos)

#str() int()  float()
edad = 20
print("La edad de el usuario es: " + str(edad))
print("El tipo de dato de edad es: " + str(type(edad)))


import math

grados = 45
radianes = grados * math.pi / 180
Seno = math.sin(radianes)
print("Seno de 45º : " + str(Seno))

def saludar (nombre):
    print("Hola" + nombre)
    print("queonda")
    print("Un saludito de lejitos")


def despedir():
    print("Ya me voy")
    print("bai")

def concatenar(parte1, parte2):
    return parte1 + parte2


print("Eso no es parte de la función")
saludar("Alexia")

frase = concatenar("Hola", "Adios")
print(frase)
