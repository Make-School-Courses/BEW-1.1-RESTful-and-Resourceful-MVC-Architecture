# Node.js Nuts and Bolts

## Intro

If we are just using node and node modules, we might never need to really understand what's happening under the hood of node itself. But as soon as we want to modify the modules we are using or if we want to write our own modules of if we want to solve exotic problems, we're going to need to know what is going on. We might also just be curious!

## Competencies & Objectives

1. List Node.js's unique features.
1. List some of Node.js's major affordances and limitations.
1. Compare and contrast Node.js with other web servers.
1. Draw a picture of the JS event loop and how Node.js uses it to respond to requests.

## Videos & Resources

Required:
* [What is Node.js (video)](https://www.youtube.com/watch?v=GJmFG4ffJZU)
* [Philip Robert Explains The Event Loop](https://www.youtube.com/watch?v=8aGhZQkoFbQ) (His description is about the browser, but Node works the same way.)
* [Google's V8 JavaScript Engine](https://www.youtube.com/watch?v=86tgU7UaJmU&list=PL4cUxeGkcC9gcy9lrvMJ75z9maRw4byYp&index=3)
* [The Original Node.js presentation by Ryan Dahl (video)](https://www.youtube.com/watch?v=ztspvPYybIY)

Optional:
* [Streams and Buffers (video)](https://www.youtube.com/watch?v=GlybFFMXXmQ)
* [The Basics of Node.js Streams](https://www.sitepoint.com/basics-node-js-streams/)
* [Why Does Node.js use Streams? (Quora Question)](https://www.quora.com/Why-do-servers-like-Node-js-Express-use-streams-to-represent-the-request-and-response-objects)

## Baseline Challenges

1. Watch or read all the required videos and resources and take notes. (2x speed will make things go faster!)
1. Complete [nodeschool.io](https://nodeschool.io/)'s preliminary node lesson. (1 hour)

    ```bash
    $ npm install -g learnyounode
    $ learnyounode
    ```

1. Pick five question from [this article](https://medium.freecodecamp.com/before-you-bury-yourself-in-packages-learn-the-node-js-runtime-itself-f9031fbd8b69) and discuss each one with a partner. Look up answers if you don't know between each other.

## Stretch Challenges

1. Use node's native `http` module to query the Giphy API.
