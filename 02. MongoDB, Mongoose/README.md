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

#### Display posts using Post model

1. In your `/posts` GET webhook find your posts from your database using the `Post` model.([documentation here](http://mongoosejs.com/docs/queries.html)). Return those to your `posts-index` view.

#### Save posts using Post model
1. In your `scripts.js` file, use the jQuery `ajax()` function to make a asynchronous post requests to your server to send the `post` object to the `/posts` POST webhook.
1. In your `/posts` route use your Post model to create new post. e.g.
  ```js
    var small = new Tank({ size: 'small' });
    small.save(function (err) {
      if (err) return handleError(err);
      // saved!
    })
  ```
