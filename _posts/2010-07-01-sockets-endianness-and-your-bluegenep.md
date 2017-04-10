---
layout: post
status: publish
published: true
title: Sockets, Endianness and Your BlueGene/P
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 855
date: '2010-07-01 12:32:36 -0700'
date_gmt: '2010-07-01 19:32:36 -0700'
categories:
- miscellany
tags:
- endianness
- bluegene
comments: []
---
Endianness is one of those things that, as a computer scientist you learn about but rarely have to think about.  It does occasionally come into play and I recently had some frustration with it.

For the uninitiated, it's talking about the [order in which bytes are stored](http://en.wikipedia.org/wiki/Endianness) in memory, and unsurprisingly, different processors have different philosophies regarding this.

The term itself comes from Gulliver's Travels, when two groups have strongly-held beliefs regarding on which end it was best to crack a hard-boiled egg.  And as in the book, it can cause tension.

I'm working with a library in which a server and client communicate over sockets, and they tend to prepend their messages with the length of the message to follow.  In the code, it's stored as a four-byte integer, and for the most part, it works beautifully.  However, we recently ported it to the BlueGene/P, which uses PowerPC chips.  These, unlike the common Intel chip, are big-endian, and so client and server would hang, waiting for an exceptionally large message when only a small one was sent.  For example, there are some common messages that are 329 bytes long.  If you interpret the value 329 using the alternative endianness, you'll expect 1224802304 bytes, or about 1.2 GB.

I'll admit that it took a while to catch, but we eventually got it figured out.  We don't use sockets much, but couldn't imagine that this was a problem that hadn't been encountered before.  After all, the internet uses sockets, has been around for a long time, and it's not as if big-endian devices aren't allowed on.  It turns out that there is in fact a convention - that information sent over sockets ought to be in big-endian format, but networking libraries provide you with functions to help out with this.

The functions `htons`, `htonl` and sometimes `htonll` convert `H`ost `to` `n`etwork two-byte, four-byte and eight-byte messages respectively.  And the inverse functionality is encapsulated by `ntohs`, `ntohl` and `ntohll`.

Lesson learned.
