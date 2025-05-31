# Temporary banned user (from platform) is able to make submissions via embedded submission forms

## Report Details
- **Report ID**: 1133536
- **URL**: https://hackerone.com/reports/1133536
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-29T05:16:18.688Z
- **Disclosed**: 2021-09-22T19:34:25.307Z

## Reporter
- **Username**: muon4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
## Summary:
Hello team!

We have discovered issue which allows temporary banned user to submit new reports using embedded submission forms. The hacker can submit submissions via embedded forms using his/her email address. Once the ban is over the hacker can claim his/her report via invitation link.

## Steps To Reproduce:

- Login as a program user and invite one of your test user to be part of it
- Temporary ban this user from the platform 
- Make sure that the user is now banned and you can't login
- Open the embedded submission form
- Submit submission with the email address of the banned hacker
- If you try to open this invitation link as a user who is not banned but logged in to the hackerone you will see the following error message `It seems you have hacked your way into an invitation that belongs to banned-user`
- This clearly indicates that you were able to make new submission as a banned user

However, if you now unban the banned user and log in as it's account you are able to claim this report to the user who was banned at the time of submission was made.

## Recommendation:

If a hacker is banned make sure that embedded forms does not allow to use his/her email address.
 

## References:

-

## Impact

Banned hackers can submit new reports using banned email addresses

## Attachments
No attachments
