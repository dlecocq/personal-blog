---
layout: post
status: publish
published: true
title: Ray Tracer - Texturing Support
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 501
date: '2009-04-24 11:26:51 -0700'
date_gmt: '2009-04-24 18:26:51 -0700'
categories:
- computer science
tags:
- graphics
- ray tracer
- raytracing
- earth
- texturing
comments:
- id: 321
  author: CQ
  author_email: creutter@gmail.com
  date: '2009-04-26 15:50:29 -0700'
  date_gmt: '2009-04-26 22:50:29 -0700'
  content: "That is pretty cool.\r\n\r\nThere is a project at sourceforge for providing
    real time cloud maps.\r\n(http:&#47;&#47;xplanet.sourceforge.net&#47;clouds.php)"
- id: 322
  author: Dan
  author_email: dlecocq@mines.edu
  date: '2009-04-26 22:09:14 -0700'
  date_gmt: '2009-04-27 05:09:14 -0700'
  content: Nice.  I did a quick render with one of their pictures, but was disappointed
    with how lackluster it looked without color.  But I did find some links from there
    that worked out pretty well for textures for other planets (see most recent post).
- id: 326
  author: CQ
  author_email: creutter@gmail.com
  date: '2009-04-28 03:15:51 -0700'
  date_gmt: '2009-04-28 10:15:51 -0700'
  content: Could you add (or whatever it's called...screen maybe) the pictures together
    and then render it.
---
It's all well and good to be able to render shapes in space in a photorealistic way, but at some point you'd like to draw something that doesn't have just one surface color.  After all, a billboard isn't just a bunch of shapes each of which has one color - it's one object with paint / ink placed on it in an ordered way.

Texturing accomplishes by taking a primitive shape (like a sphere, triangle, surface of revolution, etc.) and wrapping an image onto and over it.  Let's consider a sphere in space:

![A white sphere in space.]({{ site.github.url }}/assets/2009/04/output4.png)

Now let's say we mean it to be Earth.  Then we can take a picture of Earth that's flat:

![Flattened map of Earth]({{ site.github.url }}/assets/2009/04/texturesmall.png)

and then map it onto a sphere to get a picture of what we all know Earth to look like:

![Behold!]({{ site.github.url }}/assets/2009/04/earth.png)

![Two Mars globes where the left is what is seen with the eye, and the right is a topographic map.]({{ site.github.url }}/assets/2009/04/mars-twin.png)
