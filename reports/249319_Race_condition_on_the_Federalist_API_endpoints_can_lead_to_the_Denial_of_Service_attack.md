# Race condition on the Federalist API endpoints can lead to the Denial of Service attack

## Report Details
- **Report ID**: 249319
- **URL**: https://hackerone.com/reports/249319
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-13T14:36:09.244Z
- **Disclosed**: 2017-09-05T19:50:53.553Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hello. I discovered that the Federalist API doesn't have rate limiting in place, and executes any amount of request to the endpoint in parallel mode.

##The impact
Since you are using the cloud, and i can't test the production environment, impact is theoretical in this case - it can be a problem, or it not.
On my localhost instance executing of 1000 parallel GET requests to the http://localhost:1337/v0/me endpoint on behalf of authenticated user was lead to the complete instance inaccessibility. It is a light enough request, and executing of 1000 PUT requests (for example, saving site settings) will have greater impact.
{F202845}
Each request cause execution of the PostgreSQL command, which can lead to the high resource usage.
{F202846}

##Reproduction steps
1) Login to the Federalist instance (unauthenticated requests is possible too, but it have too low impact)
2) Look to the request to the `/v0/me` endpoint. Using Burp Intruder or Charles, repeat the request 1000 times in parallel mode. The server will accept and try to execute all of them in the same time. You can notice increased server resource consumption.
3) You can repeat the test with more heavily site settings saving request.

##Suggested fix
You can consider to implement rate-limiting on the API endpoints (for example, executing not more than 5 API requests in same time from the single user), or implement queue (accept requests from single user in сonsistent mode instead parallel), or use module like https://www.npmjs.com/package/express-rate-limit. 

If your production environment somehow mitigates this issue (e.g. has load balancers in place, etc), let me know - i'll close the ticket.


## Attachments
- n.PNG
- l.PNG
