# Testing RESTful Routes

## Objectives

## Testing

Unit Testing (models), Routes Testing (controllers), View Testing (views)

**Assertions**

## Resources

1. [Mocha](https://mochajs.org/#installation)
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
