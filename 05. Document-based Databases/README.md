# RESTful & Resourceful Routing

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

## Resources

1. [Mongo Shell Quick Reference](https://docs.mongodb.com/manual/reference/mongo-shell/)

## Baseline Challenges

1. Open the mongo shell in your terminal.
1. Query what databases you have.
1. Create a database called `my-blog`.
1. Insert an article in a new articles collection with the attributes title and body.
1. Query for all articles.
1. Add 3 more articles.
1. Query for just one article.
1. Delete that article.
1. Download robomongo and look at the database you created with the mongo shell.
1. Continue with the Project Portfolio App
