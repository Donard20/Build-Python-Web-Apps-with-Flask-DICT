from app import Author, db

Author.query.filter_by(id=5).delete()
db.session.commit()

# in terminal
# python delete.py (enter)
# flask run

# delete() used to remove specific entries
# .filter_by is used to find a specific entry by property