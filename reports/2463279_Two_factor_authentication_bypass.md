# Two factor authentication bypass

## Report Details
- **Report ID**: 2463279
- **URL**: https://hackerone.com/reports/2463279
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-04-15T07:06:17.718Z
- **Disclosed**: 2024-07-11T15:18:55.046Z

## Reporter
- **Username**: pranshux0x_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Two factor authentication bypass means. We have access to victim email and password. But we don't have access to 2fa code. So somehow we have to bypass 2fa code requirement.
so what I do here.
I had access to victim email that is used in his hackerone account. 
Victim also deactivate his account
I find out that when  user deactivate his account. Then reset his password and login again ,  2fa removed. 

**Description:**

### Steps To Reproduce

#### As a victim
- Login to your hackerone account
- Turn on your two factor authentication. 
- Deactivate your account

#### As an attacker
- You have access to victim email
- Forgot victim password on hackerone, because you have access to victim email you can do this easily.
- Now login with new password on hackerone , you will see 2fa removed completely.

## Impact

Impact is quite high two factor authentication bypass.

## Attachments
No attachments
