---
layout: post
status: publish
published: true
title: Stanford Bunny
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 534
date: '2009-05-03 23:16:52 -0700'
date_gmt: '2009-05-04 06:16:52 -0700'
categories:
- computer science
tags:
- graphics
- ray tracing
- ray tracer
- stanford bunny
- models
- scan
comments: []
---
The Stanford Bunny is a graphics benchmark of sorts.  It was a high-resolution scan that the imaging lab there did of a ceramic bunny, and the triangulation is a popular model to test systems on.

It contains a little under 70,000 triangles which makes brute-force ray tracing intractable.  I mentioned octtrees earlier, and so having built octtrees into my ray tracer, I was able to render the Stanford Bunny in about 40 minutes on one core.  Granted, that's with only 1-pass anti-aliasing, but I feel pretty good about this.  I don't think I'll have a chance to implement Gouraud shading (or normal interpolation for that matter), but as soon as I do, it will look a lot less blocky.

![The Stanford Bunny rendered with my ray tracer.]({{ site.github.url }}/assets/2009/05/bunny.png)
