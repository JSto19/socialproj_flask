from . import bp as allStories
from .models import Story
from flask import jsonify, request


@allStories.route('/stories')
def stories():
    """
    [GET] /allStories/stories
    """
    stories = Story.query.all()
    return jsonify([p.to_dict() for p in stories])


@allStories.route('/stories/<int:id>')
def single_story(id):
    """
    [GET] /allStories/stories/<id>
    """
    p = Story.query.get_or_404(id)
    return jsonify(p.to_dict())

@allStories.route('test', methods=['POST'])
def test():
    print(request.json)
    return jsonify(request.json)