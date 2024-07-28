Creamos nuestro proyecto en Flask
Ahora pasamos a instalar lo que seria
 
```py
pip install -U Flask-SQLAlchemy
pip install Flask-Migrate

```

Ahora vamos a crear nuestro archivo categorias

De aqui viene los tipos de datos para nuestra bd
https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types

De aqui viene lo que va a nuestra bd
https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column.__init__


Para ejecutar las migraciones 
# Crear la carpeta migrations (Solo la primera vez)
flask db init

# Crear la migración (Cada vez que se modifique el modelo)
flask db migrate -m "Create tables"

# Aplicar la migración (Cada vez que se modifique el modelo)
flask db upgrade