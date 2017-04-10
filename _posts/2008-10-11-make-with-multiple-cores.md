---
layout: post
status: publish
published: true
title: Make With Multiple Cores
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 125
date: '2008-10-11 20:09:12 -0700'
date_gmt: '2008-10-12 03:09:12 -0700'
categories:
- computer science
tags:
- make
- multiple cores
- building
- ninja magic
comments: []
---
I was building something, and I remembered a friend was saying a while ago that you could tell gcc how many cores to use when building something.  I don't know if that's true or not, but it turns out you can certainly tell make:

```
make -j(number of cores to use)
```

For example,

```
make -j2
```

I took a screen capture of System Monitor after building each way (make and make -j2), to see the difference.  The first box is using just one core, and the second is using both.

![Multicore Make]({{ site.github.url }}/assets/2008/10/multicore-make.png)

I had initially thought I'd have to tell gcc, and so I had planned to edit the makefile to automatically find the number of cores on the system, and then run gcc with that as an argument, so I went in search of how to find the number of cores on a Linux system.  It turns out the easiest way to get that number that I came across was to use /proc/cpuinfo:

```
cat /proc/cpuinfo | grep 'cpu cores' | head -1 | sed -r 's/^.+([[:digit:]]+)/1/'
```
