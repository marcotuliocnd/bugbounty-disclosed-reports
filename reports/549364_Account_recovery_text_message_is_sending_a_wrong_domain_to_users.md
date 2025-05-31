# Account recovery text message is sending a wrong domain to users.

## Report Details
- **Report ID**: 549364
- **URL**: https://hackerone.com/reports/549364
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-04-27T15:50:20.341Z
- **Disclosed**: 2019-05-31T06:14:21.904Z

## Reporter
- **Username**: zeesek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hey,

I hope you're fine. :)

**Summary:**
When users setup Account recovery at Authentication section Hackerone sends them text message to their updated phone number with a wrong domain link.

**Description:**
When users adds phone number at Account recovery, they get a text message on their phone number, which shows "Your Hackerone account recovery phone number has been updated. If this is unexpected, please contact **supportahackerone.com**. Which is not your domain and can be bought or can be own by anyone. If a user contact to this domain and attacker have own this domain already, he can easy manipulate him/her to do something wrong with their accounts. He don't have to find another way to into the official Hackerone text messages to give his own website as Hackerone already doing it. He just have to own this domain and start manipulating users. And it also sounds very much similar "supportahackerone.com" to support.hackerone.com . Which can help him also.
 
**Steps To Reproduce:**
1. Go to Authentication section. And setup account recovery.
2. Add phone number and you'll receive a text message.

Fix:
Use support.hackerone.com instead of supportahackerone.com.

## Impact

Attacker can easily manipulate a user to do a wrong thing to his account.

Thank you,
Hope you'll fix this soon. And will response to my report nicely. :)
If you have any questions please feel free to ask me. :)

**And also my report is not really about support.hackerone.com subdomain, i know that is out of scope. But this message was sent through hackerone.com.**

**Screenshots:**

## Attachments
- Screenshot_20190427-195339.jpg
- supportahackerone.JPG
- supportahackerone2.JPG
