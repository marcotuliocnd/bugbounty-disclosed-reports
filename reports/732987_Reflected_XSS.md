# Reflected XSS 

## Report Details
- **Report ID**: 732987
- **URL**: https://hackerone.com/reports/732987
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-11-09T07:09:03.393Z
- **Disclosed**: 2019-12-09T15:24:52.729Z

## Reporter
- **Username**: imthehackerlor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: owox

## Vulnerability Information
Hi team,

I have found an XSS at https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28/dashboard/?trial=activated
Because the input is not properly filtered, resulting in XSS being executed
Vulnerable area: 
-----
``6177527534dc114eb07fa829e4ce4d28``
The URL will now be: https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated

PoC
---
1, go to https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated
2, Log in and ``XSS`` will execute
██████████

Tested browser
---
Firefox 
Chrome

## Impact

This vulnerability is aimed at all victims and they do not need to be involved in the ``Project``. Just paste this URL and login, XSS will automatically execute.
Therefore, it will have a ``high impact``, because before XSS is executed, the application will ask the user to login.
+ The attacker can execute JS code.
████████
████████

Documents related to ``Impact``
---
https://portswigger.net/web-security/cross-site-scripting/reflected
https://portswigger.net/web-security/cross-site-scripting/exploiting

Recommendation
----
+ Revisit the entire application and validate the user input at server side.
+ Sanitize the data collected from input fields before further processing.
+ Filter out special and meta-characters from user input.

Best regards,
@dat

## Attachments
No attachments
