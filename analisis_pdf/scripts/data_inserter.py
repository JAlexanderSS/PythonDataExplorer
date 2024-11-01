from sqlalchemy import insert
from sqlalchemy.orm import Session

# Función para insertar datos en la tabla helicobacter_tests


def insertar_datos_bd(engine, helicobacter_tests, datos):
    with Session(engine) as session:
        session.execute(insert(helicobacter_tests).values(datos))
        session.commit()  # Confirmación de la transacción
    print("Datos insertados correctamente en la base de datos.")
