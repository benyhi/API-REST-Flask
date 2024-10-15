from app import db
from models import Cliente, Persona
from flask import Blueprint, render_template, redirect, url_for, request


clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route("/clientes")
def clientes():
    clientes = db.session.query(Cliente).join(Persona).all()
    print(clientes)
    return render_template('clientes/clientes.html', clientes=clientes)