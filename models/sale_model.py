from db import db
from sqlalchemy import (Column, String, Integer, ForeignKey, Float, DateTime)
from datetime import datetime

class SaleModel(db.Model):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # Precio de venta
    timestamp = Column(DateTime, default=datetime.utcnow)
