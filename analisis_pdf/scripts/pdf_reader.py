import fitz  # PyMuPDF
from datetime import datetime
import re


def extraer_datos_pdf(ruta_pdf):
    datos = {
        "nombre_proveedor": None,
        "nombre_paciente": None,
        "fecha_emision": None,
        "resultado": None,
        "fecha_lectura": datetime.now()
    }

    with fitz.open(ruta_pdf) as pdf:
        for pagina in pdf:
            texto = pagina.get_text("text")

            # Estructura 1: Proveedor Blue Medical
            if "Blue Medical" in texto:
                datos["nombre_proveedor"] = "Blue Medical"

                # Nombre del Paciente
                match_paciente = re.search(r"Nombre:\s*(.+)", texto)
                if match_paciente:
                    datos["nombre_paciente"] = match_paciente.group(1).strip()

                # Fecha de Impresión como Fecha de Emisión
                match_fecha = re.search(
                    r"F\. Ingreso:\s*(\d{2}-\d{2}-\d{4})\s*(\d{1,2}:\d{2}\s*[APMapm]{2})", texto)
                if match_fecha:
                    fecha_str = match_fecha.group(1).strip()
                    hora_str = match_fecha.group(2).strip()
                    datos["fecha_emision"] = datetime.strptime(
                        f"{fecha_str} {hora_str}", "%d-%m-%Y %I:%M %p")

                # Resultado de Helicobacter Pylori
                match_resultado = re.search(
                    r"Helicobacter pylori Ag\.\s*\(Heces\)\s*(POSITIVO|NEGATIVO)", texto, re.IGNORECASE)
                if match_resultado:
                    datos["resultado"] = match_resultado.group(1).upper()

            # Estructura 2: Proveedor Tecniscan de Guatemala
            elif "Tecniscan de Guatemala" in texto:
                datos["nombre_proveedor"] = "Tecniscan de Guatemala"

                # Nombre del Paciente (captura hasta la "L", incluyendo saltos de línea opcionales)
                match_paciente = re.search(
                    r"Nombre del Paciente:\s*([\s\S]+?)\s*L\b", texto)
                if match_paciente:
                    datos["nombre_paciente"] = match_paciente.group(
                        1).replace('\n', ' ').strip()

                # Fecha de Ingreso como Fecha de Emisión
                match_fecha = re.search(
                    r"Fecha de Ingreso:\s*(\d{1,2}/\d{1,2}/\d{2})\n(\d{1,2}:\d{1,2}:\d{2})", texto)
                if match_fecha:
                    fecha_str = match_fecha.group(1).strip()
                    hora_str = match_fecha.group(2).strip()
                    print(fecha_str, hora_str)
                    datos["fecha_emision"] = datetime.strptime(
                        f"{fecha_str} {hora_str}", "%d/%m/%y %H:%M:%S")

                # Resultado de Helicobacter Pylori
                match_resultado = re.search(
                    r"[Hh]elicobacter ([Pp]ylor,|[Pp]ylori IgM)[^\n]*\n([*]\n)?(\d+\.\d+)", texto)
                if match_resultado:
                    resultado = match_resultado.group(3).strip()
                    valor_decimal = float(resultado)
                    if valor_decimal < 1.0:
                        datos["resultado"] = "NEGATIVO"
                    else:
                        datos["resultado"] = "POSITIVO"

            # Estructura 3: Centro De Diagnostico Centro Medico Las Americas
            elif "Centro De Diagnostico Centro Medico Las Americas" in texto:
                datos["nombre_proveedor"] = "Centro De Diagnostico Centro Medico Las Americas"

                # Nombre del Paciente
                match_paciente = re.search(r"Paciente:\s*(.+)", texto)
                if match_paciente:
                    datos["nombre_paciente"] = match_paciente.group(1).strip()

                # Fecha de Orden como Fecha de Emisión
                match_fecha = re.search(
                    r"Fecha impresión:\s*(\d{2}/\d{2}/\d{4})\s*(\d{1,2}:\d{2}(:\d{1,2})?)", texto)
                if match_fecha:
                    fecha_str = match_fecha.group(1).strip()
                    hora_str = match_fecha.group(2).strip()
                    datos["fecha_emision"] = datetime.strptime(
                        f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M" if len(hora_str) == 5 else "%d/%m/%Y %H:%M:%S")

                # Resultado de Helicobacter Pylori
                match_resultado = re.search(
                    r"HELICOBACTER PYLORI EN HECES\s*RESULTADO:\s*(.+)", texto)
                if match_resultado:
                    resultado = match_resultado.group(1).strip()
                    valor_decimal = float(resultado)
                    if valor_decimal < 1.0:
                        datos["resultado"] = "NEGATIVO"
                    else:
                        datos["resultado"] = "POSITIVO"

    # Verificar que todos los campos se hayan extraído correctamente
    for clave, valor in datos.items():
        if valor is None:
            print(f"Advertencia: No se pudo extraer el campo '{
                  clave}' del PDF.")

    return datos
