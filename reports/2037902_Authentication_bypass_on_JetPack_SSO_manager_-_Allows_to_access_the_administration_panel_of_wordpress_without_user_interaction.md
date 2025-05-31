# Authentication bypass on JetPack SSO manager - Allows to access the administration panel of wordpress without user interaction

## Report Details
- **Report ID**: 2037902
- **URL**: https://hackerone.com/reports/2037902
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-06-25T19:28:53.048Z
- **Disclosed**: 2023-12-28T07:44:04.545Z

## Reporter
- **Username**: sodium_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello team,

## Summary:
The JetPack SSO manager is plugin that allows any user to log into their wordpress using the same log-in credentials you use for WordPress.com, then they’ll now be able to register for and sign in to self-hosted WordPress.org sites quickly, example :

User creates their wordpress instance at host.com, they install and enable  JetPack SSO
They later can login into their wordpress instance at host.com using wordpress.com, users are also can make other users register/login with the same company email (@host.com) and access the administration panel of the host


## Description :
The user anyways when he tries to authenticate into his wordpress instance via wordpress.com he gotta have his email confirmed, otherwise it won't work, interstingly there is a way that bypasses the email confirmation when a user invites you to his account and you accept his invite your account will be confirmed, chaining those issues the following scenario can result for the authentication bypass of any wordpress  instance when these circumestances are met :

* wordpress installed on host.com have jetpack installed and "Match accounts using email addresses" enabled (IDK if this is necessary anyways) 
* wordpress instance have a user with specific email, that email does not exist on wordpress.com

You can access this host.com wordpress panel via

## Steps To Reproduce:
**Setup**

  1. Install Jetpack latest version, once installed go to plugins>Jetpack>settings>"Match accounts using email addresses">enable (I'm not sure if this is intended or not)
  2. Add user into your wordpress (host.com) with their email (says something@company.com)


* **As attacker (email confirmation bypass)** :
  1. Create two accounts at Wordpress.com 
        A/. One with your personal email and confirm it 
        B/.  Second with the victim's existed user at host.com email (something@company.com)

  2. At your confirmed wordpress.com account go to settings >users invite your second account (something@company.com)
  3. At your second account go to notifications at the top right, see the invitation and accept it 
  4. See that your Wordpress.com account’s email has been verified (email confirmation bypass )

* **access the wordpress admin panel**
  1. Now at the same browser where the (something@company.com) Wordpress.com account 
  2. go to host.com wordpress panel 
  3. Click on sign in with wordpress.com
  4. Forward 
  5. See yourself logged in as admin on host.com wordpress

## Platform(s) Affected:
JetPack latest version




## Supporting Material/References:
As example I bypass ███████ 

██████

## Impact

* Bypass authentication of websites that runs wordpress with JetPack plugin without any user inteaction


Regards,

Adam

## Attachments
No attachments
