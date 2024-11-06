from app import db
from models import Producto, Modelo, Proveedor, Categoria
from flask import Blueprint, jsonify, request
from schemas import ProductoSchema, ModeloSchema, ProveedorSchema, CategoriaSchema


productos_bp = Blueprint('productos', __name__)


@productos_bp.route("/productos", methods=['GET'])
def productos():
    productos = Producto.query.all()
    modelos = Modelo.query.all()
    proveedor = Proveedor.query.all()
    categoria = Categoria.query.all()
    return jsonify({
        "modelos": ModeloSchema(many=True).dump(modelos), 
        "proveedores":ProveedorSchema(many=True).dump(proveedor), 
        "categorias":CategoriaSchema(many=True).dump(categoria), 
        "productos":ProductoSchema(many=True).dump(productos)
        })

@productos_bp.route("/productos/crear", methods=['POST'])
def crear_producto():
    datos = request.json

    if datos:
        nombre = datos.get("nombre")
        precio = datos.get("precio")
        stock = datos.get("stock")
        modelo_id = datos.get("modelo_id")
        categoria_id = datos.get("categoria_id")
        proveedor_id = datos.get("proveedor_id")

        nuevo_producto = Producto(
            nombre=nombre,
            precio=precio,
            stock=stock,
            modelo_id=modelo_id,
            categoria_id=categoria_id,
            proveedor_id=proveedor_id
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'Mensaje': 'Producto cargado con exito.'})

    else:
        return jsonify({'Mensaje': 'Error al cargar el nuevo producto'})

@productos_bp.route("/productos/editar/<int:id>", methods=['GET','POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == "GET":
        return jsonify(ProductoSchema().dump(producto))

    else:
        datos = request.json
        if datos:
            producto.nombre = datos.get("nombre")
            producto.precio = datos.get("precio")
            producto.stock = datos.get("stock")
            producto.modelo_id = datos.get("modelo_id")
            producto.categoria_id = datos.get("categoria_id")
            producto.proveedor_id = datos.get("proveedor_id")

            db.session.commit()
            return jsonify({'Mensaje': 'Producto actualizado con exito.'})

        else:
            return jsonify({'Mensaje': 'Error al actualizar el producto.'})

@productos_bp.route("/productos/eliminar/<int:id>", methods=['GET'])
def eliminar_producto(id):
    producto = Producto.query.filter_by(id=id).first()
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'Mensaje': 'Producto eliminado con exito.'})
