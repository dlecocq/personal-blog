---
layout: post
status: publish
published: true
title: System Stats in Python
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1016
date: '2011-09-07 09:24:48 -0700'
date_gmt: '2011-09-07 16:24:48 -0700'
categories:
- computer science
tags:
- python
- psutils
comments: []
---
Turns out, there's a pretty handy package called [psutil](http://code.google.com/p/psutil/) that allows you to not only gain insight into the currently-running process, but other processes, physical and virtual memory usage, and CPU usage. For example:

```python
import psutil

psutil.phymem_usage().percent
# 31.2

psutil.virtmem_usage().percent
# 0.0
```

Pretty handy tool if you're doing any sort of monitoring!
