# Clickjacking Periscope.tv on Chrome

## Report Details
- **Report ID**: 198622
- **URL**: https://hackerone.com/reports/198622
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-15T21:40:43.230Z
- **Disclosed**: 2017-02-06T22:08:58.786Z

## Reporter
- **Username**: mishre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,

The X-FRAME-OPTIONS header returned from https://www.periscope.tv is:
```
X-Frame-Options: ALLOW-FROM https://twitter.com/
```
But Chrome doesn't support this value for the header: https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet.
Because of that, no value for X-FRAME-OPTIONS is set and all of the periscope.tv pages are vulnerable to Clickjacking. You can see for example my attached poc (Make sure you test it on chrome) that I am framing my own user on periscope. I can use regular Clickjacking tricks to make the user follow other users and do practically any action on the site.

## Attachments
- Clickjacking_Periscope.html
