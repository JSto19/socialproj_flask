from flask import Blueprint

bp = Blueprint('story', __name__, url_prefix='/story')

from . import routes