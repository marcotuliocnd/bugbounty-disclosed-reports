# Ability to perform actions (Tweet, Retweet, DM) and other actions, unauthenticated, on any account with SMS enabled.

## Report Details
- **Report ID**: 470749
- **URL**: https://hackerone.com/reports/470749
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-12-21T20:48:10.158Z
- **Disclosed**: 2019-09-26T22:58:00.514Z

## Reporter
- **Username**: antisocial_eng
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:** By knowing the mobile phone number associated with a Twitter account, or by using random mobile phone numbers! It is possible to perform the following actions against a target without their knowledge or interaction. With no account takeover scenario.

It's a case of, if I know the mobile number... I can control basic functions of the account.

I can do everything that is listed here: https://help.twitter.com/en/using-twitter/sms-commands on an account, completely unauthenticated.


## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Spoof target number, send an SMS to a special short code for the geographical location, as seen here: https://help.twitter.com/en/using-twitter/supported-mobile-carriers


## Impact: Massive. I can remove the SMS two factor of the account. I can DM people without them knowing. If I had the mobile number of Donald Trump, I could send Tweets as him... There is so much wrong here. 

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)

https://twitter.com/___Sh4rk___/status/1076204152546619392 this is a tweet I sent from my close friends account. She did not reveal her password or authenticate it at all.

## Impact

Remove 2FA

Tweet on someones behalf.

DM Someone.

Delete someones tweets

Turn off all phone SMS notifications

Follow people

Unfollow people.

Block/Report people - with a little script I could get 10000 phone numbers all reporting innocent tweets. Controlling media etc

More stuff really.

## Attachments
- Screenshot_2018-12-21_20.08.40.png
- Screenshot_2018-12-21_20.46.34.png
- Screenshot_2018-12-21_20.47.08.png
