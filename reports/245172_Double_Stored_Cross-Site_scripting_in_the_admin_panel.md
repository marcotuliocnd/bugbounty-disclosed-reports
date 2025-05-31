# Double Stored Cross-Site scripting in the admin panel

## Report Details
- **Report ID**: 245172
- **URL**: https://hackerone.com/reports/245172
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-01T20:03:24.854Z
- **Disclosed**: 2017-09-05T20:10:18.621Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hello. I discovered a Stored XSS attack vector in the `Custom Domain` field

##POC & Reproduction steps
1. Login to the federalist and go to the some instance `http://localhost:1337/sites/<siteid>/settings`
2. Fill the `Custom Domain` field by the
```
javascript:alert(document.domain)
```
and `Demo domain`
```
javascript:alert(document.domain);
```
(it cannot be the same so we bypass the check by adding `;`)

3. Save and press `View Website` button. You will be XSSed.
{F199337}
{F199336}
4) Go to the `http://localhost:1337/sites/<siteid>/published` - and press view on the demo site to test second Stored XSS
{F199338}

##The impact
The XSS requires user interaction (e.g. clicking the button). But still, it is a bad thing. Anyone who gain access here, can conduct stored XSS attack against other admins.

##The root cause & suggested fix
The input fields not sanitized properly - it should allow only alphanumeric characters, and dots.


## Attachments
- test3.PNG
- test2s.PNG
- test23.PNG
