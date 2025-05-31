# CSRF at [Apply to this program] that lead to submit your request automatic with out any validations

## Report Details
- **Report ID**: 334253
- **URL**: https://hackerone.com/reports/334253
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-06T14:21:28.785Z
- **Disclosed**: 2018-07-05T23:09:23.824Z

## Reporter
- **Username**: modam3r5
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi , 
the behavior found in some of programs that need to `Apply to this program` like @hackthedts this program need to your submit Application before start found/send bug to them .
this button have no any validations/check protect for CSRF bug , that can lead to auto apply to program by used this link `https://hackerone.com/hackthedts?apply=true`

#POC 
this CSRF work fine with user that have a tax confirm or had an bounty get before .
1- open this link https://hackerone.com/hackthedts?apply=true
2- if you login-in you will see that your apply has been send successfully , if not login you will redirect to login page then the apply will take a place automatic 
 


### Optional: Your Environment (Browser version, Device, etc)

 * any

this should be an step to confirm the apply or an additional step to be sure what the user/research will do .

## Impact

this can be used to send massive apply with only open link

## Attachments
No attachments
