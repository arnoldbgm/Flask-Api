from db import db
from sqlalchemy import (Column, String, Integer, ForeignKey)


class GeneroModel(db.Model):
    __tablename__ = 'generos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    # Para conectar una tabla con otra debo usar un ForeignKey('nombreTabla.elemnto')
    continente_id = Column(Integer, ForeignKey('continentes.id'))
