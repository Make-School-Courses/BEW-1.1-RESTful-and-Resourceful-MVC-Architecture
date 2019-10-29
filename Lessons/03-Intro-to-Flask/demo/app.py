
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return "Hello, World!"

@app.route('/user/<username>')
def say_hello_var(username):
    return 'Hi, ' + username

@app.route('/double/<int:the_number>')
def double(the_number):
    return str(the_number * 2)

@app.route('/search')
def search_page():
    name = request.args.get('name')
    category = request.args.get('category')
    return 'You searched for ' + name + ' in the category ' + category

@app.route('/search_form')
def search_form():
    return """
    <form action='/search'>
        Type in the product name: <input type='text' name='name'>
        <br>
        Type in the category: <input type='text' name='category'>
        <input type='submit'>
    </form>
    """