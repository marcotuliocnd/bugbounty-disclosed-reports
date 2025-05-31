# Opportunity to post hidden comments

## Report Details
- **Report ID**: 434202
- **URL**: https://hackerone.com/reports/434202
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-11-05T06:45:41.903Z
- **Disclosed**: 2018-12-11T23:33:19.337Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Twitter allows to comment on anyone's tweet. While testing this feature, observed that one can post comment on tweet which will be invisible to the victim whom the reply was posted and would be visible to any other twitter user.
This can allow an Attacker to abuse victim on a tweet. The catch here is victim cannot even know that attacker posted on his tweet but any other twitter user can see that tweet.

**Steps to reproduce**

1. Attacker login to Twitter
2. Attacker blocks victim using Block@victim button at https://twitter.com/<victim>
3. Attacker opens any popular tweet of victim
4. Attacker abuses victim in the tweet reply
5. Victim cannot see the tweet reply posted by Attacker but any other user can see that reply.

**Recommendation**
If a person blocks a twitter user then he/she should not be allowed to post on any of the blocked user tweets.

## Impact

This can allow an Attacker to abuse victim on a tweet. The catch here is victim cannot even know that attacker posted on his tweet but any other twitter user can see that tweet.

## Attachments
- 2.PNG
- 1.PNG
- 3.PNG
- 4.PNG
- 5.PNG
