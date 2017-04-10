---
layout: post
status: publish
published: true
title: Conditional Compilation
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 983
date: '2011-08-08 13:38:32 -0700'
date_gmt: '2011-08-08 20:38:32 -0700'
categories:
- computer science
tags:
- make
- autoconf
comments: []
---
Last week I had the (dis)pleasure of porting some code to Mac, and today it came time to merge with the original codebase. As helpful as it was to use macros for different code paths, we needed something in the makefile to optionally add flags when compiling on Mac.

```C
// This is all well and good
#ifndef __APPLE__
    // Do your Linux-y includes here
#else
    // Do your Apple-y includes here
#endif
```

Apparently, there are a couple conventions for doing this. First, you can inject a configuration step (à la autoconf, for example) which would detect what platform you're building on in a robust way and build a Makefile for you. Second, if you're lazy or autoconf would be like hitting a fly with a hammer, you can use make's conditionals:

```make
# Ensure that this gets declared in time, and fill it with the result of `uname`
UNAME := $(shell uname)

# If the environment is Darwin...
ifeq ($(UNAME), Darwin)
    CXXFLAGS = # Something Apple-y
else
    CXXFLAGS = # Something Linux-y
endif
```

Simple enough!
