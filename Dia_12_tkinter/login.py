import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

from pyexpat.errors import messages

#crear ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')

#grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

#crear estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white', fieldbackground='black')

estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active','#0a9396')])

#agregar frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=3)

#TITULO
etiqueta = ttk.Label(frame, text='Login', font=('Arial',20))
etiqueta.grid(row=0, column=0, columnspan=2)


#USER
usuario_label =ttk.Label(frame, text='Usuario')
usuario_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja=ttk.Entry(frame)
usuario_caja.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

#password
password_label =ttk.Label(frame, text='Password')
password_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja=ttk.Entry(frame, show='💩')
password_caja.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

#boton
login_boton = ttk.Button(frame, text='Enviar✔')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event):
    usuario = usuario_caja.get().lower()
    password = password_caja.get().lower()

    #si usuario es igual a root y pass es igual a admin

    if usuario == 'root' and password == 'admin':
        showinfo(title='login', message='👍')

    else:
        showerror(title='login', message='👎')


#asociar evento al boton de login
login_boton.bind('<Return>', validar)#presionar la tecla enter
login_boton.bind('<Button-1>', validar)#presionar click izquierdo



frame.grid(row=0, column=0)

ventana.mainloop()