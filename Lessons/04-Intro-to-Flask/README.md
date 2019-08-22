---
title:  Intro to Flask
author: Dani Roxberry <dani@makeschool.com>
---

<!-- Run this slideshow via the following command: -->
<!-- reveal-md README.md -w --css=makeschool.css -->


<!-- .slide: data-background="./header.svg" data-background-repeat="none" data-background-size="40% 40%" data-background-position="center 10%" -->
# Intro to Flask

### BEW 1.1 / Day 7

---

### Agenda

1. [**[5m]** Learning Objectives](#5m-learning-objectives)
2. [**[25m]** TT: Welcome to Web Servers](#25m-tt-welcome-to-web-servers)
3. [**[5m]** Recap](#5m-recap)
4. [**[10m]** Break](#10m-break)
5. [**[45m]** Guided Activity](#45m-guided-activity)
6. [**[15m]** TT: Flask + Function = Website](#15m-tt-flask--function--website)
7. [**[5m]** After Class](#5m-after-class)

---

## **[5m]** Learning Objectives

1. Define **what a web server is** and **how it relates to the backend**.
2. Describe **what the Flask framework is** and **how to use it**.
3. Use what you've learned in CS and BEW classes thus far to **build and run your first Python server** implemented in Flask.

---

<!-- .slide: data-background="./header.svg" data-background-repeat="none" data-background-size="40% 40%" data-background-position="center 10%" -->
# Introducting Flask

## **[25m]** TT: Welcome to Web Servers

--

### What is Flask?

- Flask is an **add-on**, or **package**, written in Python
- **Adds the power of HTTP** to your existing Python installation
- Very lightweight; **known as a [microframework]**
- **[Free & Open Source Software](https://en.wikipedia.org/wiki/Free_and_open-source_software)**: check out the code on [GitHub](https://github.com/pallets/flask)

--

### Who uses Flask?

- Companies of all sizes (Google, Affirm, etc)
- Programmers working small/medium sided projects
- RESTful API creators and maintainers
- Data Engineers / Data Scientists
- Startups during the MVP phase

--

### How do I install it?

Open `Terminal.app`, and type the following command:

```bash
$ pip3 install flask
```

**PROTIP**: The `$` in front is a common paradigm that informs the programmer to execute the command in a terminal. Be sure not to type it out!

--

### Did I do it right?

You'll see output that looks like this:

```bash
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020.
Collecting flask
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
    100% |████████████████████████████████| 102kB 1.2MB/s
Collecting itsdangerous>=0.24 (from flask)
  Using cached https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from flask)
  Downloading https://files.pythonhosted.org/packages/d1/ab/d3bed6b92042622d24decc7aadc8877badf18aeca1571045840ad4956d3f/Werkzeug-0.15.5-py2.py3-none-any.whl (328kB)
    100% |████████████████████████████████| 337kB 6.3MB/s
Collecting click>=5.1 (from flask)
  Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1 (from flask)
  Using cached https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask)
  Using cached https://files.pythonhosted.org/packages/6d/d2/0ccd2c0e2cd93b35e765d9b3205cd6602e6b202b522fc7997531353715b3/MarkupSafe-1.1.1-cp27-cp27m-macosx_10_6_intel.whl
Installing collected packages: itsdangerous, Werkzeug, click, MarkupSafe, Jinja2, flask
Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.5 click-7.0 flask-1.1.1 itsdangerous-1.1.0
```

--

### How can I check?

Use the next **5 minutes** to:

  - **Compare** output from the previous slide with yours.

  - **Verify** that Flask installed correctly with everyone at your table.

  - **Escalate any errors _(text in <span style="color:red;">RED</span>)_ by raising your hand and informing the instructor or a TA.**

--

### So, what just happened?

- **What is `pip3`**?
    - Stands for _**P**ython **I**nstalls **P**ackages_
    - Included when you install Python

- **Running `pip3 install packagename` invokes**:
    - **STEP 1**: Searches PyPI for the latest `packagename` package
    - **STEP 2**: Downloads the package's latest codebase and store it in a temporary directory
    - **STEP 3**: Installs the `packagename` codebase in a special Python directory

--

## **[5m]** Recap

### Review

- Flask is a **popular microframework**, written in Python.
- It allows us to **create a server** with very little code.
- We can **install Flask**, or any other Python package(s) **using `pip3`**.

### Integrate

Today, we'll use our knowledge from prior classes to guide us:

| BEW 1.1                | CS 1.1                |
| ---------------------- | --------------------- |
| Git & GitHub           | Variables & Functions |
| Request-Response Cycle | Pseudocode            |

---

## **[10m]** Break

---

## **[45m]** Guided Activity

### Designing a Hit Counter

--

### Getting Started (5m)

**1**. Create a file named `app.py`:

 ```bash
 touch app.py
 ```

This `bash` command creates a blank file named `app.py` in your working directory.

**2**. Open `app.py` in your favorite editor.

```bash
atom app.py
```

You'll **write all your code inside `app.py`** --- for now!

--

### Think / Pair / Share (25m)

- **THINK**: Pseudocode a function that increments a counter each time it's called.
    - **PROTIP**: **Pseudocode it on paper**, outside of your editor, first.

- **PAIR**: When you're done, **find a buddy** and **code it up!**

- **SHARE**: After writing the code:
    - **Compare your solution** with the team next to you.
    - **Test it out together**. Did it work?

<br>
_If you finish early, **commit your code**!_

--

### Solution (5m)

<br>

```python
hits = 0

def hit_counter():
    """Returns a count of how many times this function was called."""
    hits += 1
    return hits
```

---

## **[15m]** TT: Flask + Function = Website

- We're about to **create our first server**!
- Servers are the **most common form of backend**.

--

### Add Flask Imports

<br>

 ```python
from flask import Flask


hits = 0

def hit_counter():
  """Returns a count of how many times this function was called."""
  hits += 1
  return hits
 ```

--

### Define App Variable

Declare a variable named `app`, and instantiate the Flask class.

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

### Decorate the Function

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

### Declare The Entrypoint

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

### Prove it Works

Test the function by running `flask run` on the terminal:

```bash
$ flask run
```

---

### Stretch Challenges

1. What is `__name__`? What does it do in `app.py`?
2. What flag allows you to reload flask every time you make a change to `app.py`?
3. Currently, the number of hits resets back to `0` when we run `flask run`
      1. Why does this happen?
      2. Can you use what you learned about MongoDB to fix it?

---

## **[5m]** After Class

### Homework

**Create a request-response flow diagram for a minimalistic `.gif` search site that returns a list of `.gif`s from the [Tenor API](https://tenor.com/gifapi/documentation).**

Your diagram should show:

1. The ability to **type a search term into a search box** in a browser.
2. After hitting submit, the user should **receive `.gif`s that match the search term** returned and displayed.
3. Which endpoint(s) will be called during this process?
    1. **BONUS**: How can you call an endpoint using HTML?

--

### Example Deliverable

TODO
