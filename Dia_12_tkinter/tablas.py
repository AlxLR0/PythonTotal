import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#crear ventana
ventana = tk.Tk()

ventana.geometry('600x400')

ventana.title('tabla')

ventana.configure(background='#1d2d44')
#evitar resimensionar la ventana
ventana.resizable(0,0)

#configurar grid
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=0)

#definir estilos
estilos = ttk.Style()
estilos.theme_use('clam') #prepara el manejo de tema oscuro
estilos.configure('Treeview',
                  background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30)

estilos.map('Treeview',  background=[('selected','#3a86ff')])



#definir columnas
columnas = ('ID','Nombre','Edad')
tabla = ttk.Treeview(ventana, columns= columnas, show='headings')

#cabeceros
tabla.heading('ID', text='ID', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# formato a las columnas
tabla.column('ID', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

#cargar datos a la tabla
datos = ((1,'fulano', 25),(2,'sutanito',555))

for persona in datos:
    tabla.insert(parent='', index=tk.END, values= persona)

#agregar scroll bar
scrollbar =ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

#mostrar registro seleccionar

def mostrar_seleccion(event):
    elemento_seleccionado = tabla.selection()[0]#solo procesamos el primer registro
    elemento  =tabla.item(elemento_seleccionado)
    persona = elemento['values'] #tupla de persona
    showinfo(title='persona', message=f'Persona: {persona}')

#asociar el evento select de la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_seleccion)

#publicar tabla
tabla.grid(row=0,column=0, sticky=tk.NSEW)

ventana.mainloop()