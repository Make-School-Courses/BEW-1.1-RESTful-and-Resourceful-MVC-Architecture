# MEAN Authentication with JWT (JSON Web Tokens)

### Objectives
* Compare and contrast a cookie-session and JSON webtoken (JWT) authentication
* Use `express-jwt` to add JWT authentication to your express server

## Background

In Rails we used the Cookie-Session method of authentication; however, there is a better way to do communicate authentication. This new way will work better with advanced **Single Page Application** technology like **React** and **Angular 1/2** as well as with authentication in **Mobile Apps**. We're going to use an encrypted chunk of JSON called a **JSON Web Token** or JWT (pronounced ''*jot*'') to communicate authentication between client and server.

![cookie-token-auth](cookie-token-auth.png)
> Reference [auth0.com](https://auth0.com/blog/2014/01/07/angularjs-authentication-with-cookies-vs-token/)

![jwt-diagram.png](jwt-diagram.png)

## Why Use JWT?

Aren't you tired of worrying about keeping track of all these things?

1. Sessions - JWT doesn't require sessions
1. Cookies - JWT you just save the token to the client
1. CSRF - Send the JWT instead of a CSRF token
1. CORS - Forget about it, if your JWT is valid, the data is on its way

Also these benefits:

1. Speed - you don't have to look up the session
1. Storage - you don't have to store the session
1. Mobile Ready - Apps don't let you set cookies but they can save auth tokens
1. Testing - you don't have to make logging in a special case in your tests, just send the token.

## JWT FTW

A JWT is pretty easy to identify. It is three strings separated by .

```
  aaaaaaaaaa.bbbbbbbbbbb.cccccccccccc
```

Each part has a different significance:

![jwt](jwt.png)

### Here is a JWT Example:

#### Header

```js
var header = {
  "typ": "JWT",
  "alg": "HS256"
}
```

#### Payload

```js
var payload = {
  "iss": "scotch.io",
  "exp": 1300819380,
  "name": "Chris Sevilleja",
  "admin": true
}
```

#### Signature

```js
var encodedString = base64UrlEncode(header) + "." + base64UrlEncode(payload);

HMACSHA256(encodedString, 'secret');
```

> **REMEMBER** The 'secret' acts as an encryption string known only by the two parties communicating via JWT. Protect your secrets!

#### JSON Web Token
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzY290Y2guaW8iLCJleHAiOjEzMDA4MTkzODAsIm5hbWUiOiJDaHJpcyBTZXZpbGxlamEiLCJhZG1pbiI6dHJ1ZX0.03f329983b86f7d9a9f5fef85305880101d5e302afafa20154d094b229f75773
```

## Further Reading

- [jwt.io](http://jwt.io/)
- [Atlassian JWT docs](https://developer.atlassian.com/static/connect/docs/latest/concepts/understanding-jwt.html)
- [scotch.io tutorial](https://scotch.io/tutorials/the-anatomy-of-a-json-web-token)
- [JWT Express Node Mongoose](http://blog.matoski.com/articles/jwt-express-node-mongoose/)

## Challenges
1.

<!--
## JWT Flow
> Reference: [blog.matoski.com](http://blog.matoski.com/articles/jwt-express-node-mongoose/)

**Login**

1. Client logs in with email and password.
1. Server checks email and password and if valid sends back a JWT.
1. Client receives the JWT and stores it in localStorage.
1. Client makes requests with the token (this happens automatically using an **AngularJS Interceptor**)
1. JWT is decoded on the server, and the server uses the token data to decide if user has access to the resource.

**Signup**

1. Client sends in email and password.
1. Server creates a new user if everything is valid and sends back a JWT.
1. Client receives the JWT and stores it in localStorage.
1. Client makes requests with the token (this happens automatically using an **AngularJS Interceptor**)
1. JWT is decoded on the server, and the server uses the token data to decide if user has access to the resource.

# Satellizer

[Satellizer](https://github.com/sahat/satellizer) hides a lot of the complexity of using JWT tokens. This is both a good and a bad thing. Let's not lose sight of how Satellizer is helping us.

1. Generating the JWT token (resources/auth.js)
1. Making some routes require authentication:

  ```js
  app.get('/api/me', auth.ensureAuthenticated, function(req, res) {
    User.findById(req.userId, function(err, user) {
      res.send(user);
    });
  });
  ```
1. Sending the JWT with every request using an angular interceptor.


# Challenges

**Getting Started**

1. Fork, clone, npm install, nodemon [mean-auth-html](https://github.com/ajbraus/mean-auth-html).
1. Sign up, logout, and then login to make sure authentication is working.
1. Look to see that the user was created.

**Adding an Attribute**

1. Add a `username` field to the sign up form in the `navbar.html` template. Add the username attribute to the `user.js` model. Sign up with a username.

**Add a User Settings Page**

1. Create a form to edit the user's details at the url `\settings`. This template will need a url, an angular controller, and a template.
1. Set this link the navbar dropdown below `Profile`.
1. You don't have a User service, so instead just make an `$http.get` request to `/api/me` to get the user's data.
1. To submit the form, make an `$http.put` request to `/api/me`.
1. Go to the `resources/users.js` file and write psuedocode explaining the logic of these routes.
1. If the user update is successful redirect to `/profile`.

**Add a Post Resource**

1. In the `/profile`, display `user.posts` with an ng-repeat.
1. Create a form in the `/profile` template that has an input and a textarea field that use the `ng-model` directives to attach them to `post.title` and `post.body` in `$scope`.
1. Use the `ng-sumit` directive to run the function `createPost()` on submit. This function should run a `$http.post` function to post the `$scope.post` object to `/api/posts`.
1. Create a new file in `resources` called `posts.js` and model it after `users.js` but require the `post.js` model not the `user.js` model. For now only create one route - `app.post('/api/posts', function(req,res){ ... })`.
1. Require the `posts.js` file in your `server.js` file just as the `users.js` file is required so that the route is available.
1. Create another model called `post.js`
  ```js
  var mongoose = require('mongoose'),
    Schema = mongoose.Schema;

  var PostSchema = Schema({
    title  : String,
    body   : String
  });

  var Post = mongoose.model('Post', PostSchema);

  module.exports = Post;
  ```
1. Add a `posts` attribute to the User model in `user.js` that references the Post model.
  ```js
  var userSchema = Schema({
    ...
    posts : [{ type: Schema.Types.ObjectId, ref: 'Post' }]
  });
  ```
1. When you submit your new post form, can you console log the new post object in the server?
1. Now that your client is posting data to your server route, let's save it to the current user's posts. To find the current user, we have to add the `auth.ensureAuthenticated` function to our route.
  ```js
  app.post('/api/posts', auth.ensureAuthenticated, function (req,res) {
    ...
  })
  ```
1. Now find the current user using the mongoose User model and the `req.userId` that `auth.ensureAuthenticated` makes available through the JWT token.
  ```js
  User.findById(req.userId, function(err, user) {
    ...
  })
  ```
1. Now let's create a `new Post` with `req.body`, save the post, and in the callback push that `post` into `user.posts`, and then save the `user` object and send back the post `res.send(post)`.
  ```js
  app.post('/api/posts', auth.ensureAuthenticated, function (req,res) {
    User.findById(req.userId).exec(function(err, user) {
      var post = new Post(req.body);
      post.save(function(err, post) {
        user.posts.unshift(post._id);
        user.save();
        res.send(post);				
      });
    })
  })  
  ```
1. In the client can you console log the response with the user object?
1. Now unshift the post response into the `$scope.user.posts`.
1. Do you see the posts displaying? Are the Posts saving to a collection in your database?
1. Add `.populate('posts')` to your `/api/me` route in `users.js`. Now refresh the `/profile` page - do you see the user's posts? -->
