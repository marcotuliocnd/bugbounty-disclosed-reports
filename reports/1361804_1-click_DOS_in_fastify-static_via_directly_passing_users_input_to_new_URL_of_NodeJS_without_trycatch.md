# 1-click DOS in fastify-static via directly passing user's input to new URL() of NodeJS without try/catch

## Report Details
- **Report ID**: 1361804
- **URL**: https://hackerone.com/reports/1361804
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-06T15:23:51.154Z
- **Disclosed**: 2021-10-11T16:41:34.583Z

## Reporter
- **Username**: drstrnegth
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fastify

## Vulnerability Information
## Summary:
When fastify-static is mounted at root and registered the option `{ redirect: true }` (default of redirect option is `false`), the following line directly feed user's input which is `req.raw.url` to URL API without try/catch: https://github.com/fastify/fastify-static/blob/master/index.js#L439. A remote attacker can send a GET request to server with path = `//^/..`, this will cause the URL API to throw error and eventually crash the server.

## Steps To Reproduce:

  1. Download `fastify-dos.zip`
  2. bash run.sh
  3. Open your terminal and run: `curl --path-as-is "http://localhost:3000//^/.."`
 
After that the server will crash and return error `TypeError [ERR_INVALID_URL]: Invalid URL: //^/..`.

## Fix proposal

You can add a try/catch to prevent crash. However, if you only fix by adding try/catch, attacker can still cause open redirect. 

 1. Run the server in my `fastify-dos.zip` again
 2. Use Google Chrome and navigate to `http://localhost:3000//a//youtube.com/%2e%2e%2f%2e%2e` (I tested on Chrome, Firefox, Safari, Opera, Edge, worked on all of them)
 3. You will see that you get redirected to `https://www.youtube.com/..%2F..`

I like the idea of fixing open redirect  by having a base URL = `http://localhost.com/` as second parameter in https://github.com/fastify/fastify-static/blob/master/index.js#L439. However, I looked up on MDN spec about the URL API and I got surprised when I saw the last example at: https://developer.mozilla.org/en-US/docs/Web/API/URL/URL#examples, which is `new URL("//foo.com", "https://example.com")    // => 'https://foo.com' (see relative URLs)`, this is the main reason why the open redirect bug is still persist.

To fix this bug, I think we can check leading slash of `req.raw.url`, and allow at most 1 leading slash `/` before attempt to redirect.

## Impact

- Denial of service
- Open redirect

## Attachments
- fastify-dos.zip
