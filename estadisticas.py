import csv

# Funcion base correspondiente a la opcion numero 6°, esta opcion muestra un menu interactivo de 5 sub-opciones que muestran distintas estadisticas en base al archivo principal.
def realizar_estadisticas(lista_archivos):
     while True:
        try:
            print("\n ---|Menú de Estadisticas|---")
            print("1°) - País con mayor y menor población")
            print("2°) - Promedio de población")
            print("3°) - Promedio de superficie")
            print("4°) - Cantidad de países por continente")
            print("5°) - Salir al menu principal")

            sub_busqueda = int(input("Ingrese una de las opciones: "))
            if sub_busqueda <= 0 or sub_busqueda > 5:
                print("Error: Debe ingresar una opcion entre las disponibles (1/5)")
                continue

        except ValueError:
            print("Error: Caracter no valido, intente de nuevo")
            continue

        else:
            # Sub-opcion 1: muestra el pais con menor y mayor poblacion
            if sub_busqueda == 1:
                print("\n--|Pais con menor y mayor poblacion|--")

                pais_mas_poblado = max(lista_archivos, key=lambda pais: int(pais["poblacion"]))
                pais_menos_poblado = min(lista_archivos, key=lambda pais: int(pais["poblacion"]))

                print("\n---| Resultados |---")
                print(f"- Mayor población: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']} hab.)")
                print(f"- Menor población: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']} hab.)")
            
            # Sub-opcion 2: muestra un promedio de la poblacion de todos los paises del archivo
            elif sub_busqueda == 2:
                print("\n--|Promedio de población|--")

                poblacion_total = sum((int(pais["poblacion"]) for pais in lista_archivos))
                cantidad_paises = len(lista_archivos)

                promedio_poblacion = poblacion_total // cantidad_paises

                print("\n--|Resultados|--")
                print(f" El promedio total de la población es: {promedio_poblacion}")

            # Sub-opcion 3: muestra el promedio de la superficie de todos los paises del archivo
            elif sub_busqueda == 3:
                print("\n--|Promedio de superficie|--")

                superficie_total = sum(int(pais['superficie']) for pais in lista_archivos)
                cantidad_paises = len(lista_archivos)

                promedio_superficie = superficie_total // cantidad_paises

                print("\n--|Resultados|--")
                print(f"El promedio de la superficie total es: {promedio_superficie} km²")

            # Sub-opcion 4: Filtra todos los paises por sus respectivos continentes
            elif sub_busqueda == 4:
                conteo = {}
                for pais in lista_archivos: 
                    c = pais['continente']
                    conteo[c] = conteo.get(c, 0) + 1
                
                print("\n---| Paises por Continente |---")
                for continente, cantidad in conteo.items():
                    print(f" - {continente}: {cantidad} países")

            elif sub_busqueda == 5:
                return

                
                

                
                    
                



