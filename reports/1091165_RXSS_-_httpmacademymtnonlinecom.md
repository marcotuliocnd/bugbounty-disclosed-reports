# RXSS - http://macademy.mtnonline.com

## Report Details
- **Report ID**: 1091165
- **URL**: https://hackerone.com/reports/1091165
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-31T11:18:15.335Z
- **Disclosed**: 2021-12-11T15:31:49.881Z

## Reporter
- **Username**: 0xelkomy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
The page located at http://macademy.mtnonline.com
suffers from a Cross-site Scripting (XSS) vulnerability. XSS is a vulnerability that occurs when user input is unsafely encorporated into the HTML markup inside of a webpage. When not properly escaped an attacker can inject malicious JavaScript that, once evaluated, can be used to hijack authenticated sessions and rewrite the vulnerable page's layout and functionality. The following report contains information on an XSS payload that has fired on http://macademy.mtnonline.com, it can be used to reproduce and remediate the vulnerability.

Steps To Reproduce
Go to Those Links.
http://macademy.mtnonline.com/learner/ContactUs.aspx/(A('onerror='alert%60xElkomy%60'xelkomy))/Signin.aspx

Browsers
I test them on Firefox and Google Chrome.

Fix:-
Filter input on arrival
Encode data on output
Use appropriate response headers
Content Security Policy.

Regards,
xElkomy

## Impact

View any information that the user is able to view. Modify any information that the user is able to modify. Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user. || And I can used this for
1-Ad-Jacking
2-Session Hijacking
3-Bypassing CSRF protection
4-Crypto Mining ::::)))

## Attachments
No attachments
