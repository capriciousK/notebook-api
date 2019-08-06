from flask import Flask
from flask_script import Manager

from app.notebook import notebook_controller

app = Flask(__name__)
manager = Manager(app)

app.register_blueprint(notebook_controller.controller, url_prefix='/notebook')


@app.route('/')
def hello_world():
    return 'Hello, World!'
