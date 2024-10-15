from app import db
from models import Producto, Modelo, Proveedor, Categoria
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def main():
    return render_template('inicio.html')