# XSS in gist integration

## Report Details
- **Report ID**: 11073
- **URL**: https://hackerone.com/reports/11073
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2014-05-06T18:21:27.236Z
- **Disclosed**: 2019-04-28T00:11:34.790Z

## Reporter
- **Username**: zemnmez
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
1. Create a gist called:
"><svg onload=alert(1)>
2. have gist integration enabled and put a link in a slack chat
3. Visit the 'raw' or 'new window' pages for this gist, for example: https://outpost.slack.com/files/zemnmez/F029MDY33/___svg_onload_alert_1__



## Attachments
No attachments
