# CSRF to account takeover in https://█████/

## Report Details
- **Report ID**: 1018270
- **URL**: https://hackerone.com/reports/1018270
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-10-25T11:12:36.008Z
- **Disclosed**: 2020-11-09T17:10:23.106Z

## Reporter
- **Username**: i_hack_everyone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi DoD team,
I found a CSRF to account takeover in https://███████/

## NOTE:
Try to open the site in firefox because chrome sometimes is not allowing to open the site.

## Summary:
There is no protection against CSRF in changing email which lead to CSRF to account takeover on  https://██████/.

## Step-by-step Reproduction Instructions
## I have made a video POC in which I have shown the account takeover clearly Please do watch for better understanding
1. Login as victim and check your infos in the account details
2. Open the CSRF malicious file which I have attached (csrf_POC.html)
3. Now the email is different (you can also change your name and other fields as well)
4. Now you can simply takeover the account
5. All you have to do is click on reset password on main page and enter the email you used to trick the victim and you will get instructions to reset the password. And you can successfully takeover the account

## Suggested Mitigation/Remediation Actions
Use captchas and CSRF-tokens for be sure that the victim is changing the datas knowing that.

## Impact

It is a critical issue as i was able to takeover anyone account using this attack. This vulnerability is high/critical because I was able to perform account takeover

## Attachments
No attachments
