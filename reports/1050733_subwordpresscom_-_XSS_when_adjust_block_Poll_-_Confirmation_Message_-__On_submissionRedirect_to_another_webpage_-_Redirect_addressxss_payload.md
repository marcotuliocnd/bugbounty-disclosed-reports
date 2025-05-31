# [sub.wordpress.com] - XSS when adjust block Poll - Confirmation Message -  On submission:Redirect to another webpage - Redirect address:[xss_payload]

## Report Details
- **Report ID**: 1050733
- **URL**: https://hackerone.com/reports/1050733
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-04T17:35:44.036Z
- **Disclosed**: 2021-02-11T12:43:34.372Z

## Reporter
- **Username**: superman85
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
Dear Wordpress Team,

Today when I tried to create a post with block "Poll" and I have found at Poll Block -> Confirmation Message -> On submission:Redirect to another webpage and  Redirect address:[xss_payload]

At Redirect address line, I can save the ```javascript:alert(document.cookie)``` as an URL webpage after submit a poll. And when an authenticated wordpress user submitted a poll, their cookies may stolen by attacker

## Platform(s) Affected:
https://subdomain.wordpress.com

## Steps To Reproduce:


  1- Logged in your wordpress website and create a post with block Poll, fill question and some choices

{F1104221}
  2- Adjust Poll Block, Confirmation Message -> On submission:Redirect to another webpage and  Redirect address:javascript:alert(document.cookie) then click Update/Publish your post

{F1104220}
  3-  Go to your created poll and Submit, you will see xss popup

{F1104222}

You can see video PoC below for the steps:
{F1104231}

## Impact

Steal cookies

## Attachments
- p2.png
- p1.png
- p3.png
- recording-1607103274750.webm
