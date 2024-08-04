# Primero llamamos al archivo db.py
from db import db
from sqlalchemy import (Column, String, Integer, Float)


class ProductModel(db.Model):
    __tablename__ = 'productos'
