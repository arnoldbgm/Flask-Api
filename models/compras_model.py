from db import db
from datetime import datetime
from sqlalchemy import (Column, String, Integer, ForeignKey, Float, DateTime)


class ComprasModel(db.Model):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)  # Precio de compra
    timestamp = Column(DateTime, default=datetime.utcnow)