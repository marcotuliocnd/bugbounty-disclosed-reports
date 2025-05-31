# X-XSS-Protection -> Misconfiguration

## Report Details
- **Report ID**: 289846
- **URL**: https://hackerone.com/reports/289846
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-11-13T13:44:40.009Z
- **Disclosed**: 2017-12-15T21:25:10.544Z

## Reporter
- **Username**: bb343cc5cbd74210c09dafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi there,

**URL:** https://www.sfl-tap.army.mil/
I have seen that the website is using the X-XSS-Protection Header.

But it has a strange configuration.
When I take a look at securityheaders, I've seen that you guys use this as configuration.

**X-XSS-Protection:** DENY

DENY is used for the X-Frame Option instead of the X-XSS-Protection. The good configuration should be:

**XSS-XSS-Protection:** 1; mode=block

And not DENY. This is used for the X-Frame Option.

## Attachments
No attachments
