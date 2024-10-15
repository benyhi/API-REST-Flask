from .producto_view import productos_bp

def register_blueprint(app):
    app.register_blueprint(productos_bp)