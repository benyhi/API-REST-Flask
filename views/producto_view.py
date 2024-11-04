from app import db
from models import Producto, Modelo, Proveedor, Categoria
from flask import Blueprint, render_template, redirect, url_for, request
from schemas import ProductoSchema, ModeloSchema, ProveedorSchema, CategoriaSchema

from sqlalchemy import exc

from schemas import ClienteSchema

productos_bp = Blueprint('productos', __name__)


@productos_bp.route("/productos", methods=['GET'])
def productos():

    productos = Producto.query.all()
    modelos = Modelo.query.all()
    proveedor = Proveedor.query.all()
    categoria = Categoria.query.all()

    modelos_serializer = ModeloSchema(many=True).dump(modelos)
    proveedor_serializer = ProveedorSchema(many=True).dump(proveedor)
    categoria_serializer = CategoriaSchema(many=True).dump(categoria)
    productos_serializer = ProductoSchema(many=True).dump(productos)

    return render_template('productos/productos.html', productos=productos_serializer, modelos=modelos_serializer, proveedores=proveedor_serializer, categorias=categoria_serializer)

@productos_bp.route("/productos/crear", methods=['POST'])
def crear_producto():
    nombre = request.form.get('nombre')
    modelo_id = request.form.get('modelo')
    precio = request.form.get('precio')
    stock = request.form.get('stock')
    proveedor_id = request.form.get('proveedor')
    categoria_id = request.form.get('categoria')

    if nombre and modelo_id and precio and stock and proveedor_id and categoria_id:
        try:
            nuevo_producto = Producto(
                nombre = nombre,
                modelo_id = modelo_id,
                precio = precio,
                stock = stock,
                proveedor_id = proveedor_id,
                categoria_id = categoria_id
            )

            db.session.add(nuevo_producto)
            db.session.commit()

        except exc as error:
            print(f'ERROR EN LA BD:{error}')

        finally:
            return redirect(url_for('productos.productos'))
        
    else:
        print('Debes completar todos los datos del formulario.')

@productos_bp.route("/productos/editar/<int:id>", methods=['GET','POST'])
def editar_producto(id):
        producto = Producto.query.filter_by(id=id).first()
        producto_serializer = ProductoSchema().dump(producto)

        if request.method == 'GET':
            modelos = Modelo.query.all()
            proveedores = Proveedor.query.all()
            categorias = Categoria.query.all()

            modelos_serializer = ModeloSchema(many=True).dump(modelos)
            proveedor_serializer = ProveedorSchema(many=True).dump(proveedores)
            categoria_serializer = CategoriaSchema(many=True).dump(categorias)

            return render_template('productos/editar_producto.html', modelos=modelos_serializer, categorias=categoria_serializer, proveedores=proveedor_serializer, producto=producto_serializer)

        else:
            producto.nombre = request.form.get('nombre')
            producto.modelo_id = request.form.get('modelo')
            producto.precio = request.form.get('precio')
            producto.stock = request.form.get('stock')
            producto.proveedor_id = request.form.get('proveedor')
            producto.categoria_id = request.form.get('categoria')

            db.session.commit()

            return redirect(url_for('productos.productos'))

@productos_bp.route("/productos/eliminar/<int:id>", methods=['GET'])
def eliminar_producto(id):
    producto = Producto.query.filter_by(id=id).first()

    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('productos.productos'))
