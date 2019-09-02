from flask import Flask, request
from random import choice, sample

app = Flask(__name__)

compliments = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/compliment'>
        <p>
            What is your name?
            <input type="text" name="name"/>
        </p>
        <p>
            <input type="checkbox" name="show_compliments"/>
            Show Compliments
        </p>
        <p>
            How many compliments?
            <select name="num_compliments">
                <option value="1">One</option>
                <option value="2">Two</option>
                <option value="3">Three</option>
            </select>
        </p>
        <input type="submit">
    </form>
    """

@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    num_compliments = int(request.args.get('num_compliments'))
    should_show_compliments = request.args.get('show_compliments')
    compliments_to_show = ', '.join(sample(compliments, num_compliments))

    if should_show_compliments:
        return f'Hello there, {name}! You are so {compliments_to_show}!'
    else:
        return f'Hello there, {name}! Have a nice day!'
