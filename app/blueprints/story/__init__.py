from flask import Blueprint

bp = Blueprint('story', name, url_prefix='/story')

from . import routes
allstories above and the next 2 below
models.py for allstories:
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
