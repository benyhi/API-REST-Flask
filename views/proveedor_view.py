from urllib import request

from app import db
from models import Proveedor
from flask import Blueprint, render_template, redirect, url_for

from schemas import ProveedorSchema

proveedor_bp = Blueprint('proveedores', __name__)

@proveedor_bp.route("/proveedores")
def proveedores():
    proveedores = db.session.query(Proveedor).all()
    proveedores_serializer = ProveedorSchema(many=True).dump(proveedores)
    return render_template('proveedores/proveedores.html', proveedores=proveedores_serializer)

@proveedor_bp.route("/proveedores/crear")
def proveedores_crear():
    datos = request.json()
    pass

@proveedor_bp.route("/proveedores/editar/<int:id>", methods=['GET', 'POST'])
def proveedores_editar(id):
    proveedor = db.session.query(Proveedor).filter_by(id=id).first()
    proveedor_serializer = ProveedorSchema().dump(proveedor)

    if request.method == 'GET':
        return render_template('proveedores/editar_proveedor', proveedor=proveedor_serializer)

    else:
        datos = request.json()
        return redirect(url_for('proveedores.proveedores'))

@proveedor_bp.route("/proveedores/eliminar/<int:id>", methods=['GET', 'POST'])
def proveedores_eliminar(id):
    proveedor = db.session.query(Proveedor).filter_by(id=id).first()
    db.session.delete(proveedor)
    db.session.commit()
    return redirect(url_for('proveedores.proveedores'))