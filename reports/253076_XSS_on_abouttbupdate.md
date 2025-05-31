# XSS on about:tbupdate

## Report Details
- **Report ID**: 253076
- **URL**: https://hackerone.com/reports/253076
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-24T17:06:31.710Z
- **Disclosed**: 2023-11-28T09:02:55.223Z

## Reporter
- **Username**: qab
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Hello,
It appears that there is an XSS vulnerability on the about:tbupdate page.

Steps to reproduce:
1. Visit: about:tbupdate?javascript:alert(1)
2. Click on 'visit our website'

Because the page is a privileged one (given it cannot be opened from a normal web page) this XSS may lead to a more severe issue. I will post a reply if I find a way to to do either of two things, first being finding a way to open privileged about: pages from normal content and secondly, I will check to see if there are any privileged javascript functions I could execute to achieve a bigger issue.

Thank you

## Attachments
No attachments
