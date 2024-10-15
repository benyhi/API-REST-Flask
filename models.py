from app import db
from flask_sqlalchemy import SQLAlchemy

class Pais(db.Model):
    __tablename__ = 'pais'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    provincias = db.relationship('Provincia', backref='pais')

class Provincia(db.Model):
    __tablename__ = 'provincia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)

    localidades = db.relationship('Localidad', backref='provincia')

class Localidad(db.Model):
    __tablename__ = 'localidad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincia.id'), nullable=False)

    sucursales = db.relationship('Sucursal', backref='localidad')

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    localidad_id = db.Column(db.Integer, db.ForeignKey('localidad.id'), nullable=False)

    empleados = db.relationship('Empleado', backref='sucursal')

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)

class Cliente(Persona):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, db.ForeignKey('persona.id'), primary_key=True)
    usuario_id = db.Column(db.Integer)

class Empleado(Persona):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, db.ForeignKey('persona.id'), primary_key=True)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    cargo = db.Column(db.String(100), nullable=False)

class Marca(db.Model):
    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)

    modelos = db.relationship('Modelo', backref='marca')

class Fabricante(db.Model):
    __tablename__ = 'fabricante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais.id'), nullable=False)

    marcas = db.relationship('Marca', backref='fabricante')

class Modelo(db.Model):
    __tablename__ = 'modelo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)

    productos = db.relationship('Producto', backref='modelo')

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    producto = db.relationship('Producto', backref='categoria')

    def __str__(self):
        return self.nombre

class Proveedor(db.Model):
    __tablename__ = 'proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    productos = db.relationship('Producto', backref='proveedor')
