---
layout: post
status: publish
published: true
title: 'Ray Tracer Feature: Lathes'
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 488
date: '2009-04-04 21:19:28 -0700'
date_gmt: '2009-04-05 04:19:28 -0700'
categories:
- miscellany
tags: []
comments: []
---
Up to this point, my ray tracer had been limited to rendering spheres and triangles, and, while there's a lot you can do with these primitives, it's often more efficient and effective to use a lathe or surface or rotation.  Imagine you've got a curve, and you rotate it around some axis, keeping track of the surface it swept out.

Alternatively, imagine a lump of clay on a clay wheel.  As the wheel rotates, if you hold some shape against the clay, it will become a solid that's symmetrical about the vertical axis.  Here's a sine curve rotated about $$x = 0$$:

![A sinusoidal lathe and a sphere.]({{ site.github.url }}/assets/2009/04/output3.png)

![A polynomial curve rotated about x=0.]({{ site.github.url }}/assets/2009/04/poly_lathe_1_reflect.png)
