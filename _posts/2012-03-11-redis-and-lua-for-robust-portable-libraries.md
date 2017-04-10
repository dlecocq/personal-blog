---
layout: post
status: publish
published: true
title: Redis and Lua for Robust, Portable Libraries
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1061
date: '2012-03-11 08:17:10 -0700'
date_gmt: '2012-03-11 15:17:10 -0700'
categories:
- computer science
tags:
- lua
- redis
- queueing
- portable
comments:
- id: 2200
  author: Sparsh Gupta
  author_email: sparshgupta@gmail.com
  date: '2012-05-18 01:59:49 -0700'
  date_gmt: '2012-05-18 08:59:49 -0700'
  content: Great post, Thanks. By any chance do you have code samples to share of
    your queue implementation?
- id: 2201
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2012-05-18 16:14:43 -0700'
  date_gmt: '2012-05-18 23:14:43 -0700'
  content: Thanks! It's funny that you should leave that comment today, just as I
    was preparing a blog post on the the <a href="http:&#47;&#47;devblog.seomoz.org&#47;2012&#47;05&#47;introducing-qless-our-new-job-queue&#47;"
    rel="nofollow">project<&#47;a>.
---
Redis 2.6 has support for server-side Lua scripting. Off hand, this may not seem like a big deal, but it offers some surprisingly powerful features. I'll give a little bit of background on why I'm interested in this in the first place, and then I'll show why this unassuming feature is so extremely useful for __otherwise impossible atomic operations__, as well as for __easy language portability__ and __performance__.

For example, I've recently been working on a Redis-based queueing system (heavily inspired by Resque, but with some added twists) and a lot of functionality that I wanted to support would have been prohibitively difficult without Redis' support for Lua. For example, I want to make sure that jobs submitted to this queueing system do not simply get dropped on the floor. A worker is given a temporary exclusive lock on a job, and must either complete it or heartbeat it within a certain amount of time. If that worker does not, it's presumed that the worker dropped the job and it can be given to a new worker.

Now let's imagine what this locking mechanism would have to look like in order to be correct. First, we'd probably maintain a list of jobs in a queue that have been popped off, but not yet completed, sorted by when their lock expires. When a client tries to get a job, it should first check for expired locks, and if it finds any, it should assume responsibility for those jobs. So this client sees an expired lock, and attempts to update the metadata associated with the job to reflect that it now has that job. In the mean time, the original client has swooped in and tried to complete the job despite the expired lock, removes the entry for the lock, and updates the job data to reflect its completion. It's possible that the second client updates the job data after this, and inserts a new lock for itself, putting the system into an inconsistent state.

Yes, Redis has a mechanism for this, but it's only so strong. There's the `MULTI`, `WATCH` and `EXEC` combo, which allows you to detect the situation when another client has tried to modify a key for which you're trying to perform an atomic operation and allows you to try the operation again. But for highly contentious keys, you can spend a lot of time backing off and failing. That's frustrating.

Redis' Lua support has an interesting guarantee: __Lua scripts in Redis are guaranteed to be executed atomically__. No other commands can be run on the Redis instance while the Lua script is running. With that in place, you are free to no worry in the slightest about these sorts of race conditions, because they just won't happen. You can access as many keys as you'd like, without having to worry about `WATCH`-ing them for changes, and implement as simple or complex a locking mechanism as you'd like.

Another interesting feature that comes out of this is that if you implement your next Redis-based library as a collection of Lua scripts, then you can write bindings in other languages in a flash. The only requirement is that those new bindings must be able to read in a file, load the script, and then have Redis bindings to invoke those scripts. Clients no longer have to worry about mimicking any arbitrarily complex logic in their own language -- they just rely on these Lua scripts that can be shared across all the bindings! This may go without saying, but maintaining bindings is something that can be a bit of a nuisance. One example that jumps to mind immediately is working with Redis from Node.js if a lot of successive commands have to be chained together. It can get extremely messy.

Not only this laundry list of wonderful features spring out of this Lua support, but it's surprisingly performant. Without giving too much away, at SEOmoz, I recently implemented the queueing system I mentioned to support scheduled work items, heartbeating, priority and statistics collection in a collection of about 10-12 Lua scripts. Initial benchmarks have hit 4500 job pop/complete transactions per second on a 2011-ish MacBook Pro. At least for our purposes, this is _plenty_ of room to roam. And let me assure you, these scripts are not always simple, and so the fact that Redis can still maintain good performance in the face of arbitrary scripts speaks volumes about the quality of Redis.
