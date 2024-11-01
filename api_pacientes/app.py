# app.py
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Configurar conexión a la base de datos
DATABASE_URL = "postgresql+psycopg2://postgres:Alex5003+-@localhost:5432/prueba_tecnica"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
metadata = MetaData()
metadata.reflect(bind=engine)

# Cargar la tabla helicobacter_tests de la base de datos
helicobacter_tests = metadata.tables['helicobacter_tests']


@app.route('/helicobacter', methods=['GET'])
def obtener_test_helicobacter():
    nombre_paciente = request.args.get('nombre_paciente')
    if not nombre_paciente:
        return jsonify({"error": "Se requiere el parámetro 'nombre_paciente'"}), 400

    session = Session()
    try:
        # Consulta para obtener datos del test helicobacter por nombre de paciente
        test_data = session.query(helicobacter_tests).filter(
            helicobacter_tests.c.nombre_paciente == nombre_paciente
        ).all()

        if test_data:
            # Estructurar los datos en JSON
            resultados = [
                {
                    "ID": test.id,
                    "Proveedor": test.nombre_proveedor,
                    "Paciente": test.nombre_paciente,
                    "Fecha Emisión": test.fecha_emision,
                    "Resultado": test.resultado,
                    "Fecha Lectura": test.fecha_lectura
                } for test in test_data
            ]
            return jsonify(resultados), 200
        else:
            return jsonify({"error": "No se encontraron pruebas para el paciente especificado"}), 404
    finally:
        session.close()


if __name__ == '__main__':
    app.run(debug=True)
