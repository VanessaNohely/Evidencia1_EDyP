
"""
Evidencia1_EDyP

Autor: Vanessa Nohely Arrambide Escamilla - 1980877
"""

"""Librerías y Modulos"""
import csv
import os
import pandas as pd
from statistics import mean, median, mode
import numpy as np
import uuid
from datetime import datetime

"""Funciones"""

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

def consultar_por_folio():
    """Consulta una nota específica por su folio"""
    notas = cargar_notas()
    for nota in notas:
        print(f"Folio: {nota['Folio']} - Fecha: {nota['Fecha']}")
    folio = input("Ingrese el folio de la nota a consultar: ")
    for nota in notas:
        if nota['Folio'] == folio and nota['Cancelada'] == "No":
            print(nota)
            return
    print("Nota no encontrada o cancelada.")

def cancelar_nota():
    """Permite cancelar una nota, solicitando confirmación al usuario"""
    notas = cargar_notas()
    folio = input("Ingrese el folio de la nota a cancelar: ")
    for nota in notas:
        if nota['Folio'] == folio and nota['Cancelada'] == 'No':
            print("Detalles de la nota:")
            print(nota)
            confirmacion = input("¿Está seguro de cancelar esta nota? (s/n): ")
            if confirmacion.lower() == 's':
                nota['Cancelada'] = 'Si'
                guardar_notas(notas)
                print("La nota ha sido cancelada exitosamente.")
            else:
                print("La nota no fue cancelada.")
            return
    print("El folio ingresado no existe o la nota ya está cancelada.")

def recuperar_nota():
    """Permite al usuario recuperar una nota previamente cancelada"""
    notas = cargar_notas()
    notas_canceladas = [nota for nota in notas if nota['Cancelada'].strip().lower() == "si"]
    if not notas_canceladas:
        print("No hay notas canceladas disponibles para recuperar.")
        return
    print("\nNotas canceladas disponibles para recuperar:")
    for nota in notas_canceladas:
        print(f"Folio: {nota['Folio']}, Fecha: {nota['Fecha']}, Cliente: {nota['Cliente']}, Monto: {nota['Monto']}")
    folio = input("\nIngrese el folio de la nota que desea recuperar (o presione Enter para cancelar): ")
    if not folio:
        print("Operación cancelada. No se recuperó ninguna nota.")
        return
    for nota in notas:
        if nota["Folio"] == folio and nota["Cancelada"].strip().lower() == "si":
            nota["Cancelada"] = "No"
            guardar_notas(notas)
            print(f"La nota con folio {folio} ha sido recuperada con éxito.")
            return
    print("No se encontró la nota en el sistema o no está cancelada.")

def filtrarNotasEstadisticas():
    """Se obtienen los datos necesarios para filtrar notas para analisis estadísticos."""
    notas = cargar_notas()
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD) o presione Enter para omitir: ")
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD) o presione Enter para omitir: ")

    if not fecha_inicio:
        fecha_inicio = min(nota['Fecha'] for nota in notas)
    if not fecha_fin:
        fecha_fin = max(nota['Fecha'] for nota in notas)
    
    notas_filtradas = [nota for nota in notas if fecha_inicio <= nota['Fecha'] <= fecha_fin and nota['Cancelada'] == "No"]

    return notas_filtradas

def analizar_tendencias_centrales():
    """Calcula y muestra las tendencias centrales y distribución."""
    notas = filtrarNotasEstadisticas()

    montos = [nota['Monto'] for nota in notas]

    if not montos:
        print("No hay datos disponibles para el período seleccionado.")
        return
    print("\nAnálisis de tendencias centrales y distribución:")
    print(f"Conteo: {len(montos)}")
    print(f"Media: {mean(montos)}")
    print(f"Mediana: {median(montos)}")
    try:
        print(f"Moda: {mode(montos)}")
    except:
        print("Moda: No hay una moda única")

def analizar_dispersion_y_distribucion():
    """Calcula y muestra la dispersión y distribución"""
    notas = filtrarNotasEstadisticas()
    montos = [nota['Monto'] for nota in notas]
    if not montos:
        print("No hay datos disponibles para el período seleccionado.")
        return
    print("\nAnálisis de dispersión y distribución:")
    print(f"Varianza: {np.var(montos, ddof=1)}")
    print(f"Desviación estándar: {np.std(montos, ddof=1)}")
    q1 = np.percentile(montos, 25)
    q3 = np.percentile(montos, 75)
    print(f"Primer cuartil (Q1): {q1}")
    print(f"Mediana (Q2): {median(montos)}")
    print(f"Tercer cuartil (Q3): {q3}")
    print(f"Rango intercuartílico (IQR): {q3 - q1}")




"""Menú Principal"""
def menu_principal():
    """Despliega el menú principal"""
    while True:
        print("\nMenú Principal")
        print("1. Registrar una nota")
        print("2. Consultas y reportes")
        print("3. Cancelar una nota")
        print("4. Recuperar una nota")
        print("5. Análisis estadístico de los totales por nota")
        print("6. Salir del sistema")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_nota()
        elif opcion == "2":
            print("\nMenú Principal>Consultas y reportes")
            print("1. Consulta por período")
            print("2. Consulta por folio")
            print("3. Regresar al menú principal")
            sub_opcion = input("Seleccione una opción: ")
            if sub_opcion == "1":
                consultar_por_periodo()
            elif sub_opcion == "2":
                consultar_por_folio()
            elif sub_opcion == "3":
                pass
            else:
                print(f"Opción '{sub_opcion}' no válida.")
        elif opcion == "3":
            cancelar_nota()
        elif opcion == "4":
            recuperar_nota()
        elif opcion == "5":
            print("\nMenú Principal>Análisis estadístico de los totales por nota")
            print("1. Tendencias centrales")
            print("2. Dispersión y distribución")
            print("3. Regresar al menú principal")
            sub_opcion = input("Seleccione una opción: ")
            if sub_opcion == "1":
                analizar_tendencias_centrales()
            elif sub_opcion == "2":
                analizar_dispersion_y_distribucion()
            elif sub_opcion == "3":
                pass
            else:
                print(f"Opción '{sub_opcion}' no válida.")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print(f"Opción '{opcion}' inválida.")
menu_principal()