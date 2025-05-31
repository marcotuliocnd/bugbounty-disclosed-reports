# [tianma-static] Security issue with XSS.

## Report Details
- **Report ID**: 606526
- **URL**: https://hackerone.com/reports/606526
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-06-11T16:08:58.926Z
- **Disclosed**: 2020-10-12T20:44:40.207Z

## Reporter
- **Username**: wooeong22
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report XSS in tianma-static
It allows XSS and HTML Injection

First of all, It is my first report and I am sorry that I am not good at English T.T 
thank you.

# Module

**module name:** tianma-static
**version:** 1.0.4
**npm page:** `https://www.npmjs.com/package/tianma-static`

## Module Description

> Provide a static file service.

# Vulnerability

## Vulnerability Description

1) File content type
when I look a CVE-2018-16474([CVE-2018-16474](https://www.cvedetails.com/cve/CVE-2018-16474/), #403692), I think that's vulnerability need arbitrary file(name) upload.

If upload is possible, Attacker can upload `html` file. Also content type of the response header becomes `text/html` and it is possible to Stored XSS.

{F506823}

2) HTML Injection (It can lead to reflected XSS)
when a send `%2f` in path (example: http://127.0.0.1:8080/%2f), `resolve` function make a normal path on the filesystem. but `req.pathname` will print out a manipulated path.

so I can insert any html.

{F506824}

Reflected XSS using HTML only is not easy bypass the modern browser.
but if I can upload any file, Reflected XSS is possible Using load script.

{F506825}

## Steps To Reproduce:

1) File content type
> - upload html file with XSS script. 
> - xss fired

2) HTML Injection (reflected XSS)
> - upload any file with XSS script.
> - access `/%2f<script src='/[filename]'></script>`
> - xss fired

## Patch

1. add content type header in response. 
2. change `decodeURI` to `decodeURIComponent`. or denied malicious path.

# Wrap up
- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

If file upload is possible, XSS can occur.

## Attachments
- 1._html_File_Stored_XSS.png
- 2._HTML_injection.png
- 3._Reflected_XSS.png
