# Spring security configuration allows agent sessions to be hijacked

## Report Details
- **Report ID**: 241244
- **URL**: https://hackerone.com/reports/241244
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-19T00:48:58.888Z
- **Disclosed**: 2018-07-31T19:35:11.411Z

## Reporter
- **Username**: 4cad
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gocd

## Vulnerability Information
Summary
=======
If agents have successfully logged in, then unauthenticated requests to /go/agent-websocket or /go/remoting/* will randomly succeed sometimes.

Description
========

The deprecated X509ProcessingFilter apparently does not work without a HttpSessionContextIntegrationFilter earlier on the chain. After a successful authentication it sets a thread-local security context that never gets cleared - meaning that future requests on /go/remoting or /go/agent-websocket will successfully authenticate if they randomly happen to be processed by one of the threads which has a valid security context.

Steps to Reproduce
=======
1) Start up a server.
2) Run the following command a bunch of times. It should always return a 403 Forbidden

 "curl http://localhost:8153/go/remoting/api/admin/config.xml | grep -B 2 Error"

3) Start up an agent, and wait about two minutes
4) Repeat the command from step 2. It should occasionally return a 500 Server Error. This happens when the request was successfully authenticated, and then fails in the GoCD code that is handling the request.

If the server has any artifacts, the URL from step (2) can be changed to a path to that URL. In this case it will sometimes return 403 Forbidden, and sometimes return the artifact itself. 

Risk
========

This allows an attacker without any credentials to read all artifacts or even upload artifacts (combined with #240198 they could use this to execute a stored XSS). While preparing this ticket, I was able to successfully upload a stored XSS file without any credentials by submitting a bunch of POST requests to http://localhost:8153/go/remoting/files/up42/1/up42_stage/1/up42_job/attack_unauthenticated.html

This is also really easy to discover - I stumbled across it when I noticed some requests were randomly being denied as unauthorized. It turns out all of my requests should have been unauthorized!

Recommended Fix
========
Add httpSessionContextIntegrationFilter immediately before x509ProcessingFilter in the acegi-security.xml file, for the /remoting/ and /agent-websocket/ entries.

This fixes it because the httpSessionContextIntegrationFilter clears the thread-local security context after each request, thus fixing the problem. 


## Attachments
No attachments
