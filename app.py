from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from controllers import characters

app = Flask(__name__)
CORS(app)

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

@app.route('/<int:character_id>')
def profile(character_id):
    for character in characters.characters:
        if character['id'] == character_id:
            quote = character['quote']
            name = character['name']
    return f'''This is {name}'s profile\n
    Famous Quote: {quote}
    '''
        
@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops...{err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": "It's not you, it's me...{err}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

