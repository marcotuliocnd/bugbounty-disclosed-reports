# Wrong Url in Main page of sifchain.finance

## Report Details
- **Report ID**: 1195512
- **URL**: https://hackerone.com/reports/1195512
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-13T10:32:40.875Z
- **Disclosed**: 2021-12-09T17:50:02.852Z

## Reporter
- **Username**: beebeek
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
Hello Sifchain team,

I found that all the social media button is working properly except telegram button on the main page of sifchain.finance 
Misconfiguration on button can create bad reputation of a company as well as a genuine customer could not reach to a company through the mis-configured button of telegram. 

Step to reproduce: 
1) Navigate to sifchain.finance and go to bottom left of a page then right click on first social media icon and click on open new tab. 
2) Redirected to  " address  wasn't understood" error message . 
POC attached below.

## Impact

Bad reputation and cannot interact with custom through link. 

Remediation: Using a valid link on the icon.

## Attachments
- siffff-2021-05-13_16.08.31.mp4
