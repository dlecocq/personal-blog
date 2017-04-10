---
layout: post
status: publish
published: true
title: Triangle Strip for Grids - A Construction
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 791
date: '2009-12-25 02:02:36 -0800'
date_gmt: '2009-12-25 09:02:36 -0800'
categories:
- computer science
- math
tags:
- graphics
- opengl
- webgl
- mesh
- triangle strip
comments:
- id: 767
  author: jeckil
  author_email: crystaldonut@gmail.com
  date: '2010-03-30 20:32:08 -0700'
  date_gmt: '2010-03-31 03:32:08 -0700'
  content: "One of the best tutorials I have ever seen on the theory behind the topic.\r\n\r\nOne
    thing I don't understand yet:\r\n\r\n\"the 3 and 5 are explained by the fact that
    we need to change columns in the mesh, by one step at a time.\"  Can you elaborate
    on this more please? what do the columns mean?, one step at a time?\r\n\r\nThanks
    a lot. :)"
- id: 768
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2010-03-31 05:08:58 -0700'
  date_gmt: '2010-03-31 12:08:58 -0700'
  content: |-
    Here columns refers to the columns of vertices, like (0, 4, 8, 12) or (2, 6, 10, 14).  Suppose we have <em>n<&#47;em> vertices in a row (in this case, 4) and we are at vertex indexed <em>a<&#47;em> (let's say 5).  Then <em>a + 4<&#47;em> would be the vertex below it, and <em>a - 4<&#47;em> would be the vertex above it.

    If instead of adding or subtracting <em>n = 4<&#47;em> from <em>a<&#47;em>, we added or subtracted <em>n + 1 = 5<&#47;em>, we would get the vertex in the row below it, and one column to the right.  For example, vertex <em>a + 5 = 10<&#47;em> is diagonal from <em>a<&#47;em> in this fashion.  Using <em>n - 1 = 3<&#47;em> does the same thing, except for one column to the left (<em>a + 3 = 8<&#47;em> is one row down from <em>a<&#47;em> and one column to the left).

    I hope this clarifies a little bit!
- id: 1445
  author: Noa
  author_email: noa@cantin.net
  date: '2011-02-28 13:51:54 -0800'
  date_gmt: '2011-02-28 20:51:54 -0800'
  content: "It was very helpful for me to, thanks. I implemented it, and realized
    at some point that the normals are inverted at every change of row (because I'm
    setting normals per vertex). I had to add some more \"glue\" every time. So in
    the previous explanation, I inserted \"7\" twice, and got 0, 4, 1, 5, 2, 6, 3,
    7,7,7,8, 12, 9, 13, 10, 14, 11, and 15. That way the normal stays in the right
    orientation. \r\n\r\nNoa"
- id: 1449
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2011-03-01 08:13:15 -0800'
  date_gmt: '2011-03-01 15:13:15 -0800'
  content: I hadn't noticed any funny business with the normals, but that's good to
    know! I wonder if it was because I was using my own shader -- were you using the
    fixed-function pipeline?
- id: 1467
  author: Noa
  author_email: noa@cantin.net
  date: '2011-03-07 07:55:09 -0800'
  date_gmt: '2011-03-07 14:55:09 -0800'
  content: "Dan,\r\n\r\nYes I was using the FFP, pre-computing the normals per vertex
    on cpu. Because the orientation of the triangles on the triangle strip alternates,
    my normals where miss-oriented on every odd row. Because I need to compute normals
    per vertex, I had to modify the algorithm and add some glue."
- id: 1475
  author: John
  author_email: boeroboy@gmail.com
  date: '2011-03-09 16:11:37 -0800'
  date_gmt: '2011-03-09 23:11:37 -0800'
  content: Thanks for trying to cheer me up.  I still prefer display lists in more
    ways than one.  It's a shame they're trying to bury such a flexible and powerful
    feature.  VBOs are just a crippled version of the display list.
