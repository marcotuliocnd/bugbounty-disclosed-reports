# Delete anyone's content spotlight remotely.

## Report Details
- **Report ID**: 1819832
- **URL**: https://hackerone.com/reports/1819832
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-01-01T16:06:51.643Z
- **Disclosed**: 2023-03-06T21:32:15.042Z

## Reporter
- **Username**: prickn9
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hello Snapchat,
 Snapchat has viral video feature callled spotlight which alone was the biggest trend and increase snapchat users and profit in millions.
I found a way to delete anyone's spotlight remotely.

Please see the below poc:-

1. First go to https://my.snapchat.com/myposts and log in there.
2. You will see your posts .
3. Now turn burp suite and intercept.
4.Select any of your posts and click delete option.
5. Now capture the delete request. In delete request there is parameter of id


{"operationName":"DeleteStorySnaps","variables":{"ids":["███████"],"storyType":"SPOTLIGHT_STORY"},"query":"mutation DeleteStorySnaps($ids: [String!]!, $storyType: StoryType!) {\n  deleteStorySnaps(ids: $ids, storyType: $storyType)\n}\n"}

6. You just have to change this id parameter. You can easily get the id parameter. Now forward the request after replacing id with someone's else video id.

And the video of other user will get delete.

HOW TO GET ID PARAMETER

1. Whenever you share spotlight you can see the parameter in the url as:
https://story.snapchat.com/spotlight/█████


I have attached a video POC please check it out

## Impact

Delete anyone's Content Spotlight. Imagine deleting video biggest influencers and content creators.

## Attachments
No attachments
