import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from flask import Blueprint, request, jsonify
from Service.EmpleadoService import EmpleadoService

empleado_blueprint = Blueprint('empleado', __name__)
empleado_service = EmpleadoService()

@empleado_blueprint.route('/create', methods=['POST'])
def createEmp():
    data = request.json
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    puesto = data.get('puesto')
    correo = data.get('correo')
    telefono = data.get('telefono')
    direccion = data.get('direccion')

    if not nombres or not apellidos or not puesto or not correo or not telefono or not direccion:
        return jsonify({'error': 'Faltan campos'}), 400

    user = empleado_service.create(nombres, apellidos, puesto, correo, telefono, direccion)
    if user != "Correcto":
        return jsonify(f'error: {user}'), 400
    else:
        return jsonify("Empleado agregado!"), 201

@empleado_blueprint.route('/select', methods=['GET'])
def selectEmp():
    try:
        user = empleado_service.select()
        return user
    except Exception as e:
        return jsonify({f'error: {e}'}), 404

@empleado_blueprint.route('/update', methods=['PUT'])
def updateEmp():
    data = request.json
    id_empleado = data.get('id_empleado')
    nombres = data.get('nombres')
    apellidos = data.get('apellidos')
    puesto = data.get('puesto')
    correo = data.get('correo')
    telefono = data.get('telefono')
    direccion = data.get('direccion')

    if not id_empleado or not nombres or not apellidos or not puesto or not correo or not telefono or not direccion:
        return jsonify({'error': 'Missing required fields'}), 400
    
    var = empleado_service.update(id_empleado, nombres, apellidos, puesto, correo, telefono, direccion)

    if var == "Correcto":
        return jsonify("Empleado actualizado!")
    else:
        return jsonify({f'error: {var}'}), 404


@empleado_blueprint.route('/delete/<int:id_empleado>', methods=['DELETE'])
def delete_user(id_empleado):
    var = empleado_service.delete(id_empleado)
    if var == "Correcto":
        return 'Borrado Correcto!', 204
    else:
        return jsonify({f'error: {var}'}), 404
