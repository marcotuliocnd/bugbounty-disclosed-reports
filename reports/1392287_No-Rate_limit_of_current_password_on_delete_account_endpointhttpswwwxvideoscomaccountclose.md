# No-Rate limit of current password on delete account endpoint(https://www.xvideos.com/account/close)

## Report Details
- **Report ID**: 1392287
- **URL**: https://hackerone.com/reports/1392287
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-11-05T11:02:31.928Z
- **Disclosed**: 2021-11-23T11:02:21.168Z

## Reporter
- **Username**: rawat_16
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: xvideos

## Vulnerability Information
Hi Team!!!
This Attack happen when victim login in other device and forget to logout ,Then attacker can delete  it's account by brute force the current password because current password has no-rate limit.
After guessing current password attacker can easily delete the victim account.
Steps To Reproduce:
1.Login in https://www.xvideos.com/ with right credentials
2.Navigate to Dashboard --> Account->  Delete my account and Personal Data
3.add random password in current password field 
4.Capture the request and send it for fuzz
you get a different response when you enter a right password.

****  Response in right password :-
            Too fast. Please try again in few seconds

           Response of wrong password :-
          Too fast. Please try again in few seconds is missing.

POC - I have attached a video poc in which I demonstrate the attack.

## Impact

As Attacker I can delete victim account by brute force the victim current password, Due to no-rate limit on this endpoint.

## Attachments
- xvideo_delete.mp4
