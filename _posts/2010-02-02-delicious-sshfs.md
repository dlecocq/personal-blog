---
layout: post
status: publish
published: true
title: Delicious sshfs
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 809
date: '2010-02-02 23:47:22 -0800'
date_gmt: '2010-02-03 06:47:22 -0800'
categories:
- computer science
- command line ninja magic
tags:
- sshfs
- mounting volumes
- working remotely
comments: []
---
It is extremely easy for computer scientists (well, and the rest of humanity) to get entrenched in their ways.  You've learned and taken the time to become a master of a programming language, or tool, and it's a serious time investment.  As such, new tools generally have to be very compelling in order to get someone to switch.  For example, I'm a recent svn-to-git convert, and am often met with horrified looks when I suggest others give it a shot.  A visiting professor I spoke to yesterday said that it would be years before they stopped using svn.

Recently, I've begun using sshfs.  It mounts a volume over ssh and appears as any normal folder on your computer.  It behaves that way at the command line, or your text editor, or as far as VLC is concerned.  For development, I had always maintained a local copy and rsync'd changes to the remote machine I was using.  It worked well enough, and was often more convenient than using a tool like Cyberduck.

Aron recommended sshfs, and though it took me a while to try it out, I'm hooked.  No more trying to remember if I've synchronized my code with the other machine I'm using, only editing and saving.  It's really easy when you have ssh keys set up as well.  To mount your home directory on a remote machine:

```bash
$> mkdir datastore_mount
$> sshfs datastore: datastore_mount
```

And now, I've got access to remote files on datastore as if they lived in the directory datastore_mount.  Unmounting is business as usual:

```
$> umount datastore_mount
```

Try it, use it, live it.  You won't regret it.
