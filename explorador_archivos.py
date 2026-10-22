# Módulo 5: Manejo de excepciones y manipulación de archivos
# Actividad 2: Explorador y organizador de archivos

from pathlib import Path


def solicitar_directorio():
    """Solicita una ruta y valida que exista y sea un directorio."""
    entrada = input("Escribe la ruta del directorio que deseas explorar: ").strip().strip('"')
    ruta = Path(entrada).expanduser()

    if not ruta.exists():
        print("La ruta indicada no existe.")
        return None
    if not ruta.is_dir():
        print("La ruta indicada existe, pero no es un directorio.")
        return None

    return ruta


def mostrar_contenido(ruta):
    """Muestra los archivos y subdirectorios de una carpeta."""
    print(f"\nContenido de: {ruta.resolve()}")
    try:
        elementos = sorted(ruta.iterdir(), key=lambda elemento: (not elemento.is_dir(), elemento.name.lower()))
    except OSError as error:
        print(f"No se pudo leer el directorio: {error}")
        return

    if not elementos:
        print("El directorio está vacío.")
        return

    for elemento in elementos:
        tipo = "Directorio" if elemento.is_dir() else "Archivo" if elemento.is_file() else "Otro elemento"
        print(f"- [{tipo}] {elemento.name}")


def buscar_por_extension(ruta):
    """Busca archivos por extensión usando glob()."""
    extension = input("Escribe la extensión que deseas buscar (por ejemplo .pdf): ").strip()
    if not extension:
        print("Debes indicar una extensión.")
        return
    if not extension.startswith("."):
        extension = "." + extension

    try:
        resultados = sorted(
            (elemento for elemento in ruta.glob(f"*{extension}") if elemento.is_file()),
            key=lambda elemento: elemento.name.lower(),
        )
    except OSError as error:
        print(f"No se pudo realizar la búsqueda: {error}")
        return

    if not resultados:
        print(f"No se encontraron archivos con extensión {extension}.")
        return

    print(f"\nArchivos encontrados con extensión {extension}:")
    for archivo in resultados:
        print(f"Nombre: {archivo.name} | Extensión: {archivo.suffix or '(sin extensión)'} | Ubicación: {archivo.resolve()}")


def mostrar_informacion_archivo():
    """Muestra propiedades básicas de un archivo seleccionado."""
    entrada = input("Escribe la ruta del archivo: ").strip().strip('"')
    archivo = Path(entrada).expanduser()

    print("\n=== Información del archivo ===")
    print(f"Nombre: {archivo.name}")
    print(f"Extensión: {archivo.suffix or '(sin extensión)'}")
    print(f"Directorio padre: {archivo.parent}")
    print(f"Existe: {'Sí' if archivo.exists() else 'No'}")
    print(f"Es un archivo: {'Sí' if archivo.is_file() else 'No'}")
    print(f"Ruta completa: {archivo.resolve()}")

    if not archivo.exists():
        print("Aviso: el archivo o la ruta indicada no existe.")
    elif archivo.is_dir():
        print("Aviso: la ruta corresponde a un directorio, no a un archivo.")


def crear_directorio(ruta):
    """Crea un subdirectorio dentro de la carpeta seleccionada."""
    nombre = input("Nombre del nuevo directorio: ").strip()
    if not nombre:
        print("El nombre no puede quedar vacío.")
        return

    nuevo = ruta / nombre
    if nuevo.exists():
        print("Ya existe un archivo o directorio con ese nombre.")
        return

    try:
        nuevo.mkdir()
    except OSError as error:
        print(f"No se pudo crear el directorio: {error}")
    else:
        print(f"Directorio creado: {nuevo.resolve()}")


def categoria_por_extension(extension):
    """Asigna una carpeta destino según la extensión del archivo."""
    extension = extension.lower()

    categorias = {
        ".pdf": "Documentos",
        ".doc": "Documentos",
        ".docx": "Documentos",
        ".txt": "Texto",
        ".csv": "Datos",
        ".jpg": "Imagenes",
        ".jpeg": "Imagenes",
        ".png": "Imagenes",
        ".gif": "Imagenes",
    }
    return categorias.get(extension, "Otros")


def organizar_archivos(ruta):
    """Mueve archivos a carpetas según su extensión."""
    carpetas_protegidas = {"Documentos", "Texto", "Datos", "Imagenes", "Otros"}
    try:
        archivos = [elemento for elemento in ruta.iterdir() if elemento.is_file()]
    except OSError as error:
        print(f"No se pudo analizar el directorio: {error}")
        return

    if not archivos:
        print("No hay archivos para organizar en el nivel principal de este directorio.")
        return

    movidos = 0
    errores = 0

    for archivo in archivos:
        categoria = categoria_por_extension(archivo.suffix)
        destino_dir = ruta / categoria

        try:
            destino_dir.mkdir(exist_ok=True)
            destino = destino_dir / archivo.name

            if destino.exists():
                print(f"Se omitió '{archivo.name}': ya existe en '{destino_dir.name}'.")
                continue

            archivo.rename(destino)
            print(f"Movido: {archivo.name} -> {categoria}/")
            movidos += 1
        except OSError as error:
            print(f"No se pudo mover '{archivo.name}': {error}")
            errores += 1

    print(f"\nOrganización finalizada. Movidos: {movidos}. Errores: {errores}.")


def main():
    print("=== Explorador y organizador de archivos ===")
    ruta = solicitar_directorio()
    if ruta is None:
        print("No se puede continuar sin un directorio válido.")
        return

    while True:
        print(f"\nDirectorio actual: {ruta.resolve()}")
        print("1. Mostrar contenido del directorio")
        print("2. Buscar archivos por extensión")
        print("3. Mostrar información de un archivo")
        print("4. Crear directorio")
        print("5. Organizar archivos por extensión")
        print("6. Cambiar directorio")
        print("7. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mostrar_contenido(ruta)
        elif opcion == "2":
            buscar_por_extension(ruta)
        elif opcion == "3":
            mostrar_informacion_archivo()
        elif opcion == "4":
            crear_directorio(ruta)
        elif opcion == "5":
            confirmar = input("Esta opción moverá archivos dentro de subcarpetas. ¿Continuar? (s/n): ").strip().lower()
            if confirmar == "s":
                organizar_archivos(ruta)
            else:
                print("Operación cancelada.")
        elif opcion == "6":
            nueva_ruta = solicitar_directorio()
            if nueva_ruta is not None:
                ruta = nueva_ruta
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Selecciona una opción del 1 al 7.")


if __name__ == "__main__":
    main()
