# Contraseñas aleatorias
import random
import string
from tkinter import *
#Para poder mostrar ventanas emergentes:
from tkinter import messagebox

ventana=Tk()
ventana.title("Generador de Claves")
ventana.geometry("380x185")
ventana.resizable(0,0)
# letras sin la l, I, O, para no confundir y números sin el 0
letras = 'abcdefghijkmnñopqrstuvwxyzABCDEFGHJKLMNÑPQRSTUVWXYZ'
numeros = '123456789'
caracteres = letras + numeros

def generador(longitud, cantidad):
    #print ("\n", "Aquí tienes ", cantidad, " claves de ", longitud, " caracteres:", "\n")
    for x in range(cantidad):
        clave = ''.join(random.choice(caracteres) for i in range(longitud))
        print (clave)
        #return clave

def convertir(cade):
    str(cade)
    print(type(cade))

salir=lambda : ventana.destroy()


longitud_claves=StringVar()
cantidad_claves=StringVar()
longitud_claves.set("7")
cantidad_claves.set("2")

miFrame=Frame(ventana)
miFrame.pack()
longitud_c=Entry(miFrame, textvariable=longitud_claves,)
longitud_c.pack()
cantidad_c=Entry(miFrame, textvariable=cantidad_claves,)
cantidad_c.pack()

miEtiqueta=Label(miFrame, text="Introduce la longitud de las claves:")
miEtiqueta.pack()
miEtiqueta2=Label(miFrame, text="Introduce la cantidad de claves que necesitas:")
miEtiqueta2.pack()

miBoton=Button(miFrame, text="Generar", command=print("ñla"))
#miBotone=Button(miFrame, text="Generar", command=generador(4, 8))    -....command=generador(longitud_claves, cantidad_claves)
miBoton.pack()
#command=generador(longitud_c, cantidad_c)
#imprimir(longitud_claves)

botonSalir=Button(miFrame, text="Salir", command=salir)
botonSalir.pack()
ventana.mainloop()