# Default behavior of Fastifys versioned routes can be used for cache poisoning when Fastify is used in combination with a http cache / CDN

## Report Details
- **Report ID**: 1025575
- **URL**: https://hackerone.com/reports/1025575
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-03T20:22:03.726Z
- **Disclosed**: 2020-12-10T16:56:12.040Z

## Reporter
- **Username**: trygve_lie
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report possible cache poisoning in Fastify
It allows an attacker to perform an cache poisoning when Fastify is used in combination with a http cache / CDN.

# Module

**module name:** Fastify
**version:** 3.x
**npm page:** `https://www.npmjs.com/package/fastify`

## Module Description

> Fast and low overhead web framework, for Node.js

## Module Stats

159,983 weekly downloads

# Vulnerability

## Vulnerability Description

I might be missing the obvious or I've not read the documentation closely enough, but to me it seem like its not possible to turn off versioned routes in Fastify.

The reason why I am reporting this issue as a security issue are because my reason to want to turn off versioned routes in Fastify is rooted in a security issue when using Fastify in relation with a http cache / CDN and I do not want to expose this in the common issue tracker because it can be used against running services. 

My current issue is that we have a Fastify server not using versioned routes where the server live behind a http cache / CDN. By default Fastify will return a 404 if a `Accept-Version` http header is passed on to an exiting route not under versioning. When there is a http cache / CDN infront of Fastify this will make it possible for an attacker to perform an cache poisoning attack (https://owasp.org/www-community/attacks/Cache_Poisoning).

## Steps To Reproduce:

Given the following Fastify server:

```js
const app = require('fastify')();

app.get('/', async () => {
    return { hello: 'world' };
});

const start = async () => {
    await app.listen(9000)
}
start();
```

Requesting this as follow:

```sh
curl -v http://localhost:9000
```

it outputs a HTTP 200 with the expected content:

```sh
*   Trying 127.0.0.1:9000...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 9000 (#0)
> GET / HTTP/1.1
> Host: localhost:9000
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< content-type: application/json; charset=utf-8
< content-length: 17
< Date: Tue, 03 Nov 2020 19:21:41 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5
< 
* Connection #0 to host localhost left intact
{"hello":"world"}
```

Though, if we request the same route with an `Accept-Version` header:

```sh
curl -v -H "Accept-version: tada" http://localhost:9000
```

it outputs a HTTP 404:

```sh
*   Trying 127.0.0.1:9000...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 9000 (#0)
> GET / HTTP/1.1
> Host: localhost:9000
> User-Agent: curl/7.68.0
> Accept: */*
> Accept-version: tada
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< content-type: application/json; charset=utf-8
< content-length: 72
< Date: Tue, 03 Nov 2020 19:25:09 GMT
< Connection: keep-alive
< Keep-Alive: timeout=5
< 
* Connection #0 to host localhost left intact
{"message":"Route GET:/ not found","error":"Not Found","statusCode":404}
```

When a http cache / CDN are in front of such a server, an attacker can use this behavior to trigger caching of a 404 page on a legal route. Ex; A default Fastly (the CDN we use) or Varnish config will result in a cached 404 page with the above setup.

When versioned routes are in use I also think that a `Vary` http header with `Accept-Version` as a value should be added to the response. That shall prevent a http cache / CDN from caching a 404 under the same cache key as a previous response.

Though; to avoid this behavior when not using version routes I think it should be possible to turn off version routes. Is there an easy way to do so? Type a boolean on the constructor? Or do one need to write a custom version parser which according to doc affect performance?

Its highly debatable if this is a security issue in Fastify, though, behavior of this might be worth having a second look at. Personally I was a bit surprised that versioned routes was a default behavior. I would expect it to be an opt in instead of opt out (if its possible to opt out). 

## Supporting Material/References:

- All OSes
- All node.js versions
- All NPM versions
- [BROWSERS VERSIONS, IF APPLICABLE] 
- Any http cache / CDN

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

An attacker can use this cache poisoning to perform an attack where fully functionally URLs are replaced with 404's.

## Attachments
No attachments
