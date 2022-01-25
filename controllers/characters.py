from werkzeug.exceptions import BadRequest
from models.Character import Character, db
from flask import Flask
from models.Character import Character

def index(req):
    return Character.query.all(), 200

def show(req, id):
    return find_by_id(id), 200

def create(req):
    data = req.get_json()
    new_char = Character(name=data["name"], quotes=data["quotes"])
    db.session.add(new_char)
    db.session.commit()
    return new_char, 201

def update(req, id):
    char = find_by_id(id)
    data = req.get_json()
    for key, val in data.items():
        char[key] = val
    db.session.commit()
    return char, 201

def destroy(req, id):
    char = find_by_id(id)
    db.session.delete(char)
    db.session.commit()
    return char, 204

def find_by_id(id):
    try:
        char = Character.query.filter_by(id=id)
        return char
    except:
        raise BadRequest(f"Character with id {id} does not exist!")