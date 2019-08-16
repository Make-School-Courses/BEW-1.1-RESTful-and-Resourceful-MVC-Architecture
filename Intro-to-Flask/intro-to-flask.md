# 📜 Day 7: Introduction to Web Servers in Flask

<!--
What students know so far...

Week 1
    1. [BEW] Static website (static HTML/basic CSS, chrome inspector)
    2. [BEW] Git & GitHub
    3. [CS] Variables, Functions, and Program Design
    4. [CS] Control Flow and Lists
Week 2
    1. [CS] Pseudocode and Flowchart Diagrams
    2. [BEW] Request-Response Cycle and MVC Architecture


TODO: Flask Starter Pack with pre-built static front end

TODO: Questions for Alan:
  - Will they know how to import Python packages by Day 7?
  - Will they know virtual environments? Should they yet?
  -
-->

### ⏱ Agenda

1. [🏆 Learning Objectives](#%f0%9f%8f%86-learning-objectives)
2. [📖 Overview](#%f0%9f%93%96-overview)
3. [💻 Activity](#%f0%9f%92%bb-activity)
4. [🌴 [10m] Break](#%f0%9f%8c%b4-10m-break)
5. [🌃 After Class](#%f0%9f%8c%83-after-class)
6. [📚 Resources & Credits](#%f0%9f%93%9a-resources--credits)

## 🏆 Learning Objectives

1. Define what a web server is and what role it plays on the internet
1. Describe what the Flask framework is and how to use it
1. Differentiate between frontend and backend stacks
1. Understand how Python works into HTML/CSS

## 📖 Overview

<!--
- TT: overview of how we learned basic frontend, but how do we drive it forward? What about data?
- TT: Overview of Flask: what it is, why we use it
-->

### Making A Static Site Dynamic

#### Step by Step

1. Demo the static site in the browser by double clicking the `index.html` file in Finder and opening it in the browser
2. Explain that we'll be making this static site dynamic today using Python and Flask
3. Note that the URL in the browser begins with `file:///` instead of `http://`
4. Explain why static HTML and CSS  goes in the `static` folder
5. Run `flask run` in the project directory to serve the static HTML page via Flask at `http://localhost:8000/index.html`

### Adding a Python Function to the Project

<!-- TT: Review of Python, you all were introduced to this via prework -->
<!-- Activity: some easy interview problem to solve in Python to get them warmed up again -->

#### Step by Step

1. Create a file named `app.py` and explain that this is where the code will live

    ```bash
    touch app.py
    ```

2. Ask students to open `app.py` in their editor

3. **Activity**: Think / Pair / Share: Pair program a function that increments a counter every time someone calls the function.

   **Solution**:

      ```python
      hits = 0

      def hit_counter():
          """Returns a count of how many times this function was called."""
          hits += 1
          return hits
      ```

### Endpoints: How to Call a Function on the Web

<!-- TT: Python is our backend (what’s a backend?) HTML/CSS is our frontend (what’s a frontend?) -->

#### Step by Step

1. Add flask imports:

    ```python
    from flask import Flask


    def function():
        return 'hi'
    ```

2. Define `app` variable:

    ```python
    from flask import Flask

    app = Flask(__name__)


    def function():
        return 'hi'
    ```

3. Add `@app.route` to the top of the function definition and explain that this **decorator** on top of the function makes it an **endpoint**:

    ```python
    from flask import Flask

    app = Flask(__name__)


    @app.route("/")
    def function():
        return 'hi'
    ```

4. Last, define `__main__`:

    ```python
    from flask import Flask

    app = Flask(__name__)


    @app.route("/")
    def function():
        return 'hi'


    if __name__ == "__main__":
        app.run(debug=True)
    ```

5. Demo the function by running `flask run` on the terminal:

    ```bash
    flask run
    ```

### Stretch Challenges

1. What is `__name__`? What does it do in `app.py`?
2. What flag allows you to reload flask every time you make a change to `app.py`?
3. Currently, the number of hits resets back to `0` when we run `flask run`
      1. Why does this happen?
      2. Can you use what you learned about MongoDB to fix it?

<!--
## 💻 Activity

- Activity: first 2 chapters of this tutorial

## 🌴 [10m] Break
 -->

## 🌃 After Class


HW: create a design/outline for a simple Gif search site that returns a list of gifs from the Tenor API based off of a search query


## 📚 Resources & Credits

- https://blog.codeanalogies.com/2018/04/26/web-servers-explained-by-running-a-microbrewery/
- https://en.wikipedia.org/wiki/Flask_(web_framework)
- https://github.com/pallets/flask
- https://flask.palletsprojects.com/en/1.1.x/
