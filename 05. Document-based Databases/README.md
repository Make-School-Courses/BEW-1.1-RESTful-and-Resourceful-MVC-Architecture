# Document-based Databases

## Objectives

1. Identify the key characteristics of a NoSQL or Document-based database.
1. Navigate the most simple commands inside the mongo shell.

## Document-based Databases or NoSQL

**JSON** or **JavaScript Object Notation** is a way to organize data to transmit it across the internet. It looks the same as a JavaScript object. It is made up of pairs of **keys** and **values** separated by colons (`:`) and surrounded by curly braces (`{}`). The only difference between a JavaScript object and a JSON object is the **keys** are wrapped in strings. For example:

```js
// JS OBJECT
{
  title: "Great Project"
}
```

```js
// JSON OBJECT
{
  "title": "Great Project"
}
```

A MongoDB database allows you to save JavaScript Objects or JSON just as they are as **key value pairs**. In a MongoDB each object is called a single **document**, hence why this sort of database is called a **document-based database**. These documents are collected into groups called **collections**. So we will save our project documents in a collection called "projects".

MongoDB gives each document a unique identification number with the key **_id** (with an underscore). We'll use that **_id** attribute to retrieve the whole document later. MongoDB is sorta like dropping clothes off at the drycleaners. They put a number on each piece of clothing and give you a ticket for each one. Later we can get that clothing back by matching our ticket to the right number.

So if we saved a new project like this to a MongoDB database:

```js
// JS OBJECT
{
  title: "A New Project"
}
```

Then it will save something like this:

```js
// MONGODB OBJECT
{
  _id: "507f1f77bcf86cd799439011",
  title: "A New Project"
}
```

Documents are grouped into **Collections**. And these collections should have the same name as your resources. So a `User` resource should have a `users` collection. And an `Article` resource should have an `articles` collection.

![document-based db](assets/doc-based-db.jpg)

### Pros

1. Write's fast
1. Easy to get started
1. No migrations
1. "Schemaless" - can write anything you like

### Cons

1. Slow to traverse
1. Slow to read
1. No migrations - no timeline of updates to database structure
1. "Schemaless" - can be too unstructured


## ODM

Mongoose is a ODM (object document mapping) express middleware that makes it easier to interact with a MongoDB database. It lets you create and validate attributes and create model and instance methods and many other common OXM features.

### Model

To interact with the database, we use an abstraction called a **Model**. Like a resource, you can tell if something is a model because it is single and capitalized. For example:

* Article
* Pet
* Building
* City
* Trip

A model is like a prototype for an object because you can assign it attributes and define static and instance methods for it. You can also set validations on a model's attributes.

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

## Resources

1. [Mongo Shell Quick Reference](https://docs.mongodb.com/manual/reference/mongo-shell/)

## Baseline Challenges

1. Open the mongo shell in your terminal.
1. Query what databases you have.
1. Create a database called `my-blog`.
1. Insert an article in a new articles collection with the attributes `title` and `body`.
1. Query for all articles.
1. Bulk insert 3 more articles.
1. Query for just one article.
1. Delete that article.
1. Download [Robomongo](https://robomongo.org/) and look at the database you created with the mongo shell.
1. Continue with the [Rotten Potatoes App](https://www.makeschool.com/online-courses/tutorials/rotten-potatoes-movie-reviews-with-express-js/bootstrap-an-express-project)


# MongoDB Associations & Queries

## Objectives

1. Utilize the common verbiage for defining **Resource Associations**
1. Master Mongoose queries for associated resources, including the function `.populate()`
1. Master the simplest ERD diagrams

## Associations

Here are some statements that are true about the associations of the resources in Facebook. We'll call these "Has Many/Belongs To"

```
Users have many Posts
Users have many Comments
Users have many Likes
```

Here are some more, more complex associations also called "Has and Belongs to Many".

```
Users have many Events as reservations
Users belong to Events as guests
```

You can also do a "Has One/Belongs To" association (rare)

```
User has one Profile
User has one Credit Card
```

## ERDs

## Activity - Drawing ERDs

Draw ERDs for the core features of 3 the following applications. You can pick your own products if you like to draw. When you finish your first, check with a partner. Form into groups of 4 and show your favorites off.

1. Lyft
1. Pinterest
1. Airbnb
1. Facebook
1. The AppStore

## Modeling these Associations in MongoDB

In a document-based database these **Resource Associations** are modeled in a few ways.

### Attributes

```js
// Post belongs to Subreddit
{
  "title": "",
  "subreddit": "Jugglers Anonymous"
}

// User belongs to City
{
  "name": "John Brown",
  "city": "San Francisco"
}
```

### Reference Documents

```js
// Posts belong to User
{
  "name": "John Brown",
  "posts": ["a41492308329r900sdf", "9309safd0as0f9f098af"]
}
```

### Embedded Documents

```js
// Comments belong to Post
{
  "title": "Awesome Article",
  "comments": [
    { "content": "What a great article" },
    { "content": "Agreed!" }
  ]
}
```


## Queries

Now imagine you have these underlying resource associations. Let's look at the queries that Mongoose gives you to pull this data out and serve it.

### Find All

```js
Post.find()
  .then(posts => {

  })
  .catch(err => {

  })
```

### Find by Attribute

```js
Post.findOne({"name": "Bob Winthrope"})
  .then(post => {

  })
  .catch(err => {

  })
```

## Activities: Returns

Find what each of these return? (Hint: use mongoose docs)

```js
Person.find().exec(err, person => {});
Event.findOne({name: "Lightening Party"}).exec(err, event => {});
Car.findById(req.params.carId).exec(err, car => {});
Company.findOne({_id: req.params.companyId})
       .populate('employees')
       .exec(err, company => {});
```

Use your imagination and write sample JSON of what the last one might return.

## Activity: Queries

With a partner, write the queries in Mongoose for the following requests in English.

1. Find all users
1. Find one article by its id
1. Find one user by their social security number
1. Find all dogs that go to heaven sorted alphabetically by name
1. Find the 10 most recent articles to be created
1. Find the 10 oldest users
