# Session Fixation on Acronis

## Report Details
- **Report ID**: 1486341
- **URL**: https://hackerone.com/reports/1486341
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-02-20T08:07:16.281Z
- **Disclosed**: 2022-03-01T09:09:04.007Z

## Reporter
- **Username**: hatnare
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi there,
The application does not set a new Session ID in the cookie after what appears to be an authentication attempt by the user. If this was a successful login and the Session IDs are stored in cookies then this application is affected by Session Fixation vulnerability.

## Steps To Reproduce
Step-1: Open up Firefox & download Cookie Editor Extension on your browser.
Step-2: Go to https://account.acronis.com/#/auth/login & login with your credentials.
Step-3: Click on "Cookie Editor" then, click on "Export cookie" by clicking this we get a cookie copied in clipboard.
Step-4: Open another browser or Private tab.
Step-5: Go to https://account.acronis.com/#/auth/login but don't login. Just simply click on "Cookie editor" & click on "Import cookie" & paste the code which we previously exported.
Step-6: After pasting just refresh the page and that's done you are now logged into your account without any credentials.

Reference:
https://owasp.org/www-community/attacks/Session_fixation
https://hackerone.com/reports/1201396
https://hackerone.com/reports/6504
https://cs.brown.edu/courses/csci1660/wiki/attacks/Session-Fixation/
https://en.wikipedia.org/wiki/Session_fixation
https://www.acunetix.com/blog/web-security-zone/what-is-session-fixation/

Note: If there is any problem in reproduction from your side then let me know. I will provide you with a video poc.

## Impact

A successful session fixation attack gives the attacker access to the victim's account. This could mean access to higher level privileges or the ability to look at sensitive data. An attacker doesn't need any user credentials to login on an account what he/she will do, he/she will capture session value/token with any sniffing tools like Wireshark etc after getting session value/token he/she can easily login to the account. By this way an account can be controlled by an attacker and for this vulnerability it can also be impactful for xss attack if an attacker got xss vulnerability on your website he/she can chain the vulnerability with this attack.

## Attachments
No attachments
