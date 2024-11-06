# Proyecto API REST con Flask

## Instalacion del proyecto

### Crear el entorno virtual
- ```python -m venv env```
- 
### Activar el entorno virtual
#### En Linux 
- ```source env/bin/activate```
#### En Windows
- ```env\Scripts\activate.bat```
- 
### Instalar librerias necesarias
- ``` pip install -r requirements.txt```
- 
### Crear variable de entorno
1. Crear el archivo ".env" dentro directorio donde se clono el repositorio
2. Dentro del archivo colocar las siguientes lineas:
SQLALCHEMY_DATABASE_URI = tu_host_base_datos (Por defecto para MySQL: "mysql+pymysql://root@localhost/nombre_bd")
SECRET_KEY = tu_clave_secreta

### Ejecutar el Script.py
Este script es necesario para poblar la base de datos y crear el primer usuario admin.
- ``` python script.py ```
  
### Ejecutar el proyecto
- ```flask run --reload```

## Endpoints de la API
## Productos
### Consultar productos
* Metodo: GET
* Endpoint: /productos
* Ejemplo respuesta:
```json
"categorias": [
        {
            "id": 1,
            "nombre": "Categoria 1"
        },
 "modelos": [
        {
            "id": 1,
            "marca_id": {
                "id": 1,
                "nombre": "Marca A"
            },
            "nombre": "Modelo A1"
        },
"productos": [
        {
            "categoria": {
                "id": 1,
                "nombre": "Categoria 1"
            },
            "id": 1,
            "modelo": {
                "id": 1,
                "nombre": "Modelo A1"
            },
            "nombre": "Producto 1",
            "precio": 19.99,
            "proveedor": {
                "id": 24,
                "nombre": "Elena Castro"
            },
            "stock": 100
        },
```

### Crear un producto
* Metodo: POST
* Endpoint: /productos/crear
* Ejemplo de solicitud:
```json
{
"nombre": "nuevo_producto",
"precio": 100,
"stock": 10,
"modelo_id": 1,
"categoria_id": 1,
"proveedor_id": 1
}
```
* Respuesta esperada:
```json
{
"Mensaje": "Producto cargado con exito."
}
```

### Editar un producto
* Metodo: POST
* Endpoint: /clientes/editar/<id_cliente>
* Ejemplo solicitud
```json
{
"nombre": "nuevo_producto2",
"precio": 111,
"stock": 11,
"modelo_id": 2,
"categoria_id": 2,
"proveedor_id": 2
}
```
* Respuesta esperada:
```json
{
"Mensaje": "Producto editado con exito."
}
```

### Eliminar un producto
* Metodo: POST
* Endpoint: /productos/eliminar/<id_producto>
* Respuesta esperada:
```json
{
"Mensaje": "Producto eliminado con exito."
}
```

## Clientes
### Consultar cliente
* Metodo: GET
* Endpoint: /clientes
* Ejemplo respuesta:
```json
"clientes":[
    {
        "direccion": "direccion 1",
        "dni": "448274353",
        "email": "cliente@cliente.com",
        "id": 28,
        "nombre": "nombre_cliente",
        "telefono": "45968424"
    }
]
```

### Crear un cliente 
* Metodo: POST
* Endpoint: /clientes/crear
* Ejemplo de solicitud:
```json
{
"nombre": "nuevo_cliente",
"dni": 2312553453,
"telefono": 343531531,
"email": cliente@cliente.com,
"direccion": direccion 2
}
```
* Respuesta esperada:
```json
{
"Mensaje": "Cliente cargado con exito."
}
```

### Editar un cliente
* Metodo: POST
* Endpoint: /clientes/editar/<id_cliente>
* Ejemplo solicitud
```json
{
"nombre": "nuevo_nombre",
"dni": 23123535,
"telefono": 343534634631,
"email": cliente1@cliente1.com,
"direccion": direccion 3
}
```
* Respuesta esperada:
```json
{
"Mensaje": "Cliente editado con exito."
}
```

### Eliminar un cliente
* Metodo: POST
* Endpoint: /clientes/eliminar/<id_cliente>
* Respuesta esperada:
```json
{
"Mensaje": "Cliente eliminado con exito."
}
```

