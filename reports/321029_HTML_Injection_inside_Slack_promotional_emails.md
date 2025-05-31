# HTML Injection inside Slack promotional emails

## Report Details
- **Report ID**: 321029
- **URL**: https://hackerone.com/reports/321029
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-03-01T12:00:30.324Z
- **Disclosed**: 2018-07-30T13:50:03.067Z

## Reporter
- **Username**: 0x0luke
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hi,

There's a HTML injection vulnerability present inside emails sent from slack when the FIRST name on the account contains HTML. The html is stored in the backend database and when emails are sent (promotional, etc), the HTML is sent along with the rest of the email.

In my PoC, which is provided below, i inserted a <img> tag to prove this vulnerability exists. 

F268173

## Impact

This vulnerability can lead to the reformatting/editing of emails from an official slack email address, which can be used in targeted phishing attacks. 

This could lead to users being tricked into giving logins away to malicious attackers.

## Attachments
- Slack_HTML_Injection.png
