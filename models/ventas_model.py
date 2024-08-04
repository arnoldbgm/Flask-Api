from db import db
from sqlalchemy import (Column, String, Integer, ForeignKey, Float, DateTime)
from datetime import datetime

class VentasModel(db.Model):
    __tablename__ = 'ventas'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    quantity = Column(Integer,nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)