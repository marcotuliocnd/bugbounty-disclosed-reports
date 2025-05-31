# bypass to csv injection

## Report Details
- **Report ID**: 161290
- **URL**: https://hackerone.com/reports/161290
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-19T11:48:57.148Z
- **Disclosed**: 2016-09-27T21:45:51.962Z

## Reporter
- **Username**: superngorksky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: iandunn-projects

## Vulnerability Information
Hi Ian,
I would like to add payload to this report #151516.  
payload used:
http://google.com?,=2+2-2+3+cmd|' /C calc'!G2

When injecting https://google.com? it will be rendered as a link but when comma (,) it will be rendered in a new cell which will execute the command.

Thanks,


## Attachments
No attachments
