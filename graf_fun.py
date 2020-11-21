# -*- coding: utf-8 -*-

"""
Autores: Martínez Márquez Héctor
         Rosasles Valdez Edna
         Bustamante Cruz Horacio

Analisis de Algoritmos 3CV4

"""

import tkinter

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

from collections import namedtuple
from pprint import pprint as pp
import PosfixTools as psfx
from PosfixTools import evalpostfix as evl

root = tkinter.Tk()
root.wm_title("Graficador")
ta = root.geometry("1000x700")

style.use('ggplot')

fig = Figure()
axl = fig.add_subplot(111)
axl2 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master = root)
canvas.draw()
canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)
canvas.get_tk_widget().pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1)

#Variables iniciales
act_rango=False
ul_ran=""
ran=""

funciones={"sin":"np.sin","cos":"np.cos","tan":"np.tan","log":"np.log","pi":"np.pi","sqrt":"np.sqrt"}

def reemplazo(s):
    for i in funciones:
        if i in s:
            s = s.replace(i, funciones[i])
    return s

#crear grafica
def animate(i):
    global act_rango
    global ul_ran

    #Si el usuario especifica el rango
    if act_rango == True:
        try:
            lmin = float(ran[0]); lmax = float(ran[1])
            if lmin < lmax:
                evalutaor = evl(lmin, lmax, .01) 
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            #Muestra ventana de error
            messagebox.showwarning("Error","Entrada no válida")
            act_rango = False
            
            #Se elimina el contenido de la entrada
            ets.delete(0, len(ets.get()))

    #Si el usuario no especifica el rango
    else:
        if ul_ran != "":
            evalutaor = evl(ul_ran[0], ul_ran[1], .01) 
        else:
            evalutaor = evl(1, 10, .01) 
    
    #Calculando la función introducida
    try:
        #calculo_funcion = eval(graph_data)
        rp = psfx.shunting(psfx.get_input(graph_data))
        posfix = psfx.getPosfixString(rp)
        posfixEvaluation = evalutaor.centralfunc(posfix)
        print(posfixEvaluation)

        rp = psfx.shunting(psfx.get_input(graph_data2))
        posfix = psfx.getPosfixString(rp)
        posfixEvaluation2 = evalutaor.centralfunc(posfix)
        print(posfixEvaluation2)

        axl.clear()
        axl.plot(evalutaor.n, posfixEvaluation)
        axl2.plot(evalutaor.n, posfixEvaluation2)
    except:
        axl.plot()
        axl2.plot()
    #Dibujo de los ejes
    axl.axhline(0, color = "gray")
    axl.axvline(0, color = "gray")

def represent():
    global graph_data
    global graph_data2
    global ran
    global act_rango
    graph_data = et.get()
    graph_data2 = et2.get()
    if ets.get()!="":
        rann = ets.get()
        ran = rann.split(",")
        act_rango = True
    ani.event_source.start()


ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()

#Ingresa la funcion
et = tkinter.Entry(master = root, width = 60)
et.config(bg = "gray87", justify = "left")

et2 = tkinter.Entry(master = root, width = 60)
et2.config(bg = "gray87", justify = "left")

#Ingresa los rangos
ets = tkinter.Entry(master = root, width = 10)

#Etiqueta del campo Rango
label = tkinter.Label(master = root, text= "Rango de 'X'")

#Botón de enviar
button = tkinter.Button(master = root, text = "SET", bg = "gray69", command = represent)

#Ubicación de elementos
button.pack(side = tkinter.BOTTOM)
et.pack(side = tkinter.BOTTOM)
et2.pack(side = tkinter.BOTTOM)
ets.pack(side = tkinter.RIGHT)
label.pack(side = tkinter.RIGHT)

tkinter.mainloop()