from app import Author, db

Author.query.filter_by(title='adasdf').delete()
db.session.commit()

# in terminal
# python delete.py (enter)
# flask run