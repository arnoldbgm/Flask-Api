### 1. Crear un entorno virtual 🐍

```bash
python -m venv venv

```

### 2. Activar el entorno virtual ⚡

```bash
source venv/Scripts/activate

```

### 3. Instalar Flask y todo lo del proyecto 🛠️

```bash
pip install -r requirements.txt
```

### 4. Crear un archivo `app.py` 📄

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenido a mi primera app de Flask 😎'

if __name__ == '__main__':
    app.run(debug=True)

```

### 5. Ejecutar la aplicación ▶️

```bash
python app.py

```

### 6. Crear el archivo `db.py` 📂

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

### 7. Conectar a una base de datos con Flask-SQLAlchemy 🔗

```python
from flask import Flask
from db import db
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
migrate = Migrate(app, db)

class Movies(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    director = Column(String(200))
    year = Column(Integer)
    length_minutes = Column(Integer)

if __name__ == '__main__':
    app.run(debug=True)

```

### 8. Creacion de la base de datos
![image](https://github.com/user-attachments/assets/74435c01-a3ff-4e2a-b4f7-fa7753e9fef5)

### 9. Ejecutar la migración 🚀

- **Crear la carpeta `migrations` (Solo la primera vez)**:
    
    ```bash
    flask db init
    
    ```
    
- **Crear la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db migrate -m "0001-Creacion de BD"
    
    ```
    
- **Aplicar la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db upgrade
    
    ```
    

### 10. Insertaremos data dentro de nuestra bd🚀

```sql
-- Inserción de productos
INSERT INTO productos (name, price, stock) VALUES 
('Tv Samsung', 10.0, 100),
('Play Station 5', 20.0, 200),
('Moto Lineales', 30.0, 300);

-- Inserción de ventas
INSERT INTO ventas (product_id, quantity, price, timestamp) VALUES 
(1, 5, 12.0, '2024-03-05 10:00:00'),  -- Precio de venta 12.0
(2, 3, 22.0, '2024-03-10 12:00:00'),
(1, 2, 11.0, '2024-04-15 14:00:00'),
(3, 1, 33.0, '2024-04-20 16:00:00'),
(2, 4, 21.0, '2024-05-25 18:00:00'),
(1, 6, 13.0, '2024-05-30 20:00:00'),
(3, 2, 31.0, '2024-06-05 09:00:00'),
(1, 3, 12.5, '2024-06-10 11:00:00'),
(2, 5, 23.0, '2024-07-15 13:00:00'),
(3, 4, 32.0, '2024-07-20 15:00:00');

-- Inserción de compras
INSERT INTO compras (product_id, quantity, price, timestamp) VALUES 
(1, 10, 9.0, '2024-03-01 08:00:00'), 
(2, 20, 18.0, '2024-03-05 10:00:00'),
(3, 30, 27.0, '2024-03-10 12:00:00'),
(1, 15, 8.5, '2024-04-01 14:00:00'),
(2, 25, 17.5, '2024-04-05 16:00:00'),
(3, 35, 26.5, '2024-04-10 18:00:00'),
(1, 20, 9.5, '2024-05-01 08:00:00'),
(2, 30, 19.0, '2024-05-05 10:00:00'),
(3, 40, 28.0, '2024-05-10 12:00:00'),
(1, 25, 10.0, '2024-06-01 14:00:00'),
(2, 35, 20.0, '2024-06-05 16:00:00'),
(3, 45, 29.0, '2024-06-10 18:00:00'),
(1, 30, 10.5, '2024-07-01 08:00:00'),
(2, 40, 21.0, '2024-07-05 10:00:00'),
(3, 50, 30.0, '2024-07-10 12:00:00');

```

### 11. Pasamos a crear las rutas para nuestra bd🚀

```python
from flask import Blueprint, jsonify, request

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
	pass
```
