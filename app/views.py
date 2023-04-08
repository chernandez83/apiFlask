from flask import Blueprint, request
from datetime import datetime
from json import loads

from .models.task import Task
from .responses import response, not_found, bad_request

from .schemas import task_schema, tasks_schema, params_task_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


def set_task(function):
    def wrap(*args, **kwargs):
        try:
            id = int(kwargs.get('id', 0))
        except:
            return not_found()
        task = Task.query.filter_by(id=id).first()
        if task is None:
            return not_found()
        return function(task)
    wrap.__name__ = function.__name__ # evita sobreescribir endpoints
    return wrap


@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1

    try:
        order = request.args.get('order', 'asc')
    except:
        order = 'asc'

    # tasks = Task.query.all()  # SELECT * FROM tasks;
    tasks = Task.get_by_page(order, page)
    return response(tasks_schema.dump(tasks))
    # return response([
    #     task.serialize() for task in tasks
    # ])


@api_v1.route('/tasks/<id>', methods=['GET'])
@set_task
def get_task(task):
    #return response(task.serialize())
    return response(task_schema.dump(task))


@api_v1.route('/tasks', methods=['POST'])
def create_task():
    # json = request.get_json(force=True)
    json = loads(request.data.decode('latin-1'))

    # if json.get('title') is None or len(json['title']) > 50:
    #     return bad_request()

    # if json.get('description') is None:
    #     return bad_request()

    # if json.get('deadline') is None:
    #     return bad_request()
    
    error = params_task_schema.validate(json)
    if error:
        #print(error)
        return bad_request(error)

    task = Task.new(json['title'], json['description'], json['deadline'])
    if task.save():
        #return response(task.serialize())
        return response(task_schema.dump(task))

    return bad_request()


@api_v1.route('/tasks/<id>', methods=['PUT'])
@set_task
def update_task(task):
    json = request.get_json(force=True)
    # json = loads(request.data.decode('latin-1'))

    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)

    if task.save():
        #return response(task.serialize())
        return response(task_schema.dump(task))

    return bad_request()


@api_v1.route('/tasks/<id>', methods=['DELETE'])
@set_task
def delete_task(task):
    if task.delete():
        #return response(task.serialize())
        return response(task_schema.dump(task))

    return bad_request()
