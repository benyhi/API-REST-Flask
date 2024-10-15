from app import db
from models import Proveedor
from flask import Blueprint, render_template

proveedor_bp = Blueprint('proveedores', __name__)

@proveedor_bp.route("/proveedores")
def proveedores():
    proveedores = db.session.query(Proveedor).all()
    return render_template('proveedores/proveedores.html', proveedores=proveedores)