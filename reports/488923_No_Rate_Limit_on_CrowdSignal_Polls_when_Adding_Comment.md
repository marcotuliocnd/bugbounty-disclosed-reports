# No Rate Limit on CrowdSignal Polls when Adding Comment

## Report Details
- **Report ID**: 488923
- **URL**: https://hackerone.com/reports/488923
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-31T00:22:11.258Z
- **Disclosed**: 2019-04-13T21:40:58.729Z

## Reporter
- **Username**: bugra
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi team!

I hope this isn't duplicate :/ 

I created a poll on CrowdSignal.com (https://poll.fm/10226924)
When adding a comment, there is no rate limit. You can see my comments on my poll. 

1. Go to any poll.
2. Turn on Intercept and Add a Comment.
3. Send request to Intruder.
4. Set your payloads and start attack.

There is no rate-limit.

## Impact

No rate-limit on comments.

## Attachments
No attachments
