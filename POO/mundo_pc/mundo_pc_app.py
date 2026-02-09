from POO.mundo_pc.Computdora import Computadora
from POO.mundo_pc.Monitor import Monitor
from POO.mundo_pc.Orden import Orden
from POO.mundo_pc.Raton import Raton
from POO.mundo_pc.Teclado import Teclado

print('***Mundo PC***')


#pc1
teclado1 = Teclado('hp','usb')
raton1 = Raton('hp','usb')
monitor1 = Monitor('hp',27)
computadora1 = Computadora('hp', monitor1, teclado1,raton1)

#lista de pc
computadoras1 = [computadora1]
orden1 = Orden(computadoras1)
print(orden1)
