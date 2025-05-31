# [tianma-static] Stored xss on filename

## Report Details
- **Report ID**: 403692
- **URL**: https://hackerone.com/reports/403692
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-01T02:29:04.350Z
- **Disclosed**: 2018-11-02T10:45:04.803Z

## Reporter
- **Username**: abdilahrf_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
I would like to report stored xss in tianma-static
It allows anyone to execute arbitary javascript for doing anything.

# Module

**module name:** tianma-static
**version:** 1.0.4
**npm page:** `https://www.npmjs.com/package/tianma-static`

## Module Description

Provide a static file service.

# Vulnerability

## Vulnerability Description

it was possible to embed malicious js code in filename there was no sanitization performed. 

## Steps To Reproduce:

1. create filename `<img src=x onerror=alert(1)>`
2. start tianma-static
3. xss fired

F340845


# Wrap up

- I contacted the maintainer to let them know: N
- I opened an issue in the related repository: N

## Impact

It allows anyone to execute arbitary javascript for doing anything.

## Attachments
- tianma-static.PNG
