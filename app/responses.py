from flask import jsonify

def response(data):
    return jsonify({
        'success': True,
        'data': data,
    }), 200


def not_found():
    return jsonify({
        'sucess': False,
        'data': {},
        'message': 'Tarea no encontrada.',
        'code': 404,
    }), 404

def bad_request(message = 'Solicitud erronea'):
    return jsonify({
        'success': False,
        'data': {},
        'message': message,
        'code': 400,
    }), 400