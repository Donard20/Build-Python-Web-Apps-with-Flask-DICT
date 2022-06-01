from app import Author, db

# donard = Author.query.filter_by(name='Donard Azura').first()
#
# donard.title = 'Happy'
# db.session.commit()

donna = Author.query.get(5)

donna.name = 'Danielle Reyes'
db.session.commit()

