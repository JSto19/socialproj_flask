from flask import Blueprint

bp = Blueprint('story', __name__, url_prefix='/story')

from . import routes
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
