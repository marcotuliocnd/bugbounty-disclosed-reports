# Nextcloud server software: Content Spoofing

## Report Details
- **Report ID**: 145463
- **URL**: https://hackerone.com/reports/145463
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-17T16:31:11.824Z
- **Disclosed**: 2016-07-19T10:30:00.935Z

## Reporter
- **Username**: ishahriyar
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
In Nextcloud the "dir" parameter is vulnerable to content spoofing attack.
If anyone puts a valid directory name in dir parameter then it goes that directory other wise it redirects
to the home directory (/)
By putting `../../` in dir parameter I was able to stop the redirect then I had put some messages after that and that messages reflected with the same given format.

So here an  attacker can send his messages directly through url.  
Poc link
`http://192.168.0.118/nextcloud/index.php/apps/files/?dir=../../Welcome+to+Nexcloud+You+can+get+pro+account+by+navigating+this+example.com`

Thanks.

## Attachments
- csnext.png
