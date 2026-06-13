"""
datos.py — Módulo de lectura y escritura del archivo CSV.
Materia: Programación 1 — UTN Tecnicatura Universitaria en Programación
TPI: Gestión de Datos de Países con Python

Responsabilidad: mover datos entre el archivo CSV y la memoria (y viceversa).

"""

import csv

DATOS_CSV = ["nombre", "poblacion", "superficie", "continente"]

def validar_fila(fila, numero_fila):
    """
    Valida que cada fila del CSV tenga el formato correcto.

    Parámetros:
        fila (dict)       : fila leída por csv.DictReader, con claves del encabezado.
        numero_fila (int) : número de fila en el archivo (para mensajes de error).

    Retorna:
        (bool, str): True y mensaje vacío si es válida,
                     False y mensaje descriptivo si hay error.
    """

    # Verificar que existan todos los campos requeridos
    for campo in DATOS_CSV:
        if campo not in fila:
            return False, f"Fila {numero_fila}: falta la columna '{campo}' en el encabezado del CSV."

    # Verificar que ningún campo esté vacío
    for campo in DATOS_CSV:
        if fila[campo].strip() == "":
            return False, f"Fila {numero_fila}: el campo '{campo}' está vacío."

    # Verificar que población sea un entero positivo
    try:
        poblacion = int(fila["poblacion"].strip())
        if poblacion <= 0:
            return False, f"Fila {numero_fila}: -poblacion- debe ser un número entero positivo (se recibió {poblacion})."
    except ValueError:
        return False, f"Fila {numero_fila}: -poblacion- no es un dato válido (se recibió '{fila["poblacion"].strip()}')."

    # Verificar que superficie sea un entero positivo
    try:
        superficie = int(fila["superficie"].strip())
        if superficie <= 0:
            return False, f"Fila {numero_fila}: -superficie- debe ser un número positivo (se recibió {superficie})."
    except ValueError:
        return False, f"Fila {numero_fila}: -superficie- no es un número válido (se recibió '{fila["superficie"].strip()}')."

    return True, ""



def cargar_paises(archivo_csv):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada país. 
    Si el archivo no existe o contiene errores de formato, muestra un mensaje y retorna None.

    Parámetros:
        archivo_csv (str): ruta al archivo CSV (ej: "paises.csv").

    Retorna:
        list[dict] | None: lista de países si la carga fue exitosa,
                           None si hubo algún error.

    Estructura de cada diccionario:
        {
            "nombre"    : str,
            "poblacion" : int,
            "superficie": int,
            "continente": str
        }
    """

    # Intentar abrir el archivo
    try:
        with open(archivo_csv, "r", newline="", encoding="utf-8") as archivo:
      
    # Leer el CSV con DictReader (primera fila como encabezado)
            lector = csv.DictReader(archivo)

    # Verificar el encabezado tenga los campos requeridos
            for campos in lector.fieldnames:
                if not campos in DATOS_CSV:
                    print(f"\nERROR: El archivo '{archivo_csv}' no tiene los campos correctos.")
                    print(f"         Se esperan las columnas: {', '.join(DATOS_CSV)}")
                    return None
                
   
            # Recorrer las filas y validar cada una
            lista_paises = []
            numero_fila = 1  # empieza en 1 porque la fila 0 es el encabezado

            for fila in lector:
                numero_fila += 1
                es_valida, mensaje_error = validar_fila(fila, numero_fila)

                if not es_valida:
                    print(f"\nERROR El archivo CSV contiene un error de formato.")
                    print(f"        {mensaje_error}")
                    print("        Verifíquelo y vuelva a intenter.")
                    archivo.close()
                    return None

            # Construir el diccionario del país
                pais = {
                    "nombre"    : fila["nombre"].strip(),
                    "poblacion" : int(fila["poblacion"].strip()),
                    "superficie": int(fila["superficie"].strip()),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais)

        # Verificar que el CSV no esté vacío
        if len(lista_paises) == 0:
            print(f"\nERROR: El archivo -{archivo_csv}- no contiene datos de países.")
            return None

        print(f"\nExito - Se cargaron {len(lista_paises)} países desde -{archivo_csv}-.")
        return lista_paises
    
    except FileNotFoundError:
        print(f"\nERROR: No se encontró el archivo '{archivo_csv}'.")
        print("Verifique que el archivo exista en la misma carpeta que el programa.")
        return None


def guardar_paises(lista_paises, archivo_csv):
    """
    Escribe la lista de países en el archivo CSV, sobreescribiendo el contenido
    anterior. Se llama al salir del programa o después de modificar datos.

    Parámetros:
        lista_paises (list[dict]): lista de países en memoria.
        archivo_csv (str)       : ruta al archivo CSV destino.

    Retorna:
        bool: True si el guardado fue exitoso, False si hubo un error.
    """

    try:
        with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.DictWriter(archivo, fieldnames=DATOS_CSV)
            escritor.writeheader()
            escritor.writerows(lista_paises)
           
            print(f"\nExito: Se guardaron {len(lista_paises)} países en '{archivo_csv}'.")
            return True

    except OSError:
            print(f"\nERROR: No se pudo escribir el archivo '{archivo_csv}'.")
            print("        Verifique que tenga permisos de escritura en la carpeta.")
            return False
    except Exception as e:
            print("ERROR: Ocurrio un error inesperado:", type(e).__name__, {e})





    