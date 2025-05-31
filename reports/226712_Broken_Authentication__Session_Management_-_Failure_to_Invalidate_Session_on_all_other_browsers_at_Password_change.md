# Broken Authentication & Session Management - Failure to Invalidate Session on all other browsers at Password change

## Report Details
- **Report ID**: 226712
- **URL**: https://hackerone.com/reports/226712
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-05-07T12:29:01.783Z
- **Disclosed**: 2017-05-07T16:44:12.869Z

## Reporter
- **Username**: koviri_jagdish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
Broken Authentication & Session Management - Failure to Invalidate Session on all other browsers at Password change
==========================================================
Hello Team,
While I was testing your web application "Paragon Initiative Enterprises", I came to know that it is vulnerable to "Broken Authentication and Session Management > Failure to Invalidate Session > On Password Reset" at https://bridge.cspr.ng/my/account .

Description : When a user changes his account password, all the sessions on other devices/browsers should expire.

Cause : Suppose any user (victim) left his account logged in on any computer/browser (victim could use browser at Cyber Cafe or any shared computer). And after a particular he realized that he left his account logged in, and there is a security provided that when a user changes his account password all other sessions should invalidate or expire, which will expire the session from that shared computer.

But in your web application, I didn't found any such security that invalidate the session after password. Here if any user left his account logged in, any attacker can misuse the victim's account and there is no option available to the victim to invalidate the session on that shared computer which could lead to some major problems.


>Steps to reproduce the bug :
>Step 1 : Go to Browser A at (say Mozilla Firefox) and login with your credentials at https://bridge.cspr.ng/ and login with your credentials.

>Step 2 : Similarly, Go to Browser B at (say Google Chrome) and login with your same credentials at https://bridge.cspr.ng/ and login with your credentials.

>Step 3 : Suppose Browser A (Mozilla Firefox) is an shared computer's browser, and you left your account logged in at that computer. Go to Browser B (Google Chrome) and change your account
password at https://bridge.cspr.ng/my/account.

>Step 4 : When you change your account password at Browser B (Google Chrome), the session at Browser A (Mozilla Firefox) should expire and the account should automatically logged out.

>Step 5 : Go to Browser A (Mozilla Firefox), and visit your https://bridge.cspr.ng/ account page and refresh the page.

You will notice that even after changing the account password at Browser B (Google Chrome), the session at Browser A (Mozilla Firefox) didn't expired which can cause major problems.

Please fix the bug and let me know if you need any other information.

Regards
K. Jagdish


## Attachments
No attachments
