---
layout: post
status: publish
published: true
title: Mandelbrot
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 177
date: '2008-11-28 22:13:20 -0800'
date_gmt: '2008-11-29 05:13:20 -0800'
categories:
- computer science
tags:
- graphics
- Mandelbrot
comments: []
---
The [Mandelbrot set](http://en.wikipedia.org/wiki/Mandelbrot_set) is one of those things you've always seen on posters or in your math book, but never knew what it was actually.  Well, it was that way for me, until recently.

It's a graph of the [complex plane](http://en.wikipedia.org/wiki/Complex_plane), in which each point has an associated value.  This value is determined by the series:

$$ x_{n+1} = x_{n}^{2} + c$$

where c is the point in question.  If this value does not approach infinity, then it's contained in the set, and is colored in black.  Otherwise, its color is determined by how fast it grows (and there are a number of ways of doing this).

A new friend of mine, Johnny, adapted code from one of our graphics projects to render the set, and so I had to do the same.  Not one-upsmanship, but how awesome is that for a project.  That said, this is the result of my work so far, but I plan to develop a better coloring scheme, as well as adding interactivity and exploratory tools to the interface.

![My rendered version of the Mandelbrot set]({{ site.github.url }}/assets/2008/11/mandelbrot.png)
