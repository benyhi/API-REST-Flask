# Proyecto
## Descripcion del Proyecto

## Pasos necesarios para ejecutar la API

### Crear el entorno virtual
- ```python -m venv env```
### Activar el entorno virtual
### En Linux 
- ```source env/bin/activate```
### En Windows
- ```env\Scripts\activate.bat```
##### Instalar librerias necesarias
- ``` pip install -r requirements.txt```
##### Crear variable de entorno
- 1. Crear el archivo ".env" dentro directorio donde se clono el repositorio
- 2. Dentro del archivo colocar las siguientes lineas:
- SQLALCHEMY_DATABASE_URI = tu_host_base_datos (Por defecto para MySQL: "mysql+pymysql://root@localhost/nombre_bd")
- SECRET_KEY = tu_clave_secreta
## Ejecutar el Script.py
Este script es necesario para poblar la base de datos y crear el primer usuario admin.
- ``` python script.py ```
## Ejecutar el proyecto
- ```flask run --reload```

## Contacto
