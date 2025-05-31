# Chat exposed using cookie

## Report Details
- **Report ID**: 279070
- **URL**: https://hackerone.com/reports/279070
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-10-18T10:19:29.098Z
- **Disclosed**: 2017-10-19T22:18:21.348Z

## Reporter
- **Username**: sahore
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
###Hello
**Broken authentication and session management:** Attacker can use cookies of an authenticated user to reads and write the chat on the behalf of user and miss guide the legalrobot team.

**Steps to reproduce:**
 * Sign-in https://app.legalrobot.com/sign-in
 * Check the cookies of domain [legaltobot.com]
 * Cookie responsible for this attack is in attachment [cook.JPG] 
  - name: intercom-session-nmyyq5i5
 * Copy the information of above cookie
 * Signed-out from the account and reuse the cookie by using and cookie editor.
 * As you use the cookie the signing screen will look like attachment [screenshot.JPG]

**Scope:**
While exploiting this cookie I have found that after **Logged out** from legalrobot account this cookie can be used means the session for this cookie is still alive and doesn't destroy by the server.


## Attachments
- cook.JPG
- screenshot.JPG
