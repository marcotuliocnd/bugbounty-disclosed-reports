# Open redirect by the parameter redirectUri in the URL

## Report Details
- **Report ID**: 1250758
- **URL**: https://hackerone.com/reports/1250758
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-07-03T18:36:16.502Z
- **Disclosed**: 2022-04-21T22:10:00.486Z

## Reporter
- **Username**: marciosz_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: blackrock

## Vulnerability Information
The following URL is vulnerable to an open redirect (it will redirect to google.com)
https://www.blackrock.com/authplatform/user/activate-success?redirectUri=https://google.com
After clicking on "return to site" it will be redirected to the page


Steps To Reproduce:


Enter on this link https://www.blackrock.com/authplatform/user/activate-success?redirectUri=https://google.com
Redirected to https://google.com

## Impact

Phishing attacks to redirect users to malicious sites without realizing it

## Attachments
No attachments
