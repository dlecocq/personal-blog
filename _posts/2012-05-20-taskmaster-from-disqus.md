---
layout: post
status: publish
published: true
title: Taskmaster from DISQUS
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1066
date: '2012-05-20 11:03:02 -0700'
date_gmt: '2012-05-20 18:03:02 -0700'
categories:
- computer science
tags:
- python
- taskmaster
- disqus
- dcramer
comments: []
---
I have been waiting for an occasion to use [dcramer's taskmaster](https://github.com/dcramer/taskmaster), which is a queueing system meant for large, infrequently-invoked (even one-off) tasks. In his [original blog post](http://justcramer.com/2012/05/04/distributing-work-without-celery/) brings up one of the features that was particularly striking to me -- you don't put jobs into the queue per se, but you describe a generator that yields all the jobs that should be put in the queue.

Occasionally at SEOmoz, we want to perform sanity checks on customer accounts, or transitioning from one backend to another, etc. In particular, we've been transitioning to a new queueing system, and we wanted to go through every customer and ensure that they had a recent crawl, and further, were definitely in the new system. Unfortunately, much of the data we have to check involves a lookup into Cassandra (that can't be turned into a bulk operation very easily). Cassandra's not necessarily the problem, but just the latency between requests. So, spawn off 20 or so workers with taskmaster, each given the details about the customer that we needed to verify.

The serial version takes 4-5 hours. It took 15 minutes to get taskmaster installed and grokked, and then the task itself took an hour. Already a win!
