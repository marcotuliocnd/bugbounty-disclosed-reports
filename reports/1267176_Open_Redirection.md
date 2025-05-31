# Open Redirection

## Report Details
- **Report ID**: 1267176
- **URL**: https://hackerone.com/reports/1267176
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-17T23:33:10.366Z
- **Disclosed**: 2023-02-05T13:00:27.505Z

## Reporter
- **Username**: 0xjackal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: jetblue

## Vulnerability Information
## Summary:
Hi jetblue Security Team.

The following URL is vulnerable to an open redirect (it will redirect to google.com):
- https://█████_https@google.com

Work at Google Chrome & Other Browser 
Except Firefox will ask you first if you want to redirect to that page , See:-

█████████
  
##What is Open Redirect:-
Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. This behavior can be leveraged to facilitate phishing attacks against users of the application. The ability to use an authentic application URL

Supporting Material/References:
-https://blog.detectify.com/2019/05/16/the-real-impact-of-an-open-redirect/
-https://medium.com/@0xrishabh/open-redirect-to-account-takeover-e939006a9f24

## Steps To Reproduce:
1. Go to  https://████_https@google.com
2. Redirect to google.com

## Impact

Open Redirection

## Attachments
No attachments
