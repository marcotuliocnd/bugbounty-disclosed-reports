# Open Redirection while saving User account Settings 

## Report Details
- **Report ID**: 288219
- **URL**: https://hackerone.com/reports/288219
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-11-07T18:15:35.477Z
- **Disclosed**: 2017-11-15T09:05:40.611Z

## Reporter
- **Username**: 0xprial
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: moneybird

## Vulnerability Information
Hi team ,
I got a Open redirection while saving account setting . This could lead to serious issues .

**Endpoint :-** https://moneybird.com/user/edit?return_to=//evil.com

##Reproduce :-
* Visit https://moneybird.com/user/edit?return_to=//evil.com and click on `Save` .
* You will be take to evil.com .

##Impact :-
Attacker can redirect a user to a fake login page easily to get his login and other sensitive infos .

Thanks .

## Attachments
No attachments
