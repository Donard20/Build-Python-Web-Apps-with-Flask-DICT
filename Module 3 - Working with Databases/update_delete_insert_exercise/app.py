# flash-provides feedback to the user in the form of message
# url_for build url to a certain function
# redirect  will redirect users to different url to a new location in the browser

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authors.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column('author', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), default="")

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content

        def __repr__(self):
            return '<Author %r>' % self.id


db.create_all()
db.session.commit()


@app.route('/', methods=['GET'])
def list_authors():
    authors = Author.query.all()
    return render_template('list_authors.html', authors=authors)


@app.route('/add', methods=['GET', 'POST'])
def add_authors():
    if request.method == 'POST':
        if not (request.form['name'] or not request.form['title']) or not request.form['content']:
            flash('Please enter all the fields', 'error')
        else:
            author = Author(request.form['name'], request.form['title'], request.form['content'])

        db.session.add(author)
        db.session.commit()
        flash('Thanks for the awesome info!')
        return redirect(url_for('list_authors'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)

# pip install flask
# pip install flask-sqlalchemy
# set FLASK=APP=app.py
# set FLASK_DEBUG=1
#
# to run
# flask run

