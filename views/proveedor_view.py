from app import db
from models import Proveedor
from flask import Blueprint, jsonify, request

from schemas import ProveedorSchema

proveedor_bp = Blueprint('proveedores', __name__)

@proveedor_bp.route("/proveedores", methods=['GET'])
def proveedores():
    proveedores = db.session.query(Proveedor).all()
    return jsonify({'proveedores': ProveedorSchema(many=True).dump(proveedores)})

@proveedor_bp.route("/proveedores/crear", methods=['POST'])
def proveedores_crear():
    datos = request.json

    if datos:
        nombre = datos.get("nombre")
        dni = datos.get("dni")
        cuit = datos.get("cuit")
        telefono = datos.get("telefono")
        email = datos.get("email")
        direccion = datos.get("direccion")

        nuevo_proveedor = Proveedor(
            nombre=nombre,
            dni=dni,
            cuit=cuit,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        db.session.add(nuevo_proveedor)
        db.session.commit()
        return jsonify({'Mensaje': 'Proveedor cargado con exito.'})

    else:
        return jsonify({'Mensaje': 'Error al cargar el nuevo proveedor'})

@proveedor_bp.route("/proveedores/editar/<int:id>", methods=['GET', 'POST'])
def proveedores_editar(id):
    proveedor = Proveedor.query.get_or_404(id)

    if request.method == "GET":
        return jsonify(ProveedorSchema().dump(proveedor))

    else:
        datos = request.json
        if datos:
            proveedor.nombre = datos.get("nombre")
            proveedor.cuit = datos.get("cuit")
            proveedor.dni = datos.get("dni")
            proveedor.telefono = datos.get("telefono")
            proveedor.email = datos.get("email")
            proveedor.direccion = datos.get("direccion")

            db.session.commit()
            return jsonify({'Mensaje': 'Proveedor actualizado con exito.'})

        else:
            return jsonify({'Mensaje': 'Error al actualizar el proveedor.'})

@proveedor_bp.route("/proveedores/eliminar/<int:id>", methods=['GET', 'POST'])
def proveedores_eliminar(id):
    proveedor = db.session.query(Proveedor).filter_by(id=id).first()
    db.session.delete(proveedor)
    db.session.commit()
    return jsonify({'Mensaje': 'Proveedor eliminado con exito.'})