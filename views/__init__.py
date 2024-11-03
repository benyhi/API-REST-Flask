from .empleado_view import empleado_bp
from .producto_view import productos_bp
from .cliente_view import clientes_bp
from .main_view import main_bp
from .proveedor_view import proveedor_bp

def register_blueprint(app):
    app.register_blueprint(productos_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(empleado_bp)
