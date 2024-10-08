from models.bd import Producto, Modelo, Marca
from config import SessionLocal as sesion
from sqlalchemy import exc

class Productos:
    def __init__(self):
        self.db = sesion()

    def crear_producto(self, nombre, id_modelo, id_marca, costo, cantidad_disponible, id_accesorio, id_categoria):
        try:       
            nuevo_producto = Producto(nombre=nombre, id_modelo=id_modelo, id_marca=id_marca, costo=costo, cantidad_disponible=cantidad_disponible, id_accesorio=id_accesorio, id_categoria=id_categoria)
            self.db.add(nuevo_producto)
            self.db.commit()
            return f"el producto {nuevo_producto.nombre} fue añadido con exito a la base de datos", 201
        
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al crear el producto {e}")
            return None, 500
        
        finally:
            self.db.close()

    def eliminar_producto(self,id):
        try:
            producto = self.db.query(Producto).filter_by(id=id).first()

            if producto:
                self.db.delete(producto)
                self.db.commit()
                return f"el producto ID {id} fue elminada con exito"
            
            else:
                return f"No se encontró el producto con ID {id}", 404
            
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al eliminar el producto: {e}")
            return None, 500
        
        finally:
            self.db.close()
    
    def actualizar_producto(self, nombre, id_modelo, id_marca, costo, cantidad_disponible, id_accesorio, id_categoria):
        try:
            producto = self.db.query(Producto).filter_by(id=id).first()
            
            if producto:
                producto.nombre = nombre
                producto.id_modelo = id_modelo
                producto.id_marca = id_marca
                producto.costo = costo
                producto.cantidad_disponible = cantidad_disponible
                producto.id_accesorio = id_accesorio 
                producto.id_categoria = id_categoria
                self.db.commit()
                return producto

        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al actualizar el producto: {e}")
            return None, 500
        
        finally:
            self.db.close()

    def consultar_producto(self, nombre):
        try:
            producto = self.db.query(Producto).filter_by(nombre=nombre).first()

            if producto:
                return producto
            
            else:
                return f"No se encontro el producto '{producto}'"
          
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al encontrar el producto: {e}")
            return None, 500
        
        finally:
            self.db.close()
                
    def consultar_todos(self):
        try:
            producto = self.db.query(Producto).all()
            return producto
        
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al consultar los productos: {e}")
            return None, 500

        finally:
            self.db.close()

class Modelos:
    def __init__(self):
        self.db = sesion()
    
    def consultar_todos(self):
        try:
            modelo = self.db.query(Modelo).all()
            return modelo
        
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al consultar los modelos: {e}")
            return None, 500

        finally:
            self.db.close()

class Marcas:
    def __init__(self):
        self.db = sesion()

    def consultar_todos(self):
        try:
            marca = self.db.query(Marca).all()
            return marca
        
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al consultar las marcas: {e}")
            return None, 500

        finally:
            self.db.close()

class Categoria:
    def __init__(self):
        self.db = sesion()

    def consultar_todos(self):
        try:
            categoria = self.db.query(Categoria).all()
            return categoria
        
        except exc.SQLAlchemyError as e:
            print(f"Ocurrio un error al consultar los accesorios: {e}")
            return None, 500

        finally:
            self.db.close()