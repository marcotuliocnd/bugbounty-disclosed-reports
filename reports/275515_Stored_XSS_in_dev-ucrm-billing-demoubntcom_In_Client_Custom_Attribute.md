# Stored XSS in dev-ucrm-billing-demo.ubnt.com In Client Custom Attribute 

## Report Details
- **Report ID**: 275515
- **URL**: https://hackerone.com/reports/275515
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-08T15:38:12.215Z
- **Disclosed**: 2017-12-30T13:26:58.038Z

## Reporter
- **Username**: khizer47
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Hey,

Was Testing the subdomins when I came Accross the subdomain https://dev-ucrm-billing-demo.ubnt.com/ I logged in as an Administrator and while testing i added a User and In Client Custom Attribute 1 i added the Payload: `"><IMG src=x onerror=prompt(1);>"">><marquee><img src=x onerror=confirm(3)></marquee>"/` and Save the Client and Then on client page i.e: https://dev-ucrm-billing-demo.ubnt.com/client/24 When User click on Show more (under Custom Attribute 1) The XSS payload executes :) 

{F227283}

{F227284}

If another Admin or A user will perform the steps to see the custo atributes his/her account can be takenover By Such Pentest XSS By using tools like https://xsshunter.com/app etc :) 


## Attachments
- 0111.JPG
- dev_ucrm-Billing-demo_XSS.JPG
