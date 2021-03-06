---
layout: post
status: publish
published: true
title: Never Trust Callbacks
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1042
date: '2011-10-16 09:27:23 -0700'
date_gmt: '2011-10-16 16:27:23 -0700'
categories:
- computer science
tags:
- python
- lessons learned
- javascript
- callbacks
- exceptions
comments: []
---
It's a lesson that has now been hammered home repeatedly in my head: never trust callbacks. Just don't. Go ahead and execute them, but if you trust them to not throw exceptions or errors, you are in for a world of unhappiness.

For me, I first learned this lesson when making use of twisted, writing some convenience classes to help with some of the somewhat odd class structure they have. (Sidebar: twisted is an extremely powerful framework, but their naming schemes are not what they could be.) Twisted makes heavy use of a deferred model where callbacks are executed in separate threads, while mission-critical operations run in the main thread. My convenience classes exposed further callbacks that could be overridden in subclasses, but I made the critical mistake of not executing that code inside of a try/except block.

Twisted has learned this lesson. In fact, their deferred model makes it very hard to throw a real exception. If your callbacks fail, execution takes a different path -- calling errback functions. In fact, twisted is so pessimistic about callbacks (rightly so) that you just can't make enough exceptions to break out of errback functions. However, wrapped in my convenience classes were pieces of code that were mission critical, and my not catching exceptions in the callbacks I provided was causing me a world of hurt.

That whole experience was enough to make me learn my lesson. Then, a few days ago I encountered it again in a different library, in a different language, in a different project, where I was exposing callbacks for user interface code in JavaScript. The logical / functional chunk of code exposed events that the UI would be interested in, but was too trusting, leading to errors in callbacks skipping over critical parts of the code.

All in all, __when exposing callbacks, never trust a callback to not throw an exception.__ Even if you wrote the callbacks it's executing (as was the case with both of these instances, at least in the beginning). __Callbacks are a courtesy -- a chance for code to be notified of an event,__ but like many courtesies, they can be abused.
