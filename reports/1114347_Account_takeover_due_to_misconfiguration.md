# Account takeover due to misconfiguration

## Report Details
- **Report ID**: 1114347
- **URL**: https://hackerone.com/reports/1114347
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-03-02T05:46:13.770Z
- **Disclosed**: 2021-09-17T05:19:55.583Z

## Reporter
- **Username**: akashhamal0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
## Summary:

HI team, i hope you are good :)

Its a very simple logical flaw that results in this

So suppose we are victim@gmail.com , now login into the website then

1. go to account settings and then change mail address to victim111@gmail.com
2. a link will be sent to victim111@gmail.com, now the user realizes that he have lost access to victim111@gmail.com due to some reasons 
3. so he will probably change mail to the another mail address for e.g victim999@gmail.com which he owns and has access to
4. but it is found that even after verifying victim999@gmail.com, the old link which was sent to victim111@gmail.com is active, so user/attacker having access to that mail can verify it and takeover acc


In a nutshell : 

It is mandatory for a web app to invalidate the tokens in time to secure its user 

In this case, suppose while changing mail address the user mistakenly typed wrong mail address, so the link will be sent to that mail address. 

So the user probably don't want the user of that mail address to verify it, so he will quickly change his mail address to one he owns and verify it

what he doesn't know is that even after verification(change of major state), the old link is still active 

the flaw :

user changes mail to attacker@gmail.com -> user realizes that he mistyped the mail -> so he again changes to mail he owns and verifies it -> old link sent to attacker@gmail.com is still active even after new mail has been verified

## Impact

An attacker can takeover acc due to misconfiguration, not invalidation of tokens at major state change, in time

## Attachments
No attachments
