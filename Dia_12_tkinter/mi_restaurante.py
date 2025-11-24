from tkinter import *

operador =''

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador=''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

#iniciar tkinter
aplicacion = Tk()
aplicacion.geometry('1090x630+0+0')
aplicacion.resizable(0, 0)
aplicacion.title('Mi restaurante - sistema pro max hd 4k 1 link mega')
aplicacion.config(bg='dark goldenrod')

# PANEL SUPERIOR
panel_superior = Frame(aplicacion, bd=1, relief=FLAT, bg='burlywood')
panel_superior.pack(side=TOP, fill="x")

panel_superior.grid_columnconfigure(0, weight=1)

etiqueta_titulo = Label(panel_superior,
                        text='Sistema de Facturacion',
                        fg='azure4',
                        font=('Dosis', 58),
                        bg='burlywood')
etiqueta_titulo.grid(row=0, column=0)

# PANEL IZQUIERDO
panel_izquiero = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquiero.pack(side=LEFT)

panel_costos = Frame(panel_izquiero, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

panel_comidas = LabelFrame(panel_izquiero, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquiero, text='Bebidas', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquiero, text='Postres', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# PANEL DERECHO (corregido)
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'pizza1', 'pizza2']
lista_bebidas = ['agua', 'soda', 'jugo', 'vino', 'Cerveza']
lista_postres = ['helado', 'chocoflan', 'brownies', 'flan', 'pay']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_comida[contador])

    comida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')

    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)

    contador += 1

# generar items bebida
variables_bebidas = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebidas in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebidas.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_bebidas[contador])

    bebida.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')


    # crear los cuadros de entrada
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)

    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0

for postres in lista_postres:
    # crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postres.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                         variable=variables_postres[contador])

    postre.grid(row=contador, column=0, sticky=W)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')

    # crear los cuadros de entrada
    cuadros_postres[contador] = Entry(panel_postres, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador, column=1)

    contador += 1

#variables
var_costo_comida= StringVar()
var_costo_bebida= StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#etiquetas de costo y campos de entrada comida
etiqueta_costo_comida= Label(panel_costos, text='Costo Comida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida=Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state= 'readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1, padx=41)

#etiquetas de costo y campos de entrada bebida
etiqueta_costo_bebida= Label(panel_costos, text='Costo Bebida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida=Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state= 'readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1, padx=41)

#etiquetas de costo y campos de entrada postres
etiqueta_costo_postre= Label(panel_costos, text='Costo Postre', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre=Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state= 'readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1, padx=41)


#etiquetas de costo y campos de entrada subtotal
etiqueta_subtotal= Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal=Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state= 'readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)

#etiquetas de costo y campos de entrada impuestos
etiqueta_impuestos= Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos=Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state= 'readonly', textvariable=var_impuesto)
texto_impuestos.grid(row=1,column=3, padx=41)

#etiquetas de costo y campos de entrada total
etiqueta_total= Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total=Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state= 'readonly', textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)


#botones
botones=['Total','Recibo','Guardar','Resetear']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 11, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    boton.grid(row=0, column=columnas)
    columnas+=1

#recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)


#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4,pady=10)

botones_calculadora=['7','8','9','+',
                     '4','5','6','-',
                     '1','2','3','x',
                     '=','B','0','/']

botones_guardados=[]

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   width=7,
                   bd=1,
                   fg='white',
                   bg='azure4')
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna,pady=1)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna=0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))


# evitar que la pantalla se cierre
aplicacion.mainloop()