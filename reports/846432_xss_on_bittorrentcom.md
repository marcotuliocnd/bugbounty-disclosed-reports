# xss on bittorrent.com

## Report Details
- **Report ID**: 846432
- **URL**: https://hackerone.com/reports/846432
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-10T13:08:07.499Z
- **Disclosed**: 2020-05-11T23:13:16.464Z

## Reporter
- **Username**: aslanemre
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: btfs

## Vulnerability Information
hi team 
i realized xss bug on  headers.php.

https://www.bittorrent.com/scripts/site/headers.php?_=1586521900793&callback=<PAYLOAD>
https://www.bittorrent.com/scripts/social/get_tweet.php?_=1586521900791&callback=<PAYLOAD>
its works on IE browsers.

## Impact

fix them

## Attachments
- xss.png
