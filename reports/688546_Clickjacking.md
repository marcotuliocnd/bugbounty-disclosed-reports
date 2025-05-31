#  Clickjacking

## Report Details
- **Report ID**: 688546
- **URL**: https://hackerone.com/reports/688546
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2019-09-05T09:09:57.721Z
- **Disclosed**: 2022-01-17T07:27:37.227Z

## Reporter
- **Username**: paramdham
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: palo_alto_software

## Vulnerability Information
##Summary

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

Websites are at risk of a clickjacking attack when they allow content to be embedded within a frame.

An attacker may use this risk to invisibly load the target website into their own site and trick users into clicking on links which they never intended to. An "X-Frame-Options" header should be sent by the server to either deny framing of content, only allow it from the same origin or allow it from a trusted URIs.


##Proof of concept code :- 

Copy the above code and paste it in notepad and save it with .html extention
and open it in browser

```
<html> 
<head> 
<title>Clickjack test page</title> 
</head> 
<body> 
<p>Website is vulnerable to clickjacking!</p>

<iframe src="https://app.outpost.co/settings/preferences"  sandbox="allow-top-navigation allow-same-origin allow-scripts" width="500" height="500"></iframe> 

</body> 
</html>
```

Copy and paste above given code and  save it with hack.html and  open it in browser




##Recommendation :- 

Add X-FRAME-OPTIONS header to mitigate the issue

## Impact

It allows remote attackers to do some clickjacking which can be used for adding arbitrary tasks . Why? Almost all of your page has missing X-FRAME-OPTIONS header.


##Thanks

## Attachments
No attachments
