# User account blocking by Internal Server error

## Report Details
- **Report ID**: 451052
- **URL**: https://hackerone.com/reports/451052
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-11-28T13:26:59.500Z
- **Disclosed**: 2018-12-28T14:45:39.029Z

## Reporter
- **Username**: marataziat
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
If you send a language[]=en in https://infogram.com/api/users/me user be forever get an Internal Server error ( EVEN AFTER re-logining):
https://youtu.be/AxYa11lEiWA
(I idk why does hackerone can't upload this video so I uploaded this video privately to the youtube!) 
In this video, I'm trying to relogin to the my another account that also was exploited by this vulnerability and I'm getting the same error! https://youtu.be/1mihr5_oe3s 

It's like a permanent ban! And if that can be exploited by CSRF it becomes more dangerous because the user can just go to some page like inex.html (F381888)! I don't know if it is 100% possible to exploit by CSRF because I have blocked all my two accounts by using this issue! But the browser network tools shows that it's possible to exploit it by CSRF here the video https://youtu.be/5TliXljf4V4 !

## Impact

An attacker can permanently ban any user by exploiting this vulnerability using CSRF!

## Attachments
- index.html
