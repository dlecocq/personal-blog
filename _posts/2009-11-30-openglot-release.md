---
layout: post
status: publish
published: true
title: OpenGLot Release
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 746
date: '2009-11-30 00:31:59 -0800'
date_gmt: '2009-11-30 07:31:59 -0800'
categories:
- school
- computer science
- math
- KAUST
tags:
- graphics
- openglot
- plotting
comments:
- id: 534
  author: Andrew Ferguson
  author_email: andrew@fergcorp.com
  date: '2009-11-30 15:09:12 -0800'
  date_gmt: '2009-11-30 22:09:12 -0800'
  content: Dan, I'm pretty sure you are having too much fun. I'm going to need you
    to tone it down a bit ;)
- id: 538
  author: Matt Matteson
  author_email: matt@dlzip.com
  date: '2009-12-01 22:44:50 -0800'
  date_gmt: '2009-12-02 05:44:50 -0800'
  content: Great work Dan! Care to tell us how you setup and orchestrated the tiled
    display?
- id: 539
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2009-12-02 02:24:27 -0800'
  date_gmt: '2009-12-02 09:24:27 -0800'
  content: I used a framework called CGLX (developed at UCSD) as the windowing system
    for the tiled display.  Each of their setups has a head node where the code is
    run, and then geometry is split up to be rendered among the various display nodes.  Each
    of those computers is responsible for running a few displays.
- id: 551
  author: Murad
  author_email: mmourad211@hotmail.com
  date: '2009-12-09 06:01:06 -0800'
  date_gmt: '2009-12-09 13:01:06 -0800'
  content: Nice pictures... But it is good to indicate the real application... Good
    luck
- id: 565
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2009-12-19 00:02:56 -0800'
  date_gmt: '2009-12-19 07:02:56 -0800'
  content: |-
    Of course.  It's easy to grow so accustomed to one's own work and purpose to the point where one assumes everyone is thinking the same things.

    I'll be expanding on this break, and I'll be providing some better demos and a `getting started' section.  Thanks for reading!
- id: 2888
  author: fastest weight loss method
  author_email: BuffkinWegleitner4319@aol.com
  date: '2013-04-21 21:36:11 -0700'
  date_gmt: '2013-04-22 04:36:11 -0700'
  content: Great Job. Thank you for posting this. I'll definitely check again to find
    out more and recommend my coworkers about your writing.
---
A short while ago I posted a new release of OpenGLot, which featured parametric curves, scalar fields, contour lines and flow fields all implemented in GLSL shaders.

And they support time dependence.

It can plot virtually any function in x, y and t, and on my MacBook with its NVIDIA GeForce 9400M it has been getting 10k+ fps.  I'm still a little surprised by this number, but it seems to be running at that speed.

![Flow (vector) fields appear as advected dye. They\'re currently streamlines, but in the near future I hope to support streaklines and particle flow as well.]({{ site.github.url }}/assets/2009/11/flow.png)

![Scalar fields appear as a mapping of height onto color.  If this function were to be plotted in 3D, it would like a sheet rippling, but sometimes it\'s more useful to see it in 2D.]({{ site.github.url }}/assets/2009/11/scalar.png)

On of the great thing about implementing this on the graphics card is that it doesn't require much CPU time on the machine running it.  Even at 10k frames per second, my MacBook never uses more than 30% of a single core's time.  A place where this particularly shines is on tiled displays - a bunch of HDTVs tiled together to run as if it were one large screen.  In such setups, a computer will control 2-4 screens, and each computer's graphics card has enough power to run the animation for its portion of the screen.  There are still some bugs to be worked out, but I ran a proof-of-concept on one of the tiled displays at KAUST.

![Running a demo of OpenGLot on a KAUST tiled display]({{ site.github.url }}/assets/2009/11/IMG_0014.JPG)

Lately I've been working on getting the 3D analogs of the various 2D primitives working, again all with time dependence (it's the support for animation that really makes this shine in my mind).  So far it's surfaces, parametric curves and surfaces and flow fields, but the flow fields have some work yet.  It turns out that while modern hardware is definitely capable of handling 3D flow fields, it doesn't actually make much sense when you see the result - it's just too busy.  To be able to easily visualize flow in 3D is very much an open problem.

![3D streamlines end up just becoming confusing more than they are helpful.]({{ site.github.url }}/assets/2009/11/3d-flow.png)

In order to get some interesting shapes working, I had to add support for cylindrical and spherical coordinates which is actually providing an interesting challenge - how best to generate the shaders.  The shader source code (that runs on the graphics card) is generated and compiled when you run OpenGLot, and I've not found an altogether easy and intuitive interface for adding simple coordinate transformations to it.  Still, it works, but the programatic interface will likely change.

![This is a torus of sorts, which I got as an example from Grapher.app]({{ site.github.url }}/assets/2009/11/torus.png)

![This is the same torus, just colored by using its surface normals as RGB values]({{ site.github.url }}/assets/2009/11/torus_normals.png)

In order to determine surface normals (which are something usually determined when one defines the geometry of an object), the vertex shader approximates various derivatives numerically.  So far, the shading results have been pretty decent.

![A trigonometric function, colored by mapping the surface normals to colors]({{ site.github.url }}/assets/2009/11/surface_normals.png)

![The superimposition of two trigonometric functions, lit based on their surface normals and a texture to give visual clues about distortion]({{ site.github.url }}/assets/2009/11/surface2_texture.png)

I'm still working on making video of this in action available, but so far a number of the tools I would usually use have come up short.  I've been trying to integrate a video encoder into a utility library for OpenGLot so it can record video straight out of the box, but the framerate is still too low.
