# Slowvote and Countdown can cause Denial of Service due to recursive inclusion

## Report Details
- **Report ID**: 1563142
- **URL**: https://hackerone.com/reports/1563142
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-05-09T00:33:09.871Z
- **Disclosed**: 2022-05-09T18:37:16.485Z

## Reporter
- **Username**: dyls
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
Similar to #85011, if you edit a Slowvote or Countdown object and include its own object ID in the description, then it will recursively include and prevent the page from loading.

mongoose

## Impact

Denial of Service. You can include the Slowvote or Countdown object on any other object to also prevent it from loading. If it is included in the feed, you could also prevent the home page from loading.

## Attachments
No attachments
