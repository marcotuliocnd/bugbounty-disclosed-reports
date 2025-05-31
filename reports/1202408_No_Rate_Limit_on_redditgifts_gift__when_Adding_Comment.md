# No Rate Limit on redditgifts gift  when Adding Comment

## Report Details
- **Report ID**: 1202408
- **URL**: https://hackerone.com/reports/1202408
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-19T06:09:45.761Z
- **Disclosed**: 2021-10-21T19:52:19.094Z

## Reporter
- **Username**: gaurav-bhatia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
Hi team,
I hope this report should not be closed as INFORMATIVE

#**Summary:**
The add comment endpoint was improperly rate-limited so the potential attacker could post a large number of comments, overloading the server .

#**Description:**
The add comment endpoint has a speed limit, but the number is set too high, so speed limiting is activated when you write more than 1000 comments per minute.

#**Environment:**
Scope: Web Application
Attack type: OWASP API TOP10 Lack of Resources & Rate Limiting
Maximum user privileges needed to reproduce your issue: no privileges

#**Steps To Reproduce:**
1.Go to any post.
2.Turn on Intercept and Add a Comment.
3.Send request to Intruder.
4.Set your payloads and start attack.
5.There is no rate-limit.

#**Note:**
If there is any problem in reproduction from your side then i will provide you with video poc.

#**POC:**
You can observe the time taken to load the post before performing the attack and after performing the attack. It will show  that the post takes alot time to load after the attack. 

#**Fix:**
Developers alleviated the problem by setting the speed limit to low for endpoints that set the speed too high. 

Regards,
Gaurav Bhatia

## Impact

No rate limit on comments can lead to slow down of server due to large number of comments in the post.

## Attachments
No attachments
