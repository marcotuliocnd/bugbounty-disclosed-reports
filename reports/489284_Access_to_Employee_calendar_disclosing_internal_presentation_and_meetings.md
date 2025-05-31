# Access to Employee calendar disclosing internal presentation and meetings

## Report Details
- **Report ID**: 489284
- **URL**: https://hackerone.com/reports/489284
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-31T20:20:27.307Z
- **Disclosed**: 2019-03-08T21:22:29.145Z

## Reporter
- **Username**: commandersnuggle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
**Summary**

During a school research, we found out that some Shopify employees have their google calendar set to public. This discloses some sensitive informations: 

* New hire information ( due to onsite interviews )
* Internal presentation ( we found at least one internal presentation that we could access )
* Zoom meetings link - These meetings can be accessed without login which puts a lot of internal information at risk. 


**Description**

For the analysis of this, we used Hunter.io's API to get list of all @shopify.com emails that it had (this does not mean we queried every existent shopify.com emails). After we had done that, we ran it through a Google Calendar feature that allows adding other people's calendar. While some email did not exist anymore and some had private calendar, we found one employee█████████that had the calendar public. 

_Joining meetings_
{F415901}

As you can see one of the meeting that we show in the above image has a Zoom link. Based on our research, we can confirm with 100% certainty that anyone can join this meeting without logging in. Which means at 3PM PST an attacker who has this info can join the meeting and potentially gather sensitive information.  Specially this meeting seems to be one for handling `difficult tickets` which could have customer information on it. 

_Interviews_
{F415902}

Additionally as the image above shows, looking up `interview` gives list of some old on-site interviews. 

_Presentations_

We also found access to an internal presentation through this person's calendar. This presentation has now been locked down. The link of the presentation was: ███████

**Asking for permission**
While this might be a little too much to ask, we want to see if Shopify is fine with us joining the 3PM meeting to take a quick screenshot of anyone who would be in the meeting. If not, we can share a redacted picture of another meeting we joined for another company (Not shopify) to show that it is possible. 

Cheers,
@commandersnuggle & @rijalrojan

## Impact

Access to private information of company meetings, interviews etc.

## Attachments
No attachments
