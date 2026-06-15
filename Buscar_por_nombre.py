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

def buscar_pais(lista_paises):
    print("\n---| Buscar un País por Nombre |---")
    busqueda = eliminar_tildes(input("Ingrese el nombre del país a buscar: "))

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
                break  

        if not encontrado:
            print(f"\nEl país '{busqueda.title()}' no está en la enciclopedia.")

    except FileNotFoundError:
        print(f"\n Error: El archivo aún no existe. Cargá un país primero.")