- id: 1476
  author: John
  author_email: boeroboy@gmail.com
  date: '2011-03-09 16:16:20 -0800'
  date_gmt: '2011-03-09 23:16:20 -0800'
  content: "Correction: it looks like gl.NewList (); is available.  Was it added after
    this article?  Feel free to skip my post or update the article if display lists
    are truly currently supported in webgl.\r\n\r\nThanks"
- id: 1478
  author: dan.lecocq
  author_email: dan.lecocq@kaust.edu.sa
  date: '2011-03-10 06:39:58 -0800'
  date_gmt: '2011-03-10 13:39:58 -0800'
  content: |-
    As far as I know, WebGL doesn't have display lists. At least in Chrome and WebKit&#47;Safari, I didn't find a gl.NewList(). I'd be surprised if there were, as it's supposed to essentially follow the OpenGL ES 2.0 spec, which doesn't include display lists.

    In what environment did you find gl.NewList()? You've make me curious!
- id: 1744
  author: Ricardo Sanchez
  author_email: nardove@yahoo.com
  date: '2011-08-10 13:33:05 -0700'
  date_gmt: '2011-08-10 20:33:05 -0700'
  content: "Dan excellent tutorial!\r\n\r\nI am new to opengl in general and I am
    struggling to implement this, I start a stackoverflow topic on the subject and
    I wonder if you will be able to have a look and let me know and assist on my implementation,
    any help will be much appreciated\r\n\r\nHere is the link\r\nhttp:&#47;&#47;stackoverflow.com&#47;questions&#47;7011017&#47;help-getting-vertex-indices-from-a-grid\r\n\r\nThanks"
- id: 2177
  author: Lani Starr Hawaii
  author_email: Zaragoza80@gmail.com
  date: '2012-04-14 02:09:19 -0700'
  date_gmt: '2012-04-14 09:09:19 -0700'
  content: Hey there I just wanted to take a moment to say I really like reading your
    website.
- id: 2206
  author: Nathan Upchurch
  author_email: nupchurc@asu.edu
  date: '2012-05-25 13:44:15 -0700'
  date_gmt: '2012-05-25 20:44:15 -0700'
  content: Excellent tutorial! Wish I would have read it sooner!
- id: 2372
  author: Dagstjerna
  author_email: dagstjerna@hotmail.com
  date: '2012-08-24 14:11:23 -0700'
  date_gmt: '2012-08-24 21:11:23 -0700'
  content: "here is a implementation in javascript,\r\nits quite ugly, but it works,\r\nI
    will rewright it som day. \r\nSo thanks for the tutorial it was realy good,\r\nnow
    i have to figure out how to get webgl to use this cind of data. \r\n\r\n\r\n\r\n\r\nfunction
    CreateCustomMersh(GridRow,GridCol,GridSize)\r\n    {        \r\n        result
    = {};\r\n        var vertexPositions=[];\r\n        var vertexNormals=[];\r\n
    \       var vertexTextureCoords=[];\r\n        var indices=[];\r\n        var
    c=0;\r\n\r\n        for (var i = 0; i <= GridRow; i++)\r\n        {\r\n        \r\n
    \           for (var j = 0; j <= GridCol; j++)\r\n            {\r\n                vertexPositions.push((GridSize*i),
    0, (GridSize*j));         \r\n                vertexNormals.push(0, 1, 0);  \r\n
    \               vertexTextureCoords.push(0.0, 1.0); \r\n            };\r\n        };\r\n\r\n
    \       for (var i = 0; i < GridRow; i++)\r\n        {\r\n            if(i % 2
    === 0)\r\n            {\r\n                for (var j = 0; j <= (GridCol+0.5)*2;
    j++)\r\n                {\r\n                    indices.push(c);\r\n                    if(j
    == (GridCol+0.5)*2 || j==0 &amp;&amp; indices.length<1)\r\n                    {\r\n
    \                       if(i==GridRow-1){break;}\r\n                        indices.push(c);\r\n
    \                       j++\r\n                    }\r\n            \r\n                    if(j
    % 2 === 0)\r\n                    {\r\n                        c=c+4;\r\n                    }\r\n
    \                   else\r\n                    {\r\n                        c=(c-3);\r\n
    \                   } \r\n                }\r\n            }\r\n            else\r\n
    \           {\r\n                for (var j = (GridCol+0.5)*2; 0 <= j; j--)\r\n
    \               {    \r\n                    indices.push(c);\r\n                    if(j==1)\r\n
    \                   {\r\n                        break;\r\n                    }\r\n\r\n
    \                   if(j % 2 === 0)\r\n                    {\r\n                        c=c+4;\r\n
    \                   }\r\n                    else\r\n                    {\r\n
    \                       c=(c-5);\r\n                    } \r\n                };\r\n
    \           };\r\n        };\r\n};"
