# Actividad 2: Explorador y organizador de archivos

**Materia:** Programación Avanzada  
**Módulo:** 5 — Manejo de rutas y directorios  
**Archivo principal:** `explorador_archivos.py`

## Descripción

Programa de consola que permite explorar un directorio indicado por el usuario, buscar archivos por extensión, consultar información de una ruta, crear carpetas y organizar archivos por tipo.

## Funcionalidades

1. **Mostrar contenido:** usa `Path` e `iterdir()` para distinguir archivos y directorios.
2. **Buscar por extensión:** utiliza `glob()` y muestra nombre, extensión y ubicación.
3. **Información de archivo:** muestra `.name`, `.suffix`, `.parent`, `exists()`, `is_file()` y la ruta completa.
4. **Crear directorio:** comprueba si el nombre ya existe y usa `mkdir()` para crear una carpeta.
5. **Organizar archivos:** mueve archivos del nivel principal a carpetas según su extensión:
   - `Documentos`: PDF, DOC y DOCX.
   - `Texto`: TXT.
   - `Datos`: CSV.
   - `Imagenes`: JPG, JPEG, PNG y GIF.
   - `Otros`: extensiones no contempladas en las categorías anteriores.
6. **Cambiar directorio:** permite seleccionar otra carpeta sin modificar el código.

## Precaución al organizar

La opción de organización **mueve los archivos** a subcarpetas dentro del directorio seleccionado. Utilízala primero con `carpeta_prueba` o con una carpeta de prueba. Si ya existe un archivo con el mismo nombre en la carpeta destino, el programa lo omite para no sobrescribirlo.

## Cómo ejecutar

Requiere Python 3. No necesita bibliotecas externas.

```bash
python explorador_archivos.py
```

En algunos sistemas puedes utilizar `python3 explorador_archivos.py`.

Al iniciar, escribe la ruta de la carpeta que deseas explorar. Puedes introducir una ruta absoluta o una ruta relativa al directorio desde el que ejecutas Python.

## Carpeta de prueba

El proyecto incluye `carpeta_prueba` con archivos ficticios de diferentes extensiones para probar la búsqueda y organización. No contienen información personal.
