from app import db
from flask_sqlalchemy import SQLAlchemy

class Pais(db.Model):
    __tablename__ = 'pais'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    provincias = db.relationship('Provincia', back_populates='pais')

class Provincia(db.Model):
    __tablename__ = 'provincia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)

    pais = db.relationship('Pais', back_populates='provincias')
    localidades = db.relationship('Localidad', back_populates='provincia')

class Localidad(db.Model):
    __tablename__ = 'localidad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincia.id'), nullable=False)

    provincia = db.relationship('Provincia', back_populates='localidades')
    sucursales = db.relationship('Sucursal', back_populates='localidad')

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    localidad_id = db.Column(db.Integer, db.ForeignKey('localidad.id'), nullable=False)

    localidad = db.relationship('Localidad', back_populates='sucursales')
    empleados = db.relationship('Empleado', back_populates='sucursal')

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    tipo = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'persona',
        'polymorphic_on': tipo
    }

class Cliente(Persona):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, db.ForeignKey('persona.id'), primary_key=True)
    usuario_id = db.Column(db.Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'cliente',
    }

class Empleado(Persona):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, db.ForeignKey('persona.id'), primary_key=True)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)

    sucursal = db.relationship('Sucursal', back_populates='empleados')

    __mapper_args__ = {
        'polymorphic_identity': 'empleado',
    }

class Marca(db.Model):
    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    modelos = db.relationship('Modelo', back_populates='marca')

class Modelo(db.Model):
    __tablename__ = 'modelo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)

    marca = db.relationship('Marca', back_populates='modelos')
    productos = db.relationship('Producto', back_populates='modelo')

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    modelo = db.relationship('Modelo', back_populates='productos')
    categoria = db.relationship('Categoria', back_populates='productos')
    proveedor = db.relationship('Proveedor', back_populates='productos')

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    productos = db.relationship('Producto', back_populates='categoria')

class Proveedor(Persona):
    __tablename__ = 'proveedor'
    id = db.Column(db.Integer, db.ForeignKey('persona.id'), primary_key=True)
    cuit = db.Column(db.Integer, unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'proveedor',
    }

    productos = db.relationship('Producto', back_populates='proveedor')

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(50), nullable=False)
    contrasena_hash = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
