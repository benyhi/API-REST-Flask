from app import db
from models import Cliente
from flask import Blueprint, request, jsonify

from schemas import ClienteSchema

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route("/clientes", methods=["GET"])
def clientes():
    clientes = Cliente.query.all()
    return jsonify(ClienteSchema(many=True).dump(clientes))

@clientes_bp.route("/clientes/crear", methods=['POST'])
def crear_cliente():
    datos = request.json

    if datos:
        nombre = datos.get("nombre")
        dni = datos.get("dni")
        telefono = datos.get("telefono")
        email = datos.get("email")
        direccion = datos.get("direccion")

        nuevo_cliente = Cliente(
            nombre=nombre,
            dni=dni,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify({'Mensaje': 'Cliente cargado con exito.'})

    else:
        return jsonify({'Mensaje': 'Error al cargar el nuevo cliente'})

@clientes_bp.route("/clientes/editar/<int:id>", methods=['GET','POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == "GET":
        return jsonify(ClienteSchema().dump(cliente))

    else:
        datos = request.json
        if datos:
            cliente.nombre = datos.get("nombre")
            cliente.dni = datos.get("dni")
            cliente.telefono = datos.get("telefono")
            cliente.email = datos.get("email")
            cliente.direccion = datos.get("direccion")

            db.session.commit()
            return jsonify({'Mensaje': 'Cliente actualizado con exito.'})

        else:
            return jsonify({'Mensaje': 'Error al actualizar el cliente.'})

@clientes_bp.route("/clientes/delete/<int:id>", methods=['GET','POST'])
def eliminar_cliente(id):
    empleado = Cliente.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({'Mensaje': 'Cliente eliminado con exito.'})
