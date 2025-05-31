# The Federalsit session cookie (federalist.sid) is not properly invalidated - backdoor access to the account is possible

## Report Details
- **Report ID**: 250688
- **URL**: https://hackerone.com/reports/250688
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-07-17T22:40:51.946Z
- **Disclosed**: 2017-09-05T19:47:58.630Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hello. This issue is not very dangerous itself, but can be dangerous in combination of others (like XSS, or malicious access to the user account). The user/attacker, who got once valid cookie `federalist.sid` from the account, can use it as backdoor for some time, because it is not actually invalidated on Logout. Also, i discovered, that privilege escalation is possible (it is possible to attack another user account in some cases). Actually, logout just invalidating GitHub access token, but session still can be valid. How it can be used by attacker, or malicious user? Let's see the POC below.

##POC
Case 1. Using the flaw as BackDoor access to the account.
1) Login to the Federalist instance with your test account.
2) Save the `federalist.sid` cookie from the `/v0/me` endpoint using Burp or similar Web Debbuger.
3) Do logout.
4) Replay the request to the `/v0/me` endpoint using web debugger with same cookie. You will got 403 forbidden, as it should be.
5) Login with same account.
6) Replay the request to the `/v0/me` endpoint using web debugger with same cookie. You will got success response.
Case 2. Using the flaw (same session value) as BackDoor access to the account of another user.
Continue testing from the last step.
7) Do logout again.
8) Login with the second test account.
9) Replay the request to the `/v0/me` endpoint using web debugger with same cookie from previous steps. You will got success response, and info about users.

##Impact
Exploitation scenario.

Lets suppose, that some Federalist user worked on his PC, and did logout from Github and Federalist. It is supposed, that malicious user can't access his account without GitHub credentials. But, because `federalist.sid` was not invalidated properly, it is only a temporary restriction for the attacker. Let's suppose, that attacker somehow got `federalist.sid` cookie (using XSS, physical access to the PC, or attacker was previously the legit user, and saved cookie for the future access). He can't access the API just now, (as it throws 403), but he will can, when the login action will be performed on that PC again. Session will become valid, and, not matter, which user did the login! For example, if the second user logged in to the Federalist from different account, old `federalist.sid` will be assigned to him, and attacker's backdoor `federalist.sid` will work for the another account!
Sure the session cookie has limited lifetime, but still, insufficient invalidation can pose some risks.

##Suggested fix
1. The session cookie should be destroyed on user logout.
2. The new session cookie should be established on login.

## Attachments
No attachments
