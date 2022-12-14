"""A madlib game that compliments its users."""

from random import choice
from random import sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("homepage.html")


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliments = sample(AWESOMENESS, 3)
    return render_template("compliment.html", person=player, compliments = compliments)

@app.route("/game")
def show_madlib_form():
    """Respond to user desire to play game."""

    answer = request.args.get("game_answer")
    player = request.args.get("person")

    if answer == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html", person=player)

@app.route("/madlib")
def show_madlib():

    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    color = request.args.get("color")
    person_name = request.args.get("person_name")

    return render_template("madlib.html", noun=noun, adjective=adjective, color=color, person_name=person_name)
    
if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
