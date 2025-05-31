# Flash Based Reflected XSS on www.grouplogic.com/jwplayer/player.swf

## Report Details
- **Report ID**: 859806
- **URL**: https://hackerone.com/reports/859806
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-26T17:33:38.251Z
- **Disclosed**: 2021-04-13T13:24:03.004Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello there,
I hope you are well!

Steps:
1. Open firefox.
2. Go to http://www.grouplogic.com/jwplayer/player.swf?playerready=alert(document.domain) 
You will see xss alert.

## Impact

Reflected XSS

Regards,
@mygf

## Attachments
No attachments
