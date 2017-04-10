---
layout: post
status: publish
published: true
title: IP Geolocation
author:
  display_name: ''
  login: ''
  email: ''
  url: ''
wordpress_id: 498
date: '2009-04-16 09:59:36 -0700'
date_gmt: '2009-04-16 16:59:36 -0700'
categories:
- toys
- computer science
- tools
tags:
- mysql
- ip geolocation
- scripts
comments: []
---
There are a million services out there where you type in an IP address and get an estimate as to its location.  A few months ago I stumbled across a free IP geolocation database because I find myself using online services from time to time - I was sort of surprised how often it's helpful to know where traffic is coming from (outside of Google Analytics, etc.).

Using the [database](http://www.iplocationtools.com/sql_database.php) I found, I threw together a script that takes a list of domain names and / or IP addresses and gives you an idea of where it lives:

```
dan-lecocqs-macbook:~ dlecocq$ ipquery google.com
 209.85.171.100        Mountain View, US 94043 37.4192 -122.0570
dan-lecocqs-macbook:~ dlecocq$ ipquery yahoo.com
 68.180.206.184            Sunnyvale, US 94089 37.4249 -122.0070
dan-lecocqs-macbook:~ dlecocq$ ipquery apple.com
  17.251.200.70            Cupertino, US 95014 37.3042 -122.0950
dan-lecocqs-macbook:~ dlecocq$ ipquery mines.edu
     138.67.1.8               Golden, US 80401 39.7146 -105.2430
```
