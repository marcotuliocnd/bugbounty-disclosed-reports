# many commands can be manipulated to delete identities or affiliations

## Report Details
- **Report ID**: 348090
- **URL**: https://hackerone.com/reports/348090
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-07T06:47:29.590Z
- **Disclosed**: 2022-08-10T14:23:14.558Z

## Reporter
- **Username**: cet2000
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: hyperledger

## Vulnerability Information
**Introduction:**

The Faric-ca  data in http body and authorization header for many commands that send from client to server are protected by signature.  

But I find the identity and affiliation commands still have the risk to be manipulated. Hacker can manipulate most other commands to delete identities or affiliations in a server (server start with –cfg.identities.allowremove and –cfg.affiliations.allowremove). 

Example 1: Manipulating list an identity command to delete any identity or affiliation. 
{F294541}
normal list identity command

you can manipulate it:

{F294542}
Manipulate the list command to delete command

If a hacker gets the request http data (maybe by sniffer), he can manipulate the GET method to DELETE method, and change the admin3 identity to any other valid identity in the server, he can delete it. 


Example 2: Manipulating add an identity command to delete an identity or affiliation. 
{F294543}
normal add an identity command

you can manipulated:
{F294544}
Manipulate the add identity command to delete an identity

or you can manipulated as:
{F294545}
Manipulate the add identity command as delete an affiliation command


Actually, you can also manipulate other commands by this way. Such as: enroll, revoke,register… and so on. 



**Analysis:**

The authentication and authorization checking just covers the Authorization header and body, 
but the code for deleting identity and affiliation gets the identity value and affiliation value from **url path**. They are not protected by signature. And you can manipulate the method from other to DELETE.  

**DELETE** /affiliations/**org1.dep2**?force=true HTTP/1.1
**DELETE** /identities/**admin2** HTTP/1.1

## Impact

If a hacker get any of the normal request data by some way (maybe by network sniffer), he can delete all identities or affiliations.

## Attachments
- identities_list.png
- identitie_list_delete.png
- identities_add.png
- identities_add_delete.png
- identities_add_delete_affi.png
