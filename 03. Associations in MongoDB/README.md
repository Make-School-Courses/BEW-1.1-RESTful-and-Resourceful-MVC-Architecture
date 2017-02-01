## Associations in MongoDB

MongoDB and NoSQL or Document-based databases structure data `hierarchically` rather than `tabularly`.

Traversing across many collections of documents in MongoDB is slow, so in order to create associations between documents, we have to use a different paradigm than joins and join tables. Instead we either "embed" documents or "reference" them by their `_id` attribute.

#### Embedded vs. Reference

80% of the time you will use references, not embedded associations. So we will focus most of our attention on reference data. Careful what you embed and what you reference. Here is a [SO question](http://stackoverflow.com/questions/21302279/embedded-document-vs-reference-in-mongoose-design-model) that explains it well.

*Embedd* information you always want whenever the parent document is returned, maybe like family members. *Reference* data you have to "populate" on demand in only some cases.

  ```js
  // EMBEDDED
  {
    name: "Jacob Alabaster",
    siblings: [
      { name: "Michael" },
      { name: "Jordan" },
      { name: "Ursula" }
    ]
  }

  // REFERENCE
  {
    name: "Bob Nicolas",
    friends:["2u343284013923", "09r32romf2092390", "04893jsjlf0039"]
  }
  ```

Here are some ways to add a reference or embedded subdocuments to your model.

```js
  // ARRAY OF STRINGS
  , statuses      : [String]
  // SINGLE REF DOC
  , author          : { type: Schema.Types.ObjectId, ref: 'User', required: true }
  // ARRAY OF REF DOCS
  , posts         : [{ type: Schema.Types.ObjectId, ref: 'Post' }]
  // ARRAY OF EMBEDDED DOCS (SCHEMA IS DEFINED ABOVE LIKE ANOTHER MODEL)
  , posts         : [CommentSchema]

```

In order to get the actual reference data, you have to use the `.populate()` Mongoose query function. The `populate()` function will look at the model collection reference and perform the lookup on the array of id's and return that array inside the parent document.

  ```js
    User.findOneById(req.param.id).populate('friends').exec(function (users, err) {
      res.render('users-show', user)
    })

    // TURNING THIS
    // {
    //   name: "Bob the User",
    //   friends:["2u3432840923", "09r32romf2092390", "04893jsjlf0039"]
    // }

    // INTO THIS
    // {
    //   name: "Bob the User",
    //   friends:[
    //     {
    //       name: "Bob the User",
    //       friends:["2u3432840923", "09r32romf2092390", "04893jsjlf0039"]
    //     },
    //     {
    //       name: "Bob the User",
    //       friends:["2u3432840923", "09r32romf2092390", "04893jsjlf0039"]
    //     },
    //     {
    //       name: "Bob the User",
    //       friends:["2u3432840923", "09r32romf2092390", "04893jsjlf0039"]
    //     }
    //   ]
    // }
  ```

**! DO NOT REFERENCE MORE THAN 1 LEVEL DEEP !**

### Challenges

#### Reference Docs: Comments

1. Create a `Comment` model using the boiler plate from `post.js`.
1. Add a reference `comments` attribute to your `post` model following the pattern in the notes above. (Notice that we do not have to add a single reference `post` subdocument attribute to the `comment` model, so associations are not bi-directional by default like in SQL.)
1. Populate comments in posts-show.
1. We don't need to see comments in post-index, but we can still display the comments count by counting the number of child comment `_id`'s are in `comments`. (e.g. `post.comments.length`). Display these counts in post-index.
1. Create a comments form in posts-show and validate that you can serialize a `comment` object and prepend it to the posts comments. (Do not make a request to your server)
1. Create a create-comments route that looks up the parent post and adds the comment to it. (hint: add the comment to the top of the array with `post.comments.unshift(comment);` and then save the parent post.)

#### Reference Doc: Author

1. Add a reference to a single `author` subdocument attribute in your post model that references a User model. (Use the pattern from above in the notes)
1. Create a `User` model with the attributes `first`, `last`, and `username`.
1. Download [robomongo](https://robomongo.org/), a GUI for MongoDB, so you can do some direct manipulation of your databases. Open your database in robomongo.
1. Create a "user" collection and some user docs that fit your model.
1. Can you get them? Associate them?
