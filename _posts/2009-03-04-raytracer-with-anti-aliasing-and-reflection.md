---
layout: post
status: publish
published: true
title: Raytracer with Anti-aliasing and Reflection
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 458
date: '2009-03-04 15:28:44 -0800'
date_gmt: '2009-03-04 22:28:44 -0800'
categories:
- computer science
tags:
- graphics
- raytracer
comments: []
---
For Graphics II, we had to implement a raytracer, and then add anti-aliasing and a feature of our choice.  I selected mirrored surfaces.

First, anti-aliasing.  Here are a few pictures of the same image rendered with a different number of passes to change the smoothness.

![Using one pass]({{ site.github.url }}/assets/2009/03/anti-alias-1.png)

![Using 5 passes.]({{ site.github.url }}/assets/2009/03/anti-alias-5.png)

![Using 50 passes.]({{ site.github.url }}/assets/2009/03/anti-alias-50.png)

And lastly, here's a scene of several spheres, some of which are reflective.

![A set of spheres, some of which are mirror-like.]({{ site.github.url }}/assets/2009/03/output.png)

![A reflective sphere next to some triangles.]({{ site.github.url }}/assets/2009/03/input8r.png)

![A mirrored sphere in the center of four other sphere.]({{ site.github.url }}/assets/2009/03/input12r.png)

![More spheres!]({{ site.github.url }}/assets/2009/03/input16r.png)
