# Primero llamamos al archivo db.py
from db import db
from sqlalchemy import (Column, String, Integer, Float)


class ProductModel(db.Model):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)