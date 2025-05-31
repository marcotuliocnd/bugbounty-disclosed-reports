# Emails of invited collaborators are disclosed in full in payload for report participants

## Report Details
- **Report ID**: 269230
- **URL**: https://hackerone.com/reports/269230
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-18T14:20:15.669Z
- **Disclosed**: 2019-04-09T16:00:34.467Z

## Reporter
- **Username**: flashdisk
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hackerone added new feature in which hackers can add collaborators to their reports.
this can be done using two ways: 
 1. by email address
 2. by user name  
adding hackers using their email address doesn't disclose the email address of the hacker and every participant will see something like this in the comments section of the specific report:

```
flashdisk  invited m.*************************om as a collaborator.
```
 
but moving the mouse pointer over the hacker icon would reveal his email address to all participants for that report which is definitely should hidden.  

#Fix

the email address should be hidden also in the upper report section.
please look at the attached screenshot which discloses my email address:

{F221867}

 
thanks.

## Attachments
No attachments
