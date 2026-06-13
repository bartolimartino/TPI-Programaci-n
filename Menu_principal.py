import csv


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

while True:
   # Vamos añadiendo las opciones a medida que completemos
    opcion = mostrar_menu()

