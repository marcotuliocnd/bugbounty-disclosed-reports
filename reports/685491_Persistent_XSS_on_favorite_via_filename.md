# Persistent XSS on favorite via filename

## Report Details
- **Report ID**: 685491
- **URL**: https://hackerone.com/reports/685491
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-08-31T11:38:01.777Z
- **Disclosed**: 2019-12-12T09:42:51.382Z

## Reporter
- **Username**: foobar7
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
CVSS
----

Medium 6.4 [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N)

Description
-----------

The name of a file is echoed without encoding when favoring the file, leading to persistent XSS. 

POC
---

To place the payload:

- Create a file called `test'"><img src=x onerror=alert(document.location)>.pdf` and upload it. 

To trigger the payload:

- click on ... next to the file followed by "add to favorites". The payload will trigger here.

## Impact

With a successful attack, an attacker can access all data the attacked user has access to, as well as perform arbitrary requests in the name of the attacked user.

## Attachments
No attachments
