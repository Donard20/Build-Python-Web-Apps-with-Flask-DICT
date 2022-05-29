from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<Hello, World!"
@app.route('/animal')
def animal():
    return "Fun Animal Facts!"

