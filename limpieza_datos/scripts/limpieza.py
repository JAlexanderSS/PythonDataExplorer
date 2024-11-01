import pandas as pd
from datetime import datetime
import unicodedata


def quitar_tildes(texto):
    """Remueve las tildes de un texto."""
    if isinstance(texto, str):
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
    return texto


def limpiar_datos(df):
    """Limpia y estandariza los datos del DataFrame."""

    # Quitar tildes de los nombres de las columnas
    df.columns = [quitar_tildes(col) for col in df.columns]

    # Completar o corregir campos faltantes y estandarizar valores de NA/N/A
    df.replace(["N/A", "NA"], None, inplace=True)

    # Corrección de nombres y apellidos tipográficos
    if 'Apellido' in df.columns:
        df['Apellido'] = df['Apellido'].replace({
            'MarZnez': 'Martinez'  # Cambiar MarZnez a Martinez sin tilde
        })

    # Corrección en los correos electrónicos
    if 'Email' in df.columns:
        df['Email'] = df['Email'].str.replace(
            "marZnez", "martinez", regex=False)

    # Formato para números de teléfono (puedes adaptar a tus necesidades)
    if 'Telefono' in df.columns:
        df['Telefono'] = df['Telefono'].apply(
            lambda x: f"+{x}" if isinstance(x, str) and not x.startswith('+') else x)

    # Convertir fechas al formato YYYY-MM-DD y manejar valores nulos
    for col in ["Fecha Nacimiento", "Fecha Muestra", "Fecha Resultado"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col].astype(str).str.replace(
                r'[/-]', '-', regex=True), errors='coerce')

    # Calcular edad basada en la fecha de nacimiento
    if 'Fecha Nacimiento' in df.columns:
        today = pd.Timestamp.now()
        df['Edad'] = df['Fecha Nacimiento'].apply(
            lambda x: today.year - x.year -
            ((today.month, today.day) < (x.month, x.day))
            if pd.notnull(x) else None
        )

    # Convertir "Temperatura" a numérico y manejar valores nulos
    if 'Temperatura' in df.columns:
        df['Temperatura'] = pd.to_numeric(df['Temperatura'], errors='coerce')

    # Normalizar nombres de países y ciudades
    if 'Pais' in df.columns:
        df['Pais'] = df['Pais'].replace({
            'ArgenZna': 'Argentina',
            'Mexico': 'Mexico',
            'Peru': 'Peru'
        })
    if 'Ciudad' in df.columns:
        df['Ciudad'] = df['Ciudad'].replace({
            'SanZago': 'Santiago',
            'Ciudad de Mexico.': 'Ciudad de Mexico'
        })

    # Corrección para el campo "Resultado Influenza"
    if 'Resultado Influenza' in df.columns:
        df['Resultado Influenza'] = df['Resultado Influenza'].replace({
            'PosiZvo': 'Positivo',
            'NegaZvo': 'Negativo'
        })

    # Remover tildes de todos los valores de texto en el DataFrame
    df = df.applymap(quitar_tildes)

    return df
