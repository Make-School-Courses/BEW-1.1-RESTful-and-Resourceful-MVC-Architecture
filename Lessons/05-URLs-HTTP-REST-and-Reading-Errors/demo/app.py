import requests
from flask import Flask

app = Flask(__name__)

@app.route('/joke')
def make_joke():
    params = { "limitTo": "nerdy" }
    r = requests.get("http://api.icndb.com/jokes/random", params=params)
    joke_json = r.json()
    joke_str = joke_json["value"]["joke"]
    return joke_str