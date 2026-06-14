"""
ordenar.py — Módulo de ordenamiento por nombre, población o superficie.
Materia: Programación 1 — UTN Tecnicatura Universitaria en Programación
TPI: Gestión de Datos de Países con Python

Responsabilidad: Ordenar los paises en funcion del criterio solicitado por el usuario.

"""
    
# Funciones auxiliares
def obtener_nombre(pais):
    return pais["nombre"].lower()

def obtener_poblacion(pais):
    return pais["poblacion"]

def obtener_superficie(pais):
    return pais["superficie"]

"""
    Ordena la lista de países por nombre alfabéticamente.
 
    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.
        ascendente (bool)        : True para A a Z, False para Z a A.
 
    Retorna:
        list[dict]: nueva lista ordenada (la original no se modifica).
    """
# Funciones de ordenamiento

def ordenar_por_nombre(lista_paises, ascendente=True):
    
    if len(lista_paises) == 0:
        print("\nERROR: No hay países cargados para ordenar.")
        return lista_paises
    
    lista_ordenada = sorted(lista_paises,key=obtener_nombre,reverse=not ascendente)
    direccion = "A a Z" if ascendente else "Z a A"
    print(f"\nPaíses ordenados por nombre ({direccion}):")
    mostrar_lista(lista_ordenada)
    return lista_ordenada

"""
    Ordena la lista de países por poblacion ascendente o descendente.
 
    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.
        ascendente (bool)        : True para menor a mayor, False para mayor a menor.
 
    Retorna:
        list[dict]: nueva lista ordenada (la original no se modifica).
    """

def ordenar_por_poblacion(lista_paises, ascendente=True):
    
    lista_ordenada = sorted(lista_paises, key=obtener_poblacion, reverse=not ascendente)
    direccion = "menor a mayor" if ascendente else "mayor a menor"
    print(f"\nPaíses ordenados por población ({direccion}):")
    mostrar_lista(lista_ordenada)
    return lista_ordenada

"""
    Ordena la lista de países por superficie ascendente o descendente.
 
    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.
        ascendente (bool)        : True para menor a mayor, False para mayor a menor.
 
    Retorna:
        list[dict]: nueva lista ordenada (la original no se modifica).
    """

def ordenar_por_superficie(lista_paises, ascendente=True):
    
    lista_ordenada = sorted(lista_paises, key=obtener_superficie, reverse=not ascendente)
    direccion = "menor a mayor" if ascendente else "mayor a menor"
    print(f"\nPaíses ordenados por superficie ({direccion}):")
    mostrar_lista(lista_ordenada)
    return lista_ordenada    
 

def mostrar_lista(lista_paises):
    """
    Muestra la lista de países en formato de tabla en consola.
 
    Parámetros:
        lista_paises (list[dict]): lista de países a mostrar.
    """
 
    print()
    print(f"{"-"*81}")
    print(f"|{"N°":<4} | {"Nombre":<25}| {"Población":<15}| {"Superficie":<15}| {"Continente":<11}|")
    print(f"{"-"*81}")
 
    for i, pais in enumerate(lista_paises, start=1):
        print(f"|{i:<4} "
            f"|{pais["nombre"]:<25} "
            f"|{pais["poblacion"]:>15,} "
            f"|{pais["superficie"]:>15,} "
            f"|{pais["continente"]:<12}|"
        )
    print()
 
# Submenu de opciones
def submenu_orden(lista_paises):
    """
    Muestra el menu de opciones para elegir el tipo de orden.
 
    Parámetros:
        lista_paises (list[dict]): lista de países a ordenar.
    """
    while True:
        try:
            print("╔═════════════════════════════════════════════════════╗")
            print("║         SUBMENU PARA ORDENAMIENTO DE PAISES         ║")
            print("╠═════════════════════════════════════════════════════╣")
            print("║Menu de Opciones:                                    ║")
            print("║1- Ordenar por nombre alfabeticamente                ║")
            print("║2- Ordenar por población                             ║")
            print("║3- Ordenar por Superficie                            ║")
            print("║4- Menu Principal 🚪                                 ║")
            print("╚═════════════════════════════════════════════════════╝\n")

            opcion = input("Ingrese una opcion: ")

            if opcion == "1":
                while True:
                    try:
                        orden =input("\nPara ordenar de (A → Z) ingrese A    -   Para ordenar de (Z → A) ingrese D: ").lower()
                        if orden not in ("a","d"): raise ValueError 
                        break
                    except ValueError: print("ERROR: Ingrese A o D. Reintente")
                if orden == "a" : ordenar_por_nombre(lista_paises)
                else: ordenar_por_nombre(lista_paises, ascendente=False)
                input("\nPresione un tecla para continuar...")
            elif opcion == "2":
                while True:
                    try:
                        orden =input("\nPara ordenar de (Menor → Mayor) ingrese A    -   Para ordenar de (Mayor → Menor) ingrese D: ").lower()
                        if orden not in ("a","d"): raise ValueError 
                        break
                    except ValueError: print("ERROR: Ingrese A o D. Reintente")
                if orden == "a" : ordenar_por_poblacion(lista_paises)
                else: ordenar_por_poblacion(lista_paises, ascendente=False)
                input("\nPresione un tecla para continuar...")
            elif opcion == "3":
                while True:
                    try:
                        orden =input("\nPara ordenar de (Menor → Mayor) ingrese A    -   Para ordenar de (Mayor → Menor) ingrese D: ").lower()
                        if orden not in ("a","d"): raise ValueError 
                        break
                    except ValueError: print("ERROR: Ingrese A o D. Reintente")
                if orden == "a" : ordenar_por_superficie(lista_paises)
                else: ordenar_por_superficie(lista_paises, ascendente=False)
                input("\nPresione un tecla para continuar...")
            elif opcion == "4":
                break
            else:
                print("Opcion no validad intente nuevamente")
        except Exception as e:
            print("ERROR: Ocurrio un error inesperado:", type(e).__name__, {e})
