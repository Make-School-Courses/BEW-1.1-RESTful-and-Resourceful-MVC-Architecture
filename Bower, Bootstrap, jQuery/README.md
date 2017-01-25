## Bower, Bootstrap, jQuery

### Challenges

#### Installing

1. Finish the [Static Files](http://expressjs.com/en/starter/static-files.html) tutorial in the express app so you have a `public` folder.
1. Install bower `$ npm install -g bower`
1. `$ touch` a bower configuration file called `.bowerrc`
  ```
    { 'directory': 'public/vendor' }
  ```
1. Use bower to install jquery and bootstrap.
1. Add jquery and bootstrap to your `<head>` in your `main.handlebars` layout template.

#### Bootstrap

1. Add a [bootstrap navbar](http://getbootstrap.com/components/#navbar) to your `main` layout.
1. Use bootstrap's 12-column grid (optionally watch [this video explanation](https://www.youtube.com/watch?v=g3j7eRunzv4))). Add a `.container` class below the navbar.

#### posts-index

1. Create a `/posts` route that displays an array of posts
  ```
    [
      { body: "the stuff" },
      { body: "the stuff" },
      { body: "the stuff" }
    ]
  ```
1. Put those posts into a `.list-group` bootstrap element inside the middle six columns of the 12 column grid.
1. Add a post form like the following:
  ```
    <form action='#' id='post-form'>
      <textarea name="body" class="form-control"/>
      <div class='text-right'>
        <button type='submit'>Save</button>
      </div>
    </form>
  ```
1. Create a file: `public/scripts.js`
1. In this file use the jQuery function that detects a [submit event](https://api.jquery.com/submit/). (hint: remember to prevent the default behavior of the form upon submit).
1. Use the jQuery `serialize()` function to serialize the form data into a JavaScript object called `post`.
1. Write the post to the page to the top of the `.list-group` using the jQuery `text()`.


<!--
#### Create a post
1. Use the jQuery `ajax()` function to make a asynchronous post requests to your server to send the `post` object to the `/posts` webhook. -->
