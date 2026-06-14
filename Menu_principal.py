import csv
from datos import cargar_paises, guardar_paises
from agregar_modificar import agregar_pais, modificar_pais
from Buscar_por_nombre import buscar_pais
from busqueda_filtros import busqueda_filtros

def mostrar_menu():   
    while True:
        try:
            print("\n---|Enciclopedia de paises|---")
            print("1°) - Agregar un pais")
            print("2°) - Actualizar los datos de Población y Superficie de un País")
            print("3°) - Buscar un país por nombre")
            print("4°) - Buscar por filtro")
            print("5°) - Ordenar paises")
            print("6°) - Salir")  

            eleccion = int(input("Ingrese una opción del menu: "))

            if eleccion < 1 or eleccion > 6:
                print(
                    "\nError: Debe ingresar un numero dentro del rango de las opciones (1/6)"
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
   # Vamos añadiendo las opciones a medida que completemos
    
    opcion = mostrar_menu()
    if opcion == 1:
        agregar_pais(paises)
        guardar_paises(paises, archivo)
    if opcion == 2:
        modificar_pais(paises) 
        guardar_paises(paises, archivo)
    if opcion == 3:
        buscar_pais(archivo)
        guardar_paises(paises, archivo)
    if opcion == 4:
        busqueda_filtros(archivo)
        guardar_paises(paises, archivo)

        # guardar_paises(archivo) ver si guardamos
        print("Saliendo del programa, hasta pronto")
        break