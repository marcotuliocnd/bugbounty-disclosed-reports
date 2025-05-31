# CSRF in github integration

## Report Details
- **Report ID**: 174328
- **URL**: https://hackerone.com/reports/174328
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-06T11:34:47.622Z
- **Disclosed**: 2016-11-18T04:24:01.420Z

## Reporter
- **Username**: asanso
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
There is a CSRF in the github integration in the case of "Only pre-approved apps can be installed by team members: (slack1.png)
Github is not one of those pre approved application. So a normal user cannot install it (slack2)
Now lets assume the channel administrator is adding this integration to one common channel e.g. #random (slack3.png).
Now the other non admin users receive a notification "added an integration to this channel: github" (slack4.png) but if they try to click the link they will have a page saying "added an integration to this channel: github" (slack5.png). The problem is that they still have the uri of the integration, that is something like https://vecchiowerther.slack.com/services/CODE E.g. https://vecchiowerther.slack.com/services/B2L476P3P

This can be used to make the admin of the channel to  "switch to unauthed mode".
For the attacker is enough to forge a an html page as

<html>
<img src="https://vecchiowerther.slack.com/services/88143227125?no_auth_mode=1">
</html>

e.g. in http://asanso.github.io/csrf.html (or in any website). 
If the admin will visit this website he will loose the github integration and switch to the unauthed mode (slack6.png)

## Attachments
- slack2.png
- slack1.png
- slack4.png
- slack3.png
- slack5.png
- slack6.png
