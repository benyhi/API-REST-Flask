from marshmallow_sqlalchemy import auto_field

from app import ma
from marshmallow import validates, ValidationError
from models import Cliente, Empleado, Producto, Proveedor, Usuario, Persona, Provincia, Localidad, Sucursal, Marca, \
    Modelo, Categoria, Pais


class PaisSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pais

    nombre = ma.auto_field()

class ProvinciaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Provincia

    nombre = ma.auto_field()

class LocalidadSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Localidad

    nombre = ma.auto_field()

class SucursalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sucursal

    id = ma.auto_field()
    nombre = ma.auto_field()
    direccion = ma.auto_field()
    localidad_id = ma.Nested(LocalidadSchema)

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca

    id = ma.auto_field()
    nombre = ma.auto_field()

class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo

    id = ma.auto_field()
    nombre = ma.auto_field()
    marca = ma.Nested(MarcaSchema, only=('id','nombre'))

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

    id = ma.auto_field()
    nombre = ma.auto_field()

class PersonaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Persona

    id = ma.auto_field()
    nombre = ma.auto_field()
    dni = ma.auto_field()
    telefono = ma.auto_field()
    direccion = ma.auto_field()
    email = ma.auto_field()

    @validates('dni')
    def validate_dni(self, value):
        if len(value) < 9:
            return ValidationError("El dni debe contener al menos 9 caracteres.")

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario

    id = ma.auto_field()
    nombre_usuario = ma.auto_field()
    contrasena_hash = ma.auto_field()
    is_admin = ma.auto_field()

class ClienteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cliente

    id = ma.auto_field()
    nombre = ma.auto_field()
    dni = ma.auto_field()
    direccion = ma.auto_field()
    telefono = ma.auto_field()
    email = ma.auto_field()

class EmpleadoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Empleado

    id = auto_field()
    nombre = ma.auto_field()
    dni = ma.auto_field()
    sucursal = ma.Nested(SucursalSchema, only=('id', 'nombre'))
    cargo = ma.auto_field()

class ProveedorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Proveedor

    id = ma.auto_field()
    nombre = ma.auto_field()
    dni = ma.auto_field()
    cuit = ma.auto_field()
    telefono = ma.auto_field()
    email = ma.auto_field()

    @validates('cuit')
    def validate_cuit(self, value):
        if len(value) < 10:
            return ValidationError("El cuit debe contener al menos 10 caracteres.")


class ProductoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Producto
        load_instance = True

    id = ma.auto_field()
    nombre = ma.auto_field()
    precio = ma.auto_field()
    stock = ma.auto_field()
    modelo = ma.Nested(ModeloSchema, only=('id','nombre'))
    categoria = ma.Nested(CategoriaSchema, only=('id','nombre'))
    proveedor = ma.Nested(ProveedorSchema, only=('id','nombre'))



