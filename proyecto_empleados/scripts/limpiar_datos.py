# limpiar_datos.py
def procesar_datos(field_names, records):
    employees = {}

    for record_line in records:
        # Reemplazar múltiples espacios por uno solo
        record_line = ' '.join(record_line.split())
        # Separar los campos
        fields = [field.strip() for field in record_line.split(
            ',', maxsplit=len(field_names)-1)]

        if len(fields) < len(field_names):
            print(f"Registro con campos insuficientes: {fields}")
            continue

        data = dict(zip(field_names, fields))

        employee_id = data['ID_Empleado']
        project_id = data['ID_Proyecto']

        revisores_str = data['Revisores']
        revisores = [rev.strip() for rev in revisores_str.split(',')]

        if employee_id not in employees:
            employee_data = {
                'ID_Empleado': data['ID_Empleado'],
                'Nombre': data['Nombre'],
                'Apellido': data['Apellido'],
                'Edad': data['Edad'],
                'Email': data['Email'],
                'Departamento': data['Departamento'],
                'Rol': data['Rol'],
                'Fecha_Contratacion': data['Fecha_Contratacion'],
                'Proyectos': {}
            }
            employees[employee_id] = employee_data

        employee_data = employees[employee_id]

        proyectos = employee_data['Proyectos']
        if project_id not in proyectos:
            project_data = {
                'ID_Proyecto': data['ID_Proyecto'],
                'Nombre_Proyecto': data['Nombre_Proyecto'],
                'Estado_Proyecto': data['Estado_Proyecto'],
                'Fecha_Inicio': data['Fecha_Inicio'],
                'Tareas': []
            }
            proyectos[project_id] = project_data

        project_data = proyectos[project_id]

        task_data = {
            'Tarea': data['Tarea'],
            'Fecha_Limite_Tarea': data['Fecha_Limite_Tarea'],
            'Estado_Tarea': data['Estado_Tarea'],
            'Revisores': revisores
        }

        project_data['Tareas'].append(task_data)

    # Convertir 'Proyectos' de diccionario a lista
    for employee in employees.values():
        employee['Proyectos'] = list(employee['Proyectos'].values())

    print("Estructura Final:", employees)  # Debug: Ver estructura final
    return list(employees.values())
