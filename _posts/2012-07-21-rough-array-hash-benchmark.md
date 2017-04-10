---
layout: post
status: publish
published: true
title: Rough Array Hash Benchmark
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 1070
date: '2012-07-21 09:59:06 -0700'
date_gmt: '2012-07-21 16:59:06 -0700'
categories:
- computer science
tags:
- hash array map
- array hash
- askitis
- map
- trie
- hat-trie
comments: []
---
I recently went on a mission to find (and perhaps build) a better dictionary. I've been looking at [Dr. Askitis' work](http://www.naskitis.com/) on so-called HAT-tries, which are something akin to a burst trie. It all seems reasonable enough, and his experimental results seem very promising. In particular, I was looking for an open source version of this data structure that didn't preclude commercial use (as Askitis' version does).

HAT-tries rely on another of Askitis' data structures, the [hash array map](http://crpit.com/confpapers/CRPITV91Askitis.pdf). Essentially, it's a hash table, but instead of using linked lists to store nodes containing the various key/value pairs stored in a particular slot, each slot is actually a buffer that stores a bunch of packed information, including the number of items in the buffer, the length of the string key, and the value itself. The idea is that this arrangement is much more conducive to caching (and hardware prefetches out of memory since each slot is a contiguous slab of memory). Contrast this to a more conventional approach in which each slot is a linked list that must be traversed to find the actual key/value pair that's being retrieved.

I should note that there are a [couple](https://github.com/dcjones/hat-trie) of [implementations](https://github.com/chris-vaszauskas/hat-trie) that I looked at before venturing out to [make my own](https://github.com/dlecocq/hat-trie). The design is actually relatively simple: hash a provided key to map it onto one of many internal buckets. If that bucket is empty, allocate enough memory to store an 1) integer counter of the number of pairs in this buffer, 2) integer length of the provided key, 3) a byte copy of the key itself, and 4) a byte copy of the value.

For the hash, I chose my personal favorite, [superfasthash](http://www.azillionmonkeys.com/qed/hash.html). I actually began by having my implementation follow the STL style of being able to provide a memory allocator, and when I didn't see the performance I wanted, I switched to `malloc` and `realloc` as prescribed in the paper. Even then, I did not see the performance I wanted. Of course, I imagine that my implementation could be improved, but I felt like it was certainly at least reasonable. I tried a number of alterations, including preallocating more memory than was needed in each slot with hopes that realloc would save me. No dice.

My benchmark was focused on speed. Memory was less of a concern for my needs, and so long as it stayed mostly unnoticeable (say, less than a couple hundred megabytes for a million keys), I was happy. I decided to give it a run against `std::map` (mostly to feel better about myself), and then `tr1::unordered_map` (mostly out of hubris). Although my rough implementation doesn't (yet) include fancy-schmancy features like iterators, it _barely_ edged out `tr1::unordered_map` for a small number of keys (less than 10k). When scaling up, however, the story was less than impressive.

This benchmark was performed using the first _k_ words from Askitis' `distinct_1` data set, and the strings were loaded into memory before running the tests. These numbers are each the best of 10 consecutive runs (hoping to warm the cache and cast each of these in the best possible light), with each of these containers being a mapping of `std::string` to `size_t`. Each key was associated with the value 1, and when querying, it was verified that the resulting value was still 1. The query was performed on the same input set of keys, and random query was run exactly the same, but after performing `std::random_shuffle` on the vector. It was compiled with `g++-4.2` with flags `-O3 -Wall` (though other optimization levels had almost no impact). I also tried with `clang-2.1` and the results were very similar. I encourage you to run the same bench on your own system and your own compiler version.

![Insertion Time Relative to std::tr1::unordered_map]({{ site.github.url }}/assets/2012/07/insert.png)

![Query Time Relative to std::tr1::unordered_map]({{ site.github.url }}/assets/2012/07/query.png)

![Random Query Time Relative to std::tr1::unordered_map]({{ site.github.url }}/assets/2012/07/random.png)

While `tr1::unordered_map` scaled better, at least for the purposes of HAT-trie, the number of items in the hash is relatively limited (roughly in the range of 10k). When testing the HAT-trie itself, I think the hash array map has earned at least a chance for a trial. For those curious, [my source is available on github](https://github.com/dlecocq/hat-trie).
