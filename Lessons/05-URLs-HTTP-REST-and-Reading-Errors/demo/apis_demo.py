import requests
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

params = { "limitTo": "nerdy" }
r = requests.get("http://api.icndb.com/jokes/random", params=params)
joke_json = r.json()
joke_str = joke_json["value"]["joke"]
pp.pprint(joke_json)