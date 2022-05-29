from flask import Flask, render_template # 1 add render_template

app = Flask(__name__)

# for loops
# posts = [{"author": "Don",
#         "title": "Wow",
#         "content": "Animal fun facts",
#         "date_posted": "April 1, 2019"},
#         {"author": "Nard",
#         "title": "Wew",
#         "content": "Animal fun facts",
#         "date_posted": "April 2, 2019"}
# ]

# for exercise module 2
characters = [{"name": "Arthurius",
              "power": "Telepathy",
              "weapon":"Sword",
              "description": """Really smart but grades are pretty low, which is surprising because he should be able 
              to read his professor's during a test. Maybe he chooses not to. He's also super-friendly and kind."""},
              {"name": "Fantasia",
              "power": "Telekinesis",
              "weapon":"Crossbow",
              "description": """Shy and likes to play with talking racoons."""},
              {"name": "Obsidian",
              "power": "Invisibility",
              "weapon":"Spear",
              "description": """No one knows for sure who is Obsidian really is. This boy just popped out out of nowhere 
              one day. Many people suspect that he's always been around, silently staring at everyone."""}
]

# @app.route('/')
# @app.route('/home')
# def home():
#     return "Hello World" # 2 add render template with link to html file

# for loops
# @app.route('/animal')
# def animal():
#     return render_template('animal.html', posts=posts)

# if statements
# @app.route('/animal')
# def animal():
#     return render_template('animal.html', posts=posts, title = "Fun Animal Facts") # 3 add title
#

# for characters
@app.route('/character')
def character():
    return render_template("character.html", characters=characters)

# if __name__ == "__main__":
#     app.run()
