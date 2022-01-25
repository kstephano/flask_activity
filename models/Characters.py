from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quotes = db.Column(db.String(255), nullable=False)

    