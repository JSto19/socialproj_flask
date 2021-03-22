from flask import Blueprint

bp = Blueprint('chapter', __name__, url_prefix='/chapter')

from . import routes, models