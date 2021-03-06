---
layout: post
status: publish
published: true
title: New Render
author:
  display_name: ''
  login: ''
  email: ''
  url: ''
wordpress_id: 508
date: '2009-04-26 21:56:54 -0700'
date_gmt: '2009-04-27 04:56:54 -0700'
categories:
- computer science
tags:
- graphics
- ray tracing
- ray tracer
- animation
- texturing
- planets
- clips
comments:
- id: 323
  author: Andrew Ferguson
  author_email: andrew@fergcorp.com
  author_url: http://andrewferguson.net
  date: '2009-04-26 23:48:19 -0700'
  date_gmt: '2009-04-27 06:48:19 -0700'
  content: 'Queue Holst: http:&#47;&#47;en.wikipedia.org&#47;wiki&#47;File:Holst-_mars.ogg'
---
I got a new render up from my ray tracer that applies planetary textures to spheres and makes them spin on their respective axes (none of the planets in our solar system spin on a "vertical" axis).  I hope to do one with their orbits, but I haven't had a chance to get to it; though, the nice thing is, I just have to define their paths and rotations as a function of time, and where I want the viewpoint to be.  It took about 15 minutes to render in full HD 1080x1920 on 18 processors:

<object width="480" height="295"><param name="movie" value="http://www.youtube.com/v/z56qL2bHqNo&hl=en&fs=1&rel=0&color1=0x2b405b&color2=0x6b8ab6"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/z56qL2bHqNo&hl=en&fs=1&rel=0&color1=0x2b405b&color2=0x6b8ab6" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="295"></embed></object>
