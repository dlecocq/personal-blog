---
layout: post
status: publish
published: true
title: Promises to my OS Prof
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 893
date: '2010-08-13 06:09:15 -0700'
date_gmt: '2010-08-13 13:09:15 -0700'
categories:
- computer science
tags:
- strncpy
- return value
comments: []
---
For me, operating systems was one of the most worth-while courses in my undergraduate career.  Not only gaining insight into the black-box that can be the operating system, but learning a bunch of skills that I have found invaluable since then.

Even in graduate school, I encounter computer scientists that have never used the command line.  While its all well and good to use your IDE, it is absolutely crippling to not be able to do all the same magics from the command line.  Not only that, but there is a wealth of tools accessible from your favorite shell and bash scripting is a useful piece to keep in one's toolbox.  The command line was one thing with which I was better acquainted through operating systems; this was especially true in one project where we had to roll our own shell.  This was particularly good because the shell gives access to a lot of system tools that I've since found I want to use in other programs: forking, dup'ing, interacting with environment variables, etc.

Other good experiences were working with threading libraries and even booting up EC2 instances and testing out code there.  I am extremely grateful to then-professor Mike Colagrosso for making it such a worthwhile experience.  Lately I've been working with code where I remember quality code promises he made us make:

__ALWAYS save the return value of system calls.__  I try to avoid programming in C as much as possible (after all, C++ is usually an alternative, if not Python), but whenever I do I am constantly reminded of this one.  The most common design for functions that I encounter in that kind of code is to accept the variable that is to be updated, and return instead, a code indicating the success/failure/warnings/etc. of the code.  In some cases, the return value is the only way you'll have access to the resource just requested (for example in the case of fork(2) ), but either way it's the basic mechanism for getting feedback about how code has executed.

__NEVER use strcpy(3).__ I've never used a buffer overflow in a clever way (though this is a someday project), or I should say on purpose.  But I've dealt with enough instances of me being distracted and writing bad code that I've gotten to know gdb (the GNU DeBugger) better than I would like.  The strcpy(3) function relies on null character termination to stop copying memory from one string into another.  If, however, a string isn't null terminated or isn't terminated before the length of the string buffer being copied into, then the operation will overrun the buffer.  Instead, __ALWAYS use strncpy(3)__.  It allows you to specify the maximum length that should be copied (like, for instance the length of the buffer being copied into) so as to avoid this embarrassing problem.

Despite the taking the class just over three years ago (it's unsettling to realize its been so long), these few promises have stuck with me.  So Mike, if you're reading this, I'm doing my part!
