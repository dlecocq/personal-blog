---
layout: post
status: publish
published: true
title: Command Line Stopwatch (time cat)
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 975
date: '2011-08-04 15:56:20 -0700'
date_gmt: '2011-08-04 22:56:20 -0700'
categories:
- command line ninja magic
tags: []
comments:
- id: 1728
  author: Matt M
  author_email: Matt@MattMatteson.com
  date: '2011-08-04 18:34:26 -0700'
  date_gmt: '2011-08-05 01:34:26 -0700'
  content: Very nifty. I'm putting that one in my back pocket for later.
- id: 3026
  author: Lynelle Chris
  author_email: MauritaCleveland@gmail.com
  date: '2013-07-29 12:23:59 -0700'
  date_gmt: '2013-07-29 19:23:59 -0700'
  content: It&rsquo;s hard to find well-informed people in this particular topic,
    however, you seem like you know what you&rsquo;re talking about! Thanks
- id: 3029
  author: Jacinto Stridiron
  author_email: JulianneGarland@gmail.com
  date: '2013-07-30 20:13:19 -0700'
  date_gmt: '2013-07-31 03:13:19 -0700'
  content: The heart of your writing whilst sounding reasonable at first, did not
    work perfectly with me personally after some time. Someplace throughout the paragraphs
    you actually were able to make me a believer unfortunately just for a short while.
    I however have got a problem with your leaps in logic and one might do nicely
    to help fill in those breaks. If you actually can accomplish that, I will undoubtedly
    end up being fascinated.
---
If you find yourself with a terminal and you need a stopwatch:

```bash
$> time cat
```

`cat(1)` by default waits on `stdin` if no arguments are provided, until an EOF is reached (`ctrl+d`). `time(1)` waits until the run command terminates, so in effect, it's a stopwatch that runs until you press `ctrl+d`.
