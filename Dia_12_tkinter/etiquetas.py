import tkinter as tk

#crear ventana
ventana = tk.Tk()

ventana.geometry('600x400')

ventana.title('ventanona')

ventana.configure(background='#1d2d44')

# crear etiqueta
etiqueta = tk.Label(ventana, text='hola mundo')

#cambiar el teexto usando el metodo configure
etiqueta.configure(text='🤖')

#cambiar el texto con la llave text
etiqueta['text']= 'holaa'

#publicar componente
etiqueta.pack(pady=20)

ventana.mainloop()