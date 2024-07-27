from flask import Flask
# Ahora usaremos la conexion para poder crear nuestra base de datos
from db import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/flask"

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main':
    app.run(debug=True)
