from datetime import timedelta
from flask import Blueprint, request, jsonify

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
    data = request.get_json()
    nombre_usuario = data['nombre_usuario']
    contrasena = data['contrasena']
    usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()

    if usuario and check_password_hash(usuario.contrasena_hash, contrasena):
        access_token = create_access_token(
            identity=nombre_usuario,
            expires_delta=timedelta(minutes=60),
            additional_claims={"is_admin": usuario.is_admin}
        )

        return jsonify({'Token': access_token})

    return jsonify({'Mensaje':'El usuario o contraseña no coinciden.'})

@auth_bp.route('/usuarios')
@jwt_required()
def usuarios():
    data_jwt = get_jwt()
    administrador = data_jwt.get('is_admin')

    if administrador is True:
        usuarios = Usuario.query.all()
        usuarios_serializer = UsuarioSchema(many=True).dump(usuarios)
        return jsonify({"usuarios":usuarios_serializer})
    else:
        return jsonify({'Mensaje':"Se requieren permisos de administrador para ejecutar esta accion."})

@auth_bp.route('/usuarios/crear', methods=['POST'])
@jwt_required()
def crear_usuario():
    data_jwt = get_jwt()
    administrador = data_jwt.get('is_admin')

    if administrador is True:
        data = request.get_json()
        print(data)

        if data:
            try:
                nuevo_usuario= Usuario(
                    nombre_usuario= data['nombre_usuario'],
                    contrasena_hash= generate_password_hash(data['contrasena']),
                    is_admin= data['is_admin']
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify({'Mensaje':'Usuario creado exitosamente'}), 200

            except Exception as e:
                return jsonify({'Mensaje':'El usuario ya existe', 'Error': e})

    else:
        return jsonify({'Mensaje':"Se requieren permisos de administrador para ejecutar esta accion."})
        
@auth_bp.route('/usuarios/editar/<int:id>', methods=['GET','PUT'])
@jwt_required()
def editar_usuarios(id):
    data_jwt = get_jwt()
    administrador = data_jwt.get('is_admin')
    usuario = Usuario.query.get_or_404(id)

    if administrador is True:
        if request.method == 'GET':
            return jsonify(UsuarioSchema().dump(usuario))
        
        else:
            datos = request.get_json()
            print(datos)
            if datos:
                if 'nombre_usuario' in datos:
                    usuario.nombre_usuario = datos.get('nombre_usuario')

                if 'contrasena' in datos and check_password_hash(usuario.contrasena_hash, 'contrsena') == False:
                    usuario.contrasena_hash = generate_password_hash(datos.get('contrasena'))

                if 'is_admin' in datos:
                    usuario.is_admin = datos.get('is_admin')

                db.session.commit()
                db.session.close()
                return jsonify({'Mensaje':'Usuario actualizado con exito.'}), 200
            else:
                return jsonify({'Mensaje':'Error al obtener el usuario.'})
    else:
        return jsonify({"Mensaje":"Se requieren permisos de administrador para ejecutar esta accion."})

@auth_bp.route('/usuarios/eliminar/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_usuario(id):
    data_jwt = get_jwt()
    administrador = data_jwt.get('is_admin')

    if administrador is True:
        usuario = Usuario.query.filter_by(id=id).first()
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'Mensaje':'Usuario eliminado exitosamente'})

    else:
        jsonify({"Mensaje":"Se requieren permisos de administrador para ejecutar esta accion."})