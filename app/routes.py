from app import db, mail, Message
from flask import current_app as app, render_template, request, flash, redirect, url_for, jsonify
from app.models import User, Chapter, Story
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    context = {
        'title': 'Kekambas Blog | HOME',
        'story': Story.query.order_by(Story.date_created.desc()).all()
    }
    return render_template('index.html', **context)

@app.route('/stories')
def story():
    s = Story.query.all()
    return jsonify([[s.to_dict() for s in story]])

@app.route('/stories/<int:id>')
def single_story(id):
    s = Story.query.get_or_404(id)
    return jsonify(s.to_dict())

@app.route('/chapter')
def chapter():
    c = Chapter.query.all()
    return jsonify([[c.to_dict() for c in chapter]])

@app.route('/chapter/<int:id>')
def single_chapter(id):
    c = Chapter.query.get_or_404(id)
    return jsonify(c.to_dict())