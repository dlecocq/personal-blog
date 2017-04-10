---
layout: post
status: publish
published: true
title: zsh (or bash++)
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 736
date: '2009-11-15 10:54:33 -0800'
date_gmt: '2009-11-15 17:54:33 -0800'
categories:
- computer science
- command line ninja magic
tags:
- bash
- zsh
- shells
comments:
- id: 1984
  author: noogie
  author_email: noogie.brown@gmail.com
  date: '2011-11-14 12:19:08 -0800'
  date_gmt: '2011-11-14 19:19:08 -0800'
  content: "you may want to look at .inputrc  modifications where you can bind pg&#47;pg
    down to history autocompletetiong... \r\n\r\n\"\\e[6~\": history-search-forward\r\n\"\\e[5~\":
    history-search-backward"
---
A professor of mine mentioned that he didn't use bash but Z shell (zsh).  I asked him about his choice and he said that it happened years ago when he asked a system administrator how to accomplish a task in bash and the guy replied that it was really easy in zsh.  There have been worse reasons to switch, I suppose.

(Incidentally, the best way I've found to improve your command-line-fu is to work near system administrators.  They have the most amazing bits of command line ninja magic you'll ever see.)

I decided to give it a shot this evening and after 30 minutes of use, I'm switching.  The features I've liked thus far as that when you want to search for a command you recently ran, you don't need any of the ctrl-r nonsense.  One simply begins the command as he remembers it and presses up.  Old functionality mapped to the intuitive keystroke.  You can scroll through your command history by pressing the up arrow key in bash, but to search, it's a different story.

The feature that clinched it for me is that it has better autocompletion.  If you are not using tabs to autocomplete, you are wasting keystrokes and make typos, but something I find frustrating is that when I want to ssh into some computer with some long and difficult-to-type name, I had to search my history for it.  Or, in zsh, you can tab complete the name.  It remembers that stuff!  Imagine that!

Of course, there's a very real possibility I'll switch back if I run into too many gotchas, but this many niceties this soon in make mean think that the good will outweigh the bad.
