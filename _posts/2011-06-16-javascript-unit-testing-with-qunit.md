---
layout: post
status: publish
published: true
title: JavaScript Unit Testing with QUnit
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 947
date: '2011-06-16 10:47:07 -0700'
date_gmt: '2011-06-16 17:47:07 -0700'
categories:
- computer science
tags:
- unit testing
- qunit
- jquery
comments: []
---
In the vein of habits I wish I had picked up in Software Engineering, I've been increasingly using unit tests. Working on a project recently with a friend of mine, it fell to me to pick out a unit testing library for our development.

My uninformed search led me to [QUnit](http://docs.jquery.com/Qunit), from the same people that bring us [jQuery](http://jquery.com/), which we already use heavily. We found it immediately simple to use, expressive and powerful. Much of this particular site involves AJAX, and as such, we wanted to be able to test and make sure our interface to these resources is working, as well. Not to mention that most operations rely on information retrieved from remote resources.

To that end, the vast majority of our tests use their `asyncTest` function, which lets you perform any kind of asynchronous request, and then in your callback, you indicate to the system that your test has all its necessary information and can continue. For example,

```javascript
asyncTest("Our Site's API", function() {
  $.ajax({
    ...
    success: function(response) {
      ok('data' in response, "We expect data in the response.");
    }
  }
}
```

One big 'get' in my mind is that it's from the same group that produces a library we already use heavily, so they tend to be thought-out in similar ways. Plus, it runs in the browser, and has nice styling for the interface that make your unit tests look extra classy!

The QUnit site has a lot more examples and demos, but this concludes my shameless plug for a unit testing quite I've come to appreciate very much.
