---
layout: post
status: publish
published: true
title: Git in Four Commands
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 941
date: '2011-06-05 10:47:09 -0700'
date_gmt: '2011-06-05 17:47:09 -0700'
categories:
- computer science
tags:
- version control
- git
comments: []
---
[Git](http://book.git-scm.com/) is not a complicated tool for most things. I still find it a little tricky to set up for multiple users, but even that's pretty easy. It really caters to the use-case where you're just starting a project, or are the sole developer, but just want to keep track of changes and versions, make branches, etc.

The first major point of git is that everyone has their own copy of the repository. When you commit changes, you commit them to your local copy of the repository. If you are working on a group project, there is a shared resource that can be __pushed to__ and __pulled from__, but I actually like that it takes an extra command to do that -- it forces me to make sure that it's what I actually want to do. Now, to the bare-bones commands:

1. __git init__ -- Wherever you're writing your code, type "git init". It creates an empty repository in that directory (there's a magical hidden folder ".git" that gets created and knows things).
2. __git status__ -- Git knows which files have changed since you last saved changes, and it will happily tell you which files are new and changed with this command.
3. __git add__ -- When you change files and are at a point where it make sense to save changes to your code (a bug fix, a new feature, etc.), then tell git which files you want to put in this commit  with "git add". If committing a set of changes with git is like shooting a gun, then adding files to be committed is like loading that gun. Git knows which files have changed, but it can make sense to group changed files into different logical commits. For example, if you fix two bugs between commits, you might want to add the changes for each bug fix separately.
4. __git commit__ -- When you have added a bunch of changed files to be committed, now you're ready to actually commit those changes. Type "git commit -m 'A short, meaningful summary of the changes that happened.'"

There is a lot more to git, and a [million tutorials](http://www.kernel.org/pub/software/scm/git/docs/gittutorial.html), that will explain things in more detail, but these are the commands I spend 95% of my time using, and enough to at least get you starting tracking changes for anything and everything. It doesn't matter very much what version control you use, __just use something.__
