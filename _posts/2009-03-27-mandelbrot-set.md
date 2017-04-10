---
layout: post
status: publish
published: true
title: Mandelbrot Set
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 474
date: '2009-03-27 21:39:34 -0700'
date_gmt: '2009-03-28 04:39:34 -0700'
categories:
- miscellany
tags: []
comments: []
---
I take another look at my Mandelbrot code because we recently did a project with antialiasing in a raytracer.  I updated my project so that instead of bouncing light, it would instead sample a point on the complex plane, and determine if it was in the Mandelbrot set, and so on and so forth.

I ran the code with 10 passes and 16,384 by 16,384 pixels (~27 megapixels) on my desktop.  It took about an hour and a half, but this is the picture that came out of it ([full resolution here]({{ site.github.url }}/assets/2009/03/mandelbrot.1024x1024.png)):

![A recent rendering of mine of the Mandelbrot set.]({{ site.github.url }}/assets/2009/03/mandelbrot.1024x1024.png)

I also have a couple of extra pictures that show portions of the set in their detail:

![A region of the Mandelbrot set.]({{ site.github.url }}/assets/2009/03/zoom.png)

![Another zoomed-in portion of the set.]({{ site.github.url }}/assets/2009/03/zoom2.png)
