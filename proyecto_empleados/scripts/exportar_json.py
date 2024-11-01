# exportar_json.py
import json


def exportar_a_json(data, ruta_salida):
    """Exporta la estructura de datos a un archivo JSON."""
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Archivo JSON generado con éxito.")
