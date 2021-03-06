---
layout: post
status: publish
published: true
title: 'Boost, typedef, #define and GCC Pain'
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 969
date: '2011-08-04 08:40:34 -0700'
date_gmt: '2011-08-04 15:40:34 -0700'
categories:
- computer science
- command line ninja magic
- SEOmoz
tags:
- gcc
- g++
- preprocessor
- define
- typedef
- boost
comments:
- id: 1726
  author: cwalsh
  author_email: walshrych@gmail.com
  date: '2011-08-04 14:31:30 -0700'
  date_gmt: '2011-08-04 21:31:30 -0700'
  content: 'Brilliant! I''ll put that -E flag into my toolbox :) I''m working in a
    very old and very ugly c&#47;c++ code-base; there are #defines and externs all
    over the place!'
- id: 1727
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2011-08-04 15:52:08 -0700'
  date_gmt: '2011-08-04 22:52:08 -0700'
  content: Yeah, I was really pleased to find this one. Also, really, Effective C++
    is one of the most useful things I've read in recent memory.
- id: 2108
  author: Merissa Safford
  author_email: Dagel63693@gmail.com
  date: '2012-03-14 04:31:35 -0700'
  date_gmt: '2012-03-14 11:31:35 -0700'
  content: Some truly fantastic content on this site, regards for contribution.
- id: 2413
  author: Bonusy bukmacherskie
  author_email: Deshong6858@gmail.com
  date: '2012-11-06 16:32:11 -0800'
  date_gmt: '2012-11-06 23:32:11 -0800'
  content: 'I seldom leave responses, however I read a lot of responses on this page
    Boost, typedef, #define and GCC Pain. I do have 2 questions for you if it''s okay.
    Could it be just me or does it give the impression like a few of these remarks
    appear like they are left by brain dead people? :-P And, if you are writing at
    other online social sites, I would like to keep up with you. Could you make a
    list of the complete urls of your social community sites like your twitter feed,
    Facebook page or linkedin profile?'
- id: 3014
  author: Auto Spiele
  author_email: Zarella30919@yahoo.com
  date: '2013-07-07 16:44:53 -0700'
  date_gmt: '2013-07-07 23:44:53 -0700'
  content: Just wish to say your article is as amazing. The clearness in your post
    is simply great and i can assume you are an expert on this subject. Well with
    your permission allow me to grab your feed to keep updated with forthcoming post.
    Thanks a million and please continue the enjoyable work.
- id: 3150
  author: Beth
  author_email: guillermohardiman@googlemail.com
  date: '2014-07-20 23:45:03 -0700'
  date_gmt: '2014-07-21 06:45:03 -0700'
  content: "It was hard for me to find your posts in google. I found it on 12 position,
    you have to build \r\na lot of quality backlinks , it will help you to increase
    traffic.\r\nI know how to help you, just type in google - k2 seo tricks"
---
Recently I've been working on porting some code to Mac, and yesterday I ran into a bug that stumped me for a little bit. Compiling against Boost was raising a bunch of errors, specifically in lines that seemed pretty innocuous (from `cstdint.hpp`):

```
using ::int8_t;
using ::int_least8_t;
using ::int_fast8_t;
using ::uint8_t;
using ::uint_least8_t;
using ::uint_fast8_t;
```

G++ kept giving me errors for each of those lines: `error: expected unqualified-id before ‘signed’,` referring to the line `using ::int8_t.` I'm a little embarrassed that I couldn't figure it out right away, but eventually I figured out that it was caused by `int8_t` being `#define`d somewhere else. For those of you that don't know, #define really just takes one term and substitutes every subsequent occurrence of that term with one you provide.

```
// If you define it as a macro
#define int8_t signed char

// Then this line will be interpreted very differently from how you expect
using ::int8_t;

// Gets interpreted as "using ::signed char"!!!
```

And this is what `g++` had been complaining about. That is not legal C++ syntax; I'm sorry I doubted you, `g++`! But there still remained a larger question: where were these types getting defined? I didn't want to be in the business of "patching" a library, and especially the largely impeccable Boost library. Typically these types (`int8_t`, `uint8_t`, etc.) are defined in `cstdint` or `stdint.h`, but looking at the system's version, I found to my surprise that they were not macro-defined, but typedef'd, which is the right way to do it.

__Sidebar:__ In general, you should be using typedef instead of `#define` for this reason, and another very good reason. Because #define macros just go through code and blindly replace references, it can be difficult to trace the origin of a type, but typedefs are carried through, and so even after preprocessing, you can still see what the semantic meaning was (that you wanted `int8_t` specifically, not just something that happens to be the same type). And when debugging, this extra type information can be helpful. Similarly, you should generally also use const to define constants in your code, instead of #define macros, because while you might remember what a magic number is when you write it into your library, the meaning of that particular constant becomes unclear when you encounter it's value when debugging. (If you haven't, read [Scott Meyer's Effective C++](http://www.aristeia.com/books.html).)

Getting back to the morality tale, the library I was porting wasn't macro-defining `int8_t`, and stdint.h wasn't, so where was the culprit? Clearly there are potentially hundreds of places it could be, and I was running out of good guesses. Luckily, SEOmoz C++ shaman Martin taught me a little __ninja magic__: use the `-E` flag with `g++` to only run the preprocessor stage, and redirect the output into a file! When compiling with `make`, it typically spits out the offending `g++` command, so rerun it to just pass that one through the preprocessor, which reaches out and fetches the header files and gloms them in order into one giant input file. Then, step through _this_ file to see where `define` and `int8_t` occur on the same line! In two minutes we were able to find the header that was causing all this trouble, where I had spent two hours learning and reading about where the problem might be.

In the end we found it in a very small library that we happened to use, and on Mac we had just been using a slightly old version and this problem had been fixed in subsequent releases. Still, I'm glad to have added this preprocessor trick to my toolkit.
