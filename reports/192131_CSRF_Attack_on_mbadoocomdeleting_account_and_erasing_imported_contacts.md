# CSRF Attack on (m.badoo.com)deleting account and erasing imported contacts

## Report Details
- **Report ID**: 192131
- **URL**: https://hackerone.com/reports/192131
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-18T05:44:48.620Z
- **Disclosed**: 2017-02-06T21:16:54.310Z

## Reporter
- **Username**: tikoo_sahil
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Hello ,

##Summary :-
I would like to report a __Csrf__ bug that i found today that can cause deletion of any victim's account and also I was able to __erase all imported contacts of victim__ on sub-domain--->_m.badoo.com_ . 

When attacker send a crafted malicious html file to victim and as soon as the victim opens the file and clicks on submit button(I m using submit button for demonstration purposes) , a delete _POST_ request is made to m.badoo.com and the account of victim gets deleted. In a much similar way i was able to make an html file that when opened up by victim would erase victim's all imported contacts. (Note--->victim must possess an active session).

##Reproduction steps :-

>>Basically when i was capturing the request and response http headers in burpsuite , it basically caught my eye that there was no use of csrf token being implemented here, so I crafted two html files one for erasing imported contacts and another one for deleting accounts on m.badoo.com . Also , as the content-type was __json__ so parser introduced "=" at the end of content in header, but it was bypassed by adding _"ignore_me":"' value='test"._ 

1) Create 2 html files one for deletion and one for erasing contacts(both files have been attached)
2)send the html file to victim(victim should have an active session)
3)after clicking the submit button in both the html files , one will lead to deletion and other one erasing victim's contacts.

Below images describe the results  :-

1) results of deleting account --->

{F144646}

2) results of erasing contacts --->

{F144647}

## Attack Scenario  and Patch :-

Attack scenario can be critical as an attacker would be able to delete and erase contacts of any person who has an account on m.badoo.com sub domain  . Patch for the above scenario can be using __CSRF token__ that must be random and keep on changing for every outgoing request to m.badoo.com 

##Proof-Of-Concept:-

_I have attached html files , image poc for the above attack scenario_

Video PoC demonstration :- I have uploaded an unlisted video on youtube , here is a link :-  https://youtu.be/rWm1RGXyK7I

regards
tikoo_sahil




## Attachments
- delete_account(csrf).png
- erase_contacts(csrf).png
- badoo(delete).html
- badoo(erase_contacts).html
- badoo(delete).html
