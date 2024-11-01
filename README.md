# Proyecto de Prueba Técnica

Este repositorio contiene la solución a una serie de ejercicios diseñados para evaluar habilidades en Python, manipulación de datos, manejo de bases de datos, creación de APIs y transformación de datos. Los ejercicios fueron desarrollados en Jupyter Notebook utilizando Python.

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
    - [Clonar el Repositorio](#clonar-el-repositorio)
    - [Configuración del Entorno Virtual](#configuración-del-entorno-virtual)
    - [Instalación de Dependencias](#instalación-de-dependencias)
- [Configuración de la Base de Datos](#configuración-de-la-base-de-datos)
    - [Reemplazo de Credenciales](#reemplazo-de-credenciales)
- [Ejecución de los Ejercicios](#ejecución-de-los-ejercicios)
    - [Ejercicio 1: Lectura de Archivos PDF](#ejercicio-1-lectura-de-archivos-pdf)
    - [Ejercicio 2: Limpieza y Traslado de Datos](#ejercicio-2-limpieza-y-traslado-de-datos)
    - [Ejercicio 3: Creación de API](#ejercicio-3-creación-de-api)
    - [Ejercicio 4: Transformación de Datos en JSON Complejo](#ejercicio-4-transformación-de-datos-en-json-complejo)
- [Uso de GIT para Versionado](#uso-de-git-para-versionado)
- [Conclusión](#conclusión)

## Descripción General

El proyecto aborda los siguientes ejercicios:

1. **Lectura de Archivos PDF**: Desarrollo de un algoritmo para extraer información de archivos PDF que contienen pruebas de Helicobacter Pylori y almacenamiento en una base de datos.

2. **Limpieza y Traslado de Datos**: Procesamiento y limpieza de un conjunto de datos, seguido de su inserción en una base de datos estructurada.

3. **Creación de API**: Desarrollo de una API que permite consultar los datos del ejercicio 1 utilizando Postman.

4. **Transformación de Datos en JSON Complejo**: Conversión de datos tabulares en una estructura JSON jerárquica y compleja.

## Requisitos Previos

- Python 3.7 o superior
- `pip` instalado
- PostgreSQL (o MySQL) para las bases de datos
- Postman para pruebas de la API
- Git para clonación y control de versiones

## Instalación y Configuración

### Clonar el Repositorio

Clona el repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

### Configuración del Entorno Virtual

Crea y activa un entorno virtual para aislar las dependencias del proyecto:

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate

# Activar el entorno virtual (Unix o MacOS)
source venv/bin/activate
```

### Instalación de Dependencias

Instala las dependencias necesarias utilizando `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Antes de ejecutar los ejercicios que interactúan con la base de datos, asegúrate de tener PostgreSQL (o MySQL) instalado y configurado.

### Reemplazo de Credenciales

En los scripts y notebooks, encontrarás cadenas de conexión a la base de datos. Reemplaza las credenciales de ejemplo con las de tu entorno:

```python
# Ejemplo de cadena de conexión
DATABASE_URI = "postgresql+psycopg2://usuario:contraseña@localhost:5432/nombre_base_datos"
```

Asegúrate de reemplazar:

- `usuario` por tu nombre de usuario de la base de datos.
- `contraseña` por tu contraseña de la base de datos.
- `nombre_base_datos` por el nombre de tu base de datos.

**Nota:** No compartas tus credenciales personales en repositorios públicos.

## Ejecución de los Ejercicios

A continuación, se detallan los pasos para ejecutar cada uno de los ejercicios.

### Ejercicio 1: Lectura de Archivos PDF

#### Descripción

Se desarrolló un algoritmo para leer archivos PDF que contienen pruebas de Helicobacter Pylori y extraer los siguientes datos:

- Nombre del proveedor
- Nombre del paciente
- Fecha de emisión del estudio
- Resultado del estudio (POSITIVO / NEGATIVO)
- Fecha y hora de lectura

#### Pasos para Ejecutar

1. **Preparar los Archivos PDF**: Coloca los archivos PDF en una carpeta específica dentro del proyecto, por ejemplo, `data/pdfs`.

2. **Configurar la Base de Datos**: Crea una base de datos en PostgreSQL y reemplaza la cadena de conexión en el notebook.

3. **Ejecutar el Notebook**: Abre y ejecuta el notebook `ejercicio1_lectura_pdfs.ipynb`.

#### Almacenamiento de Datos

Los datos extraídos se almacenan en una tabla llamada `pruebas_helicobacter` en la base de datos configurada.

### Ejercicio 2: Limpieza y Traslado de Datos

#### Descripción

Se realizó la limpieza y normalización de un conjunto de datos, abordando:

- Completar y corregir campos faltantes.
- Estandarización de fechas.
- Normalización de direcciones y ciudades.
- Eliminación de filas con datos irreparables.

#### Pasos para Ejecutar

1. **Cargar el Dataset**: Asegúrate de que el archivo de datos está disponible.

2. **Configurar la Base de Datos**: Crea las tablas `pacientes` y `resultados_influenza` en tu base de datos.

3. **Ejecutar el Notebook**: Abre y ejecuta el notebook.

#### Estructura de la Base de Datos

- **Tabla pacientes**: Contiene información personal del paciente.
- **Tabla resultados_influenza**: Contiene los resultados de laboratorio, enlazados por el ID del paciente.

### Ejercicio 3: Creación de API

#### Descripción

Se creó una API utilizando Flask que permite consultar los datos del ejercicio 1. La API devuelve los datos basados en el nombre del paciente.

#### Pasos para Ejecutar

1. **Configurar la Aplicación**: Asegúrate de que la cadena de conexión a la base de datos en `app.py` está correctamente configurada.

2. **Ejecutar la Aplicación**:

   ```bash
   python app.py
   ```

3. **Pruebas con Postman**:

    - Abre Postman y crea una nueva solicitud GET.
    - URL: `http://localhost:5000/pacientes?nombre=NombreDelPaciente`
    - Reemplaza `NombreDelPaciente` por el nombre del paciente que deseas consultar.
    - Envía la solicitud y verifica la respuesta.

### Ejercicio 4: Transformación de Datos en JSON Complejo

#### Descripción

Se transformaron datos tabulares en una estructura JSON jerárquica que refleja la organización de una empresa y sus proyectos.

#### Pasos para Ejecutar

1. **Preparar el Archivo de Datos**: Asegúrate de que el archivo `data/datos.txt` está disponible y correctamente formateado.

2. **Ejecutar el Notebook**: Abre y ejecuta el notebook.

3. **Visualizar el JSON**: El resultado se almacena en `data/empleados_proyectos.json`.

#### Estructura del JSON

El JSON resultante tiene la siguiente estructura:

- **Empleado**
    - Información básica
    - **Proyectos**
        - Detalles del proyecto
        - **Tareas**
            - Detalles de la tarea
            - **Revisores**

## Uso de GIT para Versionado

Se utilizó Git para el control de versiones durante el desarrollo del proyecto. A continuación, algunos de los comandos más utilizados:

- Clonar el repositorio:

  ```bash
  git clone https://github.com/JAlexanderSS/PythonDataExplorer.git
  ```

- Ver el estado de los cambios:

  ```bash
  git status
  ```

- Agregar cambios al staging:

  ```bash
  git add nombre_del_archivo
  ```

- Confirmar cambios:

  ```bash
  git commit -m "Descripción de los cambios"
  ```

- Enviar cambios al repositorio remoto:

  ```bash
  git push origin main
  ```

**Nota:** Recuerda de reemplazar `tu_usuario` y `tu_repositorio` por los valores correspondientes.

## Conclusión

Este proyecto aborda diferentes aspectos clave en el manejo de datos y desarrollo de software:

- **Procesamiento y extracción de información** de archivos PDF.
- **Limpieza y normalización de datos** para asegurar la calidad de la información.
- **Interacción con bases de datos relacionales** para almacenamiento y recuperación de datos.
- **Desarrollo de APIs RESTful** para exponer servicios y facilitar la comunicación entre aplicaciones.
- **Transformación y estructuración de datos** en formatos complejos como JSON.

**Información de Contacto**

- **Autor**: [José Alexander Sey Sirin]
- **Correo**: [jalexanderss5003@gmail.com]
- **GitHub**: [https://github.com/JAlexanderSS](https://github.com/JAlexanderSS)
