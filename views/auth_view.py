from datetime import timedelta
from flask import Blueprint, render_template, redirect, url_for, request, jsonify

from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app import db
from models import Usuario

from schemas import UsuarioSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    nombre_usuario = data.username
    contrasena = data.password
    print(nombre_usuario, contrasena)
    usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

    if usuario and check_password_hash(usuario.contrasena_hash, contrasena):
        access_token = create_access_token(
            identity=nombre_usuario,
            expires_delta=timedelta(minutes=60),
            additional_claims=dict(usuario.is_admin))

        return jsonify({'Token': access_token})

    return jsonify({'Mensaje':'El usuario o contraseña no coinciden.'})



@auth_bp.route('/usuarios', methods=['GET', 'POST'])
@jwt_required
def usuarios():
    data_jwt = get_jwt()
    administrador = data_jwt.get('administrador')

    if request.method == 'POST':
        if administrador is True:
            data = request.json()
            nombre_usuario = data['nombre_usuario']
            contrasena = data['contrasena']

            try:
                nuevo_usuario= Usuario(
                    nombre_usuario=nombre_usuario,
                    contrasena_hash=generate_password_hash(contrasena),
                    is_admin=False
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify({'Mensaje':'Usuario creado exitosamente', 'Usuario':nuevo_usuario})

            except:
                return jsonify({'Mensaje':'El usuario ya existe'})

        else:
            return jsonify({'Mensaje':'Solo el admin puede crear usuarios.'})

    else:
        if administrador is True:
            usuarios = Usuario.query.all()
            return UsuarioSchema(many=True).dump(usuarios)
