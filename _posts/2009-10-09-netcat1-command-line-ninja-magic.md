---
layout: post
status: publish
published: true
title: netcat(1) [Command Line Ninja Magic]
author:
  display_name: ''
  login: ''
  email: ''
  url: ''
wordpress_id: 612
date: '2009-10-09 00:57:27 -0700'
date_gmt: '2009-10-09 07:57:27 -0700'
categories:
- computer science
- command line ninja magic
tags: []
comments: []
---
The best way to learn what command-line tools you should be using is to hang out around system administrators.  There are a couple in this office space, and they're always willing to give advice about which utility you should use instead of another.

I've been using scp and rsync since I started using bash, and thought they were the bee's knees.  Of course, they certainly have their purpose, but when it comes to sending files over the tubes quickly, I've learned of a better one: `nc` / `netcat`.

It goes like this: you've got a big file to transfer, and the tubes aren't really your bottleneck.  You might not care about security in this instance, but just want to get it done quickly. You start the `netcat` daemon on the remote machine, it listens on a port, and then things that get sent to that port are output to a file on that box:

```
my-remote-machine $> netcat -l -p 1234 > ubuntu.iso
```

And then on the machine I'm transferring from:

```
my-local-machine $> netcat #remote-ip 1234 < ubuntu-9.04-desktop-i386.iso
```

With `scp` for this same task, I was clocking about 28 MBps, but `netcat` posted 47 MBps pretty consistently.  This is a neat little tool I will be using with some regularity.
