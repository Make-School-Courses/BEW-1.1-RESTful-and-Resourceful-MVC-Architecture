# Authentication with JWT (JSON Web Tokens) in Node

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
  "exp": 1300819380,
  "name": "Chris Sevilleja",
  "_id": "3sfas687a789dadf998"
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

1. **Make a Controller** Create a new controller file called `auth.js` and require it in your main server file.
1. **GET route** - In that new file, create a GET route to `/sign-up`. In your `/scripts.js` file use a `$.post()` or `$.ajax()` jQuery function to submit the serialized form data to `/sign-up`.
1. **POST route** - Now, create a POST route to `/sign-up` and console log if you are receiving the form data in `req.body`.
1. **Create User Model** - Once you are receiving the form data, create a `User` model in `models/user.js` and require it at the top of your `auth.js` file. Here is boilerplate code for the model (REMINDER: do not just copy and paste this code into your project. Read each line and figure out what each line does before using it.). (HINT: You will need to install the [bcryptjs](https://www.npmjs.com/package/bcryptjs) package to your project for bcrypt to work.)

  ```js
    var mongoose = require('mongoose'),
        bcrypt = require("bcryptjs"),
        Schema = mongoose.Schema;

    var UserSchema = new Schema({
        createdAt       : { type: Date }
      , updatedAt       : { type: Date }

      , email           : { type: String, unique: true, required: true }
      , password        : { type: String, required: true }
      , first           : { type: String, required: true }
      , last            : { type: String, required: true }

    });

    UserSchema.pre('save', function(next){
      // SET createdAt AND updatedAt
      var now = new Date();
      this.updatedAt = now;
      if ( !this.createdAt ) {
        this.createdAt = now;
      };

      // ENCRYPT PASSWORD
      var user = this;
      if (!user.isModified('password')) {
        return next();
      };
      bcrypt.genSalt(10, function(err, salt) {
        bcrypt.hash(user.password, salt, function(err, hash) {
          user.password = hash;
          next();
        });
      });
    });


    UserSchema.methods.comparePassword = function(password, done) {
      bcrypt.compare(password, this.password, function(err, isMatch) {
        done(err, isMatch);
      });
    };

    module.exports = mongoose.model('User', UserSchema);
  ```
1. **Create the user** - Now use the `User` model to create a new user in your `/sign-up` POST route. e.g.

  ```js
    var small = new Tank(req.body);
    small.save(function (err) {
      if (err) return handleError(err);
      // saved!
    });
  ```

1. **Create and Sign the JWT** - Now add the package [jsonwebtoken](https://github.com/auth0/node-jsonwebtoken) to your project and require it at the top of `auth.js`. Now, if the user saves successfully, use `jsonwebtoken` to create and sign a JWT and send it back to the client. Console log your token on the client.

  ```js
    var jwt = require('jsonwebtoken');

    ...
    var token = jwt.sign({ _id: user._id }, 'shhhhhhared-secret');
    ...
  ```
1. **Save the token as a cookie** - Use bower to install [js-cookie](https://github.com/js-cookie/js-cookie) to your client and reference it in your `<head>` with a `<script>` tag. Now you can use the `Cookie` object anywhere in your front end scripts. Use it to save a cookie called `token` of the data returned.

  ```js
    Cookies.set('token', data.token);
    // IF YOU'D LIKE TO REDIRECT NOW, ADD THIS:
    window.location.href = "/";
  ```
1. **Tell server look at cookies for JWT** - Add the [express-jwt](https://github.com/auth0/express-jwt) and the [cookie-parser](https://www.npmjs.com/package/cookie-parser) libraries to your server and include them in your main server file. Use this code to use this middleware and tell it to look at the cookie for a token. Once you save the cookie saved, can you see your cookie in "Application" tab of the Chrome web tools?

  ```js
    var cookieParser = require('cookie-parser');
    ...

    app.use(cookieParser());
    app.use(jwt({
      secret: 'shhhhhhared-secret',
      getToken: function fromHeaderOrCookie (req) { //fromHeaderOrQuerystring
        if (req.headers.authorization && req.headers.authorization.split(' ')[0] === 'Bearer') {
          return req.headers.authorization.split(' ')[1];
        } else if (req.cookies && req.cookies.token) {
          return req.cookies.token;
        }
        return null;  
      }
    }).unless({path: ['/', '/login', '/sign-up']}));
  ```
1. **Test a Secure a Route** - Make a new route called `/bananas`, and have it send back the text "I love bananas". Now navigate to it without being logged in.

1. Ok now do all the above again but for `/login`.
1. Can you create a link/button that when you click it the client logs out?
