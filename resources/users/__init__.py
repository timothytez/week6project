from flask_smorest import Blueprint

bp = Blueprint('users', __name__, description='Ops on Users')

from . import routes
from . import auth_routes
