# Authorization with JWT & Cookies

### Objectives
* Explain the differences between authentication and authorization.
* Use jQuery to manage authorization in your app.

## Background

We are using securely signed Json Web Tokens (JWT) to authenticate our users access to our APIs. We can have webhooks that are only accessible by people who are logged in and can prove it with verifiable, signed JWT's.

However, what about making your site look different if a user is logged in or logged out? Or what if you have different types of users that should see things a little differently?

jQuery to the rescue!!!

## jQuery DOM Manipulation

jQuery is a library that extends vanilla JavaScript. For example, the following two lines of code do the same thing:

```js
// jQuery
$ (‘body’) .css (‘background’, ‘#ccc’);

// VANILLA JS
Function changeBachground(color) {
  Document.body.style.background = color;
}

Onload=”changeBackground (‘red’);”
```

jQuery lets you easily select elements from the DOM and make changes to them, including showing or hiding them. jQuery also lets you easily make AJAX requests to your server posting or receiving data.

## Challenges

1. **Hiding Login/Signup Links** - Here is a psuedocode plan in plain English for how to hide your login and signup links when a user is logged in. Try to implement it with jQuery.

  ```bash
    If login/signup is successful, hide all HTML elements with the class `.unauthenticated` and show all HTML elements with the class `.authenticated`.
  ```

2. **Flashing** - are your elements flashing on the screen and then disappearing? That might be because the DOM loads before the hide and show functions run. What can you change to solve this flash?

3. **Admin** - Can you add an "admin" attribute your token, and if a logged in user is an admin, show an link to `/admin` in your navbar?

4. **Security** - Showing and hiding in jQuery only change the `display` css attribute from `visible` to `hidden`. Is this secure? Couldn't a malicious developer just look at the DOM in their browser web tools and see the link? Or someone could just navigate to `/admin`. What can you do to protect this URL more so only people who are admin can navigate to this route.

5. **A Partial Solution** - For a partial solution to the above challenges, please look at this repository: [express-jwt-jquery](https://github.com/ajbraus/express-jwt-jquery). What are some things this implementation of express does differently than yours? Can you clone it and run it?


## Onwards!
