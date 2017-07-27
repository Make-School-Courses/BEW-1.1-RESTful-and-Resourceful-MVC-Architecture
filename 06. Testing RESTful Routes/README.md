# Testing RESTful Routes

1. 5 min Intro and Objectives
1. 20 min TT on Test Types and Assertions
1. 30 min Baseline and Stretch challenges
1. 10 min Break
1. 30 min Continue with Rotten Tomatoes
1. 5 min Wrap up

## Objectives

1. Identify the various types of testing and pick the right test for a module.
1. Have familiarized oneself with the node testing suite using Mocha and Chai.
1. Master controller testing for RESTful routes.

## Testing (Mocha.js)

Depending on who you ask there are various forms of testing. For our purposes we will rely on the MVC architecture to define the various forms of tests:

1. **Unit Testing** (testing **Models**),
1. **Routes Testing** (testing **Controllers**)
1. **View Testing** (testing **Views**)

**Unit tests** are very resilient and will rarely break as you make changes to your code, they provide very narrow test coverage to your application as a whole so you have to write a lot of them.

**View tests** are more broad (they test more parts of your code simultaneously), but they are more brittle - meaning they can break because you made a trivial change, e.g. changed the HTML/CSS of your website.

**Routes Testing** or testing our controllers are in a bit of a Goldilocks position where they are broad and test a lot of behavior across the model and the controller, but they are not too brittle that they will break when we change something minor like the styling.

We will focus primarily on routes testing.

### Assertions & Assertion Libraries (Chai.js)

An **Assertion** is a true/false statement that defines a test. Mocha.js ships with [Node.js's native assertion library (`assert`)](https://nodejs.org/api/assert.html), which is very simple, and sometimes clunky way to write assertions. Mocha.js itself actually recommends that you use an **Assertion Library** like [Chai.js](http://chaijs.com/) that gives assertions more elegance and range.

Compare and contrast the following assertion expressions.

```js
// assert()
assert.ok(true); // => a value is true
assert.equal(-1, [1,2,3].indexOf(4)); // => 4 is not in a given array
assert.equal(res.status, 200); // => the response HTTP status is 200
assert.equal('tony')

// chai.should();
foo.should.be.a('string');
foo.should.equal('bar');
foo.should.have.lengthOf(3);
tea.should.have.property('flavors').with.lengthOf(3);

// var expect = chai.expect;
expect(foo).to.be.a('string');
expect(foo).to.equal('bar');
expect(foo).to.have.lengthOf(3);
expect(tea).to.have.property('flavors').with.lengthOf(3);

// var assert = chai.assert;
assert.typeOf(foo, 'string');
assert.equal(foo, 'bar');
assert.lengthOf(foo, 3)
assert.property(tea, 'flavors');
assert.lengthOf(tea.flavors, 3);
```

Here are some examples of assertions you'll use to test RESTful routes for a hypothetical`Book` resource:

```js
// SHOW
res.should.have.status(200);
res.body.should.be.a('object');
res.body.should.have.property('title');
res.body.should.have.property('author');
res.body.should.have.property('pages');
res.body.should.have.property('year');
res.body.should.have.property('_id').eql(book.id);

// CREATE SUCCESS
res.should.have.status(200);
res.body.should.be.a('object');
res.body.should.have.property('message').eql('Book successfully added!');
res.body.book.should.have.property('title');
res.body.book.should.have.property('author');
res.body.book.should.have.property('pages');
res.body.book.should.have.property('year');

// CREATE VALIDATION ERROR
res.should.have.status(400); //Bad Request
res.body.should.be.a('object');
res.body.should.have.property('errors');
res.body.errors.should.have.property('pages');
res.body.errors.pages.should.have.property('kind').eql('required');

// UPDATE
res.should.have.status(200);
res.body.should.be.a('object');
res.body.should.have.property('message').eql('Book updated!');
res.body.book.should.have.property('year').eql(1950);

// DELETE
res.should.have.status(200);
res.body.should.be.a('object');
res.body.should.have.property('message').eql('Book successfully deleted!');
res.body.result.should.have.property('ok').eql(1);
res.body.result.should.have.property('n').eql(1);

// SOME OTHERS
res.req.path.should.equal('/profile') // path after redirect should be equal to a value
res.should.have.header('Content-Type', 'text/html; charset=utf-8') // response should be of a certain type: e.g. HTML or JSON
```

### Structure of a Test

Here is an example `test/index.js` file.

> Notice that we are using `chai-http` to make the HTTP request to our local server. You'll have to add that to your project.

```js
var chai = require('chai')
var chaiHttp = require('chai-http');
var should = chai.should();

chai.use(chaiHttp);

describe('Site', function() {
  it('should have a live landing page', function (done) {
    chai.request('localhost:3000')
      .get('/')
      .end(function (err, res){
        res.status.should.be.equal(200);
        done();
      });
  });
});
```

## Resources

1. [Mocha](https://mochajs.org/#installation)
1. [Chai.js](http://chaijs.com/)
1. [JavaScript Testing Basics (video)](https://www.youtube.com/watch?v=yrGkDeBHqvY)
1. [Creating a Basic Chai Mocha Test (video)](https://www.youtube.com/watch?v=0AAIbEAyFxg)
1. [Intro to JavaScript Unit Testing With Mocha and Chai](https://www.youtube.com/watch?v=MLTRHc5dk6s) - this uses Chai - which we will look at in a future lesson.
1. [Integration Testing with Express (video)](https://www.youtube.com/watch?v=r8sPUw4uxAI) - this includes Chai and Supertest - which we will learn in a future lesson.

## Baseline Challenges

1. Add Mocha to the portfolio project
  ```bash
  $ npm install —-save-dev mocha
  ```

  ```js
  // package.json
  ...
  “scripts”: {
    "test": "mocha"
  }
  ...
  ```

1. Add test for GET `/`
1. Add test for POST `/projects`
1. Add test for GET `/projects/:id`
1. Add test for DELETE `/projects/:id`

## Stretch Challenges

1. Add tests for all other RESTful routes
1. Add tests for validation and user errors
