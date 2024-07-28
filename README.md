### 1. Crear un entorno virtual 🐍

```bash
python -m venv venv

```

### 2. Activar el entorno virtual ⚡

```bash
source venv/Scripts/activate

```

### 3. Instalar Flask y extensiones 🛠️

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install psycopg2-binary   
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
    flask db migrate -m "Create tables"
    
    ```
    
- **Aplicar la migración (Cada vez que se modifique el modelo)**:
    
    ```bash
    flask db upgrade
    
    ```
    

### 10. Insertaremos data dentro de nuestra bd🚀

```sql
-- Insertar datos en la tabla continentes
INSERT INTO continentes (nombre) VALUES
('América'),
('Europa'),
('Asia'),
('África'),
('Oceanía'),
('Namekuzein');

-- Insertar datos en la tabla generos
INSERT INTO generos (nombre, continente_id) VALUES
('Rock', 1),   -- América
('Pop', 1),    -- América
('Jazz', 1),   -- América
('Clásica', 2), -- Europa
('Electrónica', 2), -- Europa
('K-Pop', 3),  -- Asia
('Reggae', 4); -- África

-- Insertar datos en la tabla grupos_musicales
INSERT INTO grupos_musicales (nombre, anio_formacion, genero_id) VALUES
('The Beatles', 1960, 1),    -- Rock
('Queen', 1970, 1),          -- Rock
('Michael Jackson', 1964, 2),-- Pop
('Miles Davis', 1944, 3),    -- Jazz
('Ludwig van Beethoven', 1770, 4), -- Clásica
('Daft Punk', 1993, 5),      -- Electrónica
('BTS', 2013, 6),            -- K-Pop
('Bob Marley & The Wailers', 1963, 7); -- Reggae

```

### 11. Pasamos a crear las rutas para nuestra bd🚀

```python
from flask import Blueprint, jsonify, request

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
	pass
```
