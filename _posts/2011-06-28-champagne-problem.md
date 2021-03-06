---
layout: post
status: publish
published: true
title: Champagne Problem
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 953
date: '2011-06-28 01:55:49 -0700'
date_gmt: '2011-06-28 08:55:49 -0700'
categories:
- computer science
tags:
- logic
- puzzles
- interview questions
comments: []
---
I had an interview a few weeks ago, and I spent a little time preparing for it. I puzzled over some logic problems, and read some common interview questions, knowing that there would still likely be questions I hadn't heard. Still, I did have one cache hit, so to speak.

One of my favorite questions, though, was one about pouring bottles of champagne: Suppose you are in charge of pouring the champagne for the midnight toast at a prestigious party with more VIPs than you can count. You have 10 waiters, who are wheeling in 1000 bottles of champagne and some bad news; exactly one of these bottles is poisoned, and if you drink even a single drop, you will become violently ill in one hour. If you serve tainted champagne to any guest, you and your employees will be fired on the spot.

Your waiters are sympathetic to this fact, and have thus volunteered to be taste-testers -- a night home on the couch being miserable is better than being unemployed. Though, because of time constraints, you only have time for one testing before people get sick and you have to serve champagne.

The naive approach is to split the bottles up into groups of 100, and have each waiter try a drop from each. You would know from whichever waiter gets sick which group of 100 bottles has the bad bottle, but there would be 99 good bottles wasted, and of course, the wasted good bottles get deducted from your pay.

So, you want everyone to keep their jobs (and not serve tainted booze) while wasting as few good bottles as possible. How many bottles do you have to waste? Click below to reveal solution.

## Solution
You don't have to waste a single bottle of good champagne, while ensuring that no VIP gets sick. Label your waiters 1, 2, 3, and so on up to 10. Label the bottles of champagne 1, 2, 3, and so on up to 1000. Then, for each bottle, convert that number to binary representations, and let each waiter be associated with a bit. For example, bottle 417 has representation 0110100001, meaning that waiters 1, 6, 8, and 9 would sample a small drop from it, but bottle 418 would have waiters 2, 6, 8, and 9. In this way, each bottle has a unique set of waiters who sampled it. Then, when waiters start becoming sick, say, waiters 3, 5, 6, and 10, you'd know that it's bottle 1000110100 (564) that's contaminated.
