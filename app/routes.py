from app import db, mail, Message
from flask import current_app as app, render_template, request, flash, redirect, url_for, jsonify
from app.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    context = {
        'title': 'Kekambas Blog | HOME',
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    return render_template('index.html', **context)

@app.route('/posts')
def posts():
    posts = Post.query.all()
    users = User.query.all()
    return jsonify([[p.to_dict() for p in posts],[u.to_dict() for u in users]])

@app.route('/posts/<int:id>')
def single_post(id):
    p = Post.query.get_or_404(id)
    return jsonify(p.to_dict())