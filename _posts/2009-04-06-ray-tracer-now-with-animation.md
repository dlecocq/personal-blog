---
layout: post
status: publish
published: true
title: Ray Tracer - Now With Animation
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 495
date: '2009-04-06 20:16:04 -0700'
date_gmt: '2009-04-07 03:16:04 -0700'
categories:
- school
- projects
tags:
- graphics
- ray tracer
- animation
- render
comments:
- id: 314
  author: Matt Matteson
  author_email: Matt@dlzip.com
  date: '2009-04-10 00:20:48 -0700'
  date_gmt: '2009-04-10 07:20:48 -0700'
  content: "I'm glad you put this all together. \r\n\r\nTo think all of the Pixar
    videos done in this fashion; cool."
- id: 316
  author: Dan
  author_email: dlecocq@mines.edu
  date: '2009-04-10 11:44:40 -0700'
  date_gmt: '2009-04-10 18:44:40 -0700'
  content: Once I get a few more features implemented (object refraction, octrees,
    fixed lathe normals, and world rotation &#47; translation), I'm going to make
    a clip (I'm thinking about 1-2 minutes in HD) that's a little more involved, and
    really shows some of the capabilities.  I do have a clip with reflections, which,
    when they work, are pretty realistic, but there are still some residual artifacts
    from erroneous normals.
---
It occurred to me today that I could render a scene several times with slight perturbations and then mesh them together into a movie.  It took about 15 minutes to render on a cluster at Mines, and then about a minute to stitch together with Mencoder.  At 18 frames per second, here is the result.  Enjoy!

<object width="425" height="344"><param name="movie" value="http://www.youtube.com/v/mWT0UOBTT5Y&hl=en&fs=1&rel=0&color1=0x006699&color2=0x54abd6"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/mWT0UOBTT5Y&hl=en&fs=1&rel=0&color1=0x006699&color2=0x54abd6" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="344"></embed></object>
