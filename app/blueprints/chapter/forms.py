from app import db
from datetime import datetime


class Chapter(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    id = db.Column(db.Float())
    image = db.Column(db.String())
    description = db.Column(db.String())
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def init(self, username, id, image, description):
        self.username = username
        self.id = id
        self.image = image
        self.description = description

    def to_dict(self):
        return {
            'username': self.username,
            'id': self.id,
            'image': self.image,
            'description': self.description,
            'created_on': self.created_on
        }