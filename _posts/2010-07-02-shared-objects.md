---
layout: post
status: publish
published: true
title: Shared Objects
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 859
date: '2010-07-02 11:54:37 -0700'
date_gmt: '2010-07-02 18:54:37 -0700'
categories:
- miscellany
tags:
- shared objects
- static linking
- dynamic linking
comments: []
---
Shared objects are great.  Imagine you have several programs running that all make use of the same library.  If they are all statically linked against that library, then there will be several copies of essentially the same code in memory.  Shared objects allow all these programs to reference the same code, held in memory in only one spot.

I've recently been spending a lot of time trying to get a few key libraries compiled on a cluster, where the idea is to run jobs based on these libraries in parallel.  As memory is particularly limited, and there are several cores per node, I figured it would particularly make sense to compile everything as a shared object.  Also, a subsequent library depended on it.

A lot of different packages configure, build and install themselves in a number of ways and often don't adhere to conventions.  Despite trying every flag known to man into the configuration tools, I was unable to get a particular piece to build as a shared object.  But I happened upon a [particularly useful code snippet](http://www.tipcache.com/tip/Convert_a_static_library_(.a)_to_a_shared_object_(.so)_12.html) to save the day:

```bash
ar -x mylib.a
gcc -shared *.o -o mylib.so
```
