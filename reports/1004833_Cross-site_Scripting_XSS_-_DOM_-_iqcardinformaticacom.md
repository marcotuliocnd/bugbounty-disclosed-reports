# Cross-site Scripting (XSS) - DOM - iqcard.informatica.com

## Report Details
- **Report ID**: 1004833
- **URL**: https://hackerone.com/reports/1004833
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-10T21:10:57.854Z
- **Disclosed**: 2020-10-13T09:22:13.451Z

## Reporter
- **Username**: rodntt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hello all

I found a DOM based XSS at iqcard.informatica.com

# Description

After finding the path **iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html**. I noticed that the code inside attach.html was vulnerable to DOM XSS, due to the fact of the javascript *document.location function. search*. The code below illustrates the code contained in the attach.html file

```
<HTML>
<HEAD>
<SCRIPT>
function GetAttach()
{
	var strSearch = document.location.search
	strSearch = strSearch.substring(1)
	
	document.location.replace(strSearch)
}
</SCRIPT>
</HEAD>
<BODY onload='GetAttach()'>


</BODY>
</HTML>
```
As can be seen through the code above, the variable * strSearch * receives everything that comes from the URL after the character? and then insert it into the function *document.location.replace ()*. Through this scenario we have some possibilities.

1 - We can direct the user to any page we want for example:

```
https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html?evil.com
```


2 - We can run a DOM Based XSS, running the javascript schema, javascript: alert (1);

```
https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html?javascript:alert(1)
```


# PoC 

I uploaded a video and an image.

## Impact

An attacker can redirect a user to a malicious page or execute XSS attacks against users of the application or use that domain as a phishing vector to attack other users of informatica.com

## Attachments
- xss_03.png
- poc_redir.mp4
