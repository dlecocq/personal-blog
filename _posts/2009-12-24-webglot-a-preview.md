---
layout: post
status: publish
published: true
title: webGLot - A Preview
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 787
date: '2009-12-24 05:14:40 -0800'
date_gmt: '2009-12-24 12:14:40 -0800'
categories:
- computer science
- math
tags:
- graphics
- math
- webgl
- openglot
- plotting
- webglot
comments:
- id: 581
  author: Matt Matteson
  author_email: matt@dlzip.com
  date: '2009-12-25 00:19:23 -0800'
  date_gmt: '2009-12-25 07:19:23 -0800'
  content: "Thanks for the sneak peak. How does the frame rate compare to OpenGLot?\r\n\r\nGo
    ninja go!"
- id: 582
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2009-12-25 02:42:26 -0800'
  date_gmt: '2009-12-25 09:42:26 -0800'
  content: It's not quite as good as with OpenGLot.  For equivalent primitives, OpenGLot
    gets about 300 fps where WebGL gets 60-90.  Still, it's real-time.
- id: 642
  author: Jan
  author_email: jan@poeschko.com
  date: '2010-01-02 14:20:14 -0800'
  date_gmt: '2010-01-02 21:20:14 -0800'
  content: Thank you for this report, looks awesome! Are there any plans of releasing
    webGLot to the public? I would be very much interested in a (web&#47;JavaScript)
    library capable of plotting 3-D functions...
- id: 645
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2010-01-02 21:40:36 -0800'
  date_gmt: '2010-01-03 04:40:36 -0800'
  content: |-
    Yes.  I have every intention of making this project open source, but as I developed it while going to school here, I will need KAUST's permission to do so.  I don't anticipate that this will be a problem, but I will have to wait until then.  I have prepared a release - I'm just waiting on approval.

    Thanks for the interest!
- id: 770
  author: Jason
  author_email: jason-sage@creativetrax.com
  date: '2010-03-31 17:31:37 -0700'
  date_gmt: '2010-04-01 00:31:37 -0700'
  content: It would be very interesting to see if this could be integrated into Sage
    (http:&#47;&#47;www.sagemath.org) as a 3d plot viewer.  Please let us know when
    you put the code up online.
- id: 959
  author: Pete
  author_email: parente@cs.unc.edu
  date: '2010-07-27 09:54:23 -0700'
  date_gmt: '2010-07-27 16:54:23 -0700'
  content: Any luck on getting the library released? I saw the SIGGRAPH paper, so
    I assume something is still in the works?
- id: 960
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2010-07-27 10:01:30 -0700'
  date_gmt: '2010-07-27 17:01:30 -0700'
  content: Thanks for the interest, and I hope you're able to swing by the talk tomorrow
    (Wednesday).  A release is something that I'm aiming for, but for the moment it
    lacks a few things (examples and polish for example), and it clouded by some other
    issues.  I hope to have something out soon after getting back to school and having
    some time to focus!
- id: 1000
  author: ged
  author_email: gedw99@gmail.com
  date: '2010-08-12 17:17:34 -0700'
  date_gmt: '2010-08-13 00:17:34 -0700'
  content: "Please let me know when you release. \r\nwe are working on a multi GPU
    webgl project at the moment.\r\n\r\nPart of it requires direct feedback webgl
    for the real time physics feedback.\r\n\r\nGed"
---
I've [mentioned WebGL before]({{ site.baseurl }}{% post_url 2009-09-22-the-future-of-the-internet %}), and I think it could be very important.  There is a [competitor from Google](http://code.google.com/apis/o3d/), but like OpenGL and OpenCL, this API is managed by the [Khronos Group](http://www.khronos.org/) and that fact appeals to me.  Perhaps it's that I've used it fairly extensively, but I really like OpenGL.  Despite its quirks, it's quite powerful.

The big "get" is that it gives programmers access to hardware-accelerated graphics from directly within the browser.  There's a lot of interest in this arena for game development as it would obviate much of the need for separate distributions based on operating system.  (Skip to the end for more of an opinion on this subject.)

As such, I've been working with WebGL as opposed to the Google-proposed O3D.  (I have every intention to explore O3D, time permitting, as there are some jagged edges to the current specification.)  The result of this recent toil is a budding WebGL implementation of my OpenGLot project.  It's still in early stages, but in the coming weeks, it should develop even further.  To whet appetites, I have a few pictures.

![A scalar field, my persistent test function.]({{ site.github.url }}/assets/2009/12/Picture-105.png)

![A 3D surface, again one of my usual test functions.]({{ site.github.url }}/assets/2009/12/Picture-111.png)

I seriously doubt that WebGL will every match the performance of OpenGL.  Even though JavaScript interpreters are getting faster at a somewhat alarming rate, they won't match the speed of C or C++.  That said, if one can appropriately offload work onto the GPU, it won't matter as much, but there will always be that overhead.

It won't so much be a matter of having the same performance, but _enough_ performance.  If a person can go to a single webpage and get 60 frames per second performance in a game or tool without having to install software, that's tremendous.  Currently I've been getting between 60 and 90 frames per second with WebGLot, and I'm sure I can keep that number up as more features are added.

My hope is that this will be a tool and library that has a wide-enough feature set by the time WebGL is widely adopted that becomes often-used.  But that's just ego.  The purer motivation is that if you're a math teacher, and you want to have interactive demonstrations of Newton's method, or parametric surfaces, or even flow fields, you can write an application in 20 minutes that does all the heavy lifting of graphing it for you.  As long as you can describe the mathematical primitives, you should be able to render it.  Of course there will be a general-purpose grapher available for any calculus student who's having trouble visualizing this or that, too.  Or a resourceful PDE student who need to solve his homework (the GPU-based PDE solver will take a little bit more time, but it's very nearly complete).

In short, the strength of WebGL is that is has respectable performance, and in a year's time, half the browsers (well maybe not half) on computers will support it, giving the average internet-user access to a wealth of media.
