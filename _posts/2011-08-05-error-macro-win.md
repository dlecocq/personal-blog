---
layout: post
status: publish
published: true
title: Error Macro Win
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 972
date: '2011-08-05 09:31:54 -0700'
date_gmt: '2011-08-05 16:31:54 -0700'
categories:
- computer science
tags:
- computer science
- macro
- error
comments: []
---
Still porting Linux code to Mac, I've been trying to keep a useful habit: using the #warning and #error macros. This new code is riddled with #ifdef's checking whether or not we're trying to build on a Mac, and using alternatives to the Linux-only system calls, but in parsing these large chunks of code, sometimes I forget what I'm doing. How horrible would it be to accidentally leave empty the Mac-only code block when it's meant to actually do something.

So, whenever I open up one such block, I add a little macro:

```
#ifndef MAC
// ... The Linux-only code
// ... takes up
// ... a lot
// ... of space
#else
#error "Don't forget to implement it as Mac!"
#endif
```

At least I'll always catch it at compile time, and when I fix/add the Mac-only code, then I can go ahead and remove that macro. It's not that I'm forgetful, but I've shot myself in the foot so much at this point.
