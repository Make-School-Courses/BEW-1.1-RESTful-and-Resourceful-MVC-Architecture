# RESTful & Resourceful Routing

## Objectives

1. Identify and use RESTful and Resourceful routes
1. Identify and use nested routes for nested resources

## Routing

A route is a url, a web endpoint, a path, or you might just call it a link. Routes are just strings, they can look like anything at all. But we want to follow standard conventions. So we use RESTful and Resourceful routes.

![RESTful Routes](assets/RESTful-routes.png)

Please memorize these routes.

## Resources

1. [restful_routes.md](https://gist.github.com/alexpchin/09939db6f81d654af06b)

## Baseline Challenges

1. Read this Rails documentation on [routing for **Nested Resources**](http://guides.rubyonrails.org/routing.html#nested-resources).
  - What are three examples of using nested routes?
  - Could you make nested routes with Express as well?
1. Work with a partner to define what these routes expect and return:
  - PUT `/articles/:articleId`
  - GET `/users/:userId/articles/:articleId`
  - POST `/classes/:classId/students`
  - GET `/classes/:classId/students`
  - GET `/era/:eraId/dinosaurs`
1. Begin the Portfolio Template Project
