# View Failed Approval and Pending videos other users

## Report Details
- **Report ID**: 411679
- **URL**: https://hackerone.com/reports/411679
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-20T08:30:43.257Z
- **Disclosed**: 2018-10-21T05:50:04.326Z

## Reporter
- **Username**: tismayil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
See videos uploaded by a user. The video is available when it waits for confirmation or is not accepted.

## Steps To Reproduce:

1 - Go victim page : https://chaturbate.com/p/akaxanxa/?tab=bio
2 - Open video : https://chaturbate.com/photo_videos/photo/big/[user_name]/[content_id]/

3 - Get random requests - https://chaturbate.com/photo_videos/photo/big/[user_name]/[ last content id + 1 ]/

4 - Done - If the id holds the content opens up as a result.

## Impact

By collecting user information, they can access their pending content.
I can share content on my site or blog as original content from my own name by playing the contents.

## Attachments
- Screenshot_from_2018-09-20_11-23-56.png
- Screenshot_from_2018-09-20_11-23-23.png
