# Organization Admin Privilege Escalation To Owner

## Report Details
- **Report ID**: 272570
- **URL**: https://hackerone.com/reports/272570
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-28T01:05:19.847Z
- **Disclosed**: 2017-10-28T02:53:06.142Z

## Reporter
- **Username**: rhynorater
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bitwarden

## Vulnerability Information
##Summary
It seems there is an issue with your roles which allows an admin to escalate his own privileges to owner and takeover the organization. 

##Reproduce
1. Create an account, accountA
2. Create another account, accountB
3. Create an organization under accountA and invite accountB to that organization as admin
4. Accept invitation with accountB and log out
5. Confirm accountB for the organization on accountA
6. Log in with accountB
7. Navigate to the organization -> invite users -> edit accountB user and change to owner
8. See that the change worked and accountB is now owner. 
9. To proceed with organization takeover, remove the original owner
10. Note that (after login and logout) the original owner no longer is in the organization

##Impact
Anyone who is an admin on an organization can take total control of the organization and kick the original owner out. 

##Request
Could you please whitelist ip 173.167.43.57 and ip 54.197.209.98 so that I can keep reporting? It is very hard to fully test the application while I am constantly getting blacklisted and having to use my phone as a hotspot :P If not, that's cool, just figured I'd ask :)


Thanks,
Justin Gardner

## Attachments
No attachments
