from app import Author, db

# frances = Author.query.filter_by(name='Frances Esteban').first()
#
# frances.title = 'Turning Heads'
# db.session.commit()

donna = Author.query.get(3)

donna.name = 'Danielle Reyes'
db.session.commit()

