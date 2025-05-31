# Missing rate limit in current password change settings leads to Account takeover

## Report Details
- **Report ID**: 1170522
- **URL**: https://hackerone.com/reports/1170522
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-04-21T09:38:06.399Z
- **Disclosed**: 2021-10-27T14:12:10.275Z

## Reporter
- **Username**: m0hacks
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary:
Happy Wednesday,

I've found a missing rate limit protection in https://reddit.com and https://vip.reddit.com in password change settings. Enter the current password security mechanism is implemented to prevent the the cyber attackers not to change the password without knowing the current password however due to lack of rate limiting at change password page this security strict can be bypassed by brute forcing.

## Steps To Reproduce:

  1. Login to https://reddit.com/
  2. Navigate to user settings > Change password
  3.  Enter incorrect password in old password field and enter a new matching passwords in other two fields
  4. Turn on your burpsuite proxy and click save  
  5. You'll notice the error as Incorrect password
  6. send the request https://www.reddit.com/change_password to your burpsuite intruder to bruteforce
  7. Add the payload to the current_password parameter 
  8.  select list of passwords for like 100 lines and start attack

Note: The similar method is followed with https://vip.reddit.com too. PoC images of both the Brute-force succeeded domains have been attached.

Thank you

## Impact

This can lead to an Account takeover due to no rate limitation in "current password change settings" in reddit.com and vip.reddit.com. A cyber attacker can bruteforce for account password continuously till he succeed. As you can see in the PoC image Cyber Attacker succeeded the bruteforce in 101st attempt for both the domains.

## Attachments
- br2.cleaned.png
- bruu.cleaned.png