## Empleados
### Consultar empleados
* Metodo: GET
* Endpoint: /empleados
* Ejemplo respuesta:
```json
"empleados": [
    {
        "direccion": "direccion 1",
        "dni": "448274353",
        "email": "empleado@empleado.com",
        "id": 28,
        "nombre": "nombre_empleado",
        "telefono": "45968424",
        "sucursal": {
            "id":1,
            "nombre": "sucursal centro"
        }
        "cargo": "empleado"
    }
```

### Crear un empleado
* Metodo: POST
* Endpoint: /empleados/crear
* Ejemplo de solicitud:
```json
   {
        "direccion": "direccion 1",
        "dni": "448274353",
        "email": "empleado@empleado.com",
        "nombre": "nombre_empleado",
        "telefono": "45968424",
        "sucursal_id": 1
        "cargo": "gerente"
    }
```
* Respuesta esperada:
```json
{
"Mensaje": "Empleado cargado con exito."
}
```

### Editar un empleado
* Metodo: POST
* Endpoint: /empleado/editar/<id_empleado>
* Ejemplo solicitud
```json
   {
        "direccion": "direccion 2",
        "dni": "443463464353",
        "email": "empleado1@empleado1.com",
        "nombre": "nombre_empleado",
        "telefono": "45567654",
        "sucursal_id": 2
        "cargo": "gerente"
    }
```
* Respuesta esperada:
```json
{
"Mensaje": "Empleado editado con exito."
}
```

### Eliminar un empleado
* Metodo: POST
* Endpoint: /empleado/eliminar/<id_empleado>
* Respuesta esperada:
```json
{
"Mensaje": "Empleado eliminado con exito."
}
```

## Proveedores
### Consultar proveedores
* Metodo: GET
* Endpoint: /proveedores
* Ejemplo respuesta:
```json
"proveedores": [
        {
            "cuit": 216578363,
            "dni": 32132321,
            "email": "elena.castro@example.com",
            "id": 24,
            "nombre": "Elena Castro",
            "telefono": "852-741-9630,
            "direccion": "direccion 1"
        },
```

### Crear un proveedor
* Metodo: POST
* Endpoint: /proveedores/crear
* Ejemplo de solicitud:
```json
    {
        "cuit": 2543543,
        "dni": 32132321,
        "email": "proveedor@example.com",
        "nombre": "Elena Castro",
        "telefono": "852-741-9630"
        "direccion": "direccion 1"
    }
```
* Respuesta esperada:
```json
{
"Mensaje": "Proveedor cargado con exito."
}
```

### Editar un proveedor
* Metodo: POST
* Endpoint: /proveedores/editar/<id_proveedores>
* Ejemplo solicitud
```json
    {
        "cuit": 2543543,
        "dni": 32132321,
        "email": "proveedo2@example.com",
        "nombre": "Nombre proveedor",
        "telefono": "852-741-9630"
        "direccion": "direccion 2"
    }
```
* Respuesta esperada:
```json
{
"Mensaje": "Proveedor editado con exito."
}
```

### Eliminar un proveedor
* Metodo: POST
* Endpoint: /proveedores/eliminar/<id_proveedor>
* Respuesta esperada:
```json
{
"Mensaje": "Proveedor eliminado con exito."
}
```

## Usuarios
### Consultar usuarios
* Metodo: GET
* Endpoint: ```/usuarios```
* Cabecera de la solicitud: ```Authorization: Token <token_autenticacion>```
* Ejemplo respuesta:
```json
"usuarios": [
        {
            "nombre_usuario": usuario1,
            "contrasena_hash": scrypt:32768:8:1$Opoq98bkASq4idt1$67bdbb5fb7b991ddc0ca3967...,
            "is_admin": "True",
        },
```

### Crear un proveedor
* Metodo: POST
* Endpoint: ```/usuarios```
* Cabecera de la solicitud: ```Authorization: Token <token_autenticacion>```
* Ejemplo de solicitud:
```json
    {
        "nombre_usuario": 2543543,
        "contrasena": 32132321,
        "is_admin": True o False
    }
```
* Respuesta esperada:
```json
{
"Mensaje": "Usuario cargado con exito."
}
```

### Eliminar un usuario
* Metodo: DELETE
* Endpoint: ```/usuarios/eliminar/<id_usuario>```
* Cabecera de la solicitud: ```Authorization: Token <token_autenticacion>```
* Respuesta esperada:
```json
{
"Mensaje": "Usuario eliminado con exito."
}
```
