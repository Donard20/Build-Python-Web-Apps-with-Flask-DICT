# flash-provides feedback to the user in the form of message
# url_for build url to a certain function
# redirect  will redirect users to different url to a new location in the browser

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret key"

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column('employee', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    division = db.Column(db.String(500), default="")

    def __init__(self, name, position, division):
        self.name = name
        self.position = position
        self.division = division

        def __repr__(self):
            return '<Employee %r>' % self.id


db.create_all()
db.session.commit()


@app.route('/', methods=['GET'])
def list_employees():
    employees = Employee.query.all()
    return render_template('list_employees.html', employees=employees)


@app.route('/add', methods=['GET', 'POST'])
def add_employees():
    if request.method == 'POST':
        if not (request.form['name'] or not request.form['position']) or not request.form['division']:
            flash('Please enter all the fields', 'error')
        else:
            employee = Employee(request.form['name'], request.form['position'], request.form['division'])

        db.session.add(employee)
        db.session.commit()
        flash('Thanks for the awesome info!')
        return redirect(url_for('list_employees'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
