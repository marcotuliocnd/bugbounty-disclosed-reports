# A10 – Unvalidated Redirects and Forwards

## Report Details
- **Report ID**: 283269
- **URL**: https://hackerone.com/reports/283269
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-26T15:23:12.018Z
- **Disclosed**: 2017-11-09T13:08:19.382Z

## Reporter
- **Username**: romanshyadav
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
https://infogram.com/login

Web applications frequently redirect and forward users to other pages and websites, and use untrusted data to determine the destination pages. Without proper validation.
when i intercept the twitter request and change it to the google then it will redirect you to the google.
application should also verify the original request from the browser.

## Attachments
- 1.PNG
- 2.PNG
- 2-1.PNG
- 2-2.PNG
