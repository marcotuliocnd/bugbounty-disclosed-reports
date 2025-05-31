# Outsider can affect Upvote Percentage of private subreddit post by calling /api/vote API

## Report Details
- **Report ID**: 1298902
- **URL**: https://hackerone.com/reports/1298902
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-11T03:43:44.447Z
- **Disclosed**: 2021-10-27T14:05:25.410Z

## Reporter
- **Username**: trieulieuf9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Attacker that does not have access to a private subreddit, can still affect `Upvote Percentage` of any posts in this private subreddit. He does that by calling `/api/vote` API and passing post id directly.

What is `Upvote Percentage`?: F1407175


## Impact:
- Attacker can affect `Upvote Percentage` of private subreddit posts, although he does not have access to this private subreddit posts.
- Only `Upvote Percentage` is changed, vote number is not affected.
- Limitation: Attacker needs to know post id in private subreddit to start the attack.


## Steps To Reproduce:

  1. Victim prepare a private subreddit and create a post in it [1]
  2. Attacker intercepts a legitimate `/api/vote` request in Burp and send to Repeater
  3. In Repeater, request body, change param `id` value to Victim's post id (assume that attacker has a way to get post id)  F1407184
  4. Change param `dir` value to -1 and send request. `Upvote Percentage` decreases from 100% => 99%
  5. Then change param `dir` value to 1 and send request. `Upvote Percentage` decreases from 99% => 67%


[1]: If you just created a new post, please wait for half a day, until vote number is visible F1407178. It is fine to start the exploit right away, but the result does not update correctly until vote number is visible.

## Impact

- Attacker can affect `Upvote Percentage` of private subreddit posts, although he does not have access to this private subreddit posts.
- Only `Upvote Percentage` is changed, vote number is not affected.
- Limitation: Attacker needs to know post id in private subreddit to start the attack.

## Attachments
- upvote_percentage.png
- new_post.png
- post_id.png
