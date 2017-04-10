---
layout: post
status: publish
published: true
title: OpenGLot - Scalar Fields
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 694
date: '2009-11-08 07:22:05 -0800'
date_gmt: '2009-11-08 14:22:05 -0800'
categories:
- computer science
tags:
- graphics
- opengl
- openglot
- computer science
- fragment shader
comments: []
---
I'm working on OpenGLot (my OpenGL plotting library) for a class project, and two of the features I decided to implement were contour lines and scalar fields in 2D.

A few days ago I got decent-looking contour lines working and today I got scalar fields implemented with a fragment shader.  The programmer using the library can specify a function in the form of a string and have it plotted as a scalar field.  Quickly.  Really quickly.

Modern graphics cards support shaders, which are programs that get run on the graphics card, and in parallel. This is great for algorithms that can be run in isolation (one pixel doesn't need to know what the others are doing), which is the case here. OpenGLot generates a fragment shader that colors a single pixel based on the value of the function.  Each of the dozens or hundreds of cores on a GPU runs the same code in parallel for their particular pixel.

![Contouring for a sinusoidal function with the isovalue 0.]({{ site.github.url }}/assets/2009/11/Picture-16.png)

![Here\'s a first look at the results (taken moments after this first worked for me).  It\'s the same sinusoidal function, and I will be improving upon the color mapping in the coming hours.]({{ site.github.url }}/assets/2009/11/Picture-19.png)

The graphing program I use, Grapher.app is rapidly showing its age.  The results it gives for the same function (though using a much better coloring scheme) are either grainy or extremely slow (10 or more seconds).  OpenGLot is generating these in less than 0.1 seconds.  (Grapher.app implements its scalar fields on the CPU, so comparing times is a little like comparing apples and oranges.  Still, responsiveness in this type of matter is important.)

![The quick (and grainy) plot in Grapher.app]({{ site.github.url }}/assets/2009/11/Picture-17.png)

![The slow (but smooth) plot in Grapher.app]({{ site.github.url }}/assets/2009/11/Picture-18.png)
