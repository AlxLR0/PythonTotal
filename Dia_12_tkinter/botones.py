import tkinter as tk
from tkinter import ttk

#crear ventana
ventana = tk.Tk()

ventana.geometry('600x400')

ventana.title('ventanona')

ventana.configure(background='#1d2d44')

def saludar():
    print('salu2')

#botones
boton1 = ttk.Button(ventana, text= 'enviar', command=saludar)
boton1.pack(pady=20)

ventana.mainloop()