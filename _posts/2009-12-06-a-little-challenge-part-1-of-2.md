---
layout: post
status: publish
published: true
title: A Little Challenge (Part 1 of 2)
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 766
date: '2009-12-06 13:09:15 -0800'
date_gmt: '2009-12-06 20:09:15 -0800'
categories:
- web
- computer science
- hacks
- hobbies
tags:
- puzzle
- challenge
- fun
comments:
- id: 546
  author: Matt Matteson
  author_email: matt@dlzip.com
  date: '2009-12-07 00:35:25 -0800'
  date_gmt: '2009-12-07 07:35:25 -0800'
  content: "Thanks for the puzzle. \r\n\r\nsOlvEdIt - Encrypted just means obscured.
    \r\n\r\nI wish I knew all the sites I create an account for at least are doing
    this though..."
- id: 549
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2009-12-08 13:49:54 -0800'
  date_gmt: '2009-12-08 20:49:54 -0800'
  content: Yeah, it's like modern locks - not strong, but just enough inconvenience
    to keep people out for the most part.  The formatting, obfuscation and so forth
    are really the only deterrents.
---
Several months ago, I was given credentials to download a piece of software, and I needed to download another copy only to find that I had forgotten the password.  I anticipated it would take quite a while to email the people in charge, and on a whim I decided to take action.  Right click, view source.

To my surprise, all the authentication was done in JavaScript, though in all fairness it was "encrypted."  I've changed the underlying keyphrase in a code example, and I pose a small puzzle - find the password.

You may find [jconsole](http://www.jconsole.com/) helpful.

```
var pass=new Array()
var t3=""
var lim=8
pass[0]="fE13Cw9emtKIg1F"
pass[1]="wKTuZEy387Im8b2"
pass[2]="3NKevEgjpWWwmSE"
pass[3]="CryO6BmP9XpUlke"
pass[4]="8R4Gf2sgs5Xs5KI3"
pass[5]="62GZJ9Dzc2y8lBTU"

var extension=".html"
var enablelocking=0
var numletter="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
var temp3=''
var cur=0

function max(which){
return (pass[Math.ceil(which)+(3&15)].substring(0,1))
}

function testit(input){
temp=numletter.indexOf(input)
var temp2=temp^parseInt(pass[phase1-1+(1|3)].substring(0,2))
temp2=numletter.substring(temp2,temp2+1)
return (temp2)
}


function submitentry(){
t3=''
verification=document.password1.password2.value
phase1=Math.ceil(Math.random())-6+(2<<2)
var indicate=true
for (i=(1&2);i<window.max(Math.LOG10E);i++)
t3+=testit(verification.charAt(i))
for (i=(1&2);i<lim;i++){
if (t3.charAt(i)!=pass[phase1+Math.round(Math.sin(Math.PI/2)-1)].charAt(i))
indicate=false
}
if (verification.length!=window.max(Math.LOG10E))
indicate=false
if (indicate)
alert("Correct password.")
else
alert("Invalid password. Please try again")
}
```
You can also get it in a [testable html page]({{ site.github.url }}/assets/2009/12/authentication.html).
