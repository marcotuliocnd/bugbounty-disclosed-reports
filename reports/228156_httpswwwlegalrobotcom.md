# https://www.legalrobot.com/

## Report Details
- **Report ID**: 228156
- **URL**: https://hackerone.com/reports/228156
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-13T15:09:11.857Z
- **Disclosed**: 2018-03-14T15:50:55.741Z

## Reporter
- **Username**: caesar302
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
Hello,
I found a info disclosure vulnerability. We can enumerate emails via user_id parameter from Manage users.

And I found that :

hello@legalrobot.com
mbay@codex.stanford.edu
contact@hackerunit.com
conduct@legalrobot.com
dmca@legalrobot.com 

I attached photos from burp repeater to be more explicit.

We can easily bruteforce user_id parameter with ids to harvest user's emails.

Regards,

## Attachments
- Capture0.1.4.PNG
- Capture0.1.5.PNG
- Capture0.1.6.PNG
- Capture0.1.PNG
- Capture0.11.PNG
- Capture0.12.PNG
