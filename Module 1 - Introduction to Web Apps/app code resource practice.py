from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"
@app.route('/animal')
def animal():
    return """
    <h1>Fun Animal Facts!</h1>
    <p>Pet Facts
94% of pet owners say their animal pal makes them smile more than once a day.
The American Veterinary Dental Society states that 80% of Dogs and 70% of cats show signs of oral disease by age 3.




Cat Facts
Cats have 32 muscles in each ear.
Cats have 4 rows of whiskers.
Cats have no collarbone, which is one reason they are so flexible.
Cats spend approximately 30% of their waking hours grooming themselves.
 “American Shorthair” is the designation reserved for pedigreed cats, while similar-looking cats of mixed or unknown origin are called “domestic shorthairs.”
Feline’s jaws cannot move sideways.
Cats have over one hundred vocal sounds, while dogs have about ten!
Cat whiskers are so sensitive they can detect the slightest change in air current.
Cats have 26 baby teeth and 30 permanent teeth.</p>"""

