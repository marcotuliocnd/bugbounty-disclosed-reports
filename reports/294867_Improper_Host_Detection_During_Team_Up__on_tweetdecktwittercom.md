# Improper Host Detection During Team Up  on tweetdeck.twitter.com

## Report Details
- **Report ID**: 294867
- **URL**: https://hackerone.com/reports/294867
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-12-04T05:05:34.028Z
- **Disclosed**: 2018-01-04T02:38:38.801Z

## Reporter
- **Username**: avinash_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi

Give this url ```https://twitter.com/teams/authorize?target_screen_name=&authorize_callback=https%3A%2F%2F%0Agoogle.com%5C@x.twitter.com``` to any authorised user for team up and after authorization of his 2nd account he will be redirected to ```google.com``` .

First I tried to make it malicious  with adding ```%0Agoogle.com%5C@x``` but it not redirected me but after adding %0Agoogle.com%5C@x```.twitter.com``` in it, this redirected me to google.com. Which shows in this endpoint url isn't properly validating the Host after login.


Vulnerable Url: ```https://twitter.com/teams/authorize?target_screen_name=&authorize_callback=https%3A%2F%2F%0Agoogle.com%5C@x.twitter.com```

Malicious point: ```%0Agoogle.com%5C@x.twitter.com```

PoC video attached

With Best Regards

## Impact

Impact: Attacker can use this for tricking users to Phising attacks.

## Attachments
- PoC_Monday_04_December_2017_10_07_38__IST.mp4
