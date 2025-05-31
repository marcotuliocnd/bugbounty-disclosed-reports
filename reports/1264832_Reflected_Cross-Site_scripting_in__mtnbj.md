# Reflected Cross-Site scripting in : mtn.bj

## Report Details
- **Report ID**: 1264832
- **URL**: https://hackerone.com/reports/1264832
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-07-16T00:42:21.351Z
- **Disclosed**: 2021-09-26T12:59:03.117Z

## Reporter
- **Username**: alimanshester
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
Hello Team 
I have found a Reflected XSS vulnerability in mtn.jb by file name 


## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. go to : 
████
  2. enter any email and press  Suivant
  3. fill all the inputs by any data .
  4. in file upload upload any photo with payload file name : "><img src=x onerror=alert(document.cookie);.jpg

  5 . the payload executed in the page  


Supporting Material/References:
1 - video showing poc 
2 - screenshot

## Impact

An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page

## Attachments
No attachments
