from flask import Blueprint
from datetime import datetime

from .models.task import Task
from .responses import response, not_found

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@api_v1.route('/tasks/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()  # SELECT * FROM tasks;
    return response([
        task.serialize() for task in tasks
    ])


@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.filter_by(id=id).first()
    if task is not None:
        return response(task.serialize())
    return not_found()


@api_v1.route('/tasks', methods=['POST'])
def create_task():
    pass


@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_task():
    pass


@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_task():
    pass
