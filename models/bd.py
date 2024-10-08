from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from config import Base

class Marca(Base):
    __tablename__ = "marca"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    productos = relationship("Producto", back_populates="marca")

class Pais(Base):
    __tablename__ = "pais"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    provincias = relationship("Provincia", back_populates="pais")
    persona = relationship("Persona", back_populates="pais")

class Provincia(Base):
    __tablename__ = "provincia"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    id_pais = Column(Integer, ForeignKey('pais.id'))

    pais = relationship("Pais", back_populates="provincias")
    localidades = relationship("Localidad", back_populates="provincia")

class Localidad(Base):
    __tablename__ = "localidad"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    id_provincia = Column(Integer, ForeignKey('provincia.id'))

    provincia = relationship("Provincia", back_populates="localidades")
    persona = relationship("Persona", back_populates="localidad")

class Sexo(Base):
    __tablename__ = "sexo"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    persona = relationship("Persona", back_populates="sexo")

class Condicion_Fiscal(Base):
    __tablename__ = "condicion_fiscal"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    iva = Column(String(100), nullable=False)

    persona = relationship("Persona", back_populates="condicion_fiscal")

class Modelo(Base):
    __tablename__ = "modelo"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    id_fabricante = Column(Integer, ForeignKey('fabricante.id'))

    fabricante = relationship("Fabricante", back_populates="modelos")
    productos = relationship("Producto", back_populates="modelo")

class Fabricante(Base):
    __tablename__ = "fabricante"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    modelos = relationship("Modelo", back_populates="fabricante")

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    productos = relationship("Producto", back_populates="categoria")

#######################################################################
#######################################################################

class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    id_sexo = Column(Integer, ForeignKey('sexo.id'))
    id_localidad = Column(Integer, ForeignKey('localidad.id'))
    id_condicion_fiscal = Column(Integer, ForeignKey('condicion_fiscal.id'))
    nombre = Column(String(100), nullable=False)
    cuit = Column(String(20), unique=True)
    numero_documento = Column(String(20), nullable=False, unique=True)
    telefono = Column(String)
    direccion = Column(String)
    fecha_nacimiento = Column(Date)
    correo = Column(String(100))
    estado = Column(Boolean)
    fecha_registro = Column(TIMESTAMP, nullable=False)

    sexo = relationship("Sexo", back_populates="persona")
    localidad = relationship("Localidad", back_populates="persona")
    condicion_fiscal = relationship("Condicion_fiscal", back_populates="persona")
    empleados = relationship("Empleado", back_populates="persona")
    clientes = relationship("Cliente", back_populates="persona")
    proveedores = relationship("Proveedor", back_populates="persona")

class Empleado(Base):
    __tablename__ = "empleado"
    id = Column(Integer, primary_key=True)
    rol = Column(String(100))
    id_persona = Column(Integer, ForeignKey('persona.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    numero_legajo = Column(Integer, nullable=False, unique=True)
    estado = Column(Boolean)
    fecha_registro = Column(TIMESTAMP, nullable=False)

    persona = relationship("Persona", back_populates="empleados")
    puesto = relationship("Puesto", back_populates="empleados")
    usuario = relationship("Usuario", back_populates="empleados")
    ventas = relationship("Venta", back_populates="empleado")

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    id_modelo = Column(Integer, ForeignKey('modelo.id'))
    id_marca = Column(Integer, ForeignKey('marca.id'))
    id_categoria = Column(Integer, ForeignKey('categoria.id'))
    nombre = Column(String(100), nullable=False)
    costo = Column(Integer)
    cantidad_disponible = Column(Integer)
    fecha_registro = Column(TIMESTAMP)

    modelo = relationship("Modelo", back_populates="productos")
    marca = relationship("Marca", back_populates="productos")
    accesorio = relationship("Accesorio", back_populates="productos")
    categoria = relationship("Categoria", back_populates="productos")
    detalle_ventas = relationship("Detalle_venta", back_populates="producto")

class Proveedor(Base):
    __tablename__ = "proveedor"
    id = Column(Integer, primary_key=True)
    id_persona = Column(Integer, ForeignKey('persona.id'))

    persona = relationship("Persona", back_populates="proveedores")

class Venta(Base): 
    __tablename__ = "venta"
    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))
    id_empleado = Column(Integer, ForeignKey('empleado.id'))
    total = Column(Integer, nullable=False)
    fecha_venta = Column(TIMESTAMP)

    cliente = relationship("Cliente", back_populates="ventas")
    empleado = relationship("Empleado", back_populates="ventas")
    detalle_ventas = relationship("Detalle_venta", back_populates="venta")

class Detalle_Venta(Base):
    __tablename__ = "detalle_venta"
    id = Column(Integer, primary_key=True)
    id_venta = Column(Integer, ForeignKey('venta.id'))
    id_producto = Column(Integer, ForeignKey('producto.id'))
    cantidad = Column(Integer)
    precio_unitario = Column(Integer)
    subtotal = Column(Integer)

    venta = relationship("Venta", back_populates="detalle_ventas")
    producto = relationship("Producto", back_populates="detalle_ventas")

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    id_persona = Column(Integer, ForeignKey('persona.id'))
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    nombre = Column(String(100), nullable=False)
    fecha_registro = Column(TIMESTAMP)

    usuario = relationship('Usuario', back_populates="cliente")
    persona = relationship("Persona", back_populates="clientes")
    ventas = relationship("Venta", back_populates="cliente")

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(100), nullable=False)
    contrasena = Column(String(100), nullable=False)