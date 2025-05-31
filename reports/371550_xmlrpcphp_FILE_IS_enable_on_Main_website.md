# xmlrpc.php FILE IS enable on Main website

## Report Details
- **Report ID**: 371550
- **URL**: https://hackerone.com/reports/371550
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-06-27T06:18:10.171Z
- **Disclosed**: 2019-07-16T00:23:53.138Z

## Reporter
- **Username**: tibin_sunny
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
The domain contains XMLRPC activated which can cause serious damage to your server and website.Admin panel can be easily bypassed and also can cause heavy DDOS that can take down the entire server.Just a simple fix can resolve the issue.Secure your site :) 

URL:https://iandunn.name/wordpress/xmlrpc.php

Steps to Reproduce the issue is shown on the POC video attached with this report

This is what you originally see when you try to open the xmlrpc.php located at  

1)http://<targetWebSite.com>/xmlrpc.php  here ( https://iandunn.name/wordpress/xmlrpc.php )

2)Open your proxy (I am using burp )and resend the request 

3)The first thing to do now is Send a POST request and list all the available methods , why ? cause that’s how we’ll know which actions are even possible to make and potentially use one of them for an attack.
TO list all methods Send a POST request with the following POST data,like shown in the picture,you’ll get a response with all the methods avaliable

<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall> 

For more details and to understand the impact watch the video attached with this mail 

As you asked me to submit the report on curl i just installed curl on my windows :-) Just to help you Cheers

Save the below code as asd.json
<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall> 

curl.exe --data @asd.json -X POST https://iandunn.name/wordpress/xmlrpc.php


Fix/Migration 
In order to fix the isuue follow the  link: http://www.wpbeginner.com/plugins/how-to-disable-xml-rpc-in-wordpress/

https://digwp.com/2009/06/xmlrpc-php-security/

Similar Report: https://hackerone.com/reports/325040 

Check the above report to know the actual impact of the xmlrpc.php

More Details about exploitation: https://medium.com/@the.bilal.rizwan/wordpress-xmlrpc-php-common-vulnerabilites-how-to-exploit-them-d8d3c8600b32

 Thank You,
Hope You wil soon fix it :)

## Impact

Running a system which potentially carries a lot of vulnerable endpoints and bad default settings is always a risk. Hardening should always be compulsory.

## Attachments
- Bug.JPG
- xmr.mp4
- curl.JPG
