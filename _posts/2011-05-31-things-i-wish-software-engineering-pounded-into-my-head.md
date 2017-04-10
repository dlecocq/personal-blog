---
layout: post
status: publish
published: true
title: Things I Wish Software Engineering Pounded Into My Head
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 938
date: '2011-05-31 10:50:53 -0700'
date_gmt: '2011-05-31 17:50:53 -0700'
categories:
- school
- computer science
tags:
- version control
- documentation
- unit testing
- issue tracking
- best practices
- software engineering
comments: []
---
Until recently, I bore the burden of a dirty little secret: I didn't use unit testing. I don't know if this has been other students' experience, but my software engineering course could have been a lot better. Perhaps it's a topic that requires students to determine their own level of involvement, but particularly, I am irked that these issues were not as developed as they could have been:

1. Version control - svn, git, something! Anything, really! Just use something!
2. Unit testing - sure we talked about it, but its utility isn't clear until you use it in earnest.
3. Documentation - always felt more like a chore than a tool
4. Issue tracking - [Joel on Software](http://www.joelonsoftware.com/articles/fog0000000029.html) said it best: "I was born with only two bug-storing-slots in my brain."
5. More best practices - [Effective C++](http://www.aristeia.com/books.html) (it's worth it -- get it and read it) alone was worth more than the course was.

I concede that these are things whose utility might be hard to convey to college students who may or may not be working on projects they really believe in. Still, very important.

One of the things I like about documentation is that you can refer to the documentation when uncertain about side-effects, input, etc. of functions and you don't really feel like reading through code and trying to keep it in your brain-RAM. Not only that, but I usually refer to my own documentation to get an idea of the guarantee that a function was offering, to try to make sure that it's making those __same guarantees after I make changes__. Not only this, but __articulating functionality crystalizes it's implications__ in your mind. When describing how something works to a friend, it often reminds you of issues you hadn't considered. Writing documentation is the same in this respect.

When working with other people, while it's nice to be able to talk face-to-face, the issues we think of that need changing go in one ear and out the other for me. Not that it wasn't a good idea, but my brain-RAM is not infinite. __Bugs, features, ideas, issues all get paged out of my head. Write them down instead,__ which is where issue tracking comes in. Design questions and decisions come out of issues all the time, and the trail of comments and discussion make a nice reference for documentation.

I find that when I'm fixing a bug, the functionality of that chunk of code gets reduced to that particular feature in my mind. So, if when I try using it, if that bug is fixed, then my job is done. But we've all experienced unintended side effects, where in fixing one thing, we break another. Having a list of features to check is a step up from trying to remember the things that need to work, but it's much less than the power of unit testing. I've recently been using [UnitTest++](http://unittest-cpp.sourceforge.net/UnitTest++.html) for C++ applications, and [QUnit](http://docs.jquery.com/QUnit) from the jQuery people, and have been pleased to thrilled. It allows you to __check functionality exhaustively and quickly on a whim__. Even the task of __writing the tests forces you to define the functional requirements of your code__, and I find it helps to clarify a lot.

Version control lets you try crazy new approaches and track changes, isn't that great? I was helping a friend last semester with some of his code, and he was trying to make code changes with copy, paste, and the undo buffer. In the end, he ended up introducing more bugs into the code than he was fixing. __It's intractable to keep these kinds of code changes in your brain-RAM.__ Use something, use anything. I have a qualm with svn because it was something I used so rarely, I could never remember how to set it up. __Even a barrier as small as that was enough to prevent me from using version control at all.__ I love git because it's so easy to set up, I use it for almost anything: from a report (if using LaTeX), to a weekend project, to my thesis. There are tons of tools out there, but __just use something.__
