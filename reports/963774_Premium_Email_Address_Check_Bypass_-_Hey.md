# Premium Email Address Check Bypass - Hey

## Report Details
- **Report ID**: 963774
- **URL**: https://hackerone.com/reports/963774
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-20T20:24:01.869Z
- **Disclosed**: 2020-12-15T15:21:37.941Z

## Reporter
- **Username**: ok_bye_now
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
Hello, I reported a bug to support@hey.com a couple weeks ago, not realizing that I was a member of the private bug bounty program. It was fixed quickly (Less than 1 hour) which was awesome to see. Being that this was reported through a seperate channel, and it is for Hey, I'm not even sure it would eligible here. Either way, it was a pretty neat bug becuase of its simplicity and clear impact (loss of revenue). 

Anyways, here it is:

There appears to be a bypass for the premium email address sign up. 

When signing up for Hey, I tried to obtain jp@hey.com, which prompted a Premium alert box that stated it would cost $999 per year. Since that wouldn't work for me, I tried 'jp  @hey.com' (two spaces), this worked without prompting me to accept that it was a premium email address. 

It appears that the spaces are registered as characters, so it's not considered a premium domain (at 4 chars), but the spaces are stripped at a later step and I am given a two character premium email address for the same cost as a non-premium email address.

Now, it appears I can lock this email address in for $99 per year just like a typical email address on the Hey platform.

## Impact

At the time, the impact was that an premium account (less than 4 chars) could be registered for the non-premium price of $99, which is substantially cheaper than the $999 price tag.

## Attachments
- image.png
