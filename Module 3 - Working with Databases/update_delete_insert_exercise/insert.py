from app import Author, db

nardo = Author('Donna Reyes', 'Romantic Birds', 'Penguins propose to each other with pebbles.')

db.session.add(donna)
db.session.commit()

donna.id

# in terminal
# python insert.py (enter)
# flask run