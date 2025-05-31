# Stored XSS in profile page

## Report Details
- **Report ID**: 1084183
- **URL**: https://hackerone.com/reports/1084183
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-22T08:41:02.223Z
- **Disclosed**: 2021-11-14T10:59:38.325Z

## Reporter
- **Username**: darkdream
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Summary
There is a stored XSS vulnerability in the users profile page.

Steps:

1-Go to https://forum.acronis.com , create an user and login
2-Go to profile and edit it
3- enter javascript code in Signature field for exampe  use this code in Signature : <xss onmouseover="alert(1)">test</xss>
4-send this profile to other users ,or send this profile link via email to victims.

## Impact

if someone views attacker profile the script will execute

## Attachments
No attachments
