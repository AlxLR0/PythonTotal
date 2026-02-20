import tkinter as tk
from tkinter import ttk

#crear ventana
ventana = tk.Tk()

ventana.geometry('600x400')

ventana.title('ventanona')

ventana.configure(background='#1d2d44')

#grid (rejilla o cuadricula)

btn1= ttk.Button(ventana, text='Boton1')
btn2= ttk.Button(ventana, text='Boton2')
btn3= ttk.Button(ventana, text='Boton3')

btn4= ttk.Button(ventana, text='Boton4')
btn5= ttk.Button(ventana, text='Boton5')
btn6= ttk.Button(ventana, text='Boton6')

# publicar de manera horizontal, posición del btn dentro de la columna n= north w= west y asi, pad y /x es el padding y la cantidad de pixeles
btn1.grid(row=0 , column=0, sticky=tk.N, pady=10)
btn2.grid(row=0 , column=1, sticky=tk.NW)
btn3.grid(row=0 , column=2)

#publicar de manera vertical
btn4.grid(row=0 , column=0,sticky=tk.S)
btn5.grid(row=1 , column=0)
btn6.grid(row=2 , column=0)

#configurar grid, ancho de las columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=10)
ventana.columnconfigure(2, weight=1)

#configurar grid, ancho de las filas
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=10)
ventana.rowconfigure(2, weight=1)

ventana.mainloop()