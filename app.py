from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Welcome home friend'

@app.route('/penguins', methods=['GET', 'POST'])
def penguin():
    if request.method == 'GET':
        return jsonify({ 'Penguins': ['Pingu', 'Kowalski']})
    elif request.method == 'POST':
        data = request.json
        return f"{data['name']} has joined the waddle"
        
@app.error_handler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops...{err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": "It's not you, it's me...{err}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

