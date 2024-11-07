from app import db
from models import Empleado, Sucursal
from flask import Blueprint, request, jsonify

from schemas import EmpleadoSchema, SucursalSchema

empleado_bp = Blueprint('empleado', __name__)


@empleado_bp.route("/empleados", methods=['GET', 'POST'])
def empleado():
    empleados = Empleado.query.all()
    sucursal = Sucursal.query.all()
    return jsonify({
        'empleados': EmpleadoSchema(many=True).dump(empleados),
        'sucursales': SucursalSchema(many=True).dump(sucursal)
    })


@empleado_bp.route("/empleados/crear", methods=['POST'])
def crear_empleado():
    datos = request.json

    if datos:
        nombre = datos.get("nombre")
        dni = datos.get("dni")
        sucursal_id = datos.get("sucursal_id")
        cargo = datos.get("cargo")
        telefono = datos.get("telefono")
        email = datos.get("email")
        direccion = datos.get("direccion")

        nuevo_empleado = Empleado(
            nombre=nombre,
            dni=dni,
            sucursal_id=sucursal_id,
            cargo=cargo,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        db.session.add(nuevo_empleado)
        db.session.commit()
        return jsonify({'Mensaje': 'Empleado cargado con exito.'})

    else:
        return jsonify({'Mensaje': 'Error al cargar el nuevo empleado'})


@empleado_bp.route("/empleados/editar/<int:id>", methods=['GET','POST'])
def editar_empleado(id):
    empleado = Empleado.query.get_or_404(id)

    if request.method == "GET":
        return jsonify(EmpleadoSchema().dump(empleado))

    else:
        datos = request.json
        if datos:
            empleado.nombre = datos.get("nombre")
            empleado.sucursal_id = datos.get("sucursal_id")
            empleado.cargo = datos.get("cargo")
            empleado.dni = datos.get("dni")
            empleado.telefono = datos.get("telefono")
            empleado.email = datos.get("email")
            empleado.direccion = datos.get("direccion")

            db.session.commit()
            return jsonify({'Mensaje': 'Empleado actualizado con exito.'})

        else:
            return jsonify({'Mensaje': 'Error al actualizar el empleado.'})

@empleado_bp.route("/empleados/delete/<int:id>", methods=['GET','POST'])
def eliminar_empleado(id):
    empleado = Empleado.query.filter_by(id=id).first()
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({'Mensaje': 'Empleado eliminado con exito.'})
