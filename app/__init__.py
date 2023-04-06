from flask import Flask

from .models import db
from .models.task import Task

from .views import api_v1

app = Flask(__name__)


def create_app(environment):
    app.config.from_object(environment)
    app.json.ensure_ascii = False
    app.register_blueprint(api_v1)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()

    return app


@app.route('/')
def index():
    return '<h1>Hola!</h1>'
