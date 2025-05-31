# Subdomain takeover of blog.snapchat.com

## Report Details
- **Report ID**: 171942
- **URL**: https://hackerone.com/reports/171942
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-25T20:08:34.689Z
- **Disclosed**: 2016-10-05T18:41:02.256Z

## Reporter
- **Username**: jreynoldsdev
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
#Overview
The ANAME for blog.snapchat.com, which redirects to snapchat-blog.com, was pointing to tumblr for Snapchat's blog.  This blog had been expired or had removed the CNAME claim.  Adding "snapchat-blog.com" to the custom domain setting on tumblr allowed takeover of this subdomain.

#Repro Steps
1) Visit http://blog.snapchat.com
Result: Blog registered by my account "jreynoldsdev" displays title "Hello Snapchat - Jake Reynolds"

#Suggested Fixes
The best fix would be for Snapchat's tumblr blog to reclaim this CNAME.  For resolution contact me and we can coordinate switching the domain name back under your control.

If you have any further questions please feel free to reach out.

Thanks,
Jake

## Attachments
- snapchatTumblrScreen.png
- subdomainTakeoverSnapchat.png
