#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para ejecutar la aplicación Zona Fit desde cualquier ubicación
"""
import sys
import os

# Agregar la ruta del proyecto al PATH
proyecto_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, proyecto_root)

# Importar y ejecutar la aplicación
from Dia_12_tkinter.zona_fit.zona_fit_app_gui import App

if __name__ == '__main__':
    app = App()
    app.mainloop()
