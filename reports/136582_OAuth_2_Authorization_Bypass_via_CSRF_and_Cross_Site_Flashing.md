# OAuth 2 Authorization Bypass via CSRF and Cross Site Flashing

## Report Details
- **Report ID**: 136582
- **URL**: https://hackerone.com/reports/136582
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-05T18:07:47.074Z
- **Disclosed**: 2017-10-18T09:39:31.840Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: vimeo

## Vulnerability Information
Hello Vimeo Security Team,

There is a vulnerability in api.vimeo.com/oauth which allows an attacker to gain full App privilege over a Vimeo victim user account without user approval, just by having the victim open a link to the attacker webpage.

Proof of Concept link :
http://opnsec.com/vimeo/vimeoOAuth2Bypass.html

POC requirements :
-Tested on Windows 8.1/10 with Firefox 46, Chrome 50, Internet Explorer 11 
-Flash must be active
-You must be logged in Vimeo

POC instructions :
1. Open the POC link
2. Wait a few seconds
3. The leaked infos from OAuth authorization will show in the box. 
4. You can then check your vimeo Apps setting page at https://vimeo.com/settings/apps to see that the app 'OAuthBypass' is in the list of authorized Apps

----------------------

Technical info :

The vulnerability comes from the crossdomain file api.vimeo.com/oauth/crossdomain.xml which is set to 'allow-access-from domain="*" '.This means that any domain can load data with Flash from the directory 'api.vimeo.com/oauth/' AND FROM THE FOLDER'S CHILD DIRECTORIES, including the directory https://api.vimeo.com/oauth/authorize 
The url https://api.vimeo.com/oauth/authorize should not be accessible to cross domain flashing because it contains the Token to allow the App to gain access to the user account.

You can verify the Flash behavor in Adobe Flash documentation on security :
http://help.adobe.com/en_US/as3/dev/WS5b3ccc516d4fbf351e63e3d118a9b90204-7c85.html#WS11001817-24CB-48a4-AA10-59468865F751

"A URL policy file applies only to the directory from which it is loaded <b>and to its child directories."<b>

What happens when flash AS3 loads https://api.vimeo.com/oauth/authorize is that :
1. By default Flash check the Master crossdomain.xml file, which in this case is 'permitted-cross-domain-policies="by-content-type" ' which means that the policy will be based on a directory base.  
2. Then by default Flash will try to load https://api.vimeo.com/oauth/authorize/crossdomain.xml which is not allowing cross site request at all. In this case, flash will not let the cross domain request and the Vimeo OAuth is safe

HOWEVER, if the evil.swf flash calls 'Security.loadPolicyFile("api.vimeo.com/oauth/crossdomain.xml")'
before loading url https://api.vimeo.com/oauth/authorize then Flash will allow cross domain request on api.vimeo.com/oauth/ and on any child directory including https://api.vimeo.com/oauth/authorize. In that case, flash will never check https://api.vimeo.com/oauth/authorize/crossdomain.xml because api.vimeo.com/oauth/crossdomain.xml is enough for him to allow the cross domain request on https://api.vimeo.com/oauth/authorize

I hope my explaination is clear enough. In conclusion, a call to 'Security.loadPolicyFile("https://api.vimeo.com/oauth/crossdomain.xml")' will allow any domain to read the source code of https://api.vimeo.com/oauth/authorize.

From there, an attacker can steal the Token of the user and do all the authorization process (Obtaining Authentication credentials via redirect) without the need of user interaction.

Vulnerability Mitigation :

To remove the vulnerability, you just need to move the https://api.vimeo.com/oauth/authorize to another subdomain like www.vimeo.com/oauth/authorize or to another directory like api.vimeo.com/authorize where there is no allowing crossdomain.xml file between the root folder level and the "authorize" level.
To keep the same implementation for the app developpers you can make a simple redirection from https://api.vimeo.com/oauth/authorize to the new, protected "authorize"  location. That way flash will not be able to follow the redirection and only legitimate user will be able to validate App authorization.

-------------

If you need more info like POC source code or if the POC doesn't work feel free to contact me.

Regards,

Enguerran Gillier
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;
&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;&#x2588;

## Attachments
No attachments
