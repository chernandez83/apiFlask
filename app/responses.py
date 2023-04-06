from flask import jsonify

def response(data):
    return jsonify({
        'success': True,
        'data': data
    }), 200


def not_found():
    return jsonify({
        'sucess': False,
        'data': {},
        'message': 'Tarea no encontrada.',
        'code': 404
    }), 404