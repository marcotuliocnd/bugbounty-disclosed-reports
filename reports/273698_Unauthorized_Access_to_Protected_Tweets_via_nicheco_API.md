# Unauthorized Access to Protected Tweets via niche.co API

## Report Details
- **Report ID**: 273698
- **URL**: https://hackerone.com/reports/273698
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-02T05:59:23.608Z
- **Disclosed**: 2017-11-02T23:57:47.831Z

## Reporter
- **Username**: eidelweiss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hello,

**Summary:**
Normally If user __(victim)__ set to private / protect their tweets in setting Tweet privacy, other people/user will not able to see their recent or their pass status/twits when they visit his/her __(victim)__ profile. people only can see their __(victim)__ profile images and information about __how many tweet already post by that user__ , __how many followers and following by that account__ and __how many likes__ etc etc. but i found a way to view the protected tweets from other user who protect their tweets.


**Description:** 
in your policy i see there is new domain add as in scope target , and the domain is `niche.co` .
there is some condition needed to success reproduce this vulnerability:
1. the __victim__ need to connect their twitter account with `niche.co`
2. use the `niche.co` API to Access the Protected Tweets

## Steps To Reproduce:
_victim side_
 * victim account is `https://twitter.com/dummysystems`
  * lets say the victim already set to protect his/her tweets via `https://twitter.com/settings/safety`
{F225673}
  * now when other user try to visit victim profile it will look like this
{F225670}
  * now visit `https://www.niche.co/get-started` and chose twitter , allow and or Authorize Niche to use your account and complete the rest (including confirming your email address).

_attacker side_
  1. attacker no need to have twitter account and or no need to have `Niche` account here , this made the severity is high
  1. just visit `https://www.niche.co/api/v1/users/[victim_twitter_account]` ( in this case the victim is https://www.niche.co/api/v1/users/dummysystems , the attacker will show some important information disclosure regarding the victim account
   {F225668}
  1. scroll down the page till you see something like this `/users/52667/posts?accounts=162059`
  {F225669}
  1. and open it, so the full URI will become `https://www.niche.co/api/v1//users/52667/posts?accounts=162059`
  1. and BOOM! the attacker now have Access to Protected Tweets from victim account.
{F225671}
{F225672}

**noted**
to follow the rules, I use my own account as the __victim__, so there is no other / real account has been compromised.


Regards,

## Attachments
- twitter_nichi_api_user.jpg
- twitter_nichi_api_user_post.jpg
- twitter_private.jpg
- twitter_private_tweet_expose.jpg
- twitter_private_tweet_expose2.jpg
- twitter_setting_safety.jpg
