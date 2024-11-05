from werkzeug.security import generate_password_hash
from app import app,db
from models import Usuario,Pais, Provincia, Localidad, Sucursal, Cliente, Empleado, Producto, Marca, Proveedor, Modelo

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

    # Crear marcas con claves foráneas de fabricante
    marca_sony = Marca(nombre='Sony')
    marca_samsung = Marca(nombre='Samsung')
    marca_lg = Marca(nombre='LG')

    # Crear modelos con claves foráneas de marca
    modelo_playstation = Modelo(nombre='PlayStation 5', marca=marca_sony)
    modelo_galaxy = Modelo(nombre='Galaxy S21', marca=marca_samsung)
    modelo_oled_tv = Modelo(nombre='OLED TV', marca=marca_lg)

    # Crear proveedores
    proveedor_tech_store = Proveedor(nombre='Tech Store', telefono='123456789', email='tech@store.com')
    proveedor_mobile_shop = Proveedor(nombre='Mobile Shop', telefono='987654321', email='mobile@shop.com')
    proveedor_home_appliances = Proveedor(nombre='Home Appliances', telefono='112233445', email='home@appliances.com')

    # Crear productos con claves foráneas de modelo y proveedor
    producto_ps5 = Producto(nombre='PlayStation 5', modelo=modelo_playstation, precio=500.0, stock=10, proveedor=proveedor_tech_store)
    producto_galaxy = Producto(nombre='Galaxy S21', modelo=modelo_galaxy, precio=800.0, stock=5, proveedor=proveedor_mobile_shop)
    producto_oled_tv = Producto(nombre='OLED TV', modelo=modelo_oled_tv, precio=1500.0, stock=8, proveedor=proveedor_home_appliances)

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
                        fabricante_sony, fabricante_samsung, fabricante_lg, marca_sony, marca_samsung, marca_lg,
                        modelo_playstation, modelo_galaxy, modelo_oled_tv, producto_ps5, producto_galaxy, producto_oled_tv,
                        proveedor_tech_store, proveedor_mobile_shop, proveedor_home_appliances, cliente_juan, cliente_maria,
                        cliente_pablo, cliente_lucia, empleado_carlos, empleado_ana, empleado_roberto, empleado_luisa])

    # Confirmar cambios
    db.session.commit()
    print("Más entradas creadas con éxito.")

def primer_usuario():
    with app.app_context():
        if Usuario.query.filter_by(nombre_usuario="admin").first():
            print("El usuario admin ya existe.")

        else:
            primer_usuario = Usuario(
                nombre_usuario = "admin",
                contrasena_hash = generate_password_hash("admin"),
                is_admin = True,
            )
            db.session.add(primer_usuario)
            db.session.commit()
            db.session.close()

if __name__ == "__main__":
    primer_usuario()
