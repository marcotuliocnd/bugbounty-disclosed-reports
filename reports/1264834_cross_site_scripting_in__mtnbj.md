# cross site scripting in : mtn.bj

## Report Details
- **Report ID**: 1264834
- **URL**: https://hackerone.com/reports/1264834
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-16T00:56:05.571Z
- **Disclosed**: 2022-08-06T11:19:10.472Z

## Reporter
- **Username**: alimanshester
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
Xss vulnerability in mtn.bj  in file name 

## Steps To Reproduce:


  1.Go to : 
https://www.mtn.bj/business/ressources/formulaires/plan-de-localisation-de-compte/?next=https://www.mtn.bj/business/ressources/formulaires/formulaire-de-souscription/
  2 - fill all inputs with any data 
3 - in file upload upload a file with payload file name such as : "><img src=x onerror=alert(document.cookie);.jpg

4-the payload will executed in the page .

## Supporting Material/References:
1 - video showing poc 
2 - screen shot

## Impact

execute malicious java script in user browser

## Attachments
- xss_mtn_2.mp4
- xss_mtn.png
