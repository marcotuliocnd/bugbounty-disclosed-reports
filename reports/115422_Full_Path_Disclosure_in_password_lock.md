# Full Path Disclosure in password lock

## Report Details
- **Report ID**: 115422
- **URL**: https://hackerone.com/reports/115422
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-02-08T19:09:50.672Z
- **Disclosed**: 2017-10-16T05:51:57.429Z

## Reporter
- **Username**: supernatural
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Hi,

Password input must be string but not checked in PasswordLock lib,
It will throw an exception on `hash` function call

    Warning: hash() expects parameter 2 to be string

So you must validate it in `hashAndEncrypt` and `decryptAndVerify`

Regards

## Attachments
No attachments
