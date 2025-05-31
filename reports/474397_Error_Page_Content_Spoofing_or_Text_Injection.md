# Error Page Content Spoofing or Text Injection

## Report Details
- **Report ID**: 474397
- **URL**: https://hackerone.com/reports/474397
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-03T17:42:15.933Z
- **Disclosed**: 2019-01-07T07:30:26.567Z

## Reporter
- **Username**: badcracker
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cfptime

## Vulnerability Information
**Description:** 
hello sir,
i found that one you once you write any thing after / in www.cfptime.org/  is reflected in the error page
example go to www.cfptime.org/texthere you will see test here in the 404 error page
## Steps To Reproduce:

1.go  https://www.cfptime.org/!!!ATENTION!%20This%20server%20is%20on%20Maintenance%20please%20go%20to%20WWW.EVIL.COM%20since%20it%20was

2.see that The requested URL /!!!ATENTION! This server is on Maintenance please go to WWW.EVIL.COM since it was not found on this server. is found in the page
i added attached picture as poc

## Supporting Material/References:

i attached picture as poc

## Impact

attacker could use this as phishing process to attack users

## Attachments
- cfp.PNG
