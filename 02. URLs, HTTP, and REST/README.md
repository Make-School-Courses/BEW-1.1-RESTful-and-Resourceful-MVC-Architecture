# URLs, HTTP, and REST

## Objectives

1. Identify and describe each part of a URL and HTTP Request.

## Demo: Giphy Search (cont) and Q&A
  - User-Centered Development

## Initial Exercise 10 min.

1. Write your home address out and diagram what each part is called.

## URLs & Requests

The web works with a series of unique addresses like the postal service. These addresses are called URLs or **Uniform Resource Locator**.

They are the most obvious part of any request to a server.

![Detailed Req-Res](assets/req-res-detailed.gif)

URLs have a distinct anatomy and as a web developer you ought to memorize each part of a url - just as if you were a postal worker, you'd need to know what a zip code was!

![URL](assets/query.jpg)

URLs are the surface level of any request to a web server. However, there is more information in a request.

![Request](assets/request.png)

To view more about a request use the Sources tab of your Chrome web tools. Load a web page and click XHS and then select the request you want to review.

![Sources tab](assets/sources-tab.png)

## REST & HTTP

REST is the most widely used standard convention for web server behavior. You'll research more about REST in the challenges below.

HTTP is a protocol that we use to send and receive requests between servers and clients. HTTP has **HTTP Verbs** and **HTTP Statuses** and you should memorize both.

HTTP Verbs are the following:

1. GET
1. POST
1. PUT
1. PATCH
1. DELETE

The most common HTTP statuses are the following. Here is a [complete list](https://httpstatuses.com):

* 100 - Informational Response
* 200 - Success
* 300 - Redirection
* 400 - Client Error (Bad Request)
* 401 - Unauthorized
* 404 - Not found
* 418 - [I'm a tea pot](https://httpstatuses.com/418)
* 500 - Internal Server Error

## Work

1. Complete the [Giphy API Search Tutorial](https://www.makeschool.com/online-courses/tutorials/giphy-search-app-with-node-js/your-node-environment) - Due Middle of week one (today!)
1. Start [Rotten Potatoes Tutorial](https://www.makeschool.com/academy/track/rotten-potatoes---movie-reviews-with-express-js) - Due End of Week 2.

## Resources

1. [What is HTTP?](https://www.youtube.com/watch?v=SzSXHv8RKdM)
1. [Explained HTTP, HTTPS, SSL/TLS](https://www.youtube.com/watch?v=po3zYOe00O4)
1. [REST Wikipedia Article](https://en.wikipedia.org/wiki/Representational_state_transfer)
1. [REST & HTTP](https://www.youtube.com/watch?v=LHJk_ISxHHc)
1. [Intro to REST](https://www.youtube.com/watch?v=YCcAE2SCQ6k)
