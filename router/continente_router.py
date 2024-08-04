from flask import Blueprint, jsonify, request
# Importe el modelo que quiero consultar
from models.product_model import ProductModel
from models.purchanse_model import PurchaseModel
from models.sale_model import SaleModel
# Debemos de llamar a SqlAlchmey esta en mi db.py
from db import db

from sqlalchemy import func

main = Blueprint('main', __name__)


@main.route('/products', methods=['GET'])
def get_products():
    # SQL => SELECT * FROM producto;
    products = ProductModel.query.all()
    return jsonify([product.to_dict() for product in products])

@main.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = ProductModel(
        name=data['name'],
        price=data['price'],
        stock=data[ 'stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@main.route('/sale', methods=['POST'])
def add_sale():
    data = request.get_json()
    new_sale = SaleModel(
        product_id=data['product_id'],
        quantity=data['quantity'],
        price=data['price']
    )
    product = ProductModel.query.get(data['product_id'])
    product.stock -= data['quantity']
    db.session.add(new_sale)
    db.session.commit()
    return jsonify(new_sale.to_dict()), 201

@main.route('/purchase', methods=['POST'])
def add_purchase():
    data = request.get_json()
    new_purchase = PurchaseModel(
        product_id=data['product_id'],
        quantity=data['quantity'],
        price=data['price']
    )
    product = ProductModel.query.get(data['product_id'])
    product.stock += data['quantity']
    db.session.add(new_purchase)
    db.session.commit()
    return jsonify(new_purchase.to_dict()), 201

# Endpoint para obtener la máxima venta por mes
@main.route('/sales/max-per-month', methods=['GET'])
def get_max_sales_per_month():
    sales = db.session.query(
        func.to_char(SaleModel.timestamp, 'YYYY-MM').label('month'),
        func.sum(SaleModel.quantity * SaleModel.price).label('total_sales')
    ).group_by('month').all()

    max_sales = {}
    for sale in sales:
        month = sale.month
        total_sales = sale.total_sales
        if month in max_sales:
            if total_sales > max_sales[month]:
                max_sales[month] = total_sales
        else:
            max_sales[month] = total_sales

    return jsonify(max_sales)

# Endpoint para calcular el promedio de ventas por mes
@main.route('/sales/average-per-month', methods=['GET'])
def get_average_sales_per_month():
    sales = db.session.query(
        func.to_char(SaleModel.timestamp, 'YYYY-MM').label('month'),
        func.sum(SaleModel.quantity * SaleModel.price).label('total_sales')
    ).group_by('month').all()

    print(sales)

    total_sales = sum(sale.total_sales for sale in sales)
    average_sales = total_sales / len(sales) if sales else 0

    monthly_sales = {sale.month: sale.total_sales for sale in sales}

    return jsonify({
        'average_sales_per_month': average_sales,
        'monthly_sales': monthly_sales
    })

# Endpoint para obtener la máxima compra por mes
@main.route('/purchases/max-per-month', methods=['GET'])
def get_max_purchases_per_month():
    purchases = db.session.query(
        func.to_char(PurchaseModel.timestamp, 'YYYY-MM').label('month'),
        func.sum(PurchaseModel.quantity * PurchaseModel.price).label('total_purchases')
    ).group_by('month').all()

    max_purchases = {}
    for purchase in purchases:
        month = purchase.month
        total_purchases = purchase.total_purchases
        if month in max_purchases:
            if total_purchases > max_purchases[month]:
                max_purchases[month] = total_purchases
        else:
            max_purchases[month] = total_purchases

    return jsonify(max_purchases)

# Endpoint para calcular el promedio de compras por mes
@main.route('/purchases/average-per-month', methods=['GET'])
def get_average_purchases_per_month():
    purchases = db.session.query(
        func.to_char(PurchaseModel.timestamp, 'YYYY-MM').label('month'),
        func.sum(PurchaseModel.quantity * PurchaseModel.price).label('total_purchases')
    ).group_by('month').all()

    total_purchases = sum(purchase.total_purchases for purchase in purchases)
    average_purchases = total_purchases / len(purchases) if purchases else 0

    monthly_purchases = {purchase.month: purchase.total_purchases for purchase in purchases}

    return jsonify({
        'average_purchases_per_month': average_purchases,
        'monthly_purchases': monthly_purchases
    })