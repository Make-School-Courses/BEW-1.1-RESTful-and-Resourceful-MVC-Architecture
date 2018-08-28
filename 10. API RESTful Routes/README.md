# RESTful API Routes

1. 5 min Intro & Objectives
1. 15 min Challenge 1
1. 20 min TT on RESTful APIs, Service-based, and Microservice Architecture
1. 20 min Challenge 2
1. 10 min Break
1. 30 min Challenge 3
1. 5 min Wrap up

## Objectives

1. Define what an API and RESTful API is
1. Define our routes to respond to JSON requests

## Activity - Explore Service Oriented Architecture
1. With a partner pick 2 companies on [stackshare.io](https://stackshare.io/stacks) and examine the services and languages they use. Google the services you are not familiar with.

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

A Microservices Architecture is SOA on steroids. It further breaks up services into sometimes even single routes and hyper specialized sorts of databases and technology.

## Activity: Diagramming a Service-based Architecture

1. Imagine you have a service-based architecture where a browser, mobile, and desktop clients all communicate with a server. Draw a picture of the request response cycles for these clients and the server.
1. Now imagine you add using Stripe.com to process payments. Add this to your picture.
1. Now imagine you use Twillio.com to send text messages. Add this to your picture.
1. Now imagine you use AWS S3 to save images that users upload and serve them back when requested. Add this to your picture.


## Implementation of a RESTful API

To make our server a RESTful API, we need our server to respond intelligently to JSON requests. Since we already have RESTful routes that return HTML, we have two options, either we can make separate whole controllers, or we can check if the request coming in has the `Content-Type` header of `application/json`, and then behave accordingly.

New API routes
```js
// INDEX
app.get('/api/posts', function(req, res){

});

// SHOW
app.get('/api/posts/:id', function(req, res){

});

// ETC
```

Respond to application/json
```js
app.get('/api/posts', function(req, res){
  if (req.header('Content-Type') == 'application/json') {
    return res.send({ post: post }); //=> RETURN JSON
  } else {
    return res.render('posts-show', { post: post }); //=> RENDER A TEMPLATE
  }
});
```

> Notice that the NEW and EDIT routes are not necessary with a RESTful API.

## Activity: RESTful API
1. Why are the NEW and EDIT RESTful routes not necessary with a RESTful API?
1. Make Rotten Potatoes respond as an API to JSON requests.
1. Make what changes must you make to your tests to cover these new routes that respond to JSON requests.

## Fetch vs. Axios Activity

Why are we using Axios if it is just a wrapper for JavaScript's ES6 function `fetch`? Why not just use fetch by itself.

Let's look at the pro's and con's

Cons
* Having to add Axios anywhere we will use it on the client
* Having to learn Axios' API
* Having to conform to any of Axios' idiosyncrasies
* Needlessly going to a higher level of abstraction

Pros
* Axios parses JSON responses automatically meaning fewer steps and less code
* Axios has a purely resouceful API, so if you know resouceful development you already know its API
* Mirroring resourceful syntax on the client and the server
* This class is about learning Resourceful development :D

The Pro's have it! But it isn't always the right choice. Keep an open mind about the tools you or your team use. Try to be **Technically Agnostic** - the best engineers are.


## Resources

1. [REST API concepts and examples](https://www.youtube.com/watch?v=7YcW25PHnAA)
