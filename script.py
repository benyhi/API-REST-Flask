from werkzeug.security import generate_password_hash
from app import app,db
from models import Usuario, Pais, Provincia, Localidad, Sucursal, Cliente, Empleado, Producto, Marca, Proveedor, Modelo, Categoria


def poblar_bd():
    # Crear países
    argentina = Pais(nombre='Argentina')
    brasil = Pais(nombre='Brasil')
    chile = Pais(nombre='Chile')

    # Crear provincias con claves foráneas de país
    buenos_aires = Provincia(nombre='Buenos Aires', pais=argentina)
    cordoba = Provincia(nombre='Córdoba', pais=argentina)
    sao_paulo = Provincia(nombre='Sao Paulo', pais=brasil)
    rio_de_janeiro = Provincia(nombre='Río de Janeiro', pais=brasil)
    santiago = Provincia(nombre='Santiago', pais=chile)

    # Crear localidades con claves foráneas de provincia
    tigre = Localidad(nombre='Tigre', provincia=buenos_aires)
    la_plata = Localidad(nombre='La Plata', provincia=buenos_aires)
    cordoba_capital = Localidad(nombre='Córdoba Capital', provincia=cordoba)
    campinas = Localidad(nombre='Campinas', provincia=sao_paulo)
    copacabana = Localidad(nombre='Copacabana', provincia=rio_de_janeiro)
    santiago_centro = Localidad(nombre='Santiago Centro', provincia=santiago)

    # Crear sucursales con claves foráneas de localidad
    sucursal_tigre = Sucursal(nombre='Sucursal Tigre', direccion='Calle Falsa 123', localidad=tigre)
    sucursal_la_plata = Sucursal(nombre='Sucursal La Plata', direccion='Calle Verdadera 456', localidad=la_plata)
    sucursal_cordoba = Sucursal(nombre='Sucursal Córdoba', direccion='Avenida Siempreviva 789', localidad=cordoba_capital)
    sucursal_campinas = Sucursal(nombre='Sucursal Campinas', direccion='Avenida Real 456', localidad=campinas)
    sucursal_copacabana = Sucursal(nombre='Sucursal Copacabana', direccion='Rua Bonita 321', localidad=copacabana)
    sucursal_santiago = Sucursal(nombre='Sucursal Santiago', direccion='Calle Chile 654', localidad=santiago_centro)

    # Crear categoria
    categoria_A = Categoria(nombre='Categoria A')
    categoria_B = Categoria(nomre='Categoria B')
    categoria_C = Categoria(nombre='Categoria C')

    # Crear marcas
    marca_A = Marca(nombre='Marca A')
    marca_B = Marca(nombre='Marca B')
    marca_C = Marca(nombre='Marca C')

    # Crear modelos con claves foráneas de marca
    modelo_A = Modelo(nombre='Modelo A', marca=marca_A)
    modelo_B = Modelo(nombre='Modelo B', marca=marca_B)
    modelo_C = Modelo(nombre='Modelo C', marca=marca_C)

    # Crear proveedores
    proveedor_1 = Proveedor(nombre='Proveedor 1', telefono='123456789', email='proveedor1@email.com', dni='123456789', cuit='201234567893')
    proveedor_2 = Proveedor(nombre='Proveedor 2', telefono='123456789', email='proveedor2@email.com', dni='53453489', cuit='2016456233893')
    proveedor_3 = Proveedor(nombre='Proveedor 3', telefono='123456789', email='proveedor3@email.com', dni='53453456789', cuit='2546456547893')

    # Crear productos con claves foráneas de modelo, categoria y proveedor
    producto_1 = Producto(nombre='Producto 1', modelo=modelo_A, categoria=categoria_A,precio=500, stock=10, proveedor=proveedor_1)
    producto_2 = Producto(nombre='Producto 2', modelo=modelo_B, categoria=categoria_B, precio=800, stock=5, proveedor=proveedor_2)
    producto_3 = Producto(nombre='Producto 3', modelo=modelo_C, categoria=categoria_C,precio=1500, stock=8, proveedor=proveedor_3)

    # Crear clientes que heredan de Persona
    cliente_juan = Cliente(nombre='Juan', apellido='Perez', dni='12345678', telefono='111222333', email='juan@correo.com')
    cliente_maria = Cliente(nombre='Maria', apellido='Gomez', dni='87654321', telefono='444555666', email='maria@correo.com')
    cliente_pablo = Cliente(nombre='Pablo', apellido='Rodriguez', dni='13579246', telefono='777888999', email='pablo@correo.com')
    cliente_lucia = Cliente(nombre='Lucía', apellido='Fernandez', dni='24681357', telefono='123123123', email='lucia@correo.com')

    # Crear empleados con claves foráneas de sucursal
    empleado_carlos = Empleado(nombre='Carlos', apellido='Lopez', dni='56789012', telefono='777888999', email='carlos@sucursal.com', sucursal=sucursal_tigre, cargo='Vendedor')
    empleado_ana = Empleado(nombre='Ana', apellido='Martinez', dni='34567890', telefono='555666777', email='ana@sucursal.com', sucursal=sucursal_campinas, cargo='Gerente')
    empleado_roberto = Empleado(nombre='Roberto', apellido='Sanchez', dni='98765432', telefono='999888777', email='roberto@sucursal.com', sucursal=sucursal_cordoba, cargo='Encargado')
    empleado_luisa = Empleado(nombre='Luisa', apellido='Morales', dni='12309876', telefono='111444777', email='luisa@sucursal.com', sucursal=sucursal_santiago, cargo='Administrador')

    # Agregar todos los registros a la sesión
    db.session.add_all([argentina, brasil, chile, buenos_aires, cordoba, sao_paulo, rio_de_janeiro, santiago,
                        tigre, la_plata, cordoba_capital, campinas, copacabana, santiago_centro, sucursal_tigre,
                        sucursal_la_plata, sucursal_cordoba, sucursal_campinas, sucursal_copacabana, sucursal_santiago,
                        marca_A, marca_B, marca_C, categoria_A, categoria_B, categoria_C,
                        modelo_A, modelo_B, modelo_C, producto_1, producto_2, producto_3,
                        proveedor_1, proveedor_2, proveedor_3, cliente_juan, cliente_maria,
                        cliente_pablo, cliente_lucia, empleado_carlos, empleado_ana, empleado_roberto, empleado_luisa])

    # Confirmar cambios
    db.session.commit()
    db.session.close()
    print("Base de dato poblada con exito.")

def primer_usuario():
    with app.app_context():
        if Usuario.query.filter_by(nombre_usuario="admin").first():
            print("El usuario admin ya existe.")

        else:
            primer_usuario = Usuario(
                nombre_usuario = "admin",
                contrasena_hash = generate_password_hash("123"),
                is_admin = True,
            )
            print(primer_usuario.nombre_usuario, primer_usuario.contrasena_hash, primer_usuario.is_admin)

            db.session.add(primer_usuario)
            db.session.commit()
            db.session.close()

if __name__ == "__main__":
    poblar_bd()
    primer_usuario()

