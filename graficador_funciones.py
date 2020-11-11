# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:53:56 2020

@author: Ed
"""

from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
import math

plt.title('Graficador de Funciones nun')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

#Función Lineal.
def f(x):
    return 4*x-7
#En esta variable se genera una lista con valores del -10 al 10.
#Todos estos valores serán los que tomara x.
x = range(-10, 10)

#Con el método plot especificamos que función graficaremos.
#El primer argumento es la variable con los valores de x.
#El segundo argumento le pasamos todos estos valares a la función con ayuda de un bucle.
pyplot.plot(x, [f(i) for i in x])



#Especificamos los limites de los ejes.
pyplot.xlim(-11, 11)
pyplot.ylim(-11, 11)

#Guardamos el grafico en una imagen "png".
pyplot.savefig("función_lineal.png")

# Mostramos el gráfico.

#pyplot.show()

#Graficar 2 funciones
def f(x): return np.sin(x)
def g(x): return np.cos(x)

plt.plot(x,f(x))
plt.plot(x,g(x))

x = 7

# + desde la ventana 


#polinomiales
#logaritmicas
#grafiacas logaritmo base 2 (10)

#exponenciales
f = math.exp(x)

#colores

#meter datos desde pantalla de ejecucion









