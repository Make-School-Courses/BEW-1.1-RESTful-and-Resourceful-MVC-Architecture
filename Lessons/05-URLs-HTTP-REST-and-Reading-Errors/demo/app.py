from flask import Flask, request

app = Flask(__name__)

@app.route('/color')
def fav_color():
    return """
    <form action="/color_result">
    What is your favorite color? <input type="text" name="color">
    <br>
    <input type="submit">
    </form>
    """

@app.route('/color_result')
def fav_color_result():
    fav_color = request.args.get('color')
    return "Your favorite color is " + fav_color


if __name__ == "__main__":
    app.run(debug=True)
