# xss in https://www.uber.com

## Report Details
- **Report ID**: 145278
- **URL**: https://hackerone.com/reports/145278
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T01:13:29.847Z
- **Disclosed**: 2016-07-25T17:43:50.528Z

## Reporter
- **Username**: netfuzzer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hey,

this vulnerability is essentially the same as bug 145276, i'm reporting it again just in case.

there's a cross site scripting vulnerability in https://www.uber.com/.

steps to reproduce:

1.visit https://www.uber.com/?kxsrc=https%3A//beacon.krxd.net/optout_check%3Fcallback%3Dalert%28/XSSED/.source%29
2. wait until the page finishes loading
3.see the xss alert.

wonder it would be eligible for a bounty?

Cheers,
Mario

## Attachments
No attachments
