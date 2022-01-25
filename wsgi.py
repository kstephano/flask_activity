from app import app
from models.Character import append_char, Character, db


db.drop_all()
db.create_all()
append_char()

app.run()
