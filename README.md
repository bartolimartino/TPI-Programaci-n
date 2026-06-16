# TPI — Gestión de Datos de Países con Python

**Trabajo Práctico Integrador — Programación I**  
Tecnicatura Universitaria en Programación — UTN (Modalidad a Distancia)

---

## Descripción

Sistema de gestión de información sobre países desarrollado en Python 3, que permite cargar datos desde un archivo CSV y realizar operaciones de consulta, filtrado, ordenamiento y análisis estadístico sobre el dataset. El programa funciona completamente en consola mediante un menú interactivo de opciones.

El objetivo principal del proyecto es afianzar el uso de estructuras de datos (listas y diccionarios), modularización con funciones, técnicas de filtrado y ordenamiento, y persistencia de datos mediante archivos CSV, aplicando los conceptos aprendidos en Programación I.

---

## Requisitos

- Python 3.x (se recomienda Python 3.10 o superior)
- No requiere instalación de librerías externas
- Solo utiliza módulos de la librería estándar de Python: `csv` y `os`

---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/bartolimartino/TPI-Programaci-n.git
cd TPI-Programaci-n
```

### 2. Verificar que el archivo CSV esté presente

Todos los archivos deben estar en la misma carpeta:

```
TPI-Programaci-n/
├── Menu_principal.py
├── datos.py
├── agregar_modificar.py
├── Busqueda_por_nombre.py
├── busqueda_filtros.py
├── ordenar.py
├── estadisticas.py
└── paises.csv
```

### 3. Ejecutar el programa

```bash
python Menu_principal.py
```

> **Importante:** ejecutar siempre desde la carpeta raíz del repositorio para que Python encuentre correctamente el archivo `paises.csv` y los módulos del proyecto.

---

## Estructura del proyecto

| Archivo | Responsabilidad |
|---|---|
| `Menu_principal` | Punto de entrada. Menú principal y coordinación entre módulos. |
| `datos.py` | Lectura y escritura del archivo CSV. Validación de formato. |
| `agregar_modificar.py` | Agregar y actualizar datos de países. Interacción con el usuario. |
| `Buscar_por_nombre.py` | Buscar un país y mostrar sus datos. Interacción con el usuario. |
| `busqueda_filtros.py` | Permite realizar filtros por criterios. Interacción con el usuario. |
| `ordenar.py.py` | Permite ordenar los datos por criterio. Interacción con el usuario. |
| `estadisticas.py` | Cálculo de estadísticas: máximos, mínimos, promedios y conteos. |
| `paises.csv` | Dataset base con 25 países (5 por continente). |

---

## Funcionalidades

- **Agregar país:** solicita nombre, población, superficie y continente. Valida que ningún campo esté vacío, que población y superficie sean enteros positivos, y que el país no exista previamente.
- **Modificar país:** busca un país por nombre y permite modificar su población y superficie. Muestra los valores actuales y solicita confirmación antes de aplicar los cambios.
- **Buscar país:** búsqueda por nombre sin distinguir mayúsculas y minúsculas.
- **Filtrar por continente:** muestra todos los países del continente seleccionado.
- **Filtrar por rango de población:** muestra los países cuya población se encuentra entre un mínimo y un máximo ingresados por el usuario.
- **Filtrar por rango de superficie:** muestra los países cuya superficie se encuentra entre un mínimo y un máximo ingresados por el usuario.
- **Ordenar por nombre:** orden alfabético ascendente (A→Z) o descendente (Z→A).
- **Ordenar por población:** orden ascendente (menor→mayor) o descendente (mayor→menor).
- **Ordenar por superficie:** orden ascendente (menor→mayor) o descendente (mayor→menor).
- **Estadísticas:** país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.
- **Persistencia:** los cambios realizados durante la sesión se guardan automáticamente en el archivo CSV al salir del programa.

---

## Ejemplos de uso

### Menú principal

```
Enciclopedia de paises|
1°) - Agregar un pais
2°) - Actualizar los datos de Población y Superficie de un País"
3°) - Buscar un país por nombre
4°) - Buscar por filtro
5°) - Ordenar paises
6°) - Estadisticas
7°) - Salir

Ingrese una opción del menu: 
```

### Agregar un país

```
--- AGREGAR PAÍS ---
Nombre del país       : Uruguay
Población (habitantes): 3500000
Superficie (km²)      : 176215
Continente            : América

Exito: País -Uruguay- agregado correctamente.
```

### Ordenar por población descendente

```
Países ordenados por población (mayor → menor):

  N°    Nombre                    Población      Superficie   Continente
  ---- ------------------------- --------------- -----------  ------------
  1    India               1.417.173.000    3.287.263    Asia
  2    China               1.412.175.000    9.562.911    Asia
  3    Indonesia             275.501.000    1.904.569    Asia
  ...
```

### Estadísticas

```
---|Menú de Estadisticas|---
1°) - País con mayor y menor población
2°) - Promedio de población
3°) - Promedio de superficie
4°) - Cantidad de países por continente
5°) - Salir al menu principal

Ingrese una de las opciones: 

---

## Dataset

El archivo `paises.csv` contiene 25 países representativos de los cinco continentes (5 por continente). Los datos de población corresponden al año 2024 y los de superficie corresponden al año 2023 y fueron obtenidos de fuentes oficiales de organismos internacionales.:

- **Población:** Banco Mundial — indicador SP.POP.TOTL (https://data.worldbank.org/indicator/SP.POP.TOTL)
- **Superficie:** Banco Mundial / FAO — indicador AG.SRF.TOTL.K2 (https://data.worldbank.org/indicator/AG.SRF.TOTL.K2)
- **Clasificación de continentes:** ONU — Standard country or area codes M49 (https://unstats.un.org/unsd/methodology/m49/)

### Formato del CSV

```
nombre,poblacion,superficie,continente
Argentina,46235000,2780400,América
Brasil,215313000,8515767,América
...
```

---

## Integrantes

| Nombre | Participación |
|---|---|
| Monzón, Dario Alexis | Módulo `datos.py` (carga y guardado CSV), módulo `agregar_modificar.py`, modulo `ordenar.py`integración en `Menu_principal.py`, dataset `paises.csv`, documentación. |
| Martino Bartoli | Módulo `Menu_principal.py`Módulo `Buscar_por_nombre.py`, Módulo `busqueda_filtros.py`,Módulo `estadisticas.py` , README. |

---

## Links

- **Video demostrativo:** https://youtu.be/B2aIC-7Viqo
- **Documentación PDF:** [COMPLETAR — pegar aquí el link al PDF una vez subido al repositorio]

---

*Programación I — UTN Tecnicatura Universitaria en Programación — 2026*
