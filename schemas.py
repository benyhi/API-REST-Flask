from wtforms.validators import length

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

    nombre = ma.auto_field()
    direccion = ma.auto_field()
    localidad_id = ma.Nested(LocalidadSchema)

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca

    nombre = ma.auto_field()

class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo

    nombre = ma.auto_field()
    marca_id = ma.Nested(MarcaSchema)

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

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

    id = ma.Nested(PersonaSchema)
    usuario_id = ma.Nested(UsuarioSchema)

class EmpleadoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Empleado

    id = ma.Nested(PersonaSchema)
    nombre = ma.auto_field()
    sucursal_id = ma.Nested(SucursalSchema)
    cargo = ma.auto_field()

class ProveedorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Proveedor

    id = ma.auto_field()
    cuit = ma.auto_field()

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
    modelo_id = ma.Nested(ModeloSchema, only=('nombre',))
    categoria_id = ma.Nested(CategoriaSchema, only=('nombre',))
    proveedor_id = ma.Nested(ProveedorSchema, only=('id',))



