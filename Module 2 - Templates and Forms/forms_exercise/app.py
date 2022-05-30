from flask import Flask, render_template, request
from forms import SignUpForm
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# for sign up
# import "request" if going to use POST to send data to a server
# and create or update a resource
@app.route('/signup', methods=['GET' , 'POST'])
def signup():
    form = SignUpForm()
    # use if statement to view the data of user submitted
    if form.is_submitted():
        result = request.form
        return render_template("userdata.html", result=result)
    return render_template('signup.html', form=form)



#optional for running if theres an error
# if __name__ == "__main__":
#     app.run(debug=True)
