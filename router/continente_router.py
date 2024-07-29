from flask import Blueprint, jsonify, request
# Importe el modelo que quiero consultar
from models.continente_model import ContinenteModel
from models.genero_model import GeneroModel
# Debemos de llamar a SqlAlchmey esta en mi db.py
from db import db

continente_router = Blueprint('continente_router', __name__)

# Nombre /continentes-all  METODO GET
# RETORNE "Hola amigo"
# Leventar su proyecto
# poniendo en la terminal python app.py
# Prueban el endpoint en POSTMAN  Ó INSOMNIA


@continente_router.route('/continentes-all', methods=['GET'])
def listar_continentes():
    # Para usar la orm debes de poner
    # NombreDelModelo.query.METODO
    continentes = ContinenteModel.query.all()

    # METODO LARGO
    # resultado = []
    # for conti in continentes:
    #     conti = {
    #         'nombre': conti.nombre
    #     }
    #     resultado.append(conti)

    # return jsonify(resultado)

    # METODO CORTO
    return jsonify([{
        "id": conti.id,
        "nombre": conti.nombre
    } for conti in continentes])

# Quiero que cree un endpoit  /genero => GET
# Quiero usando la orm, me liste todos los generos


# Voya traer un solo continente
# Que la ruta que yo voy a enviar va a ser continente/6
@continente_router.route('/continente/<int:id>', methods=['GET'])
def traer_un_continente(id):
    continente = ContinenteModel.query.get(id)
    return jsonify({
        "id": continente.id,
        "nombre": continente.nombre
    })


# Quiero que me hagan un endpoint que me traiga un solo generos
#  genero/<int:id>    METHODO = GET


# Haremos un endpoit de tipo DELETE
@continente_router.route('/continente/<int:id>', methods=['DELETE'])
def delete_continente(id):
    continente = ContinenteModel.query.get(id)
    # Siempre que queramos ELIMINAR, ACTUALIZAR o INSERTAR
    db.session.delete(continente)  # Esto prepara la eliminacion
    db.session.commit()  # Se ejecuta la eliminacion
    return jsonify({
        "msg": "Eliminacion exitosa"
    })


# Quiero que hagan un enpoitn que me elimne los generos
# genero/<int:id> METHODO = DELETE

@continente_router.route('/continente-post', methods=['POST'])
def continente_insert():
    # Debemos de importar el request de flask
    # Nosotrs enviamos informacion
    data = request.get_json()  # Capturo la informacion que se envia
    # Debemos crear una instancia de nuestro modelo
    nuevo_continente = GeneroModel(**data)   # data.get('nombre')
    # Ahora voy a prepar el insertado
    db.session.add(nuevo_continente)
    db.session.commit()
    # Es la respuesta
    return jsonify({
        "msg": "Creacion exitosa",
        "id": nuevo_continente.id,
        "nombre": nuevo_continente.nombre,
    })

# Quiero que hagan un endpoint que me cree los generos
# genero-post METHODO = PUT

@continente_router.route('/continente-put/<int:id>', methods=['PUT'])
def continenete_put(id):
    # Capturo lo que quiero editar
    continente = ContinenteModel.query.get(id)
    data = request.get_json()  #Capturo la data para editarlo
    continente.nombre = data['nombre']
    db.session.commit()
    return jsonify({
                    "id": continente.id,
                    "nombre": continente.nombre
                    })