from flask import Blueprint, jsonify, request
# Importe el modelo que quiero consultar
from models.product_model import ProductModel
from models.compras_model import ComprasModel
from models.ventas_model import VentasModel
# Debemos de llamar a SqlAlchmey esta en mi db.py
from db import db

from sqlalchemy import func  # Esto se usa para el uso de funciones especificas de SQL

product_router = Blueprint('product_router', __name__)


@product_router.route('/products', methods=['GET'])
def get_products():
    productos = ProductModel.query.all()
    return jsonify([{
        'id': producto.id,
        'nombre': producto.name,
        'precio': producto.price,
        'stock': producto.stock
    } for producto in productos]), 200


@product_router.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    nuevo_producto = ProductModel(**data)
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({
        'msg': 'Producto guardado exitosamente',
        'id': nuevo_producto.id,
        'nombre': nuevo_producto.name,
        'stock': nuevo_producto.stock
    }), 201


@product_router.route('/ventas', methods=['POST'])
def create_sale():
    try:
        data = request.get_json()
        new_sale = VentasModel(**data)
        product = ProductModel.query.get(data['product_id'])
        product.stock = product.stock - data['quantity']
        db.session.add(new_sale)
        db.session.commit()
        return jsonify({
            "msg": "Venta exitosa",
            "id": new_sale.id,
            "quantity": new_sale.quantity,
            "price": new_sale.price,
            "timestamp": new_sale.timestamp
        }), 201
    except Exception as e:
        return {
            "message": "Error de servidor"
        }, 500


@product_router.route('/compras', methods=['POST'])
def create_purchanse():
    try:
        data = request.get_json()
        new_sale = ComprasModel(**data)
        product = ProductModel.query.get(data['product_id'])
        product.stock = + data['quantity']
        db.session.add(new_sale)
        db.session.commit()
        return jsonify({
            "msg": "Compra exitosa",
            "id": new_sale.id,
            "quantity": new_sale.quantity,
            "price": new_sale.price,
            "timestamp": new_sale.timestamp
        }), 201
    except Exception as e:
        return {
            "message": "Error de servidor"
        }, 500


# SELECT
# 	TO_CHAR(timestamp, 'YYYY-MM') AS month,
# 	SUM(quantity * price) AS total
# FROM ventas
# GROUP BY month
# ORDER BY month;


@product_router.route('/estad', methods=['GET'])
def estad():
    ventas_mensuales = db.session.query(
        func.to_char(VentasModel.timestamp, 'YYYY-MM').label('month'),
        func.sum(VentasModel.quantity * VentasModel.price).label('total')
    ).group_by('month').all()

    print(ventas_mensuales)
    return [{
        venta.month: venta.total
    } for venta in ventas_mensuales]
