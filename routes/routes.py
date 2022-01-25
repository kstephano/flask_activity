# from controllers.characters import index, create, show, destroy, update
from controllers import characters
# from controllers.characters import Character, index, create
from werkzeug import exceptions
from flask import request, jsonify
from app import app

@app.route('/')
def home():
    return '🏎 Welcome 🚓 to the 🚘 home of 🚔 cars, friend 🚗'

@app.route('/kachow')
def kerchow():
    return "Ka-chow! I am speed 🚗⚡"

@app.route('/dienda')
def dienda():
    return ":)"

@app.route('/api/characters', methods=['GET', 'POST'])
def characters_handler():
    fns = {
        'GET': characters.index,
        'POST': characters.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/characters/<int:characters_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def character_handler(characters_id):
    fns = {
        'GET': characters.show,
        'PATCH': characters.update,
        'PUT': characters.update,
        'DELETE': characters.destroy
    }
    resp, code = fns[request.method](request, characters_id)
    return jsonify(resp), code
        
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops...{err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": "It's not you, it's me...{err}"}), 500