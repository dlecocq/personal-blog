---
layout: post
status: publish
published: true
title: The Cost of Except in Python
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1052
date: '2012-01-08 12:19:03 -0800'
date_gmt: '2012-01-08 19:19:03 -0800'
categories:
- miscellany
tags: []
comments: []
---
I was curious recently about how much of a performance penalty try/except blocks incur in python. Specifically, 1) does it incur much of a cost if no exception is thrown (accepting only a penalty when something exceptional happens) and 2) how does it compare to if/else statements where possible? A snippet to answer the first question:

```python
import timeit

withTryNoThrow = '''
  try:
    a = int('5')
  except ValueError:
    pass
'''

withTryThrow = '''
  try:
    a = int('z')
  except ValueError:
    pass
'''

withoutTry = '''
  a = int('5')
'''

results = {
  'withoutTry'    : timeit.Timer(withoutTry    ).timeit(100000),
  'withTryNoThrow': timeit.Timer(withTryNoThrow).timeit(100000),
  'withTryThrow'  : timeit.Timer(withTryThrow  ).timeit(100000)
}

for k, v in results.items():
  print '%20s => %fs' % (k, v)
```

For me, the results looked something like this:

```
      withTryNoThrow => 0.082781s
          withoutTry => 0.082880s
        withTryThrow => 0.261147s
```

It would appear that while catching exceptions is expensive, catching non-exceptions is very cheap. I imagine that the reason is mostly because when you throw an exception, you actually instantiate an exception object of some kind, which necessarily introduces some overhead. In the absence of that object creation, things can be relatively fast.

Now, for the second question. This particular question came up when deciding whether or not I should try fetching a key from a dictionary and catching an exception when it's absent, or if I should use the get method and then check if the result is None.

```python
import timeit

setup = '''d = dict({
  'some'   : 1,
  'keys'   : 2,
  'are'    : 3,
  'present': 4,
  'others' : 5,
  'arent'  : 6
})'''

tryExcept = '''
  try:
    a = d['doesntexist']
  except KeyError:
    pass
'''

getIfElse = '''
  a = d.get('doesntexist', None)
  if a == None:
    pass
  else:
    pass
'''

getNoIf = '''
  a = d.get('doesntexist', None)
'''

results = {
  'tryExcept' : timeit.Timer(tryExcept, setup).timeit(100000),
  'getIfElse' : timeit.Timer(getIfElse, setup).timeit(100000),
  'getNoIf'   : timeit.Timer(getNoIf  , setup).timeit(100000)
}

for k, v in results.items():
  print '%20s => %fs' % (k, v)
```

For this second test, the results looked something like this for me:

```
             getNoIf => 0.019980s
           tryExcept => 0.083638s
           getIfElse => 0.027422s
```

Obviously, if your program is amenable to just using a default value, then happiness ensues. Failing that, using the get method and then if/else is much faster than the try/except alternative.

_Fine Print_: I am running Python 2.7.1 on a 2011-ish MacBookPro.
