from flask import Blueprint, jsonify, request
# Importe el modelo que quiero consultar
from models.product_model import ProductModel
from models.compras_model import ComprasModel
from models.ventas_model import VentasModel
# Debemos de llamar a SqlAlchmey esta en mi db.py
from db import db

from sqlalchemy import func

product_router = Blueprint('product_router', __name__)


@product_router.route('/products', methods=['GET'])
def get_products():
    pass