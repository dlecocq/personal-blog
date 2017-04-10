---
layout: post
status: publish
published: true
title: NP-Complete Library Puzzle
author:
  display_name: ''
  login: ''
  email: ''
  url: ''
wordpress_id: 50
date: '2007-10-05 09:42:29 -0700'
date_gmt: '2007-10-05 16:42:29 -0700'
categories:
- computer science
tags:
- np-complete
- complexity theory
- puzzle
- ah-ha
comments:
- id: 28
  author: Matt M
  author_email: Matt@dlzip.com
  author_url: http://MattMatteson.com
  date: '2007-10-05 12:27:53 -0700'
  date_gmt: '2007-10-05 19:27:53 -0700'
  content: "Take on me. I'll be gone... \r\n\r\nCongrats on the solving."
---
It seems like the last month, the only thing on my mind is NP-completeness.  For those of you who are not cool enough, er, nerdy enough to know about this class of problems, the basic idea is this: if you want to solve a NPC problem, you're f**ked.  See [Wikipedia](http://en.wikipedia.org/wiki/NP-complete).

The library on campus has had a puzzle available for people to take a crack at, with the potential for $50 at the book store.  If you can solve one half of it, you get one entry, and if you can solve the other half, you get a second.  The drawing is at 1 PM today.

The problem?  Shape-separability.  You've seen these genre of puzzles before: a hopeless tangle of metal parts one of which can be removed from the mess.  This... is an NP-Complete problem.

We even talked about shape-separability in Applied Algorithms, proving that it's NPC by reducing it from set-partition - a problem we proved NPC on a homework (I used subset-sum).  (A quick note: a problem is shown NPC by demonstrating that a known NPC problem, and reduce it to your problem, the thinking being that if you can solve your problem in polynomial time, you can solve this NPC complete problem in polynomial time.  Therefore, your problem is in NPC.)

I took a look at it yesterday and played with it for about an hour, leaving irked that I couldn't solve it - I had expected not a physical puzzle, but rather something a computer scientist might like.  I had also expected that it would be the kind of thing I could just show up for and solve on the spot.  On the way to school this morning, I had a sort of 'ah-ha' moment (no, not "Take On Me"), and so before class, I hopped on over the library and the solution was exactly what I had come up with.  A good start to hopefully a good day.

I've got my two entries and we'll see what happens at 1 - it's a tough problem (after all, it's NPC), and it was not well-advertised.
