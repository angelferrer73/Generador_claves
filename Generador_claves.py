# Contraseñas aleatorias v1.0
import random
import string
# letras sin la l, I, O, para no confundir y números sin el 0
letras = 'abcdefghijkmnñopqrstuvwxyzABCDEFGHJKLMNÑPQRSTUVWXYZ'
numeros = '123456789'
caracteres = letras + numeros

def generador(longitud, cantidad):
    print ("\n", "Aquí tienes ", cantidad, " claves de ", longitud, " caracteres:", "\n")
    for x in range(cantidad):
        clave = ''.join(random.choice(caracteres) for i in range(longitud))
        if 1==2:
            print (clave)
        #return clave

longitud_claves = int (input("Introduzca la longitud de las claves: "))
cantidad_claves = int (input("Introduzca la cantidad de claves a generar: "))
generador(longitud_claves, cantidad_claves)
cerrar = input("\n" "Aceptar")