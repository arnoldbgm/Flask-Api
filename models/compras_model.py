from db import db
from datetime import datetime
from sqlalchemy import (Column, String, Integer, ForeignKey, Float, DateTime)


class ComprasModel(db.Model):
    __tablename__ = 'compras'
