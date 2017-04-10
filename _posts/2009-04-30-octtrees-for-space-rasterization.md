---
layout: post
status: publish
published: true
title: Octtrees For Space Rasterization
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 525
date: '2009-04-30 14:49:09 -0700'
date_gmt: '2009-04-30 21:49:09 -0700'
categories:
- computer science
tags:
- graphics
- ray tracing
- octtree
- computational geometry
comments: []
---
Raytracing is slow.  Incredibly slow.  _Painfully_ slow.  That's because you've got to check a lot of things to accurately determine what you're seeing, if it's in shadow, if it reflects off of something, etc., so it helps quite a bit to be able to get an idea beforehand of where everything is.  Enter octtrees.

We've got a picture of a model (in this case, the Stanford bunny model).  It consists of thousands of tiny triangles that make a surface.  Then, imagine a cube surrounding the entire model.  If there are two many triangles in that cube, you cut the cube in to eight smaller cubes, and repeat.  What this build is a tree where "busy" portions of the space get divided more.

And now for pretty pictures:

![The bunny on its own.  There are tricks to smooth it out, but I left it highly triangulated to better represent the idea.]({{ site.github.url }}/assets/2009/04/bunny.png)

![Bunny with balanced wireframe octtree around it.]({{ site.github.url }}/assets/2009/04/bunnytree.png)

![Profile of the bunny with a very deep octtree.]({{ site.github.url }}/assets/2009/04/bunnytreeside.png)

I'm finishing up the implementation, and then I'll be using it as part of my octtree as a intersection speedup.
