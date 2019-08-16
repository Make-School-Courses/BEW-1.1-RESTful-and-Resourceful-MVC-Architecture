---
title:  Intro to Flask
---

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
  -
-->


<!-- .slide: data-background="./header.svg" data-background-repeat="none" data-background-size="45% 45%" data-background-position="center 10%" -->
# Intro to Flask

---

## 🏆 Learning Objectives

1. Define what a web server is and what role it plays on the internet
2. Describe what the Flask framework is and how to use it
3. Differentiate between frontend and backend stacks
4. Understand how Python works into HTML/CSS

---

## 📖 Overview

<!--
- TT: overview of how we learned basic frontend, but how do we drive it forward? What about data?
- TT: Overview of Flask: what it is, why we use it
-->

---

## Python Packages

### Installing the Flask Framework

In your terminal, type:

```bash
pip3 install flask
```

---

### What just happened?

- `pip3`: Python Installs Packages
- We just installed the Flask package
- Now we can use Flask code in our code!

---

### Adding a Python Function to the Project

<!-- TT: Review of Python, you all were introduced to this via prework -->
<!-- Activity: some easy interview problem to solve in Python to get them warmed up again -->

#### Step by Step

--

Create a file named `app.py`:

 ```bash
 touch app.py
 ```

--

## In Class Activity I (25 min)

### Think / Pair / Share

- **Think**: Pseudocode a function that increments a counter every time someone calls the function.
- **Pair**: When you're done, pair program it!
- **Share**: After coding it up, compare your solution with the team next to you.

---

## Activity I Solution (5 min)

```python
hits = 0

def hit_counter():
    """Returns a count of how many times this function was called."""
    hits += 1
    return hits
```

---

### Endpoints Connect a Function to the Web

<!-- TT: Python is our backend (what’s a backend?) HTML/CSS is our frontend (what’s a frontend?) -->

#### Step by Step

--

Add flask imports:

 ```python
 from flask import Flask

hits = 0

 def hit_counter():
    """Returns a count of how many times this function was called."""
    hits += 1
    return hits
 ```

--

Define `app` variable:

 ```python
 from flask import Flask

 app = Flask(__name__)


hits = 0

 def hit_counter():
    """Returns a count of how many times this function was called."""
    hits += 1
    return hits
 ```

--

Add `@app.route` to the top of the function definition and explain that this **decorator** on top of the function makes it an **endpoint**:

 ```python
 from flask import Flask

 app = Flask(__name__)

 hits = 0

 @app.route("/")
 def hit_counter():
    """Returns a count of how many times this function was called."""
    hits += 1
    return hits
 ```

--

Last, define `__main__`:


 ```python
 from flask import Flask

 app = Flask(__name__)


 hits = 0

 @app.route("/")
 def hit_counter():
    """Returns a count of how many times this function was called."""
    hits += 1
    return hits

 if __name__ == "__main__":
     app.run(debug=True)
```

--

Test the function by running `flask run` on the terminal:

```bash
flask run
```

---

### Making A Static Site Dynamic

#### Step by Step

1. Demo the static site in the browser by double clicking the `index.html` file in Finder and opening it in the browser
2. Explain that we'll be making this static site dynamic today using Python and Flask
3. Note that the URL in the browser begins with `file:///` instead of `http://`
4. Explain why static HTML and CSS  goes in the `static` folder
5. Run `flask run` in the project directory to serve the static HTML page via Flask at `http://localhost:8000/index.html`

---

### Stretch Challenges

1. What is `__name__`? What does it do in `app.py`?
2. What flag allows you to reload flask every time you make a change to `app.py`?
3. Currently, the number of hits resets back to `0` when we run `flask run`
      1. Why does this happen?
      2. Can you use what you learned about MongoDB to fix it?

---

## 💻 Activity

- Activity: first 2 chapters of this tutorial

---

## 🌴 [10m] Break


## 🌃 After Class

### Homework

Create a design or outline for a simple gif search site that returns a list of gifs from the [Tenor API](https://tenor.com/gifapi/documentation). You should be able to type out a search term, and have gifs that match that search term returned back to your application and displayed.

---

## 📚 Resources & Credits

- https://blog.codeanalogies.com/2018/04/26/web-servers-explained-by-running-a-microbrewery/
- https://en.wikipedia.org/wiki/Flask_(web_framework)
- https://github.com/pallets/flask
- https://flask.palletsprojects.com/en/1.1.x/
