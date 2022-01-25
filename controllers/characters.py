from werkzeug.exceptions import BadRequest
from models.Character import Character, db, serialize
from flask import Flask

def index(req):
    chars = Character.query.all()
    chars = list(map(serialize, chars))
    return chars, 200

def show(req, id):
    print(find_by_id(id))
    return serialize(find_by_id(id)), 200

def create(req):
    data = req.get_json()
    new_char = Character(name=data["name"], quotes=data["quotes"])
    db.session.add(new_char)
    db.session.commit()
    return serialize(new_char), 201

def update(req, id):
    char = find_by_id(id)
    data = req.get_json()
    for key, val in data.items():
        char[key] = val
    db.session.commit()
    return serialize(char), 201

def destroy(req, id):
    char = find_by_id(id)
    db.session.delete(char)
    db.session.commit()
    return serialize(char), 204

def find_by_id(id):
    print("id = ", id)
    try:
        char = Character.query.get(id)
        print(char)
        return char
    except:
        raise BadRequest(f"Character with id {id} does not exist!")