---
layout: post
status: publish
published: true
title: Git(1) - Your Kind of Version Control
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 687
date: '2009-11-10 07:58:48 -0800'
date_gmt: '2009-11-10 14:58:48 -0800'
categories:
- computer science
- life
tags:
- version control
- git
- computer science
- versioning
- svn
comments:
- id: 516
  author: Colin
  author_email: creutter@gmail.com
  date: '2009-11-10 12:27:15 -0800'
  date_gmt: '2009-11-10 19:27:15 -0800'
  content: "There is an article about KAUST in the latest Physics Today. \r\n\r\nhttp:&#47;&#47;ptonline.aip.org&#47;journals&#47;doc&#47;PHTOAD-ft&#47;vol_62&#47;iss_11&#47;24_1.shtml\r\nPDF:
    http:&#47;&#47;link.aip.org&#47;link&#47;PHTOAD&#47;v62&#47;i11&#47;p24&#47;s1&#47;pdf"
- id: 517
  author: Colin
  author_email: creutter@gmail.com
  date: '2009-11-10 12:35:46 -0800'
  date_gmt: '2009-11-10 19:35:46 -0800'
  content: "It looks like the photos in the article came from this guy: http:&#47;&#47;skippy.net&#47;\r\n\r\nIt
    is interesting to see them use a photo from Flickr that are licensed under creative
    commons.\r\n\r\nhttp:&#47;&#47;www.flickr.com&#47;photos&#47;skippy&#47;3958239283&#47;in&#47;set-72157622340321297&#47;"
- id: 519
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2009-11-10 22:32:16 -0800'
  date_gmt: '2009-11-11 05:32:16 -0800'
  content: |-
    I tried to check out skippy's website, but it's blocked and I don't have a VPN set up yet (or Tor for that matter).

    In that same vein, an Arab-language newspaper ripped off a student's blog (supposedly translating word for word - again I don't know about this because google translate is blocked here, too).

    Newspaper: http:&#47;&#47;www.alyaum.com&#47;issue&#47;article.php?IN=13268&amp;I=708121
    Blog: http:&#47;&#47;saudiaggie.blogspot.com&#47;2009&#47;10&#47;elections.html
---
I've been around the block a time or two (or more) with subversion, but until recently I had limited experience with git.  Sure, every now and then I've used it to check out projects, but not for my personal use.

No longer. And as of right now, I don't have any intention of using anything but git for personal development.

Last week, I held lecture for parallel programming and I talked about using subversion for versioning, and I began to suspect that something was horribly wrong.  Questions started springing up - where does the repository live?  Am I calling svnadmin on my own machine?  Where do I check out the repository?  Though there are answers to these questions, for many things, such a model just doesn't make sense.

If I'm working on a project that I'm not syncing between several computers, but I just want to have different stable versions and to try different crazy ideas using branches.  It mitigates the cost of reverting drastic changes to code.

__Use Case__: You're showing someone your code, and want to show off a neat feature you've made, or a problem you're encountering, something about the project, invariably you've run into a problem where it doesn't compile at the moment.  You type furiously, trying to find and undo the most recent changes, but to no avail - there is no hope of getting it to compile in the 5 minutes you have someone's attention.  Enter version control.  Revert to the last working copy and victory is yours.

In fact, just today I was asked if I could pull up some code I had been working on to show to a professor.  Unfortunately at the moment it wasn't compiling but was able to switch versions in 20 seconds and show off some very recent work from earlier in the day, thus saving face.

__Use Case__: You've got some crazy idea for an implementation you'd like to try out, but are worried about reverting back all the massive changes you'll have to make in the code.  Worry not!  Create a new branch and feel free to change your code in every way you can think of and not lose other branches under development.

__Use Case__: You've got multiple versions of code each implementing the same basic algorithm but with different mechanisms, techniques, etc. and have to turn it in as part of a project.  Just archive the whole directory (in a tarball or zip) and the user who unpacks it has access to every version your code has been in.  Each branch, each stage of development.  And very light-weight to boot.

I can't speak for others, but I will be using git for the foreseeable future as it's incredibly easy to use and alleviates many of the problems I encounter regularly with development.
