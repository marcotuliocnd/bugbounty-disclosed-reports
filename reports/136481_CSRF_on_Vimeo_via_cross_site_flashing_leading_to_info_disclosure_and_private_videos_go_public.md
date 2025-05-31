# CSRF on Vimeo via cross site flashing leading to info disclosure and private videos go public

## Report Details
- **Report ID**: 136481
- **URL**: https://hackerone.com/reports/136481
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-05T13:26:04.220Z
- **Disclosed**: 2016-07-29T12:01:09.922Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hello Vimeo Security Team.

There is a CSRF vulnerability on Vimeo.com. With this vulnerability, an attacker can make all the victim's vimeo videos go public just by having the victim open a link to the attacker webpage. He can also get the victim's vimeo name, user id, user account type and perform other CSRF actions such as changing the victim's vimeo name.

POC link : http://opnsec.com/vimeo/VimeoMoogaloop.html

POC requirements :
-Fully working with Firefox on Windows. POC partly working with Internet Explorer and not working with Chrome (the vulnerability is present in all browsers though)
-Flash must be active
-You must be logged in Vimeo (if you have private videos, they will be public after the POC)

POC instructions :
1. Open the POC link
2. Wait a few seconds
3. The leaked infos and CSRF actions will show in the boxes. 
4. You can then check your vimeo account to see the changes made by the CSRF POC. (Name change is immediate, videos privacy changes take 1-2 minutes)

-----------------

Technical info :

Vulnerability description :
There is a vulnerability because a Vimeo XSRF token is present in the source code of the 404 http error pages, including in https://vimeo.com/moogaloop

There is a crossdomain file in http://vimeo.com/moogaloop/crossdomain.xml, which allows connections from *.vimeocdn.com. This means that the moogaloop.swf file from vimeo cdn (https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf) can access and read the https://vimeo.com/moogaloop page, including the XSRF token value.

The moogaloop.swf is vulnerable to Cross Site Flashing, meaning that an external SWF (http://evilsite.com/evil.swf) can load moogaloop.swf and take control of it and perform a request to the https://vimeo.com/moogaloop page on behalf of https://f.vimeocdn.com/p/flash/moogaloop/6.3.5/moogaloop.swf. This means that the evil.swf file get the XSRF token value of the Vimeo user from the 404 page https://vimeo.com/moogaloop.

The evil.swf file can then use the token to perform CSRF request to Vimeo such as changing the vimeo name (POST request to https://vimeo.com/settings) or changing the privacy of all uploaded videos and futur videos to public (POST request to https://vimeo.com/settings/videos)

Vulnerability Mitigation :

If you no longer need the http://vimeo.com/moogaloop/crossdomain.xml file, removing it will remove the vulnerability.

If you don't want to remove the crossdomain file, you just need to remove any private info (user name, user id, XSRF token) from the https://vimeo.com/moogaloop 404 page and any https://vimeo.com/moogaloop/... page and the vulnerability will be remove.

It would be a good practice to remove these info from any 404 webpage to avoid any other similar CSRF vulnerability.

Regarding the moogaloop.swf file, if you want to avoid Cross site flashing, you need to sanitize user input, in particular the "config_url" flashvar parameter.

-------------

If you need more info like POC source code or if the POC doesn't work feel free to contact me.

Regards,

Enguerran Gillier
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;

## Attachments
No attachments
