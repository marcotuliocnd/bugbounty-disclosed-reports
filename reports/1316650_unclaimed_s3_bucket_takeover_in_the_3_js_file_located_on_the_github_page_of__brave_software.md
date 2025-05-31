# unclaimed s3 bucket takeover in the 3 js file located on the github page of  brave software

## Report Details
- **Report ID**: 1316650
- **URL**: https://hackerone.com/reports/1316650
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-08-23T17:34:38.678Z
- **Disclosed**: 2021-09-24T17:32:28.610Z

## Reporter
- **Username**: gaurav-bhatia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

There is a unclaimed s3 bucket i.e brave-extensions.s3.amazonaws.com located in the 3 .js  file on official brave software github page (https://github.com/search?q=org%3Abrave+brave-extensions+language%3AJavaScript&type=Code)the attacker can takeover the bucket and create file that is used in the code for e.g.(redirect.html,dt.html ) and can modify the content of the html file and can get cookies of the victim whoever uses the file.

##Proof of Exploitability

1. Github Link where there is the s3 bucket located in 3 js files :- https://github.com/search?q=org%3Abrave+brave-extensions+language%3AJavaScript&type=Code
{F1422548}

2. POC link for takeover s3 bucket ( for poc purpose i have showed index.html so that no user is harmed while testing):- http://brave-extensions.s3.amazonaws.com/index.html
{F1422547}

## Steps To Reproduce:
1. Create a s3 bucket with name brave-extensions and any region
2. Upload files with the name same as given in the code
3. Make the settings and change it as a static website
4. You have successfully taken the s3 bucket and now when any user runs the website where the js file is linked they will be redirected to the malicious website link and an attacker can get the cookies of any victim.

## Impact

An attacker can takeover the unclaimed s3 bucket and if the js file is connected with any html file of website that is hosted publicly then an attacker can create a malicious file with custom payloads and can harm the user by downloading the malicious file instead of original file.

## Attachments
- bravepoc1.JPG
- bravepoc2.JPG
