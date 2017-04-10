---
layout: post
status: publish
published: true
title: Memory Leak
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 165
date: '2008-11-24 23:48:07 -0800'
date_gmt: '2008-11-25 06:48:07 -0800'
categories:
- school
- computer science
- projects
tags:
- memory leak
- gdb
- segmentation fault
comments: []
---
Memory management is a notoriously difficult aspect of coding in C++.  Generally, the problems one runs into with pointers is that you get rid of the data you're pointing to while you still need it.  Gdb has become a good friend for finding segmentation faults.

For those of you who aren't computer scientists, here's a quick explanation - we need space to store variables and information.  So, one way to do this is ask the system for some space, and then the system gives back an address.  Imagine mailboxes at the post office - you don't have the stuff stored in your mailbox with you at all times, but rather the way (the key) to access it.  One problem that arises when you tell the post office you don't need the mailbox anymore, but you don't give back the key.  Someone else is assigned this mailbox, and his mail starts arriving in there, and when you go looking for yours, it's not what you expect (this often causes a segmentation fault).  The other problem is when one patron keeps requesting mailboxes, and you're only allowed to hold one key at a time, so you discard the old ones.  If you request too many, no mailboxes are left (this is a memory leak)!

At any rate, I don't have much experience tracking down memory leaks, and so when I came across this problem, I asked an open question to everyone in the lab of the best way to do this.  Someone suggested I put soapy water on my program and look for bubbles.

I ended up looking through my code for places where this might be happening, and I happened to find it pretty quickly.  That's pretty lucky.

![A memory leak gets out of control]({{ site.github.url }}/assets/2008/11/leak-1.png)

![We get our memory back when the program is terminated.]({{ site.github.url }}/assets/2008/11/leak-2.png)

![I got gdb to seg fault!]({{ site.github.url }}/assets/2008/11/picture-3.png)
