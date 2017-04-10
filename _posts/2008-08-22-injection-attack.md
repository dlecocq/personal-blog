---
layout: post
status: publish
published: true
title: Injection Attack
author:
  display_name: ''
  login: ''
  email: ''
  url: ''
wordpress_id: 112
date: '2008-08-22 20:39:28 -0700'
date_gmt: '2008-08-23 03:39:28 -0700'
categories:
- web
- computer science
tags:
- vulnerability
- security
- injection attack
- mysql
- sanitize
comments: []
---
For those of us familiar with SQL, we're almost certainly familiar with SQL injection attacks.  We've talked about them in class, and maybe the more nefarious of us has even tried it on a form or two.  There are vulnerable ones out there - I remember having to tell an experienced programmer about sanitizing his form input.  If you're reading this, you know who you are.

For those of you who don't know about SQL injection attacks, the long and short of it is you try to give input in a form that will be interpreted as SQL and executed.  So, for example (see comic link below), you might try to give input that deletes records, or inserts malformed records.  For example, a simple, well-formed request to insert a comment might be:

```sql
INSERT INTO `comments` (`name`, `comment`) VALUES ('Bob', 'My comment');
```

If Bob's comment has a quote in it, though, if you haven't sanitized the input, you'll get something that doesn't make any sense to the interpreter:

```sql
INSERT INTO `comments` (`name`, `comment`) VALUES ('Bob', 'It's my comment');
```

Say Bob were feeling malicious, part of his comment could be an entirely new command that the interpreter would deem valid.  If his comment were "Haha suckers!'); DROP TABLE `comments`;", then we'd get two well-formed commands that would get executed:

```sql
INSERT INTO `comments` (`name`, `comment`) VALUES ('Bob', 'Haha suckers!'); DROP TABLE `comments`;');
```

This, as you can imagine, is not desirable.  So, part of sanitizing input is to escape out characters that are normally recognized by the interpreter:

```sql
INSERT INTO `comments` (`name`, `comment`) VALUES ('Bob', 'Haha suckers!__'__); DROP TABLE `comments`;');
```

At any rate, a few months ago, I actually had an attempt more or less 'caught on tape' in the comments section of my blog.  I got an email that there was a new comment awaiting moderation, and it was this:

```
Bill164415140′,’311521868billy@msn.com’,”,’30.68.179.4′,’2008-03-12 16:12:16′,’2008-03-12 16:12:16′,”,’0′,’lynx’,'comment’,'0′,’0′),(’0′, ”, ”, ”, ”, ‘2008-03-13 16:12:16′, ‘2008-03-13 16:12:16′, ”, ’spam’, ”, ‘comment’, ‘0′,’0′ )
```

Not exactly the most harmful stuff.  Still, it was nice to see an attempt in the wild.

Another good example is [this xkcd comic](http://xkcd.com/327/).
