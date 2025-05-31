# Ability To Delete User(s) Account Without User Interaction

## Report Details
- **Report ID**: 928255
- **URL**: https://hackerone.com/reports/928255
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-20T21:34:45.676Z
- **Disclosed**: 2021-03-17T20:11:03.367Z

## Reporter
- **Username**: hx01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
### Summary:
Gitlab allows its user to exercise their GDPR rights (Right to Access/Delete) user data by sending an email to gdpr-request@gitlab.com however gitlab team doesn't ask for security question(i.e Date Of Birth) before deleting the user account moreover doesn't authenticate the incoming emails from their  instance which allows an attacker to delete user accounts without user interaction :
██████

### Steps to reproduce
1. Send an spoofed email from victim's email address to gdpr-request@gitlab.com from a reputable SMTP (e.g: Sendgrid):
███████
2. Victim will receive the following  confirmation email:

{F914565}
3. In the next few days victim's account will be deleted :

██████

### Fix :
* Add second verification i.e ask for DOB,Government ID.

## Impact

Since Gitlab doesn't verify the request with an Valid ID before triggering Right to Access/Deletion this breaches the GDPR Law(Article 15) & moreover allows an attacker to delete User Accounts without user interaction.

## Attachments
- Screen_Shot_2020-07-21_at_2.18.53_AM.png
