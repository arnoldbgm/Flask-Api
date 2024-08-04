from db import db
from sqlalchemy import (Column, String, Integer, ForeignKey, Float, DateTime)
from datetime import datetime

class VentasModel(db.Model):
    __tablename__ = 'ventas'
