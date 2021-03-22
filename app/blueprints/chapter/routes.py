from . import bp as chapter
from .models import Chapter
from flask import jsonify, request


@chapter.route('/createChapters')
def createChapters():
    """
    [GET] /chapter/createChapters
    """
    createChapters = Chapter.query.all()
    return jsonify([p.to_dict() for p in createChapters])


@chapter.route('/createChapters/<int:id>')
def single_chapter(id):
    """
    [GET] /chapter/createChapters/<id>
    """
    p = Chapter.query.get_or_404(id)
    return jsonify(p.to_dict())

@chapter.route('test', methods=['CHAPTER'])
def test():
    print(request.json)
    return jsonify(request.json)