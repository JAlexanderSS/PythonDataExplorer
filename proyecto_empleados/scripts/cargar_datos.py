# cargar_datos.py
import re


def cargar_datos(ruta_archivo):
    """Carga los datos desde un archivo .txt y retorna los encabezados y una lista de registros completos."""
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        content = f.read()

    # Reemplazar saltos de línea que no están antes de 'E' o 'ID_Empleado' con un espacio
    content = re.sub(r'\n(?!E\d{3}|ID_Empleado)', ' ', content)

    # Dividir el contenido en líneas
    lines = content.strip().split('\n')

    # Eliminar líneas vacías y espacios extra
    lines = [line.strip() for line in lines if line.strip()]

    # La primera línea es el encabezado
    header_line = lines[0]
    field_names = [field.strip() for field in header_line.split(',')]

    records = lines[1:]

    return field_names, records
