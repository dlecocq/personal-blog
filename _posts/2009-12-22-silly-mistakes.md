---
layout: post
status: publish
published: true
title: Silly Mistakes
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 784
date: '2009-12-22 06:33:07 -0800'
date_gmt: '2009-12-22 13:33:07 -0800'
categories:
- computer science
tags:
- opengl
- code
- programming
comments:
- id: 575
  author: Roni Choudhury
  author_email: aichoudh@gmail.com
  date: '2009-12-22 12:14:06 -0800'
  date_gmt: '2009-12-22 19:14:06 -0800'
  content: What was the bug?
- id: 576
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2009-12-22 16:01:09 -0800'
  date_gmt: '2009-12-22 23:01:09 -0800'
  content: |-
    I was trying to display a screen-filling quad, and apparently WebGL (and OpenGL ES 2) doesn't support GL_QUADS, but switching to GL_TRIANGLE_STRIP seems to have solved, though I'm only getting one of the triangles that way.

    What happens when you try to render a quad is a that a single pixel is drawn, and it appears to be on the interior of the primitive, but it's hard to tell.
- id: 579
  author: John Brown
  author_email: wxguy7@gmail.com
  date: '2009-12-23 19:38:16 -0800'
  date_gmt: '2009-12-24 02:38:16 -0800'
  content: "Last paragraph absolutely true for me.  Yet, it is SO HARD to let go and
    do smthg else for a while.\r\n\r\nWe consider it a good day when we find a bug.
    \ The more we find, the better day it is.  But, for every 3 bugs we find, we introduce
    a new one.  So, it seems there are always more out there waiting to be discovered...."
---
Every programmer has had this, or at least I like to think that every programmer has experienced this - you compile, press "go," and epic failure.  And the joy doesn't stop there - then the debugging begins.  Occasionally, one encounters a bug that gets the better of them, sometimes for hours, sometimes for days, and sometimes for [months](http://en.wikipedia.org/wiki/Pentium_FDIV_bug).

Hairs is pulled, teeth are gnashed, and eyeballs strain, scouring line after line.  You try to convince yourself that your algorithm is correct, and that each line of code is justified.  And yet, it still gets the better of you.

After perhaps eight hours, you swallow your pride, and ask a trusted friend to take a look.  Often the very act of explaining things to another human being is helpful, but sometimes you both have to dig into the code.  Maybe a third friend happens upon the two of you, and joins in.

Then, a light bulb goes off.  If you're lucky, it's a massive structural change that's required, but sometimes, it's a single line, or a single word or character, and you suddenly find yourself embarrassed.  But do not be.  Every programmer I've ever met, no matter how qualified has run into these problems.  Still, I find it easy to doubt my competence afterwards.

There are rare and beautiful moments when not only does code compile on the first try, but it runs as expected.  Few and far between, cherish these when they come.

This is all inspired from a recent bug I tracked down.  An embarrassing one.  Sure, had I read the 350 or so pages of the OpenGL ES 2.0 specification, I may have caught it earlier, but this was one of those times when it was a single word that had to change.  __I tell myself that I won't keep making these kinds of mistakes, and with each conquered bug I gain a tool, an experience point, and that's what makes one's craft.__

I've looked at the time I spend debugging, and I've noticed that the time it takes to solve a bug can often be reduced by leaving the problem for a bit.  Taking a walk, getting a cup of coffee, or sometimes watching an episode of Arrested Development.  __The desire to find and fix a bug is a siren's song - nearly impossible to walk away from, but often a bad idea.__
