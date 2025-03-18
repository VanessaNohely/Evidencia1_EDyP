
"""
Evidencia1_EDyP

Autor: Vanessa Nohely Arrambide Escamilla - 1980877"""

"""Librerías y Modulos"""
import csv
import os
import pandas as pd
import uuid
from datetime import datetime

def cargar_notas():
    """Carga las notas desde un archivo CSV"""
    notas = []
    if os.path.exists("notas.csv"):
        with open("notas.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Monto'] = float(row['Monto'])
                row['Servicios'] = eval(row['Servicios']) if 'Servicios' in row and row['Servicios'] else []
                notas.append(row)
    return notas

def guardar_notas(notas):
    """Guarda las notas en un archivo CSV"""
    with open("notas.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Folio", "Fecha", "Cliente", "Monto", "Servicios", "Cancelada"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for nota in notas:
            writer.writerow({**nota, "Servicios": str(nota.get("Servicios", []))})

def exportar_a_excel(notas, nombre_archivo="reporte.xlsx"):
    """Exporta las notas a un archivo de Excel"""
    df = pd.DataFrame(notas)
    df.to_excel(nombre_archivo, index=False)
    print(f"Reporte exportado como {nombre_archivo}")

def generar_folio():
    """Genera un folio único"""
    return str(uuid.uuid4())[:8]

def validar_fecha(fecha):
    """Verifica que la fecha no sea futura"""
    return datetime.strptime(fecha, "%Y-%m-%d") <= datetime.now()

def validar_monto(monto):
    """Valida que el monto sea mayor que 0"""
    return monto > 0

def registrar_nota():
    """Registra una nueva nota con múltiples servicios"""
    notas = cargar_notas()
    folio = generar_folio()
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    if not validar_fecha(fecha):
        print("Fecha inválida.")
        return
    cliente = input("Ingrese el nombre del cliente: ")
    servicios = []
    while True:
        servicio = input("Ingrese el nombre del servicio realizado: ")
        costo = float(input("Ingrese el costo del servicio: "))
        if not validar_monto(costo):
            print("Costo inválido, debe ser mayor que 0.")
            continue
        servicios.append({"Servicio": servicio, "Costo": costo})
        continuar = input("¿Desea agregar otro servicio? (s/n): ")
        if continuar.lower() != "s":
            break
    monto_total = sum(s["Costo"] for s in servicios)
    notas.append({"Folio": folio, "Fecha": fecha, "Cliente": cliente, "Monto": monto_total, "Servicios": servicios, "Cancelada": "No"})
    guardar_notas(notas)
    print("Nota registrada con éxito.")
 
def consultar_por_periodo():
    """Consulta notas en un período de tiempo y ofrece exportarlas a Excel"""
    notas = cargar_notas()
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
    notas_filtradas = [nota for nota in notas if fecha_inicio <= nota['Fecha'] <= fecha_fin and nota['Cancelada'] == "No"]
    if notas_filtradas:
        for nota in notas_filtradas:
            print(nota)
        if input("¿Desea exportar a Excel? (s/n): ") == "s":
            exportar_a_excel(notas_filtradas)
    else:
        print("No hay notas en este período.")
 
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