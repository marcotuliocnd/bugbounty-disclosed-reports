# Missing brute force protection for passwords of password protected share links

## Report Details
- **Report ID**: 1894653
- **URL**: https://hackerone.com/reports/1894653
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-03-07T04:33:46.940Z
- **Disclosed**: 2023-04-25T09:32:28.295Z

## Reporter
- **Username**: hackit_bharat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi Team,

I hope you are doing well.

Vulnerability Name :- Bypass Password of Shared Files due to Lack of Rate Limit

Vulnerability Description :- Hi Team, I found a vulnerability in which I am able to bypass password protection of shared files due to lack of Rate limit.

Vulnerable URL :- https://efss.qloud.my/index.php/s/7ARMkjXJXAEz2kr

Steps to Reproduce :- 1. Login --> Go to Files --> Set Password.
2. Copy Shared Link.
3. It looks like :- https://efss.qloud.my/index.php/s/7ARMkjXJXAEz2kr
4. Open it in other browser .
5. It asks for password .
6. Enter random password.
7. Capture this request in burp suite.
8. Send to intruder and select that position and paste the payload list.
10. Click on start attack and Boom! after few mins it got bypassed with Response code 303.

## Impact

It leads to bypass the password of protected share files.

POC Attached

If you need further info I am here to help you.

Thanks and Regards,
BhaRat

## Attachments
- Shares_bypass.mp4
