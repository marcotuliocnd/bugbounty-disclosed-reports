# Betting more than max amount

## Report Details
- **Report ID**: 147237
- **URL**: https://hackerone.com/reports/147237
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-25T16:13:08.071Z
- **Disclosed**: 2016-07-26T10:24:22.835Z

## Reporter
- **Username**: karel_origin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: fantasytote

## Vulnerability Information
Hey Fantasytote,

This is not really a security issue since this won't leak any data of other users (or something like that) but i still wanted to tell you this because there must be a reason you guys limit the max bet to 150 euro (per bet).

You can reproduce this issue by betting 150 euro, intercepting the data and modifying it to 1000 euro.
I uploaded this video to youtube (unlisted so only you can watch it.)
Please watch my PoC video:
https://youtu.be/ny6dLtu-xV0

__**How can I fix this?**__
You can fix it by not only validating the bet amount client side but also validating it server side.

Could you please reopen my previous report since you can send the token to external websites. (Non Fantasytote websites.)

Ask me if you need anything,
Karel.

## Attachments
No attachments
