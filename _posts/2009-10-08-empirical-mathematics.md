---
layout: post
status: publish
published: true
title: Empirical Mathematics
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 602
date: '2009-10-08 00:46:10 -0700'
date_gmt: '2009-10-08 07:46:10 -0700'
categories:
- computer science
- math
tags: []
comments: []
---
As I read in a lecture recently, Richard Hamming described his philosophy of computing with, "the purpose of computing is insight, not numbers."

On a relatively regular basis, I use numerical methods to verify an analytical solution I've reached and occasionally, to reach an analytical result.  At [one point]({{ site.baseurl }}{% post_url 2008-06-24-heapsort %}), I was playing around with the time complexity of heapsort, and I came across a statement about which I was unsure.  I verified that it was the case, but it brought about other questions about a more general case.

$$\sum_{h=0}^{\infty}{\frac{h}{n^h}}$$

How does this converge for different $$n$$'s?

I played around with it for a little bit to see if I saw any pattern that emerged, like with a geometric series or an arithmetic sum, but I came up with nothing.  So, I decided to explore the numbers a little bit, writing a short little Ruby script to take the first 100-or-so elements.  It turns out that even this approximation provided the insight to get the general expression:

- `n=2 => 2`
- `n=3 => 0.75 = 3/4`
- `n=4 => 0.4444... = 4/9`

The expression thus seemed to be:

```latex
$$\sum_{h=0}^{\infty}{\frac{h}{n^h}} = \frac{n}{(n-1)^2}$$
```

Of course this needed to be verified, but that task is [easy enough]({{ site.github.url }}/assets/2008/06/heap.pdf).  The point is, that sometimes the numerical approximation can give you the exploratory insight needed to solve a problem.  Sure, it's rough around the edges, and isn't as elegant as I would necessarily like, but it's very useful.
