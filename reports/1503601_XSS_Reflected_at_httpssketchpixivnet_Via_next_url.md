# XSS Reflected at https://sketch.pixiv.net/ Via `next_url`

## Report Details
- **Report ID**: 1503601
- **URL**: https://hackerone.com/reports/1503601
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-03-08T04:12:52.288Z
- **Disclosed**: 2022-03-23T01:19:37.774Z

## Reporter
- **Username**: find_me_here
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: pixiv

## Vulnerability Information
Hi,

I Found XSS Reflected at https://sketch.pixiv.net/ Via Success URL

##Follow Me :)

##Steps :
1. Open the URL below:
https://sketch.pixiv.net/resign_request/success?next_url=javascript%3Aalert%2F**%2F(document.domain)

2. Pop ups appear :)

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can: Perform any action within the application that the user can perform

## Attachments
- XSS_pixiv.jpg
