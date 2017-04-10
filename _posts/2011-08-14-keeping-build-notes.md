---
layout: post
status: publish
published: true
title: Keeping Build Notes
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 989
date: '2011-08-14 09:43:09 -0700'
date_gmt: '2011-08-14 16:43:09 -0700'
categories:
- computer science
tags:
- build notes
- good practices
comments: []
---
I initial put off upgrading to Snow Leopard until almost a year after its release because I was worried about rebuilding my development environment. It's amazing how many packages one accumulates over time without thinking about it, and when you have deadlines to meet it can be disastrous to risk your current working setup.

But rebuilding your development environment comes up more than just upgrading your OS. If you need to migrate to that new computer you got, or that work gave you, or help someone else get up and running with a project you're thinking about releasing. Admittedly, it took me a little while to learn this lesson, but finally it's drilled into my head: __keep build notes!__

A couple weeks ago I was trying to install an internal package whose docs hadn't been updated in a very long time. After struggling and hitting countless snags, I finally got it up and running when I got an email that was along the lines of, "Oh, if you could write down what problems you ran into, that would be great." Fortunately, I just made notes of what I had done in order to get it built, and I was able to whip off a reply with speed that surprised the recipient.

Even at a system-wide level, I try to make it a habit to record every package I install/build associated with development. It makes it extremely easy to get set up on the next system, even if the instructions have to be updated for a new environment. I call it a manifest and I manage it as a flat file, though I know there are package managers that can do a lot of heavy lifting for me. However, I find that no package manager is perfect and so even if I make use of one for certain libraries, it's important to me to have everything documented in one place. At a minimum (and you probably don't need more than this) keep the following:

1. __Package name and version__ - Maybe you needed readline 6.1 to get your project running, or you know that such-and-such version is buggy for your purposes.
2. __Why you installed it__ - I find that many libraries I install are used for a particular project, and so it's useful to have the motivation for getting it.
3. __How you installed it__ - Whether it was macports or a typical configure, make and install, how did you build it? Did you need special flags to make it go? You will absolutely forget these, so why not write them down? Even just copy and paste from your history!

I can't stress enough how much easier this has made my development life in a lot of ways, and how little a time investment it is.
