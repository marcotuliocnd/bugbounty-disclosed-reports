# Session Not Expire / 2FA Bypass

## Report Details
- **Report ID**: 2469706
- **URL**: https://hackerone.com/reports/2469706
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-18T14:32:41.909Z
- **Disclosed**: 2024-07-11T15:16:46.739Z

## Reporter
- **Username**: blackflyhunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello Security Team,
I hope you are having a good day!

The attacker can use the victim cookie to log in victim's account and if a victim clears her browser history victim can be logged out of her account but the attacker use the victim's previous session cookies and log in multiple times an attacker can still log in the account again and again

## Steps To Reproduce:
1. attacker stole the cookies of victims through any means - https://hackerone.com/ {{attacker perspective}}
2. Victim clears their browser history  {{Victim perspective}}
3. attacker add victim cookies using  http://www.editthiscookie.com addon to own browser {{attacker perspective}}
4. Victim login their browser again using email password (Victim created a new session but the old session has not expired)
5. The attacker could still log in victim's hackerone account again. {{attacker perspective}}


## POC: (Recommended)
███████

## Impact

1. The session does not expire 
2. 2FA Bypass

## Attachments
No attachments
