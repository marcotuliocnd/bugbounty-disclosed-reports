# [XSS] sandbox.veris.in

## Report Details
- **Report ID**: 137119
- **URL**: https://hackerone.com/reports/137119
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-05-08T14:39:14.572Z
- **Disclosed**: 2016-09-09T15:17:42.207Z

## Reporter
- **Username**: bogdantcaciuc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: veris

## Vulnerability Information
Hello I want to report a XSS in ,,Badge Types''


Steps to reproduce :


1. Create a badge with badge name "><img src=x onerror=alert(1)>  badge description "><img src=x onerror=alert(1)> , select Organization press ,,Add New Badge Key ''     in Key display name complete this with same payload "><img src=x onerror=alert(1)>  , complete all 
requirements but in ,,Input type'' select Text only''  and Confirm badge Type. 
2. Press view badge and alert was executed 

I make video if must



## Attachments
- ada.PNG
