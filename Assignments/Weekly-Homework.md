# BEW 1.1 Homework Assignments

Over the course of the 4 homework assignments, you will be making an application with 2 features: a "Fortune Teller" which gives a prediction based on user-entered data, and a weather app that tells you the weather in any given city.

## Homework 1

In your project directory, create a file called `fortune_form.html`. In it, create a form with **at least** 4 different kinds of form elements (e.g. text, number, radio button, drop-down, etc). These form elements should be asking the user various questions about themselves, which will be used to determine their fortune. (No need to actually do so now, though!)

Your form should have an `action` of `/fortune_results` and a `method` of `GET`.

You can open your HTML page in a new Chrome tab using "File -> Open". It now might look something like this:

![sample form](assets/fortune_form.png)

In your project directory, create a file called `README.md` and in it, answer the following questions:

1. What happens when you press the "submit" button? Paste the full URL you are sent to on submit. 
1. What are the *keys* of this URL query string? How do they correspond to the "name" fields of your HTML form elements?
1. What are the *values* of the URL query string? How do they correspond to what the user entered or typed?

Stretch challenge question:

1. Is there a way to pass multiple values through the URL query string for a single key? How can we do so?

## Homework 2

In your project directory, create a folder called `templates` and move your `fortune_form.html` inside of it. 

Create two new empty files, `index.html` and `fortune_results.html`, inside of your templates directory.

In your project's root directory, create a file called `app.py` and give it the following contents:

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')
```

Create a new routes after the index route to display your fortune teller form (at the URL '/fortune').

Update `index.html` to link to your two pages.

Now, create another route for the URL '/fortune_results'. In this route, create at least **four possible fortunes** based on the user's input from the form page. Display the user's fortune by passing it as a named parameter to the `fortune_results.html` template. Here is an example to get you started:

```py
@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = request.args.get('animal')
    # ... etc

    if users_favorite_animal == 'unicorn':
        # fortune is "You'll have a magical day!"
    elif condition2:
        # fortune is ...
    elif condition3:
        # fortune is ...
    else:
        # no other fortune applies, return default fortune
```

Feel free to get creative here!

Stretch challenges:

- Use the Python `random` library ([documentation](https://docs.python.org/3/library/random.html)) to introduce some randomness into your fortunes. For example, a user who likes cats might get either "Watch out for cattiness!" or "Have a purrfect day!" depending on their random result.
- Show the user a different image for each of your available fortunes.
- Add styling to your page, and change the styling based on the fortune result. (Hint: Apply a different CSS class to your page elements depending on the fortune.)

## Homework 3

## Homework 4

