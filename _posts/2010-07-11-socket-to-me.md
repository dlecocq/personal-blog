---
layout: post
status: publish
published: true
title: Socket to Me
author:
  display_name: dan.lecocq
  login: dan.lecocq
  email: dan.lecocq@kaust.edu.sa
wordpress_id: 866
date: '2010-07-11 15:23:23 -0700'
date_gmt: '2010-07-11 22:23:23 -0700'
categories:
- computer science
tags:
- sockets
- netcat
- websockets
comments: []
---
I'm not a "network guy."  I still don't know what exactly the subnet mask means, and I am often thankful that OS X is so willing to automatically configure network settings for me well.

That said, recently I've been finding myself doing a lot of programming with sockets.  They provide a low-level network interface to communicate between computers, and are used like other file descriptors.  On the C side of things there's a little more work than I'd like, and as such, I've found Python an invaluable tool.

In fact, I think any time you're working with a new concept, technique or algorithm it's extremely helpful to use a scripting language.  Like others, Python offers an interactive session where you can develop code fragments by trial and error with each step, rather than trying to debug a chunk of code you've written with only a vague notion of what's going on behind the scenes.  It allows you to pause between steps and see the effects and results of each function.

Interestingly enough, another tool has come in extremely handy - `netcat`.  It's designed to print to stdout everything that it hears on the socket, and then it sends everything it receives on stdin through the socket.  It allows you to examine some of the specifics of a protocol without worrying about the details of your own code or whether or not your code works. Netcat is tried and true, and will tell you exactly what's happening.

This all came up in the context of WebSockets.  They're a part of the HTML5 spec and provide a JavaScript interface for real socket communication (there are of course some caveats, especially with respect to how to handle binary data).  We've been using them for a project where we'd like the client to not need a special program to interact with a piece of software, and so instead implemented the protocol in JavaScript.

There was, however, some trouble at the offset.  I had a bit of difficulty finding out why exactly the WebSocket client would seem to start to make a connection but then immediately complain about handshakes.  What would have been much easier is to just open up netcat on the same port and have a conversation with the WebSocket itself.

```bash
# First off, I was running SimpleHTTPServer from a directory with a dummy html file
$> python -m SimpleHTTPServer 8888

# On the terminal, listen on port 35000
$> netcat -l 35000
```

And then try to make a connection from the JavaScript side

```javascript
# From a JavaScript terminal from that dummy html file, in Chrome or Safari for example
ws = new WebSocket("ws://localhost:35000");
ws.onopen = function() { window.console.log("Hello!"); };
ws.onmessage = function(event) { window.console.log("Received " + event.data); };
ws.onclose = function() { window.console.log("Goodbye!"); };
```

I had figured (incorrectly) that WebSockets would work in essentially the exact same way that sockets would.  This is what we'd then expect to receive:

```http
GET / HTTP/1.1
Upgrade: WebSocket
Connection: Upgrade
Host: localhost:35000
Origin: http://localhost:8888
```

It was only after realizing that this is what the WebSocket was sending that it became clear that the reason that no connection was actually happening was because the browser wasn't getting the rest of [the handshake](http://www.whatwg.org/specs/web-socket-protocol/):

```http
HTTP/1.1 101 Web Socket Protocol Handshake\r
Upgrade: WebSocket\r
Connection: Upgrade\r
WebSocket-Origin: http://localhost:8888\r
WebSocket-Location: ws://localhost:35000/\r
WebSocket-Protocol: sample\r\n\r\n
```

Oddly enough, I can't seem to get netcat to play nice sending the response code, but it can easily-enough give us an indication of what was happening at first.  Python can handle the rest for us:

```
$> python
>>> import socket
>>> s = socket.socket()
>>> s.bind(('', 35000))
>>> s.listen(1)
>>> client, info = s.accept()
>>> client.recv(1024)
'GET / HTTP/1.1\r\nUpgrade: WebSocket\r\nConnection: Upgrade\r\nHost: localhost:35000\r\nOrigin: http://localhost:8888\r\n\r\n'
>>> client.send('HTTP/1.1 101 Web Socket Protocol Handshake\r\nUpgrade: WebSocket\r\nConnection: Upgrade\r\nWebSocket-Origin: http://localhost:8888\r\nWebSocket-Location: ws://localhost:35000/\r\nWebSocket-Protocol: sample\r\n\r\n')
199
```

And notice that it's not until the listening socket sends its response portion of the handshake that the JavaScript console will print the "hello" we told it to upon opening the connection.  Now that we have the two talking, let's actually send and receive a couple of messages:

```javascript
# Again from the JavaScript console
ws.send("Hello from JavaScript!")
```

And then we receive the message in Python:

```
>>> client.recv(1024)
'\x00Hello from JavaScript!\xff'
```

And here we find another oddity of WebSockets.  All messages seem to be prepended with \x00 and appended with \xff (though this is also mentioned in the specification).  If we try to send a message from Python without these two extra characters, we'll get nothing out on the JavaScript side (go ahead and give it a try!):

```
# We get nothing on the JavaScript side :-/
client.send('hello')

# Magic happens!
client.send('\x00hello\xff');
```

Of course I'm sure there are other robust tools the real "networking guys" use to make their lives easier.  But outside of pulling up WireShark or trying to figure this out by writing C code, netcat and Python definitely saved the day.
