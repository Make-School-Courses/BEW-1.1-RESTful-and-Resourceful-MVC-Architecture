## MongoDB, Mongoose

MongoDB is an extremely popular NoSQL or "Document-based" database. Mongoose is a ODM (object document mapping) express middleware that makes it easier to interact with a MongoDB database. It lets you create and validate attributes and create model and instance methods and many other common OXM features.

### Challenges

#### Installing

1. Follow [these instructions](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/) to install mongodb onto your Mac.
1. Follow [these instructions](http://mongoosejs.com/docs/) to add Mongoose to your project.

#### Model

1. Create a file: `models/post.js` and use this boilerplate code to make your model.

  ```js
    var mongoose = require('mongoose')
    var Schema = mongoose.Schema;

    var CommentSchema = new Schema({
        createdAt     : { type: Date }
      , updatedAt     : { type: Date }

      , body   : { type: String, required: true }
    })

    // SET createdAt and updatedAt
    CommentSchema.pre('save', function(next) {
      now = new Date();
      this.updatedAt = now;
      if ( !this.createdAt ) {
        this.createdAt = now;
      }
      next();
    });

    var Comment = mongoose.model('Comment', CommentSchema);

    module.exports = Comment;
  ```

1. Require your `Post` model into your server file. (e.g. `Monkey = require('../models/monkey.js')`)

#### Display posts using Post model

1. In your `/posts` GET webhook find your posts from your database using the `Post` model.([documentation here](http://mongoosejs.com/docs/queries.html)). Return those to your `posts-index` view.

#### Save posts using Post model

1. In your `scripts.js` file, use the jQuery `ajax()` function to make a asynchronous post requests to your server to send the `post` object to the `/posts` POST webhook.
1. In order to access the form data with `req.body`, you will need to add the express middleware [body-parser](https://www.npmjs.com/package/body-parser) ([req.body in express docs](https://expressjs.com/en/api.html#req.body))
1. In your `/posts` route use your Post model to create new post. e.g.
  ```js
    var tank = new Tank(req.body);
    tank.save(function (err) {
      if (err) return handleError(err);
      // saved!
      res.send(tank);
    })
  ```

#### CRUD Challenges

1. Reverse the order you render the posts using the `.sort()` function. ([Mongoose Query docs](http://mongoosejs.com/docs/queries.html)). (hint: you'll need to use the `.exec()` function at the end of a chain of mongoose query functions in order to "execute" the function and return your objects).
1. Create a `post-show` route at `/posts/:id` route and render a template called `post-show`.
1. Create a route to edit a post. What should your path and template be named? Add a form and detect the submit event on that form.
1. Create an update post route, so your edit can submit, save to the db, and upon a successful response, redirect to the post-show route.
