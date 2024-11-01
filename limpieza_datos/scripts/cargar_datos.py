import pandas as pd
import re


def cargar_datos_ordenados(ruta_archivo):
    """
    Carga y organiza los datos de pacientes desde un archivo de texto, asegurando que cada paciente tenga una fila.
    Los valores faltantes se reemplazan por 'NA'.

    Args:
        ruta_archivo (str): Ruta del archivo de texto con los datos.

    Returns:
        pd.DataFrame: DataFrame con los datos organizados por paciente.
    """
    # Leer el archivo completo como texto
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        contenido = file.read()

    # Definir el encabezado manualmente
    encabezado = [
        "ID Paciente", "Nombre", "Apellido", "Edad", "Sexo", "Fecha Nacimiento", "Email", "Teléfono",
        "Dirección", "Ciudad", "País", "Fecha Muestra", "Tipo de Muestra", "Resultado Influenza",
        "Observaciones", "Fecha Resultado", "Temperatura", "Sintomas", "Responsable"
    ]

    # Dividir el contenido por pacientes usando el patrón ID del paciente (por ejemplo, P001)
    pacientes = re.split(r'\nP\d{3},', contenido)
    datos = []

    # Iterar sobre cada bloque de datos de un paciente
    # Ignorar el primer elemento (antes del primer paciente)
    for i, paciente in enumerate(pacientes[1:], start=1):
        # Añadir el ID del paciente al inicio del bloque
        paciente = f"P{i:03}," + paciente
        # Dividir el bloque en columnas, respetando comas dentro de comillas
        fila = re.split(r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', paciente.strip())

        # Si faltan columnas, completar con 'NA'
        if len(fila) < len(encabezado):
            fila.extend(['NA'] * (len(encabezado) - len(fila)))
        # Si hay columnas de más, recortar para que coincida con el encabezado
        elif len(fila) > len(encabezado):
            fila = fila[:len(encabezado)]

        # Añadir la fila procesada a los datos
        datos.append(fila)

    # Crear el DataFrame con el encabezado y los datos
    df = pd.DataFrame(datos, columns=encabezado)

    # Reemplazar los valores vacíos o 'NA' por el valor 'NA' de pandas
    df = df.replace('', 'NA')

    return df
