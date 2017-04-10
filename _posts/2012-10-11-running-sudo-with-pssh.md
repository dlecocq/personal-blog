---
layout: post
status: publish
published: true
title: Running sudo with pssh
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1083
date: '2012-10-11 11:28:59 -0700'
date_gmt: '2012-10-11 18:28:59 -0700'
categories:
- command line ninja magic
tags:
- computer science
- bash
- command line ninja magic
comments:
- id: 2422
  author: bronko
  author_email: amvadder@gmail.com
  date: '2012-11-13 16:38:47 -0800'
  date_gmt: '2012-11-13 23:38:47 -0800'
  content: what is the correct syntax to run pssh when sudo required password?
- id: 2423
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2012-11-13 19:46:00 -0800'
  date_gmt: '2012-11-14 02:46:00 -0800'
  content: Well, the best I can think of is ssh's -S option, which will read a password
    from stdin. That said, it's also not a very secure option, but one that's available.
- id: 3056
  author: Make Money Online
  author_email: Hornby@gmail.com
  date: '2013-10-17 22:04:02 -0700'
  date_gmt: '2013-10-18 05:04:02 -0700'
  content: This super is a super website, Keep on what youre doing
---
The [pssh](http://www.theether.org/pssh/) tool is great. Just great. At SEOmoz we use a number of deployment schemes, but every so often I find myself needing to log into 50 machines and perform some simple one-off command. I've written such a line many times:

```
for i in {01..05}; do ssh -t ec2-user@some-host-$i 'sudo ...'; done
```

This is fine if the command is quick, but it _really_ sucks if it's something that takes more than just a few seconds. So in the absence of needing to use sudo (and thus the '-t' flag), pssh makes it easy to run these all in parallel:

```
pssh -i --host=some-host-{01..50} -l ec2-user 'hostname'
```

Coercing pssh to create a pseudo-tty to enable sudo commands was a little tricky, though:

```
# And now I can sudo!

pssh -x '-t -t' -i --host=some-host-{01..50} -l ec2-user 'sudo hostname'
```
