import tkinter as tk
from tkinter import ttk

#crear ventana
ventana = tk.Tk()

ventana.geometry('600x400')

ventana.title('ventanona')

ventana.configure(background='#1d2d44')
def mostrar():
    texto = caja_texto.get() #recuperar el texto escrito
    print(texto)
    etiqueta['text'] = texto

#caja texto
caja_texto = ttk.Entry(ventana, font=('Arial',15))
caja_texto.pack(pady=20)

#agregar un boton
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack(pady=20)

#agregar etiqueta
etiqueta=ttk.Label(ventana, text='kk')
etiqueta.pack(pady=20)


ventana.mainloop()