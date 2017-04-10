---
layout: post
status: publish
published: true
title: Python and Arbitrary Function Arguments - **kwargs
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1023
date: '2011-09-14 05:18:56 -0700'
date_gmt: '2011-09-14 12:18:56 -0700'
categories:
- computer science
- Python
tags:
- python
- keyword arguments
- kwargs
comments: []
---
Python has a pretty useful policy: named arguments. When you call a function, you can explicitly say that such-and-such value is what you're providing for a particular argument, and can even include them in any order:

```python
def hello(first, last):
  print 'Hello %s %s' % (first, last)

hello(last='Lecocq', first='Dan')
```

In fact, you can programmatically gain insight into functions with the [inspect module](http://docs.python.org/library/inspect.html). But suppose you want to be able to accept an arbitrary number of parameters. For example, for a printf equivalent. Or where I encountered it in wanting to read a module name from a configuration file, as well as the arguments to instantiate it. In this case, you'd get the module and class as a string and then a dictionary of the arguments to make an instance of it. Of course, Python always has a way. In this case, `**kwargs`.

This is actually dictionary unpacking, taking all the keys in a dictionary and mapping them to argument names. For example, in the above example, I could say:

```python
hello(**{'last':'Lecocq', 'first':'Dan'})
```

Of course, in that case it's a little verbose, but if you're getting a dictionary of arguments programmatically, then it's invaluable. But wait, there's more! Not only can you use the `**dict` operator to map a dictionary into parameters, but you can accept arbitrary parameters with it, too!

```python
def kw(**kwargs):
  for key, value in kwargs.items():
    print '%s => %s' % (key, value)

kw(**{'hello':'Howdy!', 'first':'Dan'})
kw(hello='Howdy!', first='Dan')
```

Magic! __No matter how you invoke the function, it has access to the parameters.__  You can even split the difference, making some parameters named and some parameters variable. For example, if you wanted to create an instance of a class that you passed a name in for, initialized with the arguments you give it:

```python
def factory(module, cls, **kwargs):
  # The built-in __import__ does just what it sounds like
  m = __import__(module)
  # Now get the class in that module
  c = getattr(m, cls)
  # Now make an instance of it, given the args
  return c(**kwargs)

factory('datetime', 'datetime', year=2011, month=11, day=8)
factory('decimal', 'Decimal', value=7)
```

This is one place where Python's flexibility is extremely useful.
