from urllib import request

from sqlalchemy import except_

from app import db
from models import Empleado, Sucursal
from flask import Blueprint, render_template, redirect, url_for, request

empleado_bp = Blueprint('empleado', __name__)


@empleado_bp.route("/empleados", methods=['GET', 'POST'])
def empleado():
    empleados = db.session.query(Empleado, Sucursal).join(Sucursal, Empleado.sucursal_id == Sucursal.id).all()
    sucursal = Sucursal.query.all()
    return render_template('empleados/empleados.html', empleados=empleados, sucursales=sucursal)


@empleado_bp.route("/empleados/crear", methods=['POST'])
def crear_empleado():
    nombre = request.form.get('nombre')
    dni = request.form.get('dni')
    telefono = request.form.get('telefono')
    direccion = request.form.get('direccion')
    email = request.form.get('email')
    cargo = request.form.get('cargo')
    sucursal_id = request.form.get('sucursal')

    if nombre and dni and telefono and direccion and email and cargo and sucursal_id:
        try:
            nuevo_empleado = Empleado(
                nombre=nombre,
                dni=dni,
                telefono=telefono,
                direccion=direccion,
                email=email,
                cargo=cargo,
                sucursal_id=sucursal_id
            )

            db.session.add(nuevo_empleado)
            db.session.commit()

        except except_() as error:
            print(f'ERROR EN LA BD:{error}')

        finally:
            return redirect(url_for('empleado.empleado'))

    else:
        print('Debes completar todos los datos del formulario.')


@empleado_bp.route("/empleados/editar/<int:id>", methods=['GET','POST'])
def editar_empleado(id):
    empleado = Empleado.query.filter_by(id=id).first()

    if request.method == 'GET':
        sucursales = Sucursal.query.all()
        return render_template('empleados/editar_empleado.html', empleado=empleado, sucursales=sucursales)

    else:
        empleado.nombre = request.form.get('nombre')
        empleado.dni = request.form.get('dni')
        empleado.telefono = request.form.get('telefono')
        empleado.direccion = request.form.get('direccion')
        empleado.email = request.form.get('email')
        empleado.cargo = request.form.get('cargo')
        empleado.sucursal_id = request.form.get('sucursal')

        db.session.commit()

        return redirect(url_for('empleado.empleado'))

@empleado_bp.route("/empleados/delete/<int:id>", methods=['GET','POST'])
def eliminar_empleado(id):
    empleado = Empleado.query.filter_by(id=id).first()
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('empleado.empleado'))
