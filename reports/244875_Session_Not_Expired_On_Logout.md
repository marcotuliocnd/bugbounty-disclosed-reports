# Session Not Expired On Logout

## Report Details
- **Report ID**: 244875
- **URL**: https://hackerone.com/reports/244875
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-06-30T21:44:06.791Z
- **Disclosed**: 2017-07-01T21:38:44.287Z

## Reporter
- **Username**: pratyushjanghel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hi Wakatime Security Team,

There is a  session management vulnerability in your website. i.e. user's session is not expiring immediately after the logout.

You can get more information of the vulnerability here - https://www.owasp.org/index.php?title=Broken_Authentication_and_Session_Management&setlang=en

An attacker can get the user's session cookies by using Session Spoofer, Cookie Staler etc. and thus, can get the access to the user account.

# Steps To Reproduce:

1. Login into your wakatime.com account.
2. Capture any request. For example Account Settings using Burp Proxy. 
3. Logout from the website.
4. Replay the request captured in step 2 and notice it displays the proper response.

Reference From : #353

Hope you fix this soon ;)

Best Regards,
Pratyush Janghel

## Attachments
No attachments
