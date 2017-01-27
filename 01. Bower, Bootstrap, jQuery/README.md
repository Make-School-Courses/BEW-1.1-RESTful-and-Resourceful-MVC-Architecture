## Bower, Bootstrap, jQuery

Bower is a package manager (like homebrew for Mac, and npm for node) that helps you manage front end packages. Let's use it to add Boostrap 3 and jQuery to your template. Bower is one type of front end "build system" for managing front end packages. There are many others you will encounter, but Bower is one of the most popular and simple.

### Challenges

#### Static Files

1. Finish the [Static Files](http://expressjs.com/en/starter/static-files.html) tutorial in the express app so you have a `public` folder.

#### Installing and Initializing Bower

1. Install bower `$ npm install -g bower`
1. `$ touch` a bower configuration file called `.bowerrc`. We're going to tell bower to put all files into a vendor folder inside our public folder.

  ```js
    { "directory": "public/vendor" }
  ```
1. Run `$ bower init` to initialize bower and have it create a `bower.json` file.
1. Use bower to install jquery and bootstrap. (Hint: always add `--save` to make sure that the package is added to your `bower.json` file and will be available in production)
1. Add jquery and bootstrap to your `<head>` in your `main.handlebars` layout template. e.g.

  ```html
    <link rel="stylesheet" href="/vendor/bootstrap/dist/css/bootstrap.min.css">
    <script type="text/javascript" href="/vendor/bootstrap/dist/js/bootstrap.min.js"></script>
  ```

#### Bootstrap

1. Add a [bootstrap navbar](http://getbootstrap.com/components/#navbar) to your `main` layout.
1. Use bootstrap's 12-column grid (optionally watch [this video explanation](https://www.youtube.com/watch?v=g3j7eRunzv4))). Add a `.container` class below the navbar.
1. Embed a responsive image into your grid.
1. Embed a responsive youtube video into your grid.

#### posts-index

You can pass data into your templates by passing the data as the second argument to the `res.render()` function. e.g. `res.render('posts-index', posts)`.

1. Create a `/posts` route that displays an array of posts

  ```json
    [
      { body: "the stuff" },
      { body: "the stuff" },
      { body: "the stuff" }
    ]
  ```

1. Put those posts into a `.list-group` bootstrap element inside the middle six columns of the 12 column grid. (hint: use the handlebars each method)

  ```html
    <h1>Comments</h1>

    <div id="comments">
      {{#each comments}}
      <h2><a href="/posts/{{../permalink}}#{{id}}">{{title}}</a></h2>
      <div>{{body}}</div>
      {{/each}}
    </div>
  ```

1. Add a post form like the following:

  ```html
    <form action='#' id='post-form'>
      <textarea name="body" class="form-control"/>
      <div class='text-right'>
        <button type='submit'>Save</button>
      </div>
    </form>
  ```

1. Create a file: `public/scripts.js` and link it in your `<head>` after jQuery (so you can use jQuery in your scripts).
1. In this file use the jQuery function that detects a [submit event](https://api.jquery.com/submit/). (hint: remember to prevent the default behavior of the form upon submit).
1. Use the jQuery `serialize()` function to serialize the form data into a JavaScript object called `post`.
1. Write the post to the page to the top of the `.list-group` using the jQuery `text()` or `html()` functions.

#### jQuery
1. In your navbar, add links to "login" and "signup" but have them do nothing (hint: `href="#"`).
1. Use a jQuery function to make something show or hide on the page when you click a button called `Show!` and `Hide!`
1. Now make the element fade in and out instead.
1. Use a jQuery function to add or remove the `text-success` class to an element when you click a button called `Success!`.
1. Add the [jQuery validate](https://jqueryvalidation.org/) plugin and validate that the body of the post exists before you can submit the form.

#### Next up... MongoDB!
