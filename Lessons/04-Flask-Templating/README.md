
<!-- Run this slideshow via the following command: -->
<!-- reveal-md README.md -w -->


<!-- .slide: data-background="./header.svg" data-background-repeat="none" data-background-size="40% 40%" data-background-position="center 10%" class="header" -->
# Flask Templating with Jinja

### [Slides](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/Slides/04-Flask-Templating.html)

### [Demo](https://github.com/Make-School-Courses/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/tree/master/Lessons/04-Flask-Templating/demo)

<!-- > -->

## Agenda

1. Learning Objectives
1. Flask Review
1. Jinja Templates
1. Template Control Flow
1. Break
1. Template Inheritance
1. Activity: Horoscope App
1. Introducing Gif Search

<!-- > -->

## Learning Objectives

By the end of today, you should be able to:

1. Explain the uses of templates 
<!-- .element: class="fragment" data-fragment-index="1" -->
1. Render a Flask web page using a Jinja template
<!-- .element: class="fragment" data-fragment-index="2" -->
1. Use template control flow structures such as for loops & conditionals
<!-- .element: class="fragment" data-fragment-index="3" -->

<!-- > -->

# Review

<!-- v -->

## Discussion
#### (5 min)

With your partner, discuss:

- What is a web server?
- What is Flask, and what does it do?

<!-- v -->

## Our Project So Far

We defined two **routes**, one for the homepage `/` and one for the `/compliments` page. 

<!-- v -->

## Home Page Route

Our homepage route looks like this:

```python
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
```

What could we improve about this?

<!-- v -->

## Separate Concerns

There's HTML code in our Python file! Let's fix that.

<!-- > -->

# Jinja Templates

<!-- v -->

## What are Templates?

Templates are special HTML files that:

- Can use variables passed from your Flask route
- Can use some control structures (for loops, if/else)
- Can inherit from other templates to avoid repetition

<!-- v -->

## Add a Templates Folder

Put all of your template HTML files in a folder called `templates`.

```bash
my_project_directory/
    app.py
    templates/
        index.html
        compliments.html
```

<!-- v -->

## Add HTML to Template

Let's move the HTML code from the `/` route into its own `index.html` template. It should look like:

```html
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
```

<!-- v -->

## Render Template

At the top of `app.py`, import `render_template`:

```python
from flask import render_template
```

Then change our route to call the `render_template` function:

```python
@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')
```

<!-- v -->

## Check that it Works

Let's try running our server again!

```bash
$ flask run
```

<!-- > -->

# Passing Data

<!-- v -->

## Update the `/compliment` route

Let's do the same thing for `/compliment`! Here's our code so far. What do we need to change?

```python
@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliment = choice(compliments)

    if show_compliments:
        return f'Hello there, {name}! You are so {compliment}!'
    else:
        return f'Hello there, {name}! Have a nice day!'
```

<!-- v -->

## Render a Template

Let's change the `/compliment` route to render a template instead. This time, we need to pass in some data.

```python
@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliment = choice(compliments)

    return render_template(
        'compliments.html', 
        name=name, 
        show_compliments=show_compliments, 
        compliment=compliment)
```

<!-- v -->

## Write the Template

Create a new file in the `templates` folder, called `compliments.html`. 

Note that Jinja templates use a double curly bracket `{{ }}` to display variables or expressions.

```html
<p>
    Hello there, {{ name }}! You are so {{ compliment }}!
</p>
```

<!-- > -->

# Template Control Flow

<!-- v -->

## Conditionals

Let's add a conditional to `compliments.html` so that we will only show a compliment if the user checked 'Show Compliment'. 

In Jinja we use `{% %}` to indicate control structures.

```html
{% if show_compliments %}
    You are so {{ compliment }}!
{% else %}
    Have a nice day!
{% endif %}
```

<!-- v -->

## Passing a List of Compliments

Let's modify our route in `app.py` to pass in a list of compliments instead:

```python
from random import sample

...

@app.route('/compliment')
def get_compliment():
    """Give the user a compliment"""
    name = request.args.get('name')
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, 3)

    return render_template(
        'compliments.html', 
        name=name, 
        show_compliments=show_compliments, 
        compliments=compliments_to_show)
```

<!-- v -->

## Loops

I want my `compliments.html` file to look like:

```html
Hi user! You are so:
<ul>
    <li>brilliant</li>
    <li>smashing</li>
    <li>tenacious</li>
</ul>
```

<!-- v -->

## Loops

Now add a loop to `compliments.html`:

```html
{% if show_compliments %}
    You are so:
    <ul>
        {% for compliment in compliments %}
            <li>{{ compliment }}</li>
        {% endfor %}
    </ul>
{% else %}
    Have a nice day!
{% endif %}
```

<!-- > -->

## Break [10 minutes]
<!-- .slide: data-background="#087CB8" -->

<!-- > -->

# Template Inheritance

<!-- v -->

## Why Inherit Templates?

Most websites have some content that is the same for every web page:

- Header, footer
- Title, styles
- Etc.

We want to put that content in one place so that we can inherit it and avoid repeated code.

<!-- v -->

## Create `base.html`

Let's put another file, `base.html`, in our `templates` folder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
</html>
```

<!-- v -->

## Extend Base

Now we can **override** the `content` block in our child templates. Let's modify `compliments.html`:

```html
{% extends 'base.html' %}

{% block title %}
    Receive Compliments!
{% endblock %}

{% block content %}
    {% if show_compliments %}
        You are so:
        <ul>
            {% for compliment in compliments %}
                <li>{{ compliment }}</li>
            {% endfor %}
        </ul>
    {% else %}
        Have a nice day!
    {% endif %}
{% endblock %}
```

<!-- v -->

## Extend Base

And `index.html`:

```html
{% extends 'base.html' %}

{% block title %}
    Enter Your Info
{% endblock %}

{% block body %}
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
{% endblock %}
```

<!-- v -->

## Customize Compliments

I want to put the code for displaying a single compliment in its own HTML page. That way, I can include it in multiple places!

Make a file `compliment.html` in your `templates` folder:

```html
<li>{{ compliment }}</li>
```

<!-- v -->

## Include Compliment

Now, I can include this file in `compliments.html`:

```html
You are so:
<ul>
    {% for compliment in compliments %}
        {% include 'compliment.html' %}
    {% endfor %}
</ul>
```

<!-- > -->

# Activity

<!-- v -->

## Expand your Horoscope App

Modify your Horoscope app to use Jinja templates. Use the [starter code](https://github.com/Make-School-Courses/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/tree/master/Lessons/04-Flask-Templating/demo) as a guide!

<!-- > -->

# Gif Search

<!-- v -->

## Introducing the Gif Search Project

Demo

<!-- .slide: data-background="#0D4062" -->
## Homework

TODO


