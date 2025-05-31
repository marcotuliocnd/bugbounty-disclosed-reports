# [takeapeek] XSS via HTML tag injection in directory lisiting page

## Report Details
- **Report ID**: 490728
- **URL**: https://hackerone.com/reports/490728
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-03T17:29:57.570Z
- **Disclosed**: 2019-07-01T08:52:17.316Z

## Reporter
- **Username**: skyn3t
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I was taking a peek at `takeapeek` module and found it is vulnerable to XSS via malicious injection in directory listing.
It allows execution of arbitrary JS code.

# Module

**module name:** takeapeek
**version:** 0.2.2
**npm page:** `https://www.npmjs.com/package/takeapeek`

## Module Description

A simple static webserver with only one command. Heavily inspired by glance, this is really more of a learning experience then anything.

## Module Stats

**weekly downloads**
4

# Vulnerability

## Vulnerability Description

`takeapeek` module provides a directory listing feature in it's HTTP server but it doesn't sanitize the filename hence a malicious payload in the filename cane be used to invoke an XSS. For example a file can be strategically named as `javascript:alert(1)` and we can see the XSS executing in the browser on clicking that link.

## Steps To Reproduce:

- Install `takeapeek`
```
$ npm install -g takeapeek
```

- Create a file with name `javascript:alert(1)`
```
 $ touch 'javascript:alert(1)'
```

- Start server in current directory
```
$ takeapeek
takepeek listening at http://localhost:3141
```

- Visit the address in any browser and click on malicous file link that we created.
{F417367}

## Supporting Material/References:

- Ubuntu 16.04
- node v11.3.0
- npm 6.7.0
- Chrome 72

# Wrap up


- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

An attacker is able to execute malicious JavaScript in context of other user's browser.

## Attachments
- Screenshot_from_2019-02-03_22-56-26.png
