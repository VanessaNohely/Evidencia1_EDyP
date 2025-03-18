#Archivo evidencia 1- Vanessa Nohely Arrambide Escamilla-1980877
def registrar_nota():
    pass
 
def consultas_reportes():
    pass
 
def cancelar_nota():
    pass
 
def recuperar_nota():
    pass
 
def menu_principal():
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
            consultas_reportes()
        elif opcion == "3":
            cancelar_nota()
        elif opcion == "4":
            recuperar_nota()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")