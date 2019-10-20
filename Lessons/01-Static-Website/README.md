
<!-- .slide: data-background="./../Images/header.svg" data-background-repeat="none" data-background-size="40% 40%" data-background-position="center 10%" class="header" -->
# Static Websites

[Slides](https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/Slides/01-Static-Website/README.html)


<!-- > -->

## Agenda

1. Learning Outcomes
1. Overview of HTML tags
1. Overview of CSS selectors
1. Activity: Create an HTML/CSS resume for a fictional character
1. How to "hack" a website with Developer Tools

<!-- > -->

## Learning Outcomes

By the end of today, you should be able to…

1. Recognize the most common HTML tags and their standard formatting
1. Recognize the most common CSS properties
1. Make a static web page using HTML & CSS
1. Use a browser’s developer tools to examine and change the HTML & CSS of a website.

<!-- > -->

# Warm Up

#### (5 minutes)

<!-- v -->

## Think, Pair, Share

I have an idea of how I want my website to look. What are the steps I need to take to make it a reality?

<!-- > -->

# HTML Essentials

<!-- v -->

## What is HTML?

- **H**yper**T**ext **M**arkup **L**anguage
  - Not a programming language! No loops, conditionals, etc
- Tells your browser how to structure content (text, images, links, etc)

<!-- v -->

## Elements

The fundamental building block of HTML is an **element**.
  - Can have an opening and closing tag
  - Or only a single tag

Tags are enclosed in angle brackets ( `<` and `>` )

<!-- v -->

## The Document Type Declaration

At the top of every HTML page, we need to tell the browser what type of markup to expect.

```html
<!DOCTYPE html>
```

- The **doctype** tag is technically not an element.

<!-- v -->

## The `html` element

All page content must go inside of the `html` start/close tags.

```html
<!DOCTYPE html>
<html>
</html>
```

<!-- v -->

## The `head` element

Content that doesn't directly relate to the way the page is laid out - including the styles and title - go inside of the `head` element.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My Awesome Page Title</title>
    </head>
</html>
```

<!-- v -->

## The `body` element

The body contains all of the elements that will be displayed on the page itself.

```html
<!DOCTYPE html>
<html>
    <head>
        ...
    </head>
    <body>
        This will appear on the page.
    </body>
</html>
```

<!-- v -->

## Demo

Let's put it all together! Save the code snippet below and open it in your browser.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>My First Web Page</title>
    </head>
    <body>
        Hello, World!
    </body>
</html>
```

<!-- > -->

# HTML Page Elements

<!-- v -->

## Semantic HTML

Semantic HTML tags add **meaning** to a web page, rather than just specifying how the page is laid out.

This is helpful because:
- Screen readers can more easily translate the page
- Code is easier to read and understand
- Code is more organized and and reusable

<!-- v -->

## Header Tags

Headers are used to set apart page, section, etc. headers.

`h1` is a top level heading. We can use `h1` to `h6` for different sized headers.

```html
<body>
    <h1>Why Dogs are Cool</h1>
    <p>Dogs are cool because...</p>
</body>
```

<!-- v -->

## Paragraph Tags

The paragraph tag `<p>` is used to indicate a paragraph of text.

```html
<body>
    <h1>Why Dogs are Cool</h1>
    <p>Dogs are cool because...</p>
</body>
```

<!-- v -->

## The Address Tag

The address, or `<a>` tag, links to another web page.

- `href` is an **attribute** that indicates the destination.

```html
<a href="http://www.aspca.org">Adopt a Dog!</a>
```

<!-- v -->

## The Image Tag

The `img` element is a **self-closing tag**. We often end it with `/` to indicate such.

- Images must also have an **alt** attribute which describes the image in text.

```html
<img src="http://makeschool.com/images/dog" alt="cute dog" />
```

<!-- v -->

## Line Breaks

We can add a **line break** like so:

```html
<br />
```

<!-- v -->

## Bold and Italics

We can specify that text should be **bold** with the `strong` tag, or *italic* with the `em` (emphasize) tag.

```html
<p>
    Dogs are <strong>fluffy</strong> and <em>playful</em>.
</p>
```

<!-- v -->

## List Items - Unordered

We can make a bulleted **unordered list** with the `ul` tag, and add list items with the `li` tag.

```html
<p>
    I like dogs because they are...
    <ul>
        <li>fluffy</li>
        <li>playful</li>
    </ul>
</p>
```

<!-- v -->

## List Items - Ordered

We can also make an **ordered list**, starting from 1, with the `ol` tag.

```html
<p>
    My favorite dogs (in order) are:
    <ol>
        <li>Husky</li>
        <li>Chocolate Lab</li>
        <li>Shiba Inu</li>
        <li>Golden Doodle</li>
    </ol>
</p>
```

<!-- > -->

# Pop Quiz!

<!-- v -->

## What does this do?

```html
<a href="http://www.facebook.com">Take me to Google!</a>
```

<!-- v -->

## What does this do?

```html
<img src="http://makeschool.com/images/logo.png" />
```

<!-- v -->

## What does this do?

```html
<ol>
    <li>One</li>
    <li>Two</li>
    <li>Three</li>
<ol>
```

<!-- > -->

## Break [10 minutes]
<!-- .slide: data-background="#087CB8" -->

<!-- > -->

# CSS Styles

<!-- v -->

## What is CSS?

- **C**ascading **S**tyle **S**heets
- Tells our browser what the HTML elements should look like
- If HTML is the bones of the webpage, CSS is the skin/clothing

--

## Adding Style Sheets

We can link in a .css file inside of the `head` element:

```html
<head>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
```

<!-- v -->

## Anatomy of a CSS Selector

```css
body {
    color: #333;
}
```

- Select the `body` tag
- Change the `color` **property**
- To the **value** of `#333` (light gray)

<!-- v -->

## CSS Combinators

Sometimes we want to match a nested element.

```css
section p {
    background-color: yellow;
}
```

This means "Match every `p` element that is a descendant of a `section` element."

<!-- v -->

## id Attribute

We can add a **unique** id to an element...

```html
<nav id="sidebar">...</nav>
```

...and select it:

```css
#sidebar {
    margin-left: 10px;
}
```

<!-- v -->

## class Attribute

We can also add a class name to an element...

```html
<article class="archived">...</article>
```

...and select it:

```css
.archived {
    border-color: #333;
}
```

<!-- v -->

## class/id Best Practices

- Use class/id sparingly if possible.
- Use class/id names that describe an element's **purpose** (what it does), not its **presentation** (how it looks).

Bad:
```html
<div class="red-bg">...</div>
```

Good:
```html
<div class="error-msg">...</div>
```

<!-- > -->

# Let's Make a Webpage

<!-- v -->

## Activity: Resume [25 minutes]

Make a resume for your favorite fictional character using HTML & CSS. Include their address, skills, experience, and achievements.

Check out http://w3schools.com for HTML & CSS documentation and examples.

<!-- > -->

# Hacking Websites with Developer Tools

<!-- v -->

## Demo

<!-- > -->
<!-- .slide: data-background="#087CB8" -->

## Homework

- Hack 2 websites
- Take screenshots and share in **#bew1-1-server-side-python** Slack Channel
- Be as creative as possible
