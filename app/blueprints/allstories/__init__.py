from flask import Blueprint

bp = Blueprint('story', name, url_prefix='/story')

from . import routes