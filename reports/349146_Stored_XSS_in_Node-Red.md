# Stored XSS in Node-Red

## Report Details
- **Report ID**: 349146
- **URL**: https://hackerone.com/reports/349146
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-05-08T19:20:45.876Z
- **Disclosed**: 2018-07-18T09:20:01.788Z

## Reporter
- **Username**: misterch0c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a stored XSS in node-red
It allows to execute javascript in the user's browser

# Module

**module name:** node-red
**version:** v0.18.4
**npm page:** `https://www.npmjs.com/package/node-red`

## Module Description

> A visual tool for wiring the Internet of Things.

## Module Stats

1,758 downloads in the last day
10,601 downloads in the last week
40,000+ downloads in the last month

# Vulnerability
## Steps To Reproduce:

* Install the module

`sudo npm install -g --unsafe-perm node-red`

* Run it
`node-red`
then access it in http://localhost:1880

* Exploit
The same payload can be applied in different locations.
Payload: `<script>alert('xss')</script>`
Places where you can put the payload:
Drag & drop any item from the left menu to the center then put the payload in the `name` field. After clicking "done", the xss is triggered. At this point it's only triggered in your browser.
Click the "deploy" button, now any user that will browse to  http://localhost:1880 will have the javascript executed.
Second one:
Click the "+" button on the top right to create a new "flaw". Put the payload in the name field. Again you need to press "deploy". After that double clicking on the "flaw" will execute the javascript.

## Supporting Material/References:

- Archlinux
- NodeJS 9.4.0
- NPM 5.6.0
- Firefox 57.0.4 & Chromium 64.0.3282.119
- node-red v0.18.4

# Wrap up

- I contacted the maintainer to let them know: N 
- I opened an issue in the related repository: N

¯\_(ツ)_/¯

## Impact

It allows executing malicious javascript code in the user's browser

The hacker selected the **Cross-site Scripting (XSS) - Stored** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
http://localhost:1880

**Verified**
Yes



## Attachments
- Screenshot_from_2018-05-08_20-31-46.png
