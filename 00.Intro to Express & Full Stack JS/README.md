## Intro to Express & Full Stack JS

### Challenges

#### Installing

1. If you haven't, install [homebrew](http://brew.sh/)
1. Use homebrew to install node `$ brew install node`
1. Complete the Installing, Hello World, Basic Routing, and Static Files "Getting Started" tutorials in the [ExpressJS website](http://expressjs.com/).
1. Initialize a git repository and push to remote.
1. Initialize a heroku instance with `heroku create <<APP NAME>>` and push to heroku.
1. Run `$ heroku open` or navigate your browser to your heroku app to see that it is working.


#### req.params, req.send, req.json

Review [ExpressJS 4.x docs](https://expressjs.com/en/api.html) if you get stuck.

1. You are using `res.send` to send "Hello world". Instead send back "<h1>I'm Alive!</h1>". What happens in your browser?
1. Make a new webhook that takes a GET request at the path `/api/blahs` that uses `res.json` to send back this array:

  ```json
    [
      { name: "Blah"},
      { name: "Blah"},
      { name: "Blah"}
    ]
  ```

1. Make a new webhook that takes a GET request at the path `/greetings/:name`. Use `req.params.name` to return "<h1>Greetings, <<:name>></h1>" to the browser.


#### Templating Engine: Handlebars

Express does not ship with a templating engine for rendering HMTL templates. Instead you have to pick one. You could use Pug (aka Jade), or ejs, or many others. For this example we will use [Handlebars](http://handlebarsjs.com/) so we have a full featured engine but still get to practice our HTML.

1. Handlebars can be used for either client- or server-side rendering, but we are using it on the server-side only, so we'll use the `express-handlebars` node package. Use the installation and usage sections of the [repo's README](https://github.com/ericf/express-handlebars) to install this package into your project.
1. Make sure you have a `views` folder with a `home.handlebars` template and a `layouts` folder in it. And in the `layouts` folder, include a `main.handlebars` template. There is boilerplate code for the main layout template in the `express-handlebars` README.
1. Make your `/` route (root route) render your `home` template.


#### Up next... Bower!
