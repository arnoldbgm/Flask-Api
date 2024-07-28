from flask import Blueprint, jsonify, request
from models.continente_model import ContinenteModel
from db import db

continente_router = Blueprint('continente_router',__name__)

@continente_router.route('/continente', methods=['GET'])
def listar_libros():
    # Para poder usar la ORM, debo de primero, llamar al modelo
    # Entonces el query.all   == SQL (SELECT * FROM libros)
    # libros = LibroModel.query.all()
    # resultado = []
    # for libro in libros:
    #     libro_data = {
    #         'id': libro.id,
    #         'nombre': libro.nombre,
    #     }
    #     resultado.append(libro_data)
    # return jsonify(resultado)

    # Envolver el generador en una lista
    # resultado = [{
    #     'id': libro.id,
    #     'nombre': libro.nombre
    # } for libro in libros]
    # return jsonify(resultado)

    # return jsonify([{'id': libro.id,
    #                  'nombre': libro.nombre,
    #                  'estado': libro.estado,
    #                  'autor': libro.autor,
    #                  'categoria': {
    #                  'id': libro.categoria.id,
    #                  'nombre': libro.categoria.nombre
    #             }
    #                  } for libro in libros])

    continentes = ContinenteModel.query.all()
    return jsonify([{
        "id": conti.id,
        "nombre": conti.nombre
    } for conti in continentes])


@continente_router.route('/continente-crear', methods=['POST'])
def crear_continente():
    data = request.get_json()
    if not 'nombre' in data:
        return jsonify({"msg": "Debes de enviar el nombre"}), 400
    else:
        print(f"Que me muestra => {data['nombre']}")
        nuevo_continente = ContinenteModel(nombre=data['nombre'])
        db.session.add(nuevo_continente)
        db.session.commit()
        return jsonify({'id': nuevo_continente.id, 
                    'nombre': nuevo_continente.nombre})
    
@continente_router.route('/continentes/<int:id>', methods=['DELETE'])
def delete_continente(id):
    continente = ContinenteModel.query.get(id)
    
    if continente is None:
        return jsonify({"msg": f"El continente con ID {id} no existe."}), 404

    db.session.delete(continente)
    db.session.commit()
    return jsonify({
        "msg": "Eliminacion exitosa✌"
    })

@continente_router.route('/continentes/<int:id>', methods=['PUT'])
def actualizar_continente(id):
    data = request.get_json()
    continente = ContinenteModel.query.get_or_404(id)
    continente.nombre = data['nombre']
    db.session.commit()
    return jsonify({'id': continente.id, 'nombre': continente.nombre})