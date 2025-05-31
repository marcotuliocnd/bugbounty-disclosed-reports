# Stored XSS in Intense Debate comment system

## Report Details
- **Report ID**: 1039750
- **URL**: https://hackerone.com/reports/1039750
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-20T17:01:25.283Z
- **Disclosed**: 2021-02-14T16:29:23.546Z

## Reporter
- **Username**: sodium_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hi Team,

## _Summary:_
The  Intense Debate comment system is vulnerable to stored xss by users , this would allow for atacking admins/users on the blog ,

## Platform(s) Affected:
*  Intense Debate comment system



________________________________________________________________________________________
________________________________________________________________________________________

## _Steps To Reproduce:_


  1. Go to **intensedebate.com/moderate/{{-ID-}}**
  2. Go to comments > allow images in comments
  3. Now go to your blog and add this payload as comment :

```html
<img src="https://intensedebate.com/images/a-addblog.png" onload="alert()">
```
  4. You'll notice the alert will pop as result for the "onload" attribute ,
  

________________________________________________________________________________________
________________________________________________________________________________________


A helpful video :
{F1087899}

## Impact

* Stealing cookie and secter tokens 
* Editing html/css/js content for phishing attacks



Thanks for taking your valuable time to read and validate this report

## Attachments
- 2020-11-20_at_17-57-44.mp4
