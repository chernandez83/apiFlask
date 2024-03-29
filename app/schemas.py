from marshmallow import Schema, fields
from marshmallow.validate import Length


class TaskSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'deadline', 'created_at')


class ParamsTaskSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=250))
    deadline = fields.DateTime(required=True)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

params_task_schema = ParamsTaskSchema()