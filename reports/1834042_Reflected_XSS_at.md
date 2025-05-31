# Reflected XSS at ████████

## Report Details
- **Report ID**: 1834042
- **URL**: https://hackerone.com/reports/1834042
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-13T14:47:00.032Z
- **Disclosed**: 2023-02-24T18:39:53.919Z

## Reporter
- **Username**: ohzo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
The domain █████████ have dochelper where the user id is submitted.
We can submit the crafted XSS payload to pop the alert message by accesing the cookie.

POC URL: 
```
https://████/dochelper?userId=</b><script>alert(document.cookie)</script><b><!-- 
```

█████

## References
CVE-2016-5682
https://portswigger.net/web-security/cross-site-scripting
https://www.bugbountyhunter.com/vulnerability/?type=xss

## Impact

*   As an attacker, I can Steal the cookie of the User, by sending a crafted mail to them.
*   Victim's Account can be compramised
*    Impersonate or masquerade as the victim user.
*    Carry out any action that the user is able to perform.
*    Read any data that the user is able to access.
*    Capture the user's login credentials.
*    Perform virtual defacement of the web site.
*    Inject trojan functionality into the web site.

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers
CVE-2016-5682

## Steps to Reproduce
1. Visit https://████████/dochelper?userId=
2. Put a crafetd XSS payload to the userId parameter. (</b><script>alert(document.cookie)</script><b><!--)
3. Open the link in the browser

## Suggested Mitigation/Remediation Actions
1. Filter input on arrival
2. Encode data on output.



## Attachments
No attachments
