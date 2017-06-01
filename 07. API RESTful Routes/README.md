# RESTful API Routes & Their Tests

## Objectives

1. Define what an API and RESTful API is
1. Define our routes to respond to JSON requests

## Overview

### RESTful APIs

So far we've been making User Interfaces (UI's) by returning HTML templates to the client, but what if we want to let other applications use our web server, such as a mobile app or another web server? In that case we want to make an API.

![realtime-api.png](assets/realtime-api.png)

An API is a set of web endpoints that respond to JSON (or XML) rather than with HTML templates. Basically, UI's are how people use your website, while API's are how other computers use your app.

We've already used APIs - like those found at [RapidAPI.com](rapidapi.com) - but now we want to make our own.

### Service Oriented Architectures (SOA)

A Service Oriented Architecture is the most common best practice for software architecture today.

![elephant](assets/elephant.jpg)

Large companies build their own custom services for their various flows. However, even a small project will use various off-the-shelf services and will therefore resemble SOA. For example:

1. Stripe or Braintree for handling payments
1. Google Analytics for analytics
1. Auth0 to handle authentication
1. AWS S3 for file storage
1. Firebase for chat rooms

### Microservices Architecture

A Microservcies Architecture is SOA on steroids. It further breaks up services into sometimes even single routes and hyper specialized sorts of databases and technology.

## Implementation of a RESTful API

To make our server a RESTful API, we need our server to respond intelligently to JSON requests. Since we already have RESTful routes that return HTML, we have two options, either we can make separate whole controllers, or we can check if the request coming in has the `Content-Type` header of `application/json`, and then behave accordingly.

```js
if (req.header('Content-Type') == 'application/json') {
  return res.send({ article: article }); //=> RETURN JSON
} else {
  return res.render('articles-show', { article: article }); //=> RENDER A TEMPLATE
}
```

> Notice that the NEW and EDIT routes are not necessary with a RESTful API.

## Resources

1. [REST API concepts and examples](https://www.youtube.com/watch?v=7YcW25PHnAA)

## Baseline Challenges

**Service Oriented Architecture**
1. With a partner pick a company on [stackshare.io](https://stackshare.io/stacks) and examine the services and languages they use. Google the services you are not familiar with.

**RESTful API**
1. Why are the NEW and EDIT RESTful routes not necessary with a RESTful API?
1. Make your portfolio project respond as an API to JSON requests.
1. Make what changes (if any) you must to your tests to cover these new routes that respond to JSON requests.
