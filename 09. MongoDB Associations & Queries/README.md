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

## Activity: Writing JSON

Write examples in JSON for the following associations:


## Queries

Now imagine you have these underlying resource associations. Let's look at the queries that Mongoose gives you to pull this data out and serve it.

### Simple Query

```js
Post.find()
  .then((posts) => {

  })
  .catch((err) => {

  })
```

### Find by Attribute

```js
Post.find()
  .then((posts) => {

  })
  .catch((err) => {

  })
```

### Populate
```js
Post.find()
  .then((posts) => {

  })
  .catch((err) => {

  })
```

## Activity: Queries

With a partner, write the queries in Mongoose for the following requests in English. Remember that some of these will need two queries.

1. Give me
1. Give me all dogs that go to heaven.
