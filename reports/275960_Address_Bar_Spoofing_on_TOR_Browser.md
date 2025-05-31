# Address Bar Spoofing on TOR Browser

## Report Details
- **Report ID**: 275960
- **URL**: https://hackerone.com/reports/275960
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-09T21:58:07.986Z
- **Disclosed**: 2023-01-02T08:43:51.692Z

## Reporter
- **Username**: soulhunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Hi TOR team,

I would like to report a security bug in your browser:

Step 1: Goto http://www.ոokia.com/(http://jsbin.com/wuyikedaxi/1/edit?html,output)
Step 2: Observe that address bar points to http://www.ոokia.com/ which actually to be pointing to http://xn--okia-zgf.com, however browser displays www.ոokia.com/

Actual results:

Address bar points to a spoofed domain http://www.ոokia.com/. Address bar fails to parse character "ո"(U+0578 Armenian Small Letter). Several other characters from Armenian family lead to the same effect. 

Expected results:

TORbrowser should have resolved the domain to real http://xn--okia-zgf.com.  On chrome, internet explorer and firefox it resolves to xn--okia-zgf.com. 

## Attachments
- torbrowser.png
