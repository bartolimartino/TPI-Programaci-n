import csv
from datos import cargar_paises, guardar_paises
from agregar_modificar import agregar_pais, modificar_pais
from Buscar_por_nombre import buscar_pais
from busqueda_filtros import busqueda_filtros
from ordenar import submenu_orden, ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie, mostrar_lista
from estadisticas import realizar_estadisticas

def mostrar_menu():   
    while True:
        try:
            print("\n---|Enciclopedia de paises|---")
            print("1°) - Agregar un pais")
            print("2°) - Actualizar los datos de Población y Superficie de un País")
            print("3°) - Buscar un país por nombre")
            print("4°) - Buscar por filtro")
            print("5°) - Ordenar paises")
            print("6°) - Estadisticas")
            print("7°) - Salir")  

            eleccion = int(input("Ingrese una opción del menu: "))

            if eleccion < 1 or eleccion > 7:
                print(
                    "\nError: Debe ingresar un numero dentro del rango de las opciones (1/7)"
                )
                continue

            return eleccion

        except ValueError:
            print("\nError: Caracter no valido, intente de nuevo")
            continue


# ==================
# Bloque principal
# ==================

archivo = "paises.csv" 
paises = cargar_paises(archivo)

while True:
    try:
        opcion = mostrar_menu()
        if opcion == 1:
            agregar_pais(paises)
        if opcion == 2:
            modificar_pais(paises) 
        if opcion == 3:
            buscar_pais(paises)
        if opcion == 4:
            busqueda_filtros(paises)
        if opcion == 5:
            submenu_orden(paises)
        if opcion == 6:
            realizar_estadisticas(paises)
        if opcion == 7:
            guardar_paises(paises, archivo)
            print("Saliendo del programa, hasta pronto")
            break
        else:
            print("Opcion no validad intente nuevamente")
    except Exception as e:
        print("ERROR: Ocurrio un error inesperado:", type(e).__name__, {e})