- id: 2373
  author: Dagstjerna
  author_email: dagstjerna@hotmail.com
  date: '2012-08-24 14:34:55 -0700'
  date_gmt: '2012-08-24 21:34:55 -0700'
  content: "In your drawscene function you need to remember, changing \"TRIANGLES\"
    to \"TRIANGLE_STRIP\"\r\n\r\nlike this:\r\ngl.drawElements(gl.TRIANGLE_STRIP,
    inputOBJVertexIndexBuffer.numItems, gl.UNSIGNED_SHORT, 0);"
- id: 2564
  author: Joan
  author_email: noemail@noemail.com
  date: '2013-02-04 09:05:16 -0800'
  date_gmt: '2013-02-04 16:05:16 -0800'
  content: "Great article, short and to the point. Just what I was looking for.\r\n\r\nIs
    there any drawback in avoiding reinserting the last vertices of each row in order
    to get the right normal directions? As far as I can see, it only creates degenerate
    triangles like 3 7 11 or 4 8 12."
- id: 2718
  author: Sam C
  author_email: meph3x6@hotmail.com
  date: '2013-03-15 09:18:37 -0700'
  date_gmt: '2013-03-15 16:18:37 -0700'
  content: Thanks so much for this! Your explanation, along with alot of my own sketches
    and head scratching, allowed me to create an algorithm that determined the correct
    indexes. joy factor.
- id: 2768
  author: Sorry No Video | Work Hard For a Year
  author_email: ''
  date: '2013-03-25 04:03:58 -0700'
  date_gmt: '2013-03-25 11:03:58 -0700'
  content: "[...] Triange Strips [...]"
- id: 2878
  author: iPhone 6 soon
  author_email: Wansitler422@hotmail.com
  date: '2013-04-19 02:23:45 -0700'
  date_gmt: '2013-04-19 09:23:45 -0700'
  content: I've been exploring for a bit for any high-quality articles or blog posts
    on this kind of space . Exploring in Yahoo I eventually stumbled upon this website.
    Studying this info So i'm satisfied to exhibit that I have a very just right uncanny
    feeling I came upon exactly what I needed. I such a lot surely will make certain
    to don?t put out of your mind this website and give it a glance regularly.
- id: 2911
  author: ไอโฟน 5
  author_email: Petticrew711@hotmail.com
  date: '2013-04-25 02:00:32 -0700'
  date_gmt: '2013-04-25 09:00:32 -0700'
  content: Hi, Neat post. There is an issue together with your site in web explorer,
    might test this? IE nonetheless is the marketplace chief and a large section of
    folks will leave out your wonderful writing due to this problem.
- id: 2916
  author: motorolla
  author_email: Hagaman158@hotmail.com
  date: '2013-04-26 02:38:41 -0700'
  date_gmt: '2013-04-26 09:38:41 -0700'
  content: I just could not go away your site prior to suggesting that I really loved
    the standard info an individual supply for your visitors? Is gonna be back steadily
    in order to check up on new posts
- id: 2977
  author: Robert Sirois
  author_email: watchlala@hotmail.com
  date: '2013-05-28 17:17:39 -0700'
  date_gmt: '2013-05-29 00:17:39 -0700'
  content: "Thanks for posting this! It was totally useful for me. Here's an implementation
    of your approach in CoffeeScript for anyone interested.\r\n\r\nhttp:&#47;&#47;universesgames.com&#47;blog&#47;51a547f7bf0907e35359db78"
- id: 3063
  author: openGL drawElements - one extra triangle, using index array? - OpenGL Solutions
    - Developers Q &amp; A
  author_email: ''
  date: '2013-10-23 21:09:04 -0700'
  date_gmt: '2013-10-24 04:09:04 -0700'
  content: "[...] triangle-strip-for-grids-a-construction        This entry was posted
    in OpenGL on October 23, 2013 by admin. [...]"
- id: 3099
  author: Fun with 3D Time-of-Flight Cameras | Larrylisky&#039;s Wiki
  author_email: ''
  date: '2013-12-07 10:53:45 -0800'
  date_gmt: '2013-12-07 17:53:45 -0800'
  content: "[...] Now that we know how to draw triangles using OF, how do we choose
    which group of three vertices should form a triangle? Luckily, creating triangles
    is relatively straightforward for structured point clouds, but significantly more
    complex for unstructured ones. &nbsp;Depth maps gathered from the 3D cameras are
    typical of structured point clouds; that is, the pixels have predefined spatial
    arrangement, i.e., row and column, and its coordinates are defined by , where
    \ are the row and column index, respectively; and  is the Euclidean distance from
    the origin (camera center) to the vertex. &nbsp; For example, a 320 x 240 3D camera
    will have  spanning from 0 to 319, and  spanning from 0 to 239. &nbsp;Note that
    \ is not the same as ; and that  is not the same as . &nbsp;A depth map must be
    converted to a vertices map before it can be rendered in OpenGL. &nbsp;The Intel
    Perceptual Computing SDK provides the PXCUPipeline_ProjectImageToRealWorld()&nbsp;API
    to convert depth map to vertices map. With the vertices map, one can traverse
    the map to form triangular strips. [...]"
- id: 3114
  author: Depth Map Visualiser | Jatin Parekh
  author_email: ''
  date: '2014-03-08 23:14:11 -0800'
  date_gmt: '2014-03-09 06:14:11 -0700'
  content: "[...] googling for a while, I reached here&nbsp;which clearly explains
    how GL_TRIANGLE_STRIP works. So I used that logic to write a small code [...]"
- id: 3153
  author: Carl Bateman
  author_email: CarlBateman@hotmail.com
  date: '2014-07-22 01:58:29 -0700'
  date_gmt: '2014-07-22 08:58:29 -0700'
  content: Looks nice, but the winding order of triangles alternates with each row.
    :(
- id: 3386
  author: walrus1998headshothippo
  author_email: Magalong@gmail.com
  date: '2016-01-14 05:38:08 -0800'
  date_gmt: '2016-01-14 12:38:08 -0800'
  content: Thanks for sharing :)
---
I'm working with WebGL and as such, I'm discovering some quirks about OpenGL ES 2.0.  I have been using display lists as long as I've been using OpenGL, but WebGL doesn't have support for them.  So, I'm buckled down and familiarized myself with vertex buffer objects, the (perhaps better) alternative.

At any rate, I need to render a regular 2D grid, and as it doesn't support quads, either, I was forced to use triangles.  In the interest of getting things running, I just provided a wasteful list of discrete triangles.  This is wasteful because it references many more vertices than necessary - I ended up declaring $$6n^2$$ vertices when in reality there are only $$n^2 + n + 1$$ unique vertices.  This worked fine, until I wanted to increase the resolution.  It turns out, JavaScript doesn't like large arrays.

That's fair, because the implementation was pretty wasteful.  A triangle strip was the best choice anyway.  ___A triangle strip is a highly compact form of representing a mesh.  For $$n$$ triangles, it requires only $$n + 2$$ vertices defined.___  Well, that's roughly true.  We'll see another case in a minute.  It's useful when many triangles share vertices, and perhaps I'll let [Wikipedia's explanation](http://en.wikipedia.org/wiki/Triangle_strip) stand.

It wasn't immediately obvious how to define a grid out of a single triangle strip and so I got out a pen and paper.  I kept in mind a neat trick: ___if in a triangle strip, you need to skip the use of a vertex, a vertex can be introduced twice in a row.___  That is, if I need triangles (6, 3, 7) and (7, 11, 6) in that order, you can just make your strip with 6, 3, 7, 7, 11, 6.  You can think of it as if there are two triangles created (3, 7, 7) and (7, 7, 11), but they have no area and a degenerate case - a line.  Furthermore, these lines lie on triangles already defined.

Perhaps the obvious choice doesn't yield any results, and in fact in this layout, it can't be easily done (you have to have vertices appear three times in a row):

![This is a bad idea for a topology if you want to use a single triangle strip.]({{ site.github.url }}/assets/2009/12/mesh_bad.png)

To better convince yourself, try to come up with a good way to put this in a triangle strip.  I'll make the case that it is pretty difficult with a claim from graph theory.  In order for a triangle mesh to be turned into a triangle strip, each consecutive triangle must share an edge.  We can then think of the mesh as a connectivity graph (the [dual](http://en.wikipedia.org/wiki/Dual_graph) of the mesh) and then the problem will emerge more clearly:

![The dual graph of the bad idea.]({{ site.github.url }}/assets/2009/12/mesh_bad_dual.png)

To make the triangle strip "nice," we ought to be able to visit each node once and exactly once.  There's good and bad news in this - it's the same problem as finding a [Hamlitonian path](http://en.wikipedia.org/wiki/Hamiltonian_path) which is NP complete.  The good news is that if we find a solution to our small problem, we've found a solution to all such grids (with arbitrarily many triangles).  Note that we don't need an Eulerian path.

If you stare long enough at the above connectivity graph, you'll hopefully convince yourself that there's no way to traverse it visiting each node once and exactly once.  Go ahead and try - it's pretty infuriating.

Looking at how we would traverse one strip (triangles a, b, c, d, e and f) actually gives us a clue.  A triangular strip for that case would be 0, 4, 1, 5, 2, 6, 3, 7, and happiness ensues and we should move onto the next row.  Unfortunately, in the context of this new row, we're starting in a different place (topologically) than we started with the first strip.  Vertex 0 has two connected neighbors in its row - 1 and 4.  Vertex 7 has three in its row: 6, 10 and 11.  It turns out we can change up the topology to remedy this simply:

![A much better topology for drawing this with a single triangle strip.]({{ site.github.url }}/assets/2009/12/mesh_good.png)

We can also see that this is a much better solution by looking at this new graph's dual:

![The dual of the better topological choice.]({{ site.github.url }}/assets/2009/12/mesh_good_dual.png)

You can probably easily find a Hamlitonian path in this case.  But this still leaves us with how to determine the vertex orderings.  We decided that the first row ought to be 0, 4, 1, 5, 2, 6, 3, 7, but moving on from there we need a bit of "glue" to move onto the next row.  We insert 7 again, and then continue on from there: 7, 11, 6, 10, 5, 9, 4, 8.  A bit more glue for the third row: 8, 12, 9, 13, 10, 14, 11, and 15:

![An alternative representation of the vertex ordering]({{ site.github.url }}/assets/2009/12/strip.png)

Looking at the indices from the first row, starting at 0, we can get the next index by alternately adding 4 and then subtracting 3.  On the next row, we'll continue to add 4, but then alternately subtract 5.  The 4 is derived as being the number of vertices on a side (if there are $$n$$ divisions, then there are $$n+1$$ vertices), and the 3 and 5 are explained by the fact that we need to change columns in the mesh, by one step at a time.

An clean implementation is not trivial, but not extremely difficult.  In terms of results, I can fit more than 4 times as many vertices into the mesh than with a per-triangle implementation.  And to boot, it has cut the work of the vertex shader a great deal.
