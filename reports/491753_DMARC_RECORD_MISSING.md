# DMARC RECORD MISSING

## Report Details
- **Report ID**: 491753
- **URL**: https://hackerone.com/reports/491753
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-02-06T05:55:05.627Z
- **Disclosed**: 2019-02-13T18:59:01.401Z

## Reporter
- **Username**: hackthedevil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
VULNERABILITY TYPE- DMARC RECORD MISSING.
HOW TO REPRODUCE(POC-ATTACHED IMAGE):-
1.GO TO- https://mxtoolbox.com
2.ENTER THE WEBSITE(brave.org).CLICK GO.
3.YOU WILL SEE THE FAULT(No DMARC Record found)
4.In the new page that loads change MXLookup to DMARCLookup
I HAVE ALREADY INFORMEDD THEM.THEY TOLD TO OPEN THE ISSUE IN HackerOne.(POC-ATTACHED IMAGE)

## Impact

Spammers can forge the "From" address on email messages to make messages appear to come from someone in your domain. If spammers use your domain to send spam or junk email, your domain quality is negatively affected. People who get the forged emails can mark them as spam or junk, which can impact authentic messages sent from your domain.

## Attachments
- brave_contact.png
- brave_contact2.png
- brave_DMARCLookup.png
- brave_MXLookup.png
