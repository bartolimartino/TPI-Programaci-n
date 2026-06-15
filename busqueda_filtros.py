import csv

def eliminar_tildes(texto):
    texto = texto.lower().replace(" ", "")
    texto = (
        texto.replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
    )
    return texto

def busqueda_filtros(lista_paises):
    while True:
        try:
            print("\n ---|Menú de filtros|---")
            print("1°) - Filtrar pais por continente")
            print("2°) - Filtrar por Rango de Población")
            print("3°) - Filtrar por Rango de Superficie")
            print("4°) - Salir al menu principal")

            sub_busqueda = int(input("Ingrese una de las opciones: "))
            if sub_busqueda <= 0 or sub_busqueda > 4:
                print("Error: Debe ingresar una opcion entre las disponibles (1/4)")
                continue

        except ValueError:
            print("Error: Caracter no valido, intente de nuevo")
            continue
        
        else:
            
               # ---- Desarrollo de la primera 1° subopcion -----

            if sub_busqueda == 1:
                print("\n--|Busqueda por continente|--")
                filtrar_continente = eliminar_tildes(input("-Ingrese un continente para filtrar: ").replace(" ", "").lower())

                encontrado = False
                try:
                        for fila in lista_paises:
                            if eliminar_tildes(fila["continente"]) == filtrar_continente:

                                if not encontrado:
                                    print("\n---| Paises filtrados |---")

                                print(f"Pais: {fila['nombre']} | Poblacion: {fila['poblacion']} | Superficie: {fila['superficie']} km²")
                                encontrado = True
                                

                        if not encontrado:
                            print("\n No se encontraron paises en ese continente")
                    

                except FileNotFoundError:
                    print(f"\nError: El archivo no existe")



                # ---- Desarrollo de la segunda 2° subopcion -----
            elif sub_busqueda == 2:
                print("\n--|Busqueda por rango de población|--")
                while True:
                    try:
                        poblacion_minima = int(input("Ingrese el rango minimo de población: "))
                        poblacion_maxima = int(input("Ingrese el rango maximo de población: "))
                        if poblacion_minima <= 0 or poblacion_maxima <= poblacion_minima:

                            print("Error: El rango minimo no puede ser menor o igual a 0, y el rango maximo no puede ser igual o menor al rango minimo"
                                  )
                            continue
                        encontrado = False

                        for fila in lista_paises:
                            poblacion_actual = int(fila["poblacion"])

                            if poblacion_minima <= poblacion_actual <= poblacion_maxima:
                                if not encontrado:
                                    print("\n---| Países encontrados |---")

                                print(f"Pais: {fila['nombre']} | Población: {fila['poblacion']} | Superficie: {fila['superficie']} km² | Continente: {fila['continente']}")
                                encontrado = True
                                    
                            if not encontrado:
                                print("\n No se encontraron paises dentro de ese rango.")
                        break

                    except ValueError:
                        print("Error: Debes ingresar números enteros, Intenta de nuevo.")
                        continue

                        # ---- Desarrollo de la tercera 3° subopcion -----
            elif sub_busqueda == 3:
                print("\n--|Busqueda por rango de superficie|--")
                while True:
                    try:
                        superficie_minima = int(input("Ingrese el rango minimo de superficie km²: "))
                        superficie_maxima = int(input("Ingrese el rango maximo de superficie km²: "))
                        if superficie_minima <= 0 or superficie_maxima <= superficie_minima:

                            print("Error: La Superficie minima no puede ser menor o igual a 0, y la Superficie maxima no puede ser igual o menor a la Superficie minima"
                                  )
                            continue

                        encontrado = False
                        
                        for fila in lista_paises:
                            superficie_actual = int(fila["superficie"])

                            if superficie_minima <= superficie_actual <= superficie_maxima:
                                if not encontrado:
                                    print("\n---| Países encontrados |---")

                                print(f"Pais: {fila['nombre']} | Población: {fila['poblacion']} | Superficie: {fila['superficie']} km² | Continente: {fila['continente']}")
                                encontrado = True
                                    
                            if not encontrado:
                                print("\n No se encontraron paises dentro de ese rango.")

                        break

                    except ValueError:
                        print("Error: Debes ingresar números enteros, Intenta de nuevo.")
                        continue

            elif sub_busqueda == 4:
                return




                
           

