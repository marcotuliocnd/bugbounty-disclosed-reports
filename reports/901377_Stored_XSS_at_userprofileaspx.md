# Stored XSS at ██████userprofile.aspx

## Report Details
- **Report ID**: 901377
- **URL**: https://hackerone.com/reports/901377
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-06-18T04:37:20.849Z
- **Disclosed**: 2020-07-08T17:38:27.299Z

## Reporter
- **Username**: 5050thepiguy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
Stored XSS vulnerability exists at ██████████userprofile.aspx under "say something about yourself...". XSS can be used for a variety of attacks. 

## Impact
XSS can be used to steal cookies, password or to run arbitrary code in the victim's browser. 

## Step-by-step Reproduction Instructions

1. Create an account at ███████
2. Go to your profile at ████userprofile.aspx
3. Go to "Say something about yourself..." and enter the XSS payload xxx<svg/onload=alert(document.cookie);>xxx
4. Observe that XSS triggers and reload the page to observe that it is stored XSS.

## Product, Version, and Configuration (If applicable)
███userprofile.aspx#

## Suggested Mitigation/Remediation Actions
Use secure coding techniques such as sanitizing input into form fields so attackers cannot inject scripts to perform XSS attacks. XSS vulnerabilities come from a lack of data escaping. 

##References
https://hackerone.com/reports/858255
https://dzone.com/articles/reflected-xss-explained-how-to-prevent-reflected-x
https://www.imperva.com/learn/application-security/reflected-xss-attacks/
https://www.hacksplaining.com/prevention/xss-reflected

## Impact

XSS can be used to steal cookies, password or to run arbitrary code in the victim's browser.

## Attachments
No attachments
