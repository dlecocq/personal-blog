---
layout: post
status: publish
published: true
title: Python's Logging Module - Exceptions
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1044
date: '2011-10-19 09:27:40 -0700'
date_gmt: '2011-10-19 16:27:40 -0700'
categories:
- miscellany
tags:
- python
- exceptions
- logging
comments: []
---
I'm a big fan of python's [logging](http://docs.python.org/library/logging.html) module. It supports configuration files, multiple handlers (for both writing to the screen while writing to a file, for example), output formatting like crazy, and many other delicious features. One that I've only recently encountered is __its exception method.__

The basic idea of the logging module is that you can get a logger from a factory (that allows multiple pieces of code to easily access the same logical logging entity). From there, you add handlers that output messages to various places (files, screen, sockets, HTTP endpoints, etc.). Every message you log is done at a specific level, and then the configuration of the logger determines whether or not to record messages of a certain severity:

```python
import logging

# Get a logger instance
logger = logging.getLogger('testing')

# Some initialization of handlers here, unimportant in this context

# Print out at various levels
logger.warn('Oops! Something happened')
logger.info('Did you know that X?')
logger.debug('Index is : %i' % ...)
```

What's great about the module is that it __separates your messages from how they're displayed and where.__ For debugging, it's nice to be able to flip a switch and turn on a more verbose mode. Or for production to tell it to shut up and only log messages that are really critical. What the 'exception' method does is to not only __log a message as an error, but to also print a nice backtrace of where the error took place__!

```python
try:
  # So something here
  raise Exception('oops!')
except:
  logger.exception('Such-and-such failed! Stack trace to follow:')
  # Stack trace appears in the log
```
