## Bower, Bootstrap, jQuery

### Challenges

#### Installing

1. Finish the [Static Files](http://expressjs.com/en/starter/static-files.html) tutorial in the express app so you have a `public` folder.
1. Install bower `$ npm install -g bower`
1. `$ touch` a bower configuration file called `.bowerrc`

  ```js
    { 'directory': 'public/vendor' }
  ```

1. Use bower to install jquery and bootstrap.
1. Add jquery and bootstrap to your `<head>` in your `main.handlebars` layout template.

#### Bootstrap

1. Add a [bootstrap navbar](http://getbootstrap.com/components/#navbar) to your `main` layout.
1. Use bootstrap's 12-column grid (optionally watch [this video explanation](https://www.youtube.com/watch?v=g3j7eRunzv4))). Add a `.container` class below the navbar.
1. Embed a responsive image into your grid.
1. Embed a responsive youtube video into your grid.

#### posts-index

1. Create a `/posts` route that displays an array of posts

  ```json
    [
      { body: "the stuff" },
      { body: "the stuff" },
      { body: "the stuff" }
    ]
  ```

1. Put those posts into a `.list-group` bootstrap element inside the middle six columns of the 12 column grid.
1. Add a post form like the following:

  ```html
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

### jQuery
1. Use a jQuery function to make something show or hide on the page when you click a button called `Show!` and `Hide!`
1. Now make the element fade in and out instead.
1. Use a jQuery function to add or remove the `text-success` class to an element when you click a button called `Success!`.
1. Add the [jQuery validate](https://jqueryvalidation.org/) plugin and validate that the body of the post exists before you can submit the form.
