---
layout: post
status: publish
published: true
title: Named Pipes
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1018
date: '2011-09-11 04:20:59 -0700'
date_gmt: '2011-09-11 11:20:59 -0700'
categories:
- computer science
tags:
- fifo
- os
- operating system
- pipes
- named pipes
comments: []
---
Yesterday I encountered a concept I hadn't known about: named pipes. They're essentially a __path that acts as a pipe__ for reading from / writing to. In that sense, you work with them like with file redirection and traditional files. But that data doesn't get stored anywhere really permanent. All data that goes through it is meat to be written once, and read once, and it comes with a performance boost of not having to write large chunks to disk.

 Pipes, for those who don't know, are the bees knees. They're the cat's meow. They allow you to (as the name implies) make a pipeline between one or more programs, with the output of one feeding into the input of others. Suppose, for example, that we want to find out how many files that contain '.a' there are in a directory. There's a tool you might know, 'ls,' that lists all the files in a directory. And 'grep' is a tool to search for lines of text that match a regular expression. And 'wc' is a tool that can count the number of bytes, words, lines, etc. in a file.

Typically, each of these __operates in isolation__, reading from a file (in the case of grep and wc), or... standard input. And they all write to standard output. A pipe is away to hook up one's process' standard output file descriptor to the standard input file descriptor of the another, making one the __producer of information and the other the consumer__:

```bash
ls -l /path/to/some/directory | grep '.a' | wc -l
```

This is typical of the design of many command line utilities. Most either come with an option to read from standard in (usually either the absence of a filename or a single '-'). __And most do exactly one task well__. Each has one very specific purpose, but is generally happy to play along with others.

File redirection is another handy tool that is related to named pipes. File redirection lets you either read the contents of a file as if it were standard input, or have a process write to it as if it were standard output. Going back to the earlier example, if we wanted to store a list of the all such files in our own file called 'list':

```bash
ls | grep '.a' > list
```

Easy as pie. Now... for named pipes. They're also called '__FIFO__'s for their first-in-first-out behavior. You can make one with 'mkfifo <filename>'. And then, feel free to read from it and write to it. Perhaps in two different terminals:

```bash
# In one terminal:
mkfifo test
cat < test

# In another terminal:
echo 'hello' > test
```

The first terminal, cat plugs along doing the one thing it knows how to do: display what it reads in out to standard out. Take a minute for what has just happened to sink in. You were able to have one process wait around until it had something read... from a pipe. And in a completely different terminal, you had a _different_ process communicate with the first one through opening a file. This is a mechanism that's commonly used for __inter-process communication__ (IPC) for obvious reasons -- everyone knows how to read from and write to a file, so it makes use of a known paradigm. But wait -- it gets even better.

Suppose you want to aggregate some statistics about how many different types of requests your application serves, but you don't want to have to write that in. Or maybe it's an application that you know already just writes to a log file. Of course, you could trawl the log file, but there are conceivably cases where you don't want the overhead of keeping around huge files, so you'd rather avoid it if possible. You have to be careful when doing this (not all applications play nicely with named pipes -- mostly surrounding blocking described below), but chances are you might be able to dupe the application into just logging to a named pipe! If you remove the log file and in that same path you make a pipe, then your work is done -- just read from that pipe to aggregate your statistics periodically. __This works particularly well with the python logging module.__

Reading from and writing to a named pipe can be a little more nuanced, however. Some things to bear in mind:

- __Opening a named pipe can block__, so consider opening them non-blocking. Of course, it depends on your access pattern, but if you're not sure if another process has written to the pipe and you don't want that to trip up your reading, non-blocking is the way to go.
- __Named pipes have 'no size.'__ If you write to a pipe, data gets queued up for the other end to read, but even before that gets read, stat(1) reports that the file has a size of 0 bytes. So, you can't rely on a change in file size to know it's ready for reading.
- __Instead, use select, poll, epoll, etc. to detect read/write-ability on the pipe.__ If you're only interested in one file descriptor, then you can go ahead and use select, but if you're starting to listen to too many, perhaps one of the others is a better idea.
