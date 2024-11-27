from flask import Blueprint, jsonify, render_template
from models.gato import Gato
from models.perro import Perro
from models.huron import Huron
from models.boa_constrictor import BoaConstrictor

from models.boa_constrictor import BoaConstrictor


animales_bp = Blueprint('animales', __name__)

gato = Gato(1, "Felix", 3, "Miau")
perro = Perro(2, "Max", 5, "Guau")
huron = Huron(3, "Fifi", 2, "Chirrido")
#boa = BoaConstrictor(4, "Kaa", 7, "Siseo")




@animales_bp.route("/")
def index():
    return render_template ("index.html") # ("listar_users.html",guarderias=guarderias)
 
@animales_bp.route('/gatos', methods=['GET'])
def get_gatos():
    return jsonify(gato.__dict__)

@animales_bp.route('/perros', methods=['GET'])
def get_perros():
    return jsonify(perro.__dict__)

@animales_bp.route('/hurones', methods=['GET'])
def get_hurones():
    return jsonify(huron.__dict__)

""" @animales_bp.route('/serpientes', methods=['GET'])
def get_serpientes():
    return jsonify(boa.__dict__) """

@animales_bp.route('/serpientes/<int:id>', methods=['GET'])
def get_serpiente_by_id(id):
    serpiente = BoaConstrictor.buscar_por_id(id)
    if serpiente:
        return jsonify(serpiente.__dict__)
    return jsonify({"error": "Serpiente no encontrada"}), 404

@animales_bp.route('/serpientes', methods=['POST'])
def add_serpiente():
    data = request.get_json()
    nueva_serpiente = BoaConstrictor.agregar_serpiente(
        nombre=data.get('nombre'),
        edad=data.get('edad'),
        sonido=data.get('sonido')
    )
    return jsonify(nueva_serpiente.__dict__), 201