# GraphQL introspection query works through unauthenticated WebSocket

## Report Details
- **Report ID**: 862835
- **URL**: https://hackerone.com/reports/862835
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-29T21:02:01.389Z
- **Disclosed**: 2021-01-09T08:49:03.025Z

## Reporter
- **Username**: zerodivisi0n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nuri

## Vulnerability Information
## Summary:
It is possible to execute GraphQL introspection query through unauthenticated WebSocket connection. PoC included.

## Steps To Reproduce:
To simplify reproducing I provided a simple html PoC file.

  1. Start python static http server in directory with poc file: `python3 -m http.server` (this step is required to bypass CORS restrictions for opening local file in the browser)
  1. Open file in the browser: http://localhost:8000/ws.html
  1. GraphQL schema dump will be displayed on the page

The problem occurs because of the websocket request with type `start`(maybe others too, I didn't check) allows to pass introspection query in it (`{type: "start", payload: {query: "query IntrospectionQuery{ ... }"}}`)

## Supporting Material/References:

  * [GraphQL — Common vulnerabilities & how to exploit them](https://medium.com/@the.bilal.rizwan/graphql-common-vulnerabilities-how-to-exploit-them-464f9fdce696)

## Impact

This information reveals the full GraphQL API with all methods and data types. This can be used to perform more complex attacks.

## Attachments
No attachments
