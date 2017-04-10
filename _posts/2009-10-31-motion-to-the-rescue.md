---
layout: post
status: publish
published: true
title: Motion to the Rescue
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 679
date: '2009-10-31 03:15:54 -0700'
date_gmt: '2009-10-31 10:15:54 -0700'
categories:
- computer science
- life
tags:
- camera
- motion
- linux
- stolen
- theft
comments:
- id: 498
  author: Colin
  author_email: creutter@gmail.com
  date: '2009-10-31 16:59:00 -0700'
  date_gmt: '2009-10-31 23:59:00 -0700'
  content: "That's great! I made that last comment and then I remembered your camera
    was stolen. But now you have it back! (They didn't find your backpack?)\r\n\r\nLast
    year someone was spray painting cars and the side of the house I was living in
    and I tried something like this... It didn't work because they stopped and then
    the pizza delivery guy saw the camera and was like, \"Nice camera...?\" So I took
    it down.\r\n\r\nThe guy you caught is probably glad to still have both of his
    hands."
- id: 841
  author: Otto Graham
  author_email: otto@grahamcracker.com
  date: '2010-06-17 03:08:18 -0700'
  date_gmt: '2010-06-17 10:08:18 -0700'
  content: "I stumbled upon this post and thought you might be interested in free
    software that does something similar to \"motion\" but is much more sophisticated.
    \ Take a look at http:&#47;&#47;www.vitamindinc.com ... there's a free version
    which will almost certainly work with your camera.  \r\n\r\nVitamind D offers
    email alerts when certain events happen and you can set rules and filters for
    events.  Also, the software tries to be smart about what is recognized as an object,
    thus drastically culling the video review time."
- id: 843
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2010-06-17 06:23:35 -0700'
  date_gmt: '2010-06-17 13:23:35 -0700'
  content: We found Vitamin D in the process, but the hardware we had available was
    running Linux.  Tyler had found Vitamin D when we were looking for options, and
    while we are both Mac users and it could have been an option for our home use,
    part of the point was to use Linux.  Plus, we got a certain amount of experience
    with some of the inner workings of the networking scripts!
- id: 2438
  author: free chatline
  author_email: Eddins33168@yahoo.com
  date: '2012-12-20 01:22:48 -0800'
  date_gmt: '2012-12-20 08:22:48 -0800'
  content: I went over this site and I think you have a lot of superb info, saved
    to fav (:.
---
For the last several weeks, things have been disappearing from my office area.  First, a backpack I had left out.  I had assumed that people in an academic building full of offices would be trustworthy, perhaps I had this one coming.  A couple weeks after that, I went to use my camera only to find it gone.  Funny, I thought I locked that drawer.  I guess I must have been mistaken.  A couple weeks after that, my iPhone gone.  This time, I'm certain I locked the drawer, and there are marks on the cabinet that indicate it being forced open.

Fed up with the disappearing devices, my friend Tyler and I set out on a mission.  We went into Jeddah, bought a webcam and using the [popular](http://www.theregister.co.uk/2005/02/17/chav_burglar/) (thank to Iain for the link) Linux package [motion](http://www.lavrsen.dk/twiki/bin/view/Motion/WebHome), we set up a hidden motion-detecting spy cam in our office.  We have a Linux box sitting near our desk (we've locked it to the floor), and so we hid the camera, trained on the place where most of disappearances had taken place.

![A test shot of Tyler as we\'re setting it up.]({{ site.github.url }}/assets/2009/10/01-20091023174435-04.jpg)

What motion does is that every time it detects the picture it sees changing, it takes pictures for five seconds (or until the motion stops - which ever takes longer).  It's supposed to be able to encode a video with ffmpeg on the fly, but as it wasn't working right for us, we decided to just go ahead and throw it into a script.  I wrote a short bash script that just took all the photos, archived them and then generated a video (when dealing with the tens of thousands of photos generated in an average day and night I learned about xargs).  It also provides triggers for when motion is captured (for example, if you'd like to update [Twitter](http://tech.shantanugoel.com/2008/05/14/keep-tab-on-home-security-with-a-webcam-and-twitter.html) (via [Lifehacker](http://lifehacker.com/391141/get-twitter-notifications-from-a-motion+detecting-webcam)) you can do this with curl).

One night, when bored and filled with anger about the situation, I decided to check the feed and found footage of someone clear-as-day breaking into my cabinet.  I first saw it about 20 minutes after the fact, but I was sure the guy was still there.  I called Tyler and we quickly deliberated (after getting the opinions of a couple officemates) and we decided to wait until the morning and talk to the security officer.

![Looking for goodies.  The man\'s face is not visible in this shot nor is this frame alone incriminating.  In the context of the video, you can see him gain entry, begin rummaging and removing items.]({{ site.github.url }}/assets/2009/10/01-20091026215724-10.jpg)

We spent some time with them the next morning, giving them footage and printing key frames, and then they said they'd look into it.  They assured us they would not involve the local authorities if they didn't have to (the penalty for such crimes in Saudi Arabia can be quite stiff) and would take care of it discreetly.  That night, they arrested four people and recovered a number of electronic devices.  They held them as evidence for a bit, but today, I was given back my camera and iPhone (the only really big-ticket items I had stolen).

I am extremely relieved to have these back, especially my camera as I had been wanting to take photos of trips, events, etc. in its absence.  Our next step was going to have off-site storage in case the bandits took off with our computer, but it would seem it wasn't necessary.

Motion: 1, Thieves: 0

Of course, this was not a solo effort by any means.  Some system admins and colleagues in the office park offered input, and the evidence wouldn't have left our webcam if not for the security staff.  Thanks, guys.
