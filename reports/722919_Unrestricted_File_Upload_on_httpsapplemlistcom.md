# Unrestricted File Upload on https://app.lemlist.com

## Report Details
- **Report ID**: 722919
- **URL**: https://hackerone.com/reports/722919
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-10-25T16:48:42.885Z
- **Disclosed**: 2020-04-01T09:19:42.564Z

## Reporter
- **Username**: ctulhu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
## Summary:
Hi! i found an Unrestricted File Upload on https://app.lemlist.com which let me upload anything.
File Extensions Such as .html and others should not be executed on the server side.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

* 1.) Login to https://app.lemlist.com
* 2.) Go to Settings >  Email Signature > Click the 3 Dots > Upload File
{F617850}
* 3.) Download {F617851} and Upload it 
* 4.) Right Click and Get the Link of the Uploaded File, Visit the Link.
{F617852}

## Impact

attacker can bypass upload restrictions and deface the page.

## Attachments
- Screen_Shot_2019-10-26_at_12.42.33_AM.png
- page.html
- Screen_Shot_2019-10-26_at_12.45.23_AM.png
