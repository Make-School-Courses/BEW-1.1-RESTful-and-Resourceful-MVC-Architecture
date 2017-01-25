## MongoDB, Mongoose

### Challenges

#### Installing

1. Follow [these instructions](http://mongoosejs.com/docs/) to add Mongoose to your project.

#### Model

1. Create a file: `models/post.js` and use this boilerplate code to make your model.

  ```js
    var mongoose = require('mongoose')
    var Schema = mongoose.Schema;

    var PostSchema = new Schema({
        createdAt     : { type: Date }
      , updatedAt     : { type: Date }

      , body   : { type: String, required: true }
    })

    // SET createdAt and updatedAt
    PostSchema.pre('save', function(next) {
      now = new Date();
      this.updatedAt = now;
      if ( !this.createdAt ) {
        this.createdAt = now;
      }
      next();
    });

    var Post = mongoose.model('Post', PostSchema);

    module.exports = Post;
  ```
1. Require your `Post` model into your server file. e.g. `Post = require('../models/post.js')`
1.

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

#### Create a post
1. In your `scripts.js` file, use the jQuery `ajax()` function to make a asynchronous post requests to your server to send the `post` object to the `/posts` POST webhook.
1. In your `/posts` route use your Post model to create new post. e.g.
  ```js
    var small = new Tank({ size: 'small' });
    small.save(function (err) {
      if (err) return handleError(err);
      // saved!
    })
  ```

#### Display posts

1. In your `/posts` GET webhook find your posts from your database using the `Post` model.([documentation here](http://mongoosejs.com/docs/queries.html)). Return those to your `posts-index` view.
