---
layout: post
status: publish
published: true
title: First-in First-out, Least-Recently-Used
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 98
date: '2008-04-16 11:21:39 -0700'
date_gmt: '2008-04-16 18:21:39 -0700'
categories:
- computer science
tags:
- first-in first-out
- fifo
- page-replacement
- memory-management
- ruby
- script
comments: []
---
In my OS class, we've started talking about some page-replacement algorithms, including FIFO, LRU, and clock.  These are going to be on an upcoming exam, and so Mike (our prof) suggested that we make up our own page access sequences, and then run the algorithm.  That's all well and good, but without knowing whether or not you got it right, problems might arise.

Enter Ruby - make a quick little script that will run the algorithm for you, so as to check your results.

[fifo.rb]({{ site.github.url }}/assets/2008/04/fifo.rb)

[lru.rb]({{ site.github.url }}/assets/2008/04/lru.rb)

Usage:

```
fifo.rb "123412512345" 3 # Run the sequence provided with a queue size of 3
lru.rb "293847101928" 5 # Run the provided sequence with a stack size of 5
```

All the page numbers do have to be single characters, but letters and symbols are also accepted.

Sample output:

```
Dan-Lecocqs-Mac:Desktop dlecocq$ ./lru.rb "123412512345" 4
1 * 1
2 * 2 1
3 * 3 2 1
4 * 4 3 2 1
1   1 4 3 2
2   2 1 4 3
5 * 5 2 1 4
1   1 5 2 4
2   2 1 5 4
3 * 3 2 1 5
4 * 4 3 2 1
5 * 5 4 3 2
Page faults: 8 / 12
```

Please note that you'll have to change your shebang line to point to the path of your Ruby interpreter.  I found Ruby in lots of places on my system, but check in your path.  (Note: I'm using Ruby 1.8.4, but I don't think I'm using a lot, or any, recent-version specific functionality)

If you're not running it with "ruby fifo.rb ...", make sure you've chmod'd it to be executable.
