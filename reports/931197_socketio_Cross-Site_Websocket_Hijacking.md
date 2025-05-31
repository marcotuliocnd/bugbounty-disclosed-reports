# [socket.io] Cross-Site Websocket Hijacking 

## Report Details
- **Report ID**: 931197
- **URL**: https://hackerone.com/reports/931197
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-22T12:04:27.685Z
- **Disclosed**: 2021-01-31T12:33:38.717Z

## Reporter
- **Username**: sh1yo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report Cross-Site Websocket Hijacking in `socket.io`
It allows an attacker to bypass origin protection using special symbols include "`" and "$"

# Module

**module name:** `socket.io`
**version:** `2.3.0`
**npm page:** `https://www.npmjs.com/package/socket.io`

## Module Description

> Socket.IO enables real-time bidirectional event-based communication

## Module Stats

[1] weekly downloads: 3,457,682

# Vulnerability

## Vulnerability Description

I found this vulnerability while testing one of the private bugbounty programs. This vulnerability can be exploited as a typical csrf vulnerability. An attacker can send and receive WebSocket messages on behalf of a user.

## Steps To Reproduce:

- `npm install socket.io expressjs`
- Put the following code in to `index.js`

```
var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

io.origins(['http://localhost:80']); //we believe that this module will decline other origins

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

http.listen(80, () => {
  console.log('listening on *:80');
});
```
- Put the following code in to `index.html`
````
<script src="/socket.io/socket.io.js"></script>
        <script>
                var socket = io();
        </script>
```

- Run it `sudo node index.js`
- Open the burpsuite and navigate to http://localhost
- Open the proxy tab and send following request to repeater - `GET /socket.io/?EIO=3&transport=websocket&sid={{random id}}`
- Run it. We see `HTTP/1.1 101 Switching Protocols`

{F916713}

It means that the connection was successful.

- Try to change origin to `something.io`, we will see `HTTP/1.1 400 Bad Request` and it is good, because we allowed only localhost origin in our index.js

{F916722}

- Now try to change origin to
```localhost`something.io```

{F916727}

As we can see - the module thinks that origin is localhost while Safari thinks that it is a subdomain of something.io. Also, as I identified Safari isn't the only affected browser - this also works on modern firefox `Mozilla Firefox 79.0b8` as well. Try to change Origin to `http://localhost$something.io` The application still thinks that origin is localhost while firefox thinks that it is a domain `http://localhost$something.io` (During my small research I identified that firefox allows $ in domains names). 


## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- Os: Linux arch 5.7.9-arch1-1
- Node: v14.5.0
- NPM: 6.14.6
- Mozilla Firefox 79.0b8

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] N
- I opened an issue in the related repository: [Y/N] N

## Impact

After the successful connection from the attacker's domain, the attacker can receive and send websocket messages on behalf of a user.

## Attachments
- image.png
- image.png
- image.png
