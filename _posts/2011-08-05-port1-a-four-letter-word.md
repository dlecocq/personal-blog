---
layout: post
status: publish
published: true
title: 'port(1): A Four-Letter Word?'
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 980
date: '2011-08-05 22:26:45 -0700'
date_gmt: '2011-08-06 05:26:45 -0700'
categories:
- computer science
tags:
- port
- macports
comments: []
---
To me, port has always been kind of a dirty word. Sure, it's nice to have a package manager for Mac, especially after getting used to apt-get. Still, things tend to show up in weird places, and paths get confused.

For instance, I was extremely frustrated this week to find that on OS X Lion, gcc-4.4.5 just would... not... compile. Frustrating stuff. I was tasked with porting this enormous existing in-house code base (of about 60-100k lines) to Mac, but was dismayed to find that they required C++0x features, which are unsupported in gcc 4.2.

Giving up, I turned to MacPorts as a broken, empty shell of a man. MacPorts was able to compile it, though relegated to /opt/, and though I could add that to my path, this new version of gcc wasn't ready to consider the libraries I had installed in /usr/local/ by hand. Of course, I could edit all the makefiles, or do some other magics, but it turns out MacPorts can be bent to your will.

Like most, I had installed the binary release of MacPorts, configured to live in /opt/, but if you instead __build from source__, you can:

```
./configure --prefix=/usr/local --with-unsupported-prefix
```

This has not only MacPorts reside in /usr/local/, but then it will also in turn install its packages there as well! I don't think I'm the only one who appreciates that kind of consistency -- all my libraries in the right place. I still feel slightly dirty whenever I have to rely on port, but at least when I do, I can save a little face.
