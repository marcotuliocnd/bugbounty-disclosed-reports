# Missing brute force protection on password confirmation modal

## Report Details
- **Report ID**: 1842114
- **URL**: https://hackerone.com/reports/1842114
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-01-20T16:45:21.445Z
- **Disclosed**: 2023-03-21T13:46:57.708Z

## Reporter
- **Username**: hackit_bharat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team,

I hope you are doing well.

I found a vulnerability in Next cloud , let's exploit

I am not reporting this for every feature in different different report , please increase the severity in single Report. 

Vulnerability Name :- Lack of Rate limit While Generating Backup code , Deleting Account , Profile Updating

Vulnerability Description :- Hi Team , there is no rate limit while sending request to  Generating Backup code , Deleting Account , Profile Updating endpoint that leads to bypass the password protection and even attacker can view current password of user.

Steps to Reproduce :- 1. Signup with an provider and verify your account.
2. Once verified --> Go to Settings --> Security.
3. Click on Generate Backup code , enable password less authentication , Update Profile  it asks for password for authentication.
4. Enter Random Password --> Capture this request n burp suite.
5. Sent this to intruder and select password position and select Payload type as Brute Force.
6. Click on Attack.
7. Boom! On correct password you got response 200 ok and for incorrect you got 403 Forbidden.

Reference Report Next cloud team resolved previously :- #1596673

## Impact

Password protected Authentication Bypass.
2. Attacker able to know the user current password in cleartext and able to takeover the account if they are at same place or someone forgot to logout from public PC also.

POC Attached

If you need further info I am here to help you.
Thanks and Regards,
BhaRat

## Attachments
- Bypasses.mp4
