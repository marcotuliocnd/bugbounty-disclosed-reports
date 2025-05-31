# Rate limit missing at room login

## Report Details
- **Report ID**: 385381
- **URL**: https://hackerone.com/reports/385381
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-07-23T12:48:31.761Z
- **Disclosed**: 2018-09-30T07:42:38.524Z

## Reporter
- **Username**: lucky_sen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Hello there,

User are able to protect there broadcasting with password, so only password granted visitor can login to broadcast room. I notice that rate limit are missing at the endpoint `/roomlogin/user/` which enable me to brute force on password field.

I made 1k+ request but still server not block my request.

##Steps to reproduce:-

1. Create two account A and B. protect A's room with password.
2. Login to B's account and access A's room with random password.
3. Send the request to intruder and run till you get right password

  *  {F323575}

## Impact

Attacker are able to access some one private room.

***Thanks!***

## Attachments
- Screenshot_from_2018-07-23_18-17-18.png
