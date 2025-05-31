#  Stored XSS(Cross Site Scripting) In Slack App Name

## Report Details
- **Report ID**: 159460
- **URL**: https://hackerone.com/reports/159460
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-15T10:48:36.405Z
- **Disclosed**: 2016-11-22T22:04:56.590Z

## Reporter
- **Username**: imnarendrabhati
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
Hello Slack,

This vulnerability is about a Stored Cross Site Scripting

Slack Stored XSS In App(App Name)

Vulnerable URL(Edit App Page)
https://api.slack.com/apps/[appid]/general

https://api.slack.com/apps/A21B3V9GA/general

Vulnerable Parameter = name

Note -Its also work on other user as well.

Send this link to victim

===================

Reproduction Steps
POC Video - https://youtu.be/3jAbPjfPW1o
Screen shot is also attached.

1) Go to app edit page
https://api.slack.com/apps/[appid]/general
https://api.slack.com/apps/A21B3V9GA/general
2) In app name parameter enter the following payload
"/><script>alert(/Bhati/)</script>
3) Now open the app page in any other tab
https://bhativictim.slack.com/apps/A21B3V9GA--scriptalert-bhati-script
4) You will get a Alert Box
5) We can also send this same link to other user(victim).

Thanks,
Narendra

## Attachments
- xss1.png
- xss2.png
