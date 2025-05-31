# misconfigured CORS let to HPP and SOP bypass

## Report Details
- **Report ID**: 867436
- **URL**: https://hackerone.com/reports/867436
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-06T21:37:56.670Z
- **Disclosed**: 2020-05-07T21:57:21.720Z

## Reporter
- **Username**: dagamosst90
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: btfs

## Vulnerability Information
Hello team,
I found a bug on your website that let me bypass the SOP policy.
Hope you fix it, everything is in the video


https://www.youtube.com/watch?v=PYsU350S-s4

## Impact

The attacker my direct a victim to a phishing page of www.bitterrent.com/login and he/she will be convince to enter their email and password or even hijack csrf-token and sending him a password or email reset link.
I also found a link that expose the csrf-token on the URL and you should check this link in the black.svg host header URL

## Attachments
- bot.php
