from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class NoteModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(255))

    def __init__(self, title, content):
        self.title = title
        self.content = content


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NoteModel


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)
