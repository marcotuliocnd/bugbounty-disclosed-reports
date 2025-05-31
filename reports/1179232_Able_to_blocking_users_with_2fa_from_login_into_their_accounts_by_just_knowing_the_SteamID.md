# Able to blocking users with 2fa from login into their accounts by just knowing the SteamID

## Report Details
- **Report ID**: 1179232
- **URL**: https://hackerone.com/reports/1179232
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-29T02:30:17.028Z
- **Disclosed**: 2023-12-14T18:55:58.977Z

## Reporter
- **Username**: benjamin-mauss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
Hi, team!

## Summary:
By changing the steamID cookie on confirm 2fa code request, I am able to block the login of an account with 2fa for 5 minutes (300 seconds).
So I am able to block users with 2fa from login into their accounts by just knowing the SteamID.

## Steps To Reproduce:

  1. Login into your account with 2fa. 
1. Get the request to confirm the 2fa code.

{F1282394}


```http
POST /login/confirm HTTP/1.1
Host: cs.money
Content-Length: 28
Connection: close
Cookie: steamid=<victim_steam_id>;

{"token":"foo","code":"foo"}
```

2. Change the cookie steamid to the victim one.
3. Repeat the request 4 times (4 wrong codes).

-------

█████

## Impact

I hacker could block everyone with 2fa from login into cs.money.

## Attachments
- Screenshot_71.png
