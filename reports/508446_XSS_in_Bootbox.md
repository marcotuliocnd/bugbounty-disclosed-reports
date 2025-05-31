# XSS in Bootbox

## Report Details
- **Report ID**: 508446
- **URL**: https://hackerone.com/reports/508446
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-03-12T13:44:08.840Z
- **Disclosed**: 2019-05-04T16:52:39.177Z

## Reporter
- **Username**: yonjah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nodejs-ecosystem

## Vulnerability Information
Hi.  
  
Sorry for taking the time with this report.  
  
This is already publicly disclosed issue at -[https://github.com/makeusabrew/bootbox/issues/661](https://github.com/makeusabrew/bootbox/issues/661)  
  
In essence all dialogs of bootbox vulnurable to XSS injections ( bootbox.alert("\<script\>alert(1);\</script\>"); )  

This is apparently a feature to allow injecting HTML in messages but it is not very clear from the documentation.  
Even though this issue has been reported for a while no changes were made to fix this issue or even update the documentation

Kind Regards,  
Yoni

## Impact

Websites using bootbox to display messages containing user input are vulnerable to XSS

## Attachments
No attachments
