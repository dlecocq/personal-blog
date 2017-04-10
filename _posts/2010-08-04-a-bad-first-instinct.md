---
layout: post
status: publish
published: true
title: A Bad First Instinct
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 890
date: '2010-08-04 09:33:19 -0700'
date_gmt: '2010-08-04 16:33:19 -0700'
categories:
- computer science
tags:
- refactoring
comments: []
---
It's an itch.  A compulsion.  Sometimes when working with a new library I get a very strong impulse to do a very bad thing -- reinvent the wheel.  Or, in this case, re-write the wheel.

It's easy to object to the way code is organized, and can cause a certain amount of discomfort.  Whether it's the desire to go through and reformat code (braces belong on the same line as the if statement!) or the pain of hacking together relatively incompatible library designs, it can be unpleasant.

Something that I've been pushing myself to do, and slowly learning to do is to be comfortable with that discomfort.  To resist the urge to rewrite code, as it's never just a matter of rewriting it, but also testing it, an so forth.  I'm slowly beginning to accept the painful truth: no code is perfect.

That said, there are times when I do rewrite libraries.  Sometimes you're handed code from ten years ago that's no longer applicable, or antiquated, or just plain ugly.  In these scenarios it's perfectly justified to make large sweeping structural changes (with the protection of your favorite version control, of course).  Just, hold off.  Wait, and try to use the library, and the first-pass issues will either grow into systemic problems or wither and recede into the cracks.
