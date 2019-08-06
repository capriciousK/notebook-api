from flask import Blueprint

controller = Blueprint('notebook', __name__)


@controller.route('/', methods=['GET'])
def home():
    return 'this is notebook page'
