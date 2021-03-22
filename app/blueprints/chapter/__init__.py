from flask import Blueprint

bp = Blueprint('chapter', name, url_prefix='/chapter')

from . import routes, models