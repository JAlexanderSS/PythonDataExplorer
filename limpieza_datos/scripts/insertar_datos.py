import pandas as pd  # Agregar esta línea para usar pd.notnull
from sqlalchemy import Table, Column, Integer, String, Float, Date, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql import insert


def crear_tablas(engine):
    """Crea las tablas 'pacientes' y 'resultados_influenza' en la base de datos."""
    metadata = MetaData()

    # Tabla de pacientes
    pacientes = Table('pacientes', metadata,
                      Column('id_paciente', String, primary_key=True),
                      Column('nombre', String),
                      Column('apellido', String),
                      Column('edad', Integer),
                      Column('sexo', String),
                      Column('fecha_nacimiento', Date),
                      Column('email', String),
                      Column('telefono', String),
                      Column('direccion', String),
                      Column('ciudad', String),
                      Column('pais', String)
                      )

    # Tabla de resultados de influenza
    resultados_influenza = Table('resultados_influenza', metadata,
                                 Column('id_resultado', Integer,
                                        primary_key=True, autoincrement=True),
                                 Column('id_paciente', String, ForeignKey(
                                     'pacientes.id_paciente')),
                                 Column('fecha_muestra', Date),
                                 Column('tipo_muestra', String),
                                 Column('resultado_influenza', String),
                                 Column('observaciones', String),
                                 Column('fecha_resultado', Date),
                                 Column('temperatura', Float),
                                 Column('sintomas', String),
                                 Column('responsable', String)
                                 )

    # Crear las tablas
    metadata.create_all(engine)

    # Devolver referencias a las tablas creadas para ser utilizadas al insertar datos
    return pacientes, resultados_influenza


def insertar_datos(engine, df):
    """Inserta datos limpios en las tablas de la base de datos."""
    # Crear referencias a las tablas
    metadata = MetaData()
    pacientes, resultados_influenza = crear_tablas(engine)

    with engine.begin() as conn:  # Inicia una transacción
        for index, row in df.iterrows():
            # Insertar datos en 'pacientes'
            insert_paciente = insert(pacientes).values(
                id_paciente=row['ID Paciente'],
                nombre=row['Nombre'],
                apellido=row['Apellido'],
                edad=row['Edad'] if pd.notnull(row['Edad']) else None,
                sexo=row['Sexo'],
                fecha_nacimiento=row['Fecha Nacimiento'] if pd.notnull(
                    row['Fecha Nacimiento']) else None,
                email=row['Email'],
                telefono=row['Telefono'],
                direccion=row['Direccion'],
                ciudad=row['Ciudad'],
                pais=row['Pais']
            )
            conn.execute(insert_paciente)

            # Insertar datos en 'resultados_influenza'
            insert_resultado = insert(resultados_influenza).values(
                id_paciente=row['ID Paciente'],
                fecha_muestra=row['Fecha Muestra'] if pd.notnull(
                    row['Fecha Muestra']) else None,
                tipo_muestra=row['Tipo de Muestra'],
                resultado_influenza=row['Resultado Influenza'],
                observaciones=row['Observaciones'],
                fecha_resultado=row['Fecha Resultado'] if pd.notnull(
                    row['Fecha Resultado']) else None,
                temperatura=row['Temperatura'] if pd.notnull(
                    row['Temperatura']) else None,
                sintomas=row['Sintomas'],
                responsable=row['Responsable']
            )
            conn.execute(insert_resultado)
