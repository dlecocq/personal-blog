---
layout: post
status: publish
published: true
title: numerical_limits
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 929
date: '2011-05-10 16:48:34 -0700'
date_gmt: '2011-05-10 23:48:34 -0700'
categories:
- computer science
tags:
- c#
- limits
comments:
- id: 1557
  author: Andrew Ferguson
  author_email: andrew@fergcorp.com
  date: '2011-05-14 11:25:52 -0700'
  date_gmt: '2011-05-14 18:25:52 -0700'
  content: Is the goal of steerable variables to provide data validation? Why wouldn't
    you just set the variable directly?
- id: 1558
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2011-05-14 12:02:22 -0700'
  date_gmt: '2011-05-14 19:02:22 -0700'
  content: |-
    The goal is to have a class that helps to manage the interactions with outside sources (steering clients) and the variables of an application. In the end, the variable *does* get set directly, but a client might pass in a float, int, or widget to the set function for a given variable. So it's not sufficient to know the type passed into set(), but it has to also have some knowledge of the datatype the variable is pointing to.

    The necessity for the variable class is that you don't want to just hold a void*, because that requires the class to have a little more intelligence about the type, and can make it easier for the client to accidentally misuse, or abuse the class. This arrangement offers a stronger guarantee about what types of operations can and can't happen to the data you register to it.
- id: 1559
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2011-05-14 12:13:06 -0700'
  date_gmt: '2011-05-14 19:13:06 -0700'
  content: |-
    I occurs to me in reading your question what you actually meant. These variables will be set on network events. For example, the program can yield control to the steering library periodically, which checks to see if a steering client has connected, and if so, if it has issued any commands.

    There's a notion of a steerable application, which can advertise that clients can change certain parameters, or issue certain commands. One use case might be that the mouse_x coordinate and mouse_y coordinate can be specified by a client (we got a demo working of a WebSocket app acting as a trackpad on a remote machine).

    But the main use case we are trying to support is that you have a large-scale simulation running on a remote resource (cluster, supercomputer, etc.), and want to be able to interact with it through a thin client without too much extra work. The simulation codes we're working with are already behemoths, and can run for 12 hours or days at a time, and researchers often find that they could have terminated early had they been getting live updates of the results. Without yielding their allocation, this steering library enables them to check up on it as they like, issue commands, change parameters, etc. from say, an iPhone, the browser, or their desktop.
---
I'm working on a C++ class that encapsulates changes to a "steerable" variable. It's part of a system that allows trusted commands from a socket library to change the value of registered variables. For example, a client might:

```c++
int sInt(0);
float sFloat(0.3);

registerParam("someSteerableInteger", &sInt);
registerParam("someSteerableFloat", &sFloat);
...

// Library makes these calls after receiving remote commands:
setParam("someSteerableInteger", 5);
setParam("someSteerableFloat", 3.4);
```

There's some intelligence in the class to ensure integrity of the data. For example, it will cast the value past into _setParam(...)_ correctly, so that a call to _setParam("someSteerableInteger", 5.3)_ results in the 5.3 cast as an integer and then used to set the integer's value.

Some of the other intelligence needed is that the user might specify the minimum and maximum valid values the variable might take on. Or he or she might not. If not, it would be nice to have a convenient way of specifying a reasonable default minimum and maximum.

Enter [numerical_limits](http://www.cplusplus.com/reference/std/limits/numeric_limits/). It's a static templated class that can give you some insight into the built-in types. For example:

```c++
#include <iostream>

#include <limits>
using namespace std;

...

cout << "Min unsigned int: " << numerical_limits<unsigned int>::min() << endl;
cout << "Max float: " << numerical_limits<float>::max() << endl;
```
