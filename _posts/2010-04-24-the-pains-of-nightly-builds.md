---
layout: post
status: publish
published: true
title: The Pains of Nightly Builds
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 823
date: '2010-04-24 23:24:19 -0700'
date_gmt: '2010-04-25 06:24:19 -0700'
categories:
- computer science
tags:
- webgl
- bugs
- floating point textures
comments: []
---
I've been working with WebKit a lot lately.  Specifically, WebGL.  It's fantastic, and it has the potential to change a lot of important applications, but working with nightly builds is... well, frustrating.

I've been using a revision released in December.  Some later revisions have weird behaviors and draw pixelated, but I've finally come across a problem with r52426 that I just can't circumvent - floating-point textures.  They just don't seem to work properly.  I had noticed the bug before, but it wasn't absolutely crucial before.  Rather, the real bug is that you can't initialize floating-point textures from the JavaScript side.

They've fixed this in later versions, but many of these that have this bug fixed also have a problem with gl.viewport, which is pretty mission-critical.  So now I'm sifting through the changelog, hoping to find a release somewhere in the middle that isn't completely broken.

__Update:__ Victory! If you're going to be developing WebGL stuff on Mac, I'd recommend WebKit r53036.  It seems to have everything I need (so far) fixed.
