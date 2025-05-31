# open redirected by host header

## Report Details
- **Report ID**: 2828499
- **URL**: https://hackerone.com/reports/2828499
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2024-11-07T13:53:19.102Z
- **Disclosed**: 2024-12-02T13:46:09.450Z

## Reporter
- **Username**: black_world
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: localizejs

## Vulnerability Information
An Open Redirect vulnerability occurs when an application allows users to be redirected to an external, untrusted URL without validating the redirection target. By controlling the Host header and observing a redirection to the specified external site, you may have found an open redirect vulnerability.



STEP TO REPRODUCE:
go to  www.localizestaging.com and interpret then change host header .it will redirect to changed host header webisite

## Impact

This vulnerability can be exploited for phishing attacks, where users are misled into visiting a malicious site that appears to be trusted. It could also be used to bypass security filters or conduct other malicious activities.

## Attachments
- local1.png
- local2.png
- local3.png
