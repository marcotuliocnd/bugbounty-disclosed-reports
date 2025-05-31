# [flsaba] Stored XSS in the file and directory name when directories listing

## Report Details
- **Report ID**: 856588
- **URL**: https://hackerone.com/reports/856588
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-22T19:01:09.868Z
- **Disclosed**: 2020-09-14T10:52:17.556Z

## Reporter
- **Username**: d3lla
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report a Stored XSS in module "flsaba".
It allows to inject malicious scripts in the file and directory name, store them on the server, then execute these scripts in the browser via the XSS vulnerability.

# Module

**module name:** https://www.npmjs.com/package/flsaba
**version:** 1.1.0
**npm page:** `https://www.npmjs.com/package/flsaba`

## Module Description

simple http server with directory listing

## Module Stats

[5] weekly downloads

# Vulnerability

## Vulnerability Description

This XSS vulnerability occurs due to the module represents file and directory name(s) in HTML when creating the listing directory page. The file and directory name(s) are used in the `href` attribute of an anchor element (as well as the value of the anchor itself) without any sanitization. 
In this way, any malicious script written in the file/directory name and stored on the server, would be executed in the client's browser.


## Steps To Reproduce:

- install the `flsaba` module: 
    - `npm install -g flsaba`
- in the directory which will be served via `flsaba` (in my case the directory is `~/PoC`), create:
    - a file with name `"><img src=x onerror=javascript:alert("xss")>"`: 
        - `touch '"><img src=x onerror=javascript:alert("xss")>"'`
    - a directory with name `"><img src=x onerror=javascript:alert("xss2")>"` : 
        - `mkdir '"><img src=x onerror=javascript:alert("xss2")>"'`
{F799667}
- in the same directory (in my case is `~/PoC`), start `flsaba`: 

```shell
~/PoC » flsaba                                                                     
flsaba v1.1.0 server listening on port 3000
Directory: /home/ubuntu/PoC
```

{F799666}
- visit [http://localhost:3000/](http://localhost:3000/)
- the alerts will popup
{F799668}
{F799669}

## Patch

The vulnerability arises in the following lines of code:
- [https://github.com/petoem/flsaba/blob/master/server.js#L58](https://github.com/petoem/flsaba/blob/master/server.js#L58)
- [https://github.com/petoem/flsaba/blob/master/server.js#L64](https://github.com/petoem/flsaba/blob/master/server.js#L64)


## Supporting Material/References:

- OPERATING SYSTEM VERSION: Ubuntu 18.04.4 LTS
- NODEJS VERSION: v13.13.0
- NPM VERSION: 6.14.4
- BROWSERS VERSIONS: Firefox Browser 75.0 (64-bit)


# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

Thanks for your time.

Best regards,

d3lla

## Impact

Stored XSS.
Any malicious script written in the file/directory name and stored on the server, would be executed in the client's browser, so this vulnerability allows executing malicious JavaScript code in the client's browser.

## Attachments
- flsaba.png
- files.png
- PoC1.png
- PoC2.png
