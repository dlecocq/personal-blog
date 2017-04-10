---
layout: post
status: publish
published: true
title: Parallel Ray Tracer
author:
  display_name: ''
  login: ''
  email: ''
wordpress_id: 480
date: '2009-04-04 14:54:05 -0700'
date_gmt: '2009-04-04 21:54:05 -0700'
categories:
- school
- computer science
- projects
tags:
- graphics
- raytracer
- ray tracing
- cluster
- parallel
comments: []
---
This afternoon I was able to successfully parallelize the ray tracer I wrote for Graphics II to run on the Alamode cluster at Mines.  Using 17 machines, I was able to render a 4,096 x 4,096 pixel image with 25 passes and up to 5 reflections.  It took only 1 minute and 20 seconds.

![Reflective spheres rendered at high resolution on a small cluster.]({{ site.github.url }}/assets/2009/04/output.png)

![Another image rendered on the same cluster]({{ site.github.url }}/assets/2009/04/output1.png)

For the benefit of those who are not computer scientists, this is what the input file looks like:

```
8192 8192
0 0 20
-1 -1 1
2 0 0
0 2 0
3 10 10 0.8
0.2
9
# These next few lines will define a triangle
T
# With one of the points at (1, 1, 1)
1 1 1
# and the next point here:
0.12321 0.12321 -1
# and the last point here:
-1 1 1
# and with this color setting
1 1 1 1 1 1 0 1 0.7
T
-1 1 1
-0.12321 0.12321 -1
0.12321 0.12321 -1
1 1 1 1 1 1 0 1 0
T
1 -1 1
0.12321 -0.12321 -1
-1 -1 1
1 1 1 1 1 1 0 1 0
T
-1 -1 1
-0.12321 -0.12321 -1
0.12321 -0.12321 -1
1 1 1 1 1 1 0 1 0
T
1 1 1
0.12321 0.12321 -1
1 -1 1
1 0 0 1 0 0 0 1 0
T
1 -1 1
0.12321 -0.12321 -1
0.12321 0.12321 -1
1 0 0 1 0 0 0 1 0
T
-1 1 1
-0.12321 0.12321 -1
-1 -1 1
1 1 0 1 1 0 0 1 0
T
-1 -1 1
-0.12321 -0.12321 -1
-0.12321 0.12321 -1
1 1 0 1 1 0 0 1 0
S
0 0 0 0.5
1 0 1 1 0 1 0 1 0.3
```
