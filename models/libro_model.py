from db import db
from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    ForeignKey
)

class ProductoModel(db.Model):
    __tablename__ = 'libros'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    estado = Column(Boolean, default=True)
    #                                     Aqui va el nombre de la tabla y su campo
    categoria_id = Column(Integer, ForeignKey('categorias.id'))