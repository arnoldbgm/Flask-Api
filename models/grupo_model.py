from db import db
from sqlalchemy import (Column, String, Integer, ForeignKey)


class GrupoModel(db.Model):
    __tablename__ = 'grupos_musicales'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    # Para conectar una tabla con otra debo usar un ForeignKey('nombreTabla.elemnto')
    anio_formacion = Column(Integer, nullable=False)
    genero_id = Column(Integer, ForeignKey('generos.id'))