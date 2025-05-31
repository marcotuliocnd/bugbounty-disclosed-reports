# Moodle XSS on  evolve.glovoapp.com

## Report Details
- **Report ID**: 1165540
- **URL**: https://hackerone.com/reports/1165540
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-15T10:27:41.064Z
- **Disclosed**: 2021-05-12T07:41:22.898Z

## Reporter
- **Username**: sn3akysnak3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glovo

## Vulnerability Information
**Cross Site Scripting (XSS) / Moodle XSS **

**Summary : ** *Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. Cross-site scripting carried out on websites accounted for roughly 84% of all security vulnerabilities documented by Symantec as of 2007. *

*An attacker can use XSS to send a malicious script to an unsuspecting user. The end user's browser has no way to know that the script should not be trusted and will execute the script. Because it thinks the script came from a trusted source, the malicious script can access any cookies, session tokens, or other sensitive information retained by the browser and used with that site. These scripts can even rewrite the content of the HTML page. For more details on the different types of XSS flaws, see: Types of Cross-Site Scripting.*

**Payload : **javascript:alert(document.domain)
**Vulnerable Param: ** ?redirect_uri=

**Affected IP's : IP Address	Port**
https://evolve.glovoapp.com/	443

**Recommendations : **
*Sanitize all the user inputs before executing them, also add XSS protection headers on server and client side.* 

**References :**
https://www.acunetix.com/websitesecurity/cross-site-scripting/
https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet 
https://portswigger.net/web-security/cross-site-scripting 

**Proof of Concept :**
-  https://evolve.glovoapp.com:443/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)

** This XSS is escalated from Open-Redirect on the same Parameter **
** Here is the POC for the open-redirect: **

-  https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com

## Impact

**Impact :** *An Adversary can carry out XSS attack and also can take the cookie of the Admin and login through Admin Account. 
Also, an adversary can manage to login through any other users account with valid session cookies. *

## Attachments
No attachments
