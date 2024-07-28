from db import db
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)

class GrupoMusicalModel(db.Model):
    __tablename__ = 'grupos_musicales'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    anio_formacion = Column(Integer)
    genero_id = Column(Integer, ForeignKey('generos.id'))