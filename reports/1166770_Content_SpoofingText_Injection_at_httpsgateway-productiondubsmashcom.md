# Content Spoofing/Text Injection at https://gateway-production.dubsmash.com

## Report Details
- **Report ID**: 1166770
- **URL**: https://hackerone.com/reports/1166770
- **State**: Closed
- **Severity**: none
- **Submitted**: 2021-04-16T18:50:21.889Z
- **Disclosed**: 2021-10-27T14:11:02.549Z

## Reporter
- **Username**: karthik86
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
##Summary:-
Hi team i found security issue on your website https://gateway-production.dubsmash.com

##Description:-
 I have found a "Content Spoofing/Text Injection" on one of the domain which is in scope
https://gateway-production.dubsmash.com
in which Using the link the attacker can trick any genuine user to go to the attacker's phishing site.

##Steps:-
1.visit the url https://gateway-production.dubsmash.com  you get that 404 error(Cannot GET /)
2.Now here an attacker can trick any user by sending below link like example:-
https://gateway-production.dubsmash.com/gateway-production.dubsmash.com(It_Has_Been_Moved_To(evil.com)_Please_Visit_http://www.evil.com

##Reference:- 
 https://hackerone.com/reports/997198

##Proof:-
attached screenshot

## Impact

As i mentioned above Crafted phishing attacks on gateway-production.dubsmash.com

## Attachments
- reddit.JPG
