from db import db
from sqlalchemy import (
    Column,
    String,
    Integer
)

class ContinenteModel(db.Model):
    __tablename__ = 'continentes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)