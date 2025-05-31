# Clickjacking URLS

## Report Details
- **Report ID**: 1039805
- **URL**: https://hackerone.com/reports/1039805
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-11-20T18:52:08.255Z
- **Disclosed**: 2021-03-10T09:46:30.679Z

## Reporter
- **Username**: tinkerermaruthu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hey Team
While performing security testing of your websites i have found the vulnerability called Clickjacking.
Many URLS are in scope and vulnerable to Clickjacking.


The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a <frame> or <iframe>. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
This vulnerability affects Web Server.



##Steps to Reproduce

Vulnerable Urls:
 1.https://nextcloud.com
 2.https://download.nextcloud.com
 3.https://help.nextcloud.com
 4.https://apps.nextcloud.com/
 5.https://docs.nextcloud.com
 6.https://crm.nextcloud.com
 7.https://support.nextcloud.com
 8.https://scan.nextcloud.com/
 9.https://lists.nextcloud.com
10.https://portal.nextcloud.com
11.https://auth.nextcloud.com
12.https://pushfeed.nextcloud.com
13.https://newsletter.nextcloud.com



URL one by one into iframe src value  ..
this is the HTML code

<html>
<style>
   iframe {
       position:relative;
       width:500px;
       height:700px;
       opacity:0.0001;
       z-index:2;
   }
   div {
       position:absolute;
       top:500px;
       left:550px;
       z-index:1;
   }
</style>
<iframe src="url"></iframe>
</html>


The Site Is Fully Loaded

## Impact

This  technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email  account, but are instead typing into an invisible frame controlled by the attacker.

I attached a Screenshots
thank you

## Attachments
- apps.nextcloud.com.png
- auth.nextcloud.com.png
- crm.nextcloud.com.png
- docs.nextcloud.com.png
- download.nextcloud.com.png
- help.nextcloud.com.png
- newsletter.nextcloud.com.png
- lists.nextcloud.com.png
- nextcloud.com.png
- portal.nextcloud.com.png
- pushfeed.nextcloud.com.png
- scan.nextcloud.com.png
- support.nextcloud.com.png
