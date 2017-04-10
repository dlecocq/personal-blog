---
layout: post
status: publish
published: true
title: VTK and Volume Visualization
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 705
date: '2009-11-09 11:40:25 -0800'
date_gmt: '2009-11-09 18:40:25 -0800'
categories:
- school
- computer science
tags:
- graphics
- visualization
- vtk
- raw
- pvm
- convert
- volume
- chest
- CT
comments:
- id: 829
  author: RSAO
  author_email: rallendes@utalca.cl
  date: '2010-06-07 11:40:30 -0700'
  date_gmt: '2010-06-07 18:40:30 -0700'
  content: "Hey... been trying to get some pretty pictures following your comments,
    but cant get vtk to do any type of nice rendering... did you have to do any other
    sort of twicking to the datasets? I've downloaded them from the volume library,
    converted them to raw and added the header exactly as you post it... can you point
    out the points used for the transfer funcitions? perhaps show a bit of the code?\r\n\r\nthanks
    alot"
- id: 831
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2010-06-09 07:38:23 -0700'
  date_gmt: '2010-06-09 14:38:23 -0700'
  content: "I've uploaded my report for the assignment, which has a little bit
    more detail about the transfer functions.  The way I set it up, it reads the transfer
    function from a file (sure, it's a little clunky) of the following format:\n\nvalue1
    \ opacity1\nvalue2  opacity2\n....\n\nFor example:\n0\t\t0.0\n10\t\t0.0\n21\t\t0.3\n40\t\t0.3\n41\t\t0.0\n60\t\t0.0\n76\t\t1.0\n\nHere
    the transfer function is piecewise linear between these points.  As I understand
    it, transfer function selection is still a largely open research problem.  The
    biggest piece of advice that I can give is to insert single peaks into the data
    to explore where there are common values, and then mixing from there where appropriate.\n\nThere
    are also <a href=\"http:&#47;&#47;www.commontk.org&#47;index.php&#47;Documentation&#47;WidgetPlans\"
    rel=\"nofollow\">some widgets<&#47;a> available (apparently), though I've not
    used them.  This allows you to explore the function space a little more interactively."
---
This week for Scientific Visualization, we're talking about volume rendering and using VTK to explore some data.  I got some datasets from [The Volume Library](http://www9.informatik.uni-erlangen.de/External/vollib/) and after a little tinkering, got VTK to render them. (And now a quick aside on how to do this as I didn't find much information on the subject).

I used a tool (pvm2raw) available as part of the [V^3](http://www.stereofx.org/volume.html) library to convert the pvm files to raw, but VTK requires its own simple [header](http://www.eichberger.de/2005/10/how-to-convert-raw-file-to-vtk.html).  I actually found that this particular header didn't work (perhaps a VTK versioning problem?) and so taking guidance from this, checked the header of one of the VTK-included volumes:

```bash
head VTKData/ironProt.vk
```

This header more or less included a little information on the grid size, spacing and representation of the data:

```
# vtk DataFile Version 1.0
<Name of File>
BINARY
DATASET STRUCTURED_POINTS
DIMENSIONS <x> <y> <z>
ASPECT_RATIO 1 <y/x> <z/x>
ORIGIN 0 0 0
POINT_DATA <x * y * z>
SCALARS scalars <unsigned_char|unsigned_short>
LOOKUP_TABLE default
<remember to include a newline here>
```

Concatenating the header with the raw:

```
cat header CT-Head.raw > CT-Head.vtk
```

At that point, I was in business and was able to move on to generating pretty pictures.  Granted, these datasets are pretty sparse, but still VTK did a pretty reasonable job.  __Update:__ a comment asked for a little bit more detail on this assignment, and so I'm including [my report]({{ site.github.url }}/assets/2009/11/report.pdf) for the project.

![Bruce]({{ site.github.url }}/assets/2009/11/Bruce.png)
![chest]({{ site.github.url }}/assets/2009/11/chest.png)
![chest2]({{ site.github.url }}/assets/2009/11/chest2.png)
![engine]({{ site.github.url }}/assets/2009/11/engine.png)
![foot]({{ site.github.url }}/assets/2009/11/foot.png)
![orange]({{ site.github.url }}/assets/2009/11/orange.png)

I was amazed today that we can see inside of things... without taking them apart.  What an age to live in.  Especially the [virtual autopsy table](http://www.visualiseringscenter.se/1/1.0.1.0/230/1/) I read about recently.  In 20 years, we'll have Firefly-style real-time holographic body scans (ignore music, skip to 0:45):

<object width="480" height="385" class="aligncenter"><param name="movie" value="http://www.youtube.com/v/Kgq_Psl9N6Q&hl=en&fs=1&"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/Kgq_Psl9N6Q&hl=en&fs=1&" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="385"></embed></object>
