---
layout: post
status: publish
published: true
title: An Explanation of GPUs Anyone Would Love
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 874
date: '2010-07-15 20:06:23 -0700'
date_gmt: '2010-07-16 03:06:23 -0700'
categories:
- computer science
tags:
- gpu
- cpu
- paintballs
- myth buster
comments:
- id: 891
  author: Colin
  author_email: creutter@gmail.com
  date: '2010-07-18 21:53:49 -0700'
  date_gmt: '2010-07-19 04:53:49 -0700'
  content: 'So it turns out that Bozeman has the oldest computer museum in the world.
    Weird, huh. Also, it seems that they are trying to preserve some historical moment
    of the Internet with their website: http:&#47;&#47;www.compustory.com&#47;'
- id: 1168
  author: Jonathon Anderson
  author_email: anderbubble@gmail.com
  date: '2010-10-19 06:31:17 -0700'
  date_gmt: '2010-10-19 13:31:17 -0700'
  content: Hey!  That's me!
---
It's a question that comes up often in conversation, and especially when meeting new people.  The normal pleasantries of where one is from and what one does naturally lead there.  "High-Performance Computing, eh?  What's that?"

I sometimes feel it a mission to dispel myths about supercomputing that the layperson might have.  Pop culture is full of stern-looking authority figures leering at a screen, looking over the shoulder of an endearingly-disheveled nerd.  Or I think Chuck represents this well:

<object width="600" height="475"><embed src="http://www.youtube.com/v/hNYbw3ZqzQw&hl=en_US&fs=1?rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="600" height="475" /></object>

So when answering this seemingly question about what exactly my job entails, I have to start at the bottom, explaining how processors aren't getting any faster (and haven't been for quite a while, relatively speaking).  And how this fact necessitates a different way of looking at programming tasks, moving from "fast" or "deep" to "wide."  Supercomputers aren't single small boxes in the middle of a vast room covered in billions of pixels, as Chuck would seem to suggest.  No, nothing so glamorous.  In fact, seeing a rack of IBM's Blue Gene is more akin to _2001: A Space Odyssey_ - being confronted with a towering black monolith:

![The BlueGene/P system at Argonne National Lab.  The man in the picture is actually now an awesome system administrator for the KAUST Supercomputing Lab!](http://www.alcf.anl.gov/news/media_files/bluegene_p.jpg)

So modern supercomputers are not a single chip that can perform trillions of calculations per second, but are rather a set of relatively simple processors that each perform modestly.  Though when working in concert, the results are astounding.  Not long ago a supercomputer sustained calculations at a rate of 1 [petaflop](http://en.wikipedia.org/wiki/Petaflop), or a million billion operations every second.  If we were to compare that to a relatively modern desktop, a second on that computer is the equivalent of about _four days_ of computation on your desktop.  If the same code were to run on the [computers used in the Apollo missions](http://en.wikipedia.org/wiki/Apollo_Guidance_Computer), it would take approximately 630 years (this is a rough approximation based on a figure of 20 microseconds per add).

The reason for the modest clock rates of each processor in modern devices is power.  Intel successfully grew processor performance by increasing the rate at which operations were performed (among other advances), but at a great cost in power.  For example, a chip on a BlueGene/P compute node runs at a mere 850MHz, though it's impossible to use this number alone to compare performance.  In fact, of the budget allocated for the purchase of a system like that, only half that money goes towards actual equipment.  The rest goes towards the power of not only running it, but cooling the damn thing off.

Graphics cards have become an unlikely source of high-performance computing in the last ten years or so.  It's seen many struggles, from being difficult to program and even harder to debug, to early cards not supporting floating-point calculations and not supporting certain types of loops.  And yet NVIDIA now markets a graphics card with as many as 480 cores.

I recently happened upon this video of Jamie Hyneman and Adam Savage of Myth Busters explaining the difference between a CPU (the brain of your computer for the uninitiated) and a GPU (the part the handles much of the graphics).  When presented with explosions, robots and paintballs, the difference really lights up (skip to 8 minutes in for the _really_ good bit, but the whole thing is worth a watch):

<object width="600" height="475"><param name="movie" value="http://www.youtube.com/v/XtGf0HaW7x4&hl=en_US&fs=1?rel=0"><embed src="http://www.youtube.com/v/XtGf0HaW7x4&hl=en_US&fs=1?rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="600" height="475" /></object>
