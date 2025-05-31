# HTTP PUT method enabled

## Report Details
- **Report ID**: 460642
- **URL**: https://hackerone.com/reports/460642
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-12-11T19:13:25.095Z
- **Disclosed**: 2018-12-11T19:20:27.350Z

## Reporter
- **Username**: hach3ro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
Hi security team,

Summary: It is possible to upload files to the server using the PUT method

Steps To Reproduce:
I used the following request:
PUT /emitrani.txt HTTP/1.1
Host: ratelimited.me
Content-Length: 10
Connection: close

Now a file exists at https://ratelimited.me/emitrani.txt
with contents of the put request.

## Impact

impact

## Attachments
- Fixed.png
- oo.PNG
