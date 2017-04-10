---
layout: post
status: publish
published: true
title: Growlnotify
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 93
date: '2008-04-12 20:58:08 -0700'
date_gmt: '2008-04-13 03:58:08 -0700'
categories:
- mac
- hacks
tags:
- ninja magic
- Growl
- growlnotify
- command line
comments: []
---
If you're a [Growl](http://growl.info) user, you probably appreciate (or are annoyed by) being able to get updates from various applications in a relatively out-of-the-way fashion.

There is a command line utility included with Growl called growlnotify.  It allows you to send up your own alerts from your own code (say using exec(3) or in your shell scripts), but it's nice to use for other things, too.  If I have a command that's conceivably going to take a while, I tack on a && and growlnotify.  Just like some people use

```bash
make && ./myapp
```

when they run their code to ensure it's running the latest saved version, it's a nice way to get a heads-up instead of waiting a few minutes for that god-awful command to run.  For example, recently I was using curl(1) to get a bunch of files off of a server (when I fall behind on a webcomic, it's just easier to download a bunch of them and browse them quickly in Preview instead of clicking through each), and it ended up taking a good 10 minutes:

```bash
curl http://boasas.com/boasas/[1-940].gif -o "#1.gif" && growlnotify --message "I'm done downloading" --title "curl"
```

I get back to reading my dailies, and by the time I've forgotten that I set it going, up pops a nice little notification:

![Growlnotify]({{ site.github.url }}/assets/2008/04/picture-1.png)

I will note that it can be a little finnicky.  It generally has better success when no title is supplied, and if you're going to be running it with &&, I might suggest making it a

```
mycommand && echo $? && growlnotify --message "my message" --title "mycommand"
```

Since it gets its message argument from standard in, you can also pipe to it if your command returns a value of which you'd like to be notified:

```
make ; if [ $? -eq 0 ]; then echo "Success"; else echo "Failure"; fi | growlnotify --title "make"
```

![Growlnotify Make]({{ site.github.url }}/assets/2008/04/picture-2.png)
