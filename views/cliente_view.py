from app import db
from models import Cliente
from flask import Blueprint, render_template, redirect, url_for, request, jsonify

from schemas import ClienteSchema

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route("/clientes", methods=["GET"])
def clientes():
    clientes = Cliente.query.all()
    return jsonify(ClienteSchema(many=True).dump(clientes))

@clientes_bp.route("/clientes/crear", methods=['POST'])
def crear_cliente():
    datos = request.json()
    pass

@clientes_bp.route("/clientes/editar/<int:id>", methods=['GET','POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    cliente_serializer = ClienteSchema().dump(cliente)

    if request.method == "GET":
        return render_template('clientes/editar_cliente.html', cliente=cliente_serializer)

    else:
        datos=request.json()
        pass
        return redirect(url_for('clientes.clientes'))

@clientes_bp.route("/clientes/delete/<int:id>", methods=['GET','POST'])
def eliminar_cliente(id):
    empleado = Cliente.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('clientes.clientes'))
