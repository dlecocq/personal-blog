---
layout: post
status: publish
published: true
title: Stanford Dragon and Gouraud Shading
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 540
date: '2009-05-12 11:57:38 -0700'
date_gmt: '2009-05-12 18:57:38 -0700'
categories:
- school
- computer science
- projects
tags:
- graphics
- ray tracing
- models
- octtrees
- gouraud shading
comments: []
---
I recently finished up school, and part of that was finishing up my ray tracing project.  At the last minute, I implemented Gouraud shading which is a technique to try to smooth out a triangulated surface.  What it really does is just linearly interpolate the normal vectors, where the normal of a vertex is calculated as a weighted average of the normals of the triangles using that vertex.

Long story short:

![A render of the Stanford bunny with my raytracer without Gouraud shading.]({{ site.github.url }}/assets/2009/05/bunny1.png)

![A render of the Stanford bunny with smooth Gouraud shading.]({{ site.github.url }}/assets/2009/05/bunnysmooth.png)

Also, thanks to an improvement in my parallelization of the problem and a speedup in octtree traversal, I was able to render the Stanford dragon model (~1 million triangles):

![The Stanford dragon model.]({{ site.github.url }}/assets/2009/05/dragon.png)
