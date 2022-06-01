from app import Author, db

frances = Author.query.filter_by(name='Frances Esteban').first()

frances.title = 'Turning Heads'
db.session.commit()