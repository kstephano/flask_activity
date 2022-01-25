from werkzeug.exceptions import BadRequest

characters = [
    { 'id': 1, 'name': 'Lightning McQueen', 'quote': 'Speed. I am speed. Floating like a Cadillac. Stinging like a Beemer.' },
    { 'id': 2, 'name': 'Doc Hudson', 'quote': "I know his type. Race car. He's the last thing this town needs." },
    { 'id': 3, 'name': 'Tow Mater', 'quote': 'Yeah, like "tuh-mater", but without the tuh!' },
    { 'id': 4, 'name': 'Sally Carrera', 'quote': '[upon accidentally showing her pinstripe tattoo to Lightning] Oh, you saw that?' },
    { 'id': 5, 'name': 'Luigi', 'quote': 'Perfetto' },
    { 'id': 6, 'name': 'Chick Hicks', 'quote': 'Ka-Chinka! Ka-Chinka!' },
    { 'id': 7, 'name': 'Finn McMissile', 'quote': "That's how everyone sees you. That's the genius of it. Nobody realizes they're being fooled because they're too busy laughing AT the fool." },
    { 'id': 8, 'name': 'Shrek', 'quote': 'Ogres are like onions... Onions have layers. Ogres have layers... You get it?' },
    { 'id': 9, 'name': 'Guido', 'quote': 'Ti piace, eh? Si, si, bellissimo.' },
]

def index(req):
    return [c for c in characters], 200

def show(req, id):
    return find_by_uid(id), 200

def create(req):
    new_character = req.get_json()
    new_character['id'] = sorted([c['id'] for c in characters])[-1] + 1

def update(req, id):
    char = find_by_uid(id)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        char[key] = val
    return char, 200

def destroy(req, id):
    char = find_by_uid(id)
    characters.remove(char)
    return char, 204

def find_by_uid(id):
    try:
        return next(c for c in characters if c['id'] == id)
    except:
        raise BadRequest(f"We don't have that character with id {id}!")