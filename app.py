from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://root@localhost/efi1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models

from views import register_blueprint
register_blueprint(app)

if __name__ == "__main__":
    app.run(debug=True)