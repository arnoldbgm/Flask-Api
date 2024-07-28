from flask import Blueprint, jsonify, request
from models.continente_model import ContinenteModel

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
    pass