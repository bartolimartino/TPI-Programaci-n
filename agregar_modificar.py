"""
agregar_modificar.py — Módulo de operaciones sobre la lista de países.
Materia: Programación 1 — UTN Tecnicatura Universitaria en Programación
TPI: Gestión de Datos de Países en Python

"""
from datos import cargar_paises

CONTINENTES = ["América", "Europa", "Asia", "África", "Oceanía"]

# Funciones auxiliares


def verificar_texto(mensaje):
    """
    Solicita un texto por consola y repite hasta que el usuario
    ingrese algo distinto de vacío.

    Parámetros:
        mensaje (str): texto que se muestra al usuario.

    Retorna:
        str: texto ingresado sin espacios al inicio y al final.
    """
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("ERROR: Este campo no puede estar vacío. Intente nuevamente.")


def verificar_entero_positivo(mensaje):
    """
    Solicita un número entero positivo por consola y repite hasta que el usuario ingrese un valor válido.

    Parámetros:
        mensaje (str): texto que se muestra al usuario.

    Retorna:
        int: número entero positivo ingresado.
    """
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("ERROR: Este campo no puede estar vacío. Intente nuevamente.")
            continue
        try:
            numero = int(valor)
            if numero <= 0:
                print(f"ERROR: El valor debe ser mayor a cero. Intente nuevamente.")
                continue
            return numero
        except ValueError:
            print(f"ERROR: -{valor}- no es un número entero válido. Intente nuevamente.")

def verificar_repetido(lista_paises, nombre):
    """
    Busca un país por nombre exacto (sin distinguir mayúsculas y minusculas).
    
    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.
        nombre (str)             : nombre a buscar.

    Retorna:
        dict | None: el diccionario del país si lo encuentra, None si no.
    """
    nombre_title = nombre.title()
    for pais in lista_paises:
        if pais["nombre"].title() == nombre_title:
            return pais
    return None

# Agregar un pais

def agregar_pais(lista_paises):
    """
    Solicita los datos de un nuevo país por consola, valida cada campo
    y lo agrega a la lista si no existe previamente.

    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.

    Retorna:
        bool: True si se agregó el país, False si se canceló.
    """
    print("╔═════════════════════════════════════════════════════╗")
    print("║                  AGREGAR PAÍS                       ║")
    print("╚═════════════════════════════════════════════════════╝\n")
    print("(Presione Ctrl+C en cualquier momento para cancelar)\n")

    try:
        # Pedir y validar nombre
        while True:
            nombre = verificar_texto("Ingrese el Nombre del país: ").title()

            # Verificar que no exista ya en la lista
            if verificar_repetido(lista_paises, nombre) is not None:
                print(f"ERROR: El pais -{nombre}- ya existe en el sistema. Ingrese uno diferente.")
            else:
                break

        # Pedir y validar población
        poblacion = verificar_entero_positivo("Ingrese la Población (habitantes): ")

        # Pedir y validar superficie
        superficie = verificar_entero_positivo("Ingrese la Superficie en km²: ")

        # Pedir y validar continente
        print("Continentes: América, Europa, Asia, África, Oceanía")
        while True:
            continente = verificar_texto("Ingrese el Continente: ").title()

            # Verificar que no coincida con la lista
            if continente not in CONTINENTES:
                print(f"ERROR: Ingrese un continente correcto.")
            else:
                break
        

        # Construir el diccionario del nuevo país
        nuevo_pais = {
            "nombre"    : nombre,
            "poblacion" : poblacion,
            "superficie": superficie,
            "continente": continente
        }

        # Agregar a la lista
        lista_paises.append(nuevo_pais)
        print(f"\nExito - País -{nombre}- agregado correctamente.")
        return True

    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        return False



# Actualizar un país                                                              

def modificar_pais(lista_paises):
    """
    Busca un país por nombre y permite actualizar su población
    y superficie. El nombre y el continente no se modifican.

    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.

    Retorna:
        bool: True si se actualizó, False si no se encontró o se canceló.
    """

    print("╔═════════════════════════════════════════════════════╗")
    print("║                 MODIFICAR PAÍS                      ║")
    print("╚═════════════════════════════════════════════════════╝\n")
    print("(Presione Ctrl+C en cualquier momento para cancelar)\n")

    try:
        # Buscar el país
        nombre = verificar_texto("ingrese el Nombre del país a modificar: ")
        pais = verificar_repetido(lista_paises, nombre)

        if pais is None:
            print(f"\nERROR: No se encontró un país con el nombre -{nombre}-.")
            return False

        # Mostrar datos actuales
        print(f"\n  Datos actuales de -{pais["nombre"]}-:")
        print(f"    Población  : {pais["poblacion"]:,}")
        print(f"    Superficie : {pais["superficie"]:,} km²")
        print()

        # Pedir nuevos valores
        nueva_poblacion  = verificar_entero_positivo("Nueva población (habitantes): ")
        nueva_superficie = verificar_entero_positivo("Nueva superficie en (km²): ")

        # Confirmar antes de guardar
        print(f"\n  Nuevos datos para para -{pais["nombre"]}-:")
        print(f"    Población anterior: {pais["poblacion"]:,} - Nueva Poblacion: {nueva_poblacion:,}")
        print(f"    Superficie anterior: {pais["superficie"]:,} - Nueva Superficie: {nueva_superficie:,} km²")

        confirmacion = input("\n  ¿Confirma los cambios? (s/n): ").strip().lower()

        if confirmacion != "s":
            print("\nModificacion cancelada. No se realizaron cambios.")
            return False

        # Modificar el diccionario
        pais["poblacion"]  = nueva_poblacion
        pais["superficie"] = nueva_superficie

        print(f"\nEXITO - El País -{pais['nombre']}- ha sido modificado correctamente.")
        return True

    except KeyboardInterrupt:
        print("\nOperación cancelada.")
        return False

paises = cargar_paises("paises.csv")


