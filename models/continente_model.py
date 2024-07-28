# Primero llamamos al archivo db.py
from db import db
from sqlalchemy import (Column, String, Integer)

# El nombre de la clase no importa


class ContinenteModel(db.Model):
    # Esto es el nombre de la tabla
    # TIP: Las tablas deben nombrarse en plural
    __tablename__ = 'continentes'

    #nombreDelCampo =  Column(tipoDeDato, configuraciones)
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)


# RETO: 
# CREAR LA TABLA generos y grupos_musicales