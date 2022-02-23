"""A madlib game that compliments its users."""

import random

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

    compliments = random.sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route("/game")
def show_madlib_form():

    response = request.args.get("wants_to_play")

    if response == "yes":
        return render_template("game.html")
    elif response == "no":
        return render_template("goodbye.html")

@app.route("/madlib", methods=["POST"])
def show_madlib():

    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjectives_list = request.form.getlist("adjectives")
    person2 = request.form.get("person2")
    noun2 = request.form.get("noun2")
    adj2 = request.form.get("adjective2")
    ending = request.form.get("wants ending")

    #if len(adjectives_list) == 1:
       #adjectives = adjectives_list[0]
    #elif len(adjectives_list) == 2:
        #str adjectives is equal to list at index 0, space, and, space, list at index 1.
    #else:
        #str adjecitves is equal to each item in list except the last one separated by commas and spaces, the word and, the last one

    if len(adjectives_list) == 1:
        adjectives = adjectives_list[0]
    elif len(adjectives_list) == 2:
        adjectives = f"{adjectives_list[0]} and {adjectives_list[1]}"
    else: 
        adjectives = ", ".join(adjectives_list[:-1])
        adjectives = adjectives + " and " + adjectives_list[-1]

    madlib_options = ["madlib.html", "madlib2.html", "madlib3.html"]

    random_madlib = random.choice(madlib_options)

    return render_template(random_madlib, 
                            person=person, 
                            color=color, 
                            noun=noun, 
                            adjectives=adjectives,
                            person2=person2,
                            noun2=noun2,
                            adj2=adj2,
                            ending=ending)

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
