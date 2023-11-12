from flask import Blueprint, jsonify, request
from modelos.usuarios import crear_usuario, obtener_usuarios, obtener_usuario_por_id

# Creamos el blueprint
usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios/', methods=["GET"])
def obtener_usuarios_json():
    return jsonify(obtener_usuarios())

@usuarios_bp.route('/usuarios/', methods=["POST"])
def crear_usuario_json():
    if request.is_json:
        if "nombre_de_usuario" in request.json and "contraseña" in request.json:            
            # usuario = json.loads(request.data)
            # es lo mismo que
            usuario = request.get_json()
            usuario_creado=crear_usuario(usuario["nombre_de_usuario"], usuario["contraseña"])
            return jsonify(usuario_creado),200
        else:
            return jsonify({"error":"Faltan datos"}),400
    else:
        return jsonify({"error":"El formato de la solicitud no es JSON"}),400
    
@usuarios_bp.route('/usuarios/<int:id_usuario>', methods=["GET"])
def obtener_usuario_por_id_json(id_usuario):
    usuario = obtener_usuario_por_id(id_usuario)
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"error":"Usuario no encontrado"}), 404