# Primero llamamos al archivo db.py
from db import db
from sqlalchemy import (Column, String, Integer, Float)


class ProductModel(db.Model):
    # Esto es el nombre de la tabla
    # TIP: Las tablas deben nombrarse en plural
    __tablename__ = 'productos'

    # nombreDelCampo =  Column(tipoDeDato, configuraciones)
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)


# RETO: 
# CREAR LA TABLA generos