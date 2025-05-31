# If rate limit is hit, IP address is leaked to anyone who tries to login

## Report Details
- **Report ID**: 1989901
- **URL**: https://hackerone.com/reports/1989901
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-05-16T20:20:32.919Z
- **Disclosed**: 2023-09-20T12:21:58.777Z

## Reporter
- **Username**: anish-kosaraju
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
After the rate limit on https://bugzilla.mozilla.org/home on the login page is hit, bugzilla blocks the ip address. The next time someone logs in from any ip address, mozilla will say that the account has been locked and will list the ip address which broke the rate limit (which could be the user's).
This is the message that shows up: █████

## Steps To Reproduce:

  1. Activate the rate limit by getting 30+ wrong passwords. You can do an intruder attack with around 50 wrong passwords and when the attack stops without all the payloads going through, you know that the rate limit has been hit.
  2. Now, go to another tab from another ip address (using a vpn) and try to login (it doesn' t matter if it is the correct password or not). You will see the previous address you tried to login from as shown in the screenshot above.

## Supporting Material/References:
██████████

**Remediation**
Just say that the account has been locked due to excessive attempts. If you want to inform the user that this is happeneng, just email the ip address to them saying that there were too many requests coming in from that address.

## Impact

If a user logs in too many times and the rate limit is hit, an attacker who may try to attack the account will see the ip address of the user.

## Attachments
No attachments
