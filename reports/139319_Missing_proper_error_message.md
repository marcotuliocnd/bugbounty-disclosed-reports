# Missing proper error message.

## Report Details
- **Report ID**: 139319
- **URL**: https://hackerone.com/reports/139319
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-17T13:35:33.035Z
- **Disclosed**: 2016-07-21T10:25:07.366Z

## Reporter
- **Username**: exploitraja
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ok

## Vulnerability Information
Steps to reproduce:
1.Load the URL: http://ok.ru/ in any browser.
2.Now goto Browser settings and disable the Cookies.
3.Try to login using valid credentials .
4.Observed that user is redirected to login page again without any proper error message .

Technical Impact: This leads user to feel discomfort as user is not aware of the issue which is stopping him from login into his account ,which leads to loss of reputation.


Suggested Remediation:Error message like “ For smooth functioning of this site make 
sure that cookies are enabled on your browser.” should be displayed to make aware the user about the vulnerability.




## Attachments
No attachments
