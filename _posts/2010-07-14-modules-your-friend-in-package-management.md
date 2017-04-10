---
layout: post
status: publish
published: true
title: Modules - Your Friend in Package Management
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 872
date: '2010-07-14 09:07:32 -0700'
date_gmt: '2010-07-14 16:07:32 -0700'
categories:
- computer science
tags:
- modules
- package management
comments:
- id: 877
  author: Berk Geveci
  author_email: berk.geveci@kitware.com
  date: '2010-07-14 12:35:51 -0700'
  date_gmt: '2010-07-14 19:35:51 -0700'
  content: Modules rock. I use them everyday when developing VTK&#47;ParaView :-)
- id: 878
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2010-07-14 12:44:51 -0700'
  date_gmt: '2010-07-14 19:44:51 -0700'
  content: I'm glad to know that it sees real-world use outside of campus.  And at
    Kitware, no less!
---
I've been working with a large shared system at my school, sometimes building packages for myself and sometimes for others.  The one thing that's almost certain across all such installations is that it's difficult.  Installing dependencies can be a very deep rabbit hole, and there are seemingly more configuration, build and source control systems than there are atoms in the universe.

On this particular shared system, our awesome sysadmins (these guys are really pretty great!) use a package called [modules](http://modules.sourceforge.net/) to set environment variables for use with various packages.  Suppose you have several versions of a library that you're working with.  Let's say some users need Python 2.4, and other 2.6 and 3.0.  Instead of managing your path yourself, modules can help:

```bash
$> module load python-2.4
$> which python
/opt/share/python/2.4/ppc64/bin/python
```

One of the really great things about modules is that the way so-called [modulefiles](http://modules.sourceforge.net/man/modulefile.html) are written, not only can you load modules easily, but you can also _unload_ them just as easily:

```bash
$> which python
/opt/share/python/2.4/ppc64/bin/python
$> module unload python-2.4
$> module load python-2.6
$> which python
/opt/share/python/2.6/ppc64/bin/python
```

It's of course not limited to any particular environment variable.  The modulefile can specify where the man pages are, what paths to include when using [cmake](http://www.cmake.org/), dynamic library path and whatever you'd like.

Modulefiles are also extremely convenient places to store information on how you actually built the library.  When you come back to it three months from now to build the next version of some code base, you won't remember the complex arguments you had to pass into configure or cmake in order to get the damned thing to build.  Build notes are an essential part of maintaining code, especially if other people will be using the libraries you've built.

Speaking of which, I've worked on other shared systems before where several people need to use the same library and end up building it separately.  Frank and Steve both need libX, and have made their installations accessible to the other users on the system, but who wants to sully their .bash_profile by adding some long and ugly paths to their PATH?  If Steve makes his modulefiles directory public, too, then you can just that directory in MODULEPATH:

```bash
# in ~/.bash_profile
...
export MODULEPATH=~/modules/:/home/frank/modules/
...
```

Perhaps it's not the best thing since sliced bread, but I like that it affords me a way to bridge the gap between having a convention for where libraries are installed (say, if you use MacPorts, for example?) and being able to easily set all your environment variables to _easier_ if not easy compilation.

By way of a way that its helped me, I've been compiling quite a few projects recently that rely on cmake.  These projects also have a whole lot of dependencies, but my build process is now something along the lines of:

```bash
$> module load libxml2
$> module load vtk
$> module load osmesa
$> ...
$> cmake ~/ParaView
```

This, compared to:

```bash
CMAKE_INCLUDE_PATH=$CMAKE_INCLUDE_PATH:/opt/share/libxml2/2.7.7/ppc64/include:/opt/share/vtk/5.6.0/ppc64/include/:...\
CMAKE_LIBRARY_PATH=$CMAKE_LIBRARY_PATH:/opt/share/libxml2/2.7.7/ppc64/include:/opt/share/vtk/5.6.0/ppc64/lib/:...\
cmake ~/ParaView
```

Computers aren't perfect, but they are experts at remembering the details.  Almost to a fault.  Modules helps my interactions to be a little more equitable where I have to remember the important parts (the names of the modules I need, for example) and the computer can keep track of where the hell I put everything!
