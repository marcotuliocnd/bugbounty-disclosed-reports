# Lack of cross-origin request blocking allows leaking of sensitive information on several endpoints

## Report Details
- **Report ID**: 350739
- **URL**: https://hackerone.com/reports/350739
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-05-11T22:04:26.203Z
- **Disclosed**: 2018-06-07T01:14:39.203Z

## Reporter
- **Username**: herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
It is possible to make users leak sensitive information on several endpoints by measuring the time certain requests take to be cached.

**Description:**
If a request is made to https://hackerone.com/github/weaknesses and the user is logged in, the size of the response will be around 9kb (because the user both has access and is allowed to report bugs to this program).

If a request is made to https://hackerone.com/notexistent/weaknesses and the user is logged in, the size of the response will be around 1.5kb (because the program doesn't exist/user doesn't have access to it).

Note that an existing program an user has access to returns a different  response size than one that does not exist/he has not access to, and because of this, it’s possible to infer whether certain programs exist by measuring the difference in time each request takes to be cached.

Also, note that this problem isn't exclusive to this endpoint. There are others that could be used to achieve a similar effect, for example:
1. https://hackerone.com/bugs.json?subject=user&reported_to_team=github
2. https://hackerone.com/bugs?subject=github

**Steps to reproduce:**
I created a PoC that will abuse the vulnerability described above to enumerate private programs that the victim has access to. It is also able to enumerate private programs that the victim has been invited to, but has not accepted the invitation yet.

1.  https://lbherrera.github.io/lab/hackerone/private.html
2. Type the name of a private program you have access to on the prompt dialog.
2.  Open the DevTools to follow the attack's execution in real time.

* Maybe you will have to tweak the avg_time variable for it to work given I used one that works on my hardware and didn't implement a function to adjust it to other computers, but it can be done.

## Impact

Attacker can enumerate private programs a victim has access to if the victim accesses the attacker's page.
The attacker's page could be sent to high profile reporters and HackerOne employees given they have access to a large number of private programs in order to abuse the vulnerability to its full potential.

## Attachments
No attachments
