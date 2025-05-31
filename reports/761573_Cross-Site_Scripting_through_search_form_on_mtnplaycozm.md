# Cross-Site Scripting through search form on mtnplay.co.zm

## Report Details
- **Report ID**: 761573
- **URL**: https://hackerone.com/reports/761573
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-19T10:13:18.267Z
- **Disclosed**: 2021-06-08T05:40:47.001Z

## Reporter
- **Username**: droop3r
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
There is a XSS vulnerability that can be triggered through a search form on mtnplay.co.zm

## Steps To Reproduce:
  1. Navigate to http://www.mtnplay.co.zm/smart/jqm.aspx
  2. Click on the search button (or go to this link: http://www.mtnplay.co.zm/smart/jqm.aspx?event=search&mnu=search&ctrlid=92)
  3. Click on the filter button 
  4. The XSS can be triggered in any field of that form by inputting a javascript payload (Track/Album/Artist)

## Demonstration: 
https://www.youtube.com/watch?v=doLHsUqnvgE

## Impact

Malicious javascript code can be injected into the application

## Attachments
No attachments
