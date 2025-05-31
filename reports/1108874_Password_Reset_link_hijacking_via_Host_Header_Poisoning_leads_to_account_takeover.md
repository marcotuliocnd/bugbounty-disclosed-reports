# Password Reset link hijacking via Host Header Poisoning leads to account takeover

## Report Details
- **Report ID**: 1108874
- **URL**: https://hackerone.com/reports/1108874
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-02-22T16:48:14.027Z
- **Disclosed**: 2021-04-02T18:51:48.573Z

## Reporter
- **Username**: hemantsolo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
████████ uses the Host header when sending out password reset links. This allows an attacker to insert a malicious host header, leading to password reset link / token leakage.

## References
http://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html
https://hackerone.com/reports/226659

## Impact

The victim will receive the malicious link in their email, and, when clicked, will leak the user's password reset link / token to the attacker, leading to full account takeover.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1.) Open up Firefox and Burp Suite.
2.) Visit the forgot password page (http://██████/█████)
3.) Enter the victim's email address and click on SEND RESET LINK.
4.) Intercept the HTTP request in Burp Suite & change the Host Header to your malicious site/server ex. ███.
5.) Forward the request and you'll be redirected to your server.

The victim will then receive a password reset e-mail with your poisoned link.
If the victim clicks the link, the reset token will be leaked and the attacker will be able to find the reset token in the server logs. The attacker can then browse to the reset page with the token and change the password of the victim account!

## Suggested Mitigation/Remediation Actions
Use $_SERVER['SERVER_NAME'] rather than $_SERVER['HTTP_HOST']



## Attachments
No attachments
