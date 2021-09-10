from flask import Blueprint, request, jsonify
from ..model import *

api = Blueprint('api', __name__)


@api.route('/note/')
def note_list():
    all_notes = NoteModel.query.all()
    return jsonify(notes_schema.dump(all_notes))


@api.route('/note/', methods=['POST'])
def create_note():
    title = request.json.get('title', '')
    content = request.json.get('content', '')

    note = NoteModel(title=title, content=content)

    db.session.add(note)
    db.session.commit()

    return note_schema.jsonify(note)


@api.route('/note/<int:note_id>/', methods=["GET"])
def note_detail(note_id):
    note = NoteModel.query.get(note_id)
    return note_schema.jsonify(note)


@api.route('/note/<int:note_id>/', methods=['PATCH'])
def update_note(note_id):
    title = request.json.get('title', '')
    content = request.json.get('content', '')

    note = NoteModel.query.get(note_id)

    note.title = title
    note.content = content

    db.session.add(note)
    db.session.commit()

    return note_schema.jsonify(note)


@api.route('/note/<int:note_id>/', methods=["DELETE"])
def delete_note(note_id):
    note = NoteModel.query.get(note_id)

    db.session.delete(note)
    db.session.commit()

    return note_schema.jsonify(note)
