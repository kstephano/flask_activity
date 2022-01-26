from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quotes = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"id: {self.id}, Name: {self.name}, Quote: {self.quotes}"

 
characters = [
    { 'name': 'Lightning McQueen', 'quotes': 'Speed. I am speed. Floating like a Cadillac. Stinging like a Beemer.' },
    { 'name': 'Doc Hudson', 'quotes': "I know his type. Race car. He's the last thing this town needs." },
    { 'name': 'Tow Mater', 'quotes': 'Yeah, like "tuh-mater", but without the tuh!' },
    { 'name': 'Sally Carrera', 'quotes': '[upon accidentally showing her pinstripe tattoo to Lightning] Oh, you saw that?' },
    { 'name': 'Luigi', 'quotes': 'Perfetto' },
    { 'name': 'Chick Hicks', 'quotes': 'Ka-Chinka! Ka-Chinka!' },
    { 'name': 'Finn McMissile', 'quotes': "That's how everyone sees you. That's the genius of it. Nobody realizes they're being fooled because they're too busy laughing AT the fool." },
    { 'name': 'Shrek', 'quotes': 'Ogres are like onions... Onions have layers. Ogres have layers... You get it?' },
    { 'name': 'Guido', 'quotes': 'Ti piace, eh? Si, si, bellissimo.' },
]

def append_char():
    # char_list = [Character(name=c.name, quotes=c.quotes) for c in characters]
    for c in characters:
        char = Character(name=c["name"], quotes=c["quotes"])
        db.session.add(char)
    db.session.commit()

def serialize(self):
    return {
        "id": self.id,
        "name": self.name,
        "quotes": self.quotes
    }

def updateCharacter(self, data):
    for key, value in data.items():
        if key == "name": self.name = value
        if key == "quote": self.quotes = value
    return self 