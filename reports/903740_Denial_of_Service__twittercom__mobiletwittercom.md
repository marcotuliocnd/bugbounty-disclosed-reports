# Denial of Service | twitter.com & mobile.twitter.com

## Report Details
- **Report ID**: 903740
- **URL**: https://hackerone.com/reports/903740
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-20T11:31:57.245Z
- **Disclosed**: 2020-09-02T19:18:29.905Z

## Reporter
- **Username**: asdasdasdasdasda
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi Team,

Detail:
I found a DoS that works on **twitter.com** and **mobile.twitter.com**, but it doesn't work on the mobile app. The user only needs to view the message or tweet in order to be exposed to this DoS. As far as I can remember, a report similar to this report has been sent to you before, but I think it's no longer public.

Note:
- If the user tries to view the DoS message or tweet from twitter.com, DoS will definitely work, but if it enters from Chrome and displays this DoS from **mobil.twitter.com**, this DoS will not work. This works without exception in Edge and Firefox.

- I think this is a browser-based DoS, so I think it won't work on Desktop Twitter. So I didn't test it.

- I did my tests on my own accounts. I haven't done a test for any tag. But I'm sure it will work.


PoC & Steps:
`http://twitter.com:627732462`



{F875527}

## Impact

An attacker could apply this DoS to any Twitter account or popular tag. It prevents a large audience or target user from accessing Twitter from the browser.

## Attachments
- Twitter-Dos.mp4
