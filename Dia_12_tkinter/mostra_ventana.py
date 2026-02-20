import tkinter as tk

#crear ventana
ventana = tk.Tk()

#redimensionar la ventana
ventana.geometry('600x400')

#modificar titulo
ventana.title('ventanona')

#evitar resimensionar la ventana
ventana.resizable(0,0)

#color de la ventana
ventana.configure(background='#1d2d44')


#hacer visible la ventana
ventana.mainloop()