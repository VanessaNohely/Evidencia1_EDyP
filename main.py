
"""
Evidencia1_EDyP

Autor: Vanessa Nohely Arrambide Escamilla - 1980877"""

"""Librerías y Modulos"""
import csv
import os
import pandas as pd
import uuid
from datetime import datetime


def registrar_nota():
    pass
 
def consultar_notas_por_periodo():
    pass
 
def consultar_nota_por_folio():
    pass
 
def cancelar_nota():
    pass
 
def recuperar_nota():
    pass
 
"""Menú Principal"""
def menu_principal():
    """Despliega el menú principal"""
    while True:
        print("\nMenú Principal")
        print("1. Registrar una nota")
        print("2. Consultas y reportes")
        print("3. Cancelar una nota")
        print("4. Recuperar una nota")
        print("5. Salir del sistema")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_nota()
        elif opcion == "2":
            print("\nMenú Principal>Consultas y reportes")
            print("1. Consulta por período")
            print("2. Consulta por folio")
            sub_opcion = input("Seleccione una opción: ")
            if sub_opcion == "1":
                consultar_por_periodo()
            elif sub_opcion == "2":
                consultar_por_folio()
        elif opcion == "3":
            cancelar_nota()
        elif opcion == "4":
            recuperar_nota()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu_principal()