---
layout: post
status: publish
published: true
title: Wrapping printf(1)
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 914
date: '2011-02-24 12:39:18 -0800'
date_gmt: '2011-02-24 19:39:18 -0800'
categories:
- computer science
tags:
- c#
- ninja magic
- hacks
- programming
- tricks
- tips
- printf
comments:
- id: 1407
  author: Andrew Ferguson
  author_email: andrew@fergcorp.com
  date: '2011-02-25 16:12:18 -0800'
  date_gmt: '2011-02-25 23:12:18 -0800'
  content: 'Why not set different levels for the "error" function? You could set some
    as errors and others as notices...sort of like what PHP does: http:&#47;&#47;www.php.net&#47;manual&#47;en&#47;errorfunc.constants.php
    with "error_reporting()"'
- id: 1427
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2011-02-27 15:20:30 -0800'
  date_gmt: '2011-02-27 22:20:30 -0800'
  content: That's a good approach. The having different file descriptors is akin to
    an approach used in some code I work with, VisIt from LBNL.
- id: 3160
  author: buy facebook fans
  author_email: Torez88625@aol.com
  date: '2014-07-24 07:14:03 -0700'
  date_gmt: '2014-07-24 14:14:03 -0700'
  content: I would like to voice my gratitude to your kindness supporting individuals
    who really should have assistance with this important area. Your own dedication
    to finding the most effective along became exceedingly productive and get truly
    empowered women as i am to go to their pursuits. Your important useful information
    indicates these many any person like me and more to my office colleagues. Regards;
    from everyone of us.
---
Working on an application that had become a little... verbose, I decided it was finally time to wrap my prints in a function that could easily be switched on or off depending on whether or not I wanted it to be verbose.  One approach I had seen before (from my OS professor) that has a certain amount of merit is to wrap statements with a macro:

```
#ifdef DEBUG

printf(....);

#endif
```

The nice thing about this approach is that debugging can be turned on or off easily at compile time.  However, my experience has been that it leads to a lot of typing, and seeing too many macros in the middle of code makes my brain explode in a fiery rage.  So, I figured that if I wrapped my prints in another function (I called mine 'log' and 'error'), I could avoid this whole mess and keep my sanity.  I've done this with a number of other projects in other languages, but I had to learn some magic to do it in C.

Lesson Learned #1 : Variable arguments. It turns out you can define functions that take a variable number of arguments with _va_list_ (from <a href="http://en.wikipedia.org/wiki/Stdarg.h"><stdarg.h></a>).  You define such a function:

```c++
void log(const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    ...
    va_end(args);
}
```

Lesson Learned #2 : However, from what I can gather, you can't just inject printf directly into this. However, having anticipated this, there is a set of functions designed for cases like this: `vfprintf, vprintf, vsnprintf, vsprintf`. The 'v' stands for `va_list` (variable-argument list), and you can use them just like you'd expect:

```c++
void log(const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    fprintf(log_fd, "NOTE : ");
    vfprintf(log_fd, fmt, args);
    va_end(args);
}
```

The thing I like about this approach is that you have control over how log messages get printed in _one_ place.  So, for example, if I provided another function, `setLogFD`, then I could easily just set the file descriptor where all log messages get printed.  So easy!  Something I've used this for in other instances (especially servers) is to also inject additional information like a timestamp on every message.  So, when I call:

```c++
log("Some event '%s' just happened.\n", event_name);
```

Then I automatically get "NOTE : " and maybe a timestamp prefixed on that message.  Which make code look clean, and adds a great deal of functionality.  I actually added another function `error(...)` that prints to a different file descriptor in case I want to suppress debug messages, but no error messages.  For additional layers of debugging, you might do something like this:

```c++
void log(int level, const char* fmt, ...) {
    va_list args;
    va_start(args, fmt);
    FILE* fd = my_log_files[level];
    fprintf(fd, "NOTE : ");
    vfprintf(fd, fmt, args);
    va_end(args);
}
```

This way, at startup, you could easily set some of the file descriptors in _my_log_files_ to stderr and some to point to /dev/null or otherwise dissolve into the ether.
