---
layout: post
status: publish
published: true
title: Sum of Dice
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 922
date: '2011-05-10 10:28:41 -0700'
date_gmt: '2011-05-10 17:28:41 -0700'
categories:
- computer science
- math
tags:
- math
- combinatorics
- algorithms
- dice
comments: []
---
I recently had an interview in which I was asked, "how many ways can 1000 dice make the sum 3000?" I was caught a little off-guard, and the phrasing made me wonder about a closed-form solution which, after some reading, I don't believe exists. Still, a workable solution isn't as easy as that.

Let `F(n, k)` denote the number of ways `n` dice can make the sum `k`. Note that the first die can be 1, 2, 3, 4, 5 or 6, so `F(1000, 3000) = F(999, 2999) + F(999, 2998) + ... + F(999, 2994)`. While this recurrence relation leads to an easy implementation, it suffers from two big problems: performance and maximum recursion depth. Without any [memoization](http://en.wikipedia.org/wiki/Memoization) or optimization, this would lead to `6^1000` function calls, which is about `10^780`. That's a big number. If you were able to evaluate one such function call every clock cycle on every computer in the world (about `7 x 10^18` cycles/second), you would need about `10^750` years, or `10^650` lifetimes of the universe (about `10^100` years) to solve it. Get ready to wait.

One optimization is to check if the arguments n and k make sense at each level, and prune accordingly. For example, n dice can only sum to between n and 6n, so if k is outside of that range, you don't need to branch down any farther. Even using this and instantaneous branch evaluation, your code still wouldn't complete in the expected lifetime of the universe.

Obviously, this is still a solvable problem (there are about `10^757` ways 1000 dice can sum to 3000). A python implementation figured that out in 3.5 seconds. One way to help crack this egg is to use memoization. Consider the calls to `F(999, 2999)` and `F(999, 2998)`. Expand these out to get:

- `F(999, 2999) = sum[F(998, k = 2998, 2997, 2996, 2995, 2994, 2993)]_`
- `F(999, 2998) = sum[F(998, k = 2997, 2996, 2995, 2994, 2993, 2992)]_`

You'll notice that both of these expansions call `F(998, k = 2997, 2996, 2995, 2994, 2993)`, each of which is a _lot_ of work to evaluate. So, if once you determined each of these values once, you could use them in other places and save huge amounts of time.

One thing you'd need in order to implement memoization is a map (or dictionary in python) that stores key-value pairs. So once you figure out `F(998, 2997)`, you could store it like `myMap[(998, 2997)] = ...`; but this can add some complication. Every time to call F, you'd have to check if you've already evaluated the function for those arguments. And when you've figured out and stored a lot of these values, each search will take some time. It will still work and will get you the answer you need, but probably not as fast as you'd like, and not as fast as it could be. Using memoization for `F(700, 2100)` took 8.2 seconds in a python implementation, but a better approach took 1.5 seconds. The maximum recursion depth prevented it from using bigger numbers.

Algorithmically, the best you'll be able to do (as far as I can tell) is <em>O(n<sup>2</sup>)</em>, which is not bad in the scheme of things, and certainly not the combinatoric time we saw first. Enter dynamic programming. Particularly, we'll use a [bottom-up approach](http://en.wikipedia.org/wiki/Top-down_and_bottom-up_design). We'll build two arrays, each associated with a number of dice. The `i`'th index in that array is the number of ways n dice can sum up to `(n + i)`. So for 1 die, `myArray[0]` is the number of ways you can roll a 1, and for 4 dice, `myArray[10]` would be the number of ways you can roll 4 dice to get 14.

As I said, we'll keep track of two arrays, say `previous` and `current`. First, initialize previous to be the number of ways 1 die can be rolled: `{1, 1, 1, 1, 1, 1}`, because 1 die can be rolled each number in only one way. Then, we'll use that to fill the array "current" with the number of ways 2 dice can be rolled, based on the array `previous`. For example, `current[0] = previous[0] = 1`, because the only way to get a sum of n with n dice is to roll all 1's. Then, `current[1] = previous[0] + previous[1]`, because if we roll a 2 for the second dice, there are `previous[0]` ways to sum up to 1 with the remaining die, or if we roll a 1 for the second dice, there are `previous[1]` ways to sum up to 2 with the remaining die.

Each entry `current[i]` should be the sum of `previous[i-5, i-4, i-3, i-2, i-1, i]`, taking the bounds of the previous array into consideration (this can actually be generalized to any `m`-sided dice by using previous[i-m+1, ..., i]). Once you've filled the array `current`, then you assign current to previous, and move on to the next number of dice, 3. Continue this until you have filled the array for the desired number of dice. If performance is a big issue, this can be implemented as a moving frame. For example, since `current[i]` uses `previous[i-5, ..., i]` and `current[i+1]` uses `previous[i-4, ..., i+1]`, you can alternatively write `current[i+1] = current[i] - previous[i-5] + previous[i+1]`, and use only two add/subtract operations instead of 5.

A bonus to this bottom-approach is that once finished, you actually have an array with the number of ways you can make _any_ sum with the `n` dice. This makes it easy if you wish to find the number of ways `n` dice can form a sum _up to_ or _greater than_ a number.
