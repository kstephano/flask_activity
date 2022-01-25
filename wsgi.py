from app import app
from models.Character import db, append_char, Character

db.create_all()
append_char()

print(Character.query.all())
app.run()
