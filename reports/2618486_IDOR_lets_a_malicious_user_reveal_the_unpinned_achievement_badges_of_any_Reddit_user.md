# IDOR lets a malicious user reveal the unpinned achievement badges of any Reddit user

## Report Details
- **Report ID**: 2618486
- **URL**: https://hackerone.com/reports/2618486
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-07-23T07:31:19.872Z
- **Disclosed**: 2024-08-09T15:56:45.832Z

## Reporter
- **Username**: saurabhb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Reddit launched a new feature in June 2024 changelog. It is about **Achievement Badges** being available in profile . As per its the access control a badge is supposed to be hidden to other users if the badge owner unpins it. However, this IDOR vulnerability lets a malicious user find all the hidden badges with the knowledge of username (which is public) and badge id (which is a simple 1-2 digit incremental number)

## Impact:
Badges tell a lot about a Reddit user. That is the reason Reddit gave an option for user to hide them. This vulnerability is a threat to confidentiality of Reddit users. It can tell a malicious user about if the user joined more than a threshold number of communities, does this person have high (> 10%) upvote rating, does the person comment in same community in 20 days straight, does the person votes/post/comments in reddit for certain amount of days etc. Basically all the actions due to which an badge gets rewarded gets exposed.

## Steps To Reproduce:
1. Create a Reddit account.
2. Go to any post of any user.
3. Share it outside of Reddit by just creating a embedding of the post. Please use Share -> Embed feature.

{F3460176}

4. Now go to your profile's achievement section and observe that the `New Share` badge gets unlocked.
5. Click on that badge and unpin it. This makes it hidden from others.

{F3460179}

6. Please read this [support article](https://support.reddithelp.com/hc/en-us/articles/27063106698004-What-are-achievements) which states that unpinning a badge will hide it from others.

{F3460182}

7. Now create another account. Please try to create using mobile number due to some reasons.
8. Login to the newly created account.
9. Go to the first users achievement page. The way to do it is craft this URL and visit it in browser `https://www.reddit.com/user/<the-username-here>/achievements/`.
10. Observe that the `New Share` badge is hidden.

{F3460189}

11. Now request the following url in same browser `https://share.redd.it/preview/user/<the-usename-here>/achievement/10?show-user-info=true` and observe that you get a response with an image meaning that the provided username has `New Share` badge.

{F3460193}

12. Now change the `10` in URL to `11` or `9` and observe that you get a `Not found` message.

{F3460201}
{F3460200}

13. Thus, a `Not Found` response means that that particular user does not have that badge and a `Valid Image` response means that that user has that particular badge.
13. Using this technique we can enumerate the `Achievement Badges` of any arbitrary user of Reddit.


## Additional Information:
1. Confidentiality is set to HIGH because entire badge component and every badge is affected.
2. Privileges required is set to NONE because anyone can register to Reddit as it is a public platform so it is equivalent to no authentication.

## Impact

Badges tell a lot about a Reddit user. That is the reason Reddit gave an option for user to hide them. This vulnerability is a threat to confidentiality of Reddit users. It can tell a malicious user about if the user joined more than a threshold number of communities, does this person have high (> 10%) upvote rating, does the person comment in same community in 20 days straight, does the person votes/post/comments in reddit for certain amount of days etc. Basically all the actions due to which an badge gets rewarded gets exposed.

## Attachments
- 2024-07-23_124553.png
- 2024-07-23_124904.png
- 2024-07-23_125018.png
- 2024-07-23_125412.png
- 2024-07-23_125557.png
- 2024-07-23_125708.png
- 2024-07-23_125723.png
