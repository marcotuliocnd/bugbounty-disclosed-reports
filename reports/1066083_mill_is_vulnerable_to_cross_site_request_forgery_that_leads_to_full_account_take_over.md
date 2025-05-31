# ███████mill is vulnerable to cross site request forgery that leads to full account take over.

## Report Details
- **Report ID**: 1066083
- **URL**: https://hackerone.com/reports/1066083
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-25T00:50:55.138Z
- **Disclosed**: 2021-01-25T19:57:35.442Z

## Reporter
- **Username**: m4xp0w3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
The form within the "My Account" page in ███████mil fails to verify the CSRF token used when an user makes changes such as changing the password and other details. For example, an attacker can change the user's email address, full name, phone number, etc. In this way the attacker can gain full control over the user's account. 

**Note**
In order to get a valid CSRF token you will need to create an account and make any change in "My account" after this you can grab the value of the ██████████ token and use it in your CSRF attack.
**Description:**
Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.
## Impact
Attackers can take over accounts.
## Step-by-step Reproduction Instructions

1. Host the attached proof of concept in your server and change the desired values.
2. While authenticated visit the attacker's website that hosts the CSRF poc
3. On a different browser or incognito session log in with the new email address and password

## Impact

Attackers can take control over any user account.

## Attachments
No attachments
