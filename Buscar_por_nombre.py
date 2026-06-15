import csv
# Funcion encargada de limpiar espacios vacios, tildes y mayusculas. 
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

# Funcion base de la opcion numero 3°, el usuario busca un pais por su nombre y el programa filtra el nombre ingresado para corroborar su existencia
# y posteriormente mostrar la información del mismo
def buscar_pais(lista_paises):
    while True:    
        print("\n---| Buscar un País por Nombre |---")
        busqueda = eliminar_tildes(input("Ingrese el nombre del país a buscar: "))

        # Filtro de espacios vacios
        if busqueda == "":
            print("Error: No se aceptan espacios vacios.")
            continue
        # Bucle for para buscar si el nombre se encuentra o no en el archivo.
        encontrado = False
        try:
            for fila in lista_paises:
                if eliminar_tildes(fila["nombre"]) == busqueda:
                    print("\n¡País Encontrado!")
                    print(f" Nombre:     {fila['nombre']}")
                    print(f" Población:  {fila['poblacion']}")
                    print(f" Superficie: {fila['superficie']} km²")
                    print(f" Continente: {fila['continente']}")
                    encontrado = True
                    
            if not encontrado:
                print(f"\nEl país '{busqueda.title()}' no está en la enciclopedia.")

            break

        except FileNotFoundError:
            print(f"\n Error: El archivo aún no existe. Cargá un país primero.")


