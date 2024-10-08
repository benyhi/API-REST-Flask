from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Base, engine
from models.manejo_bd import Productos, Modelos, Marcas, Categoria

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("base.html")

#########PRODUCTOS########
@app.route("/productos")
def main():
    productos = Productos()
    lista = productos.consultar_todos()
    return render_template("products/productos.html", lista=lista)

@app.route("/productos/create", methods=['GET','POST'])
def create_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        marca = request.form['marca']
        categoria = request.form['categoria']
        costo = request.form['costo']
        cantidad_disponible = request.form['cantidad_disponible']

        productos = Productos()
        productos.crear_producto(nombre,modelo,marca,costo,cantidad_disponible,categoria)
        return redirect(url_for('main'))
    
    else:
        modelos = Modelos()
        lista_modelos = modelos.consultar_todos()
        categoria = Categoria()
        lista_categoria = categoria.consultar_todos()
        marcas = Marcas()
        lista_marcas = marcas.consultar_todos()

        return render_template('products/create_producto.html', modelos=lista_modelos, marca=lista_marcas, categoria=lista_categoria)

@app.route("/productos/del/<int:id>", methods=['POST'])
def delete_producto(id):
    productos = Productos()
    productos.eliminar_producto(id)
    return redirect(url_for('main'))

@app.route("/productos/edit/<int:id>", methods=['GET','POST'])
def edit_producto(id):
    productos = Productos()
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo = request.form['modelo']
        marca = request.form['marca']
        costo = request.form['costo']
        cantidad_disponible = request.form['cantidad_disponible']
        categoria = request.form['categoria']

        productos.actualizar_producto(nombre,modelo,marca,costo,cantidad_disponible,categoria)
        return redirect(url_for('main'))
    
    else:
        producto = productos.consultar_producto(id)

        modelos = Modelos()
        lista_modelos = modelos.consultar_todos()

        marcas = Marcas()
        lista_marcas = marcas.consultar_todos()

        categoria = Categoria()
        lista_categoria = categoria.consultar_todos()

        return render_template('products/edit_producto.html',producto=producto ,modelos=lista_modelos, marca=lista_marcas, categoria=lista_categoria)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)