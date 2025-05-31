# Stored XSS through Facebook Page Connection

## Report Details
- **Report ID**: 267570
- **URL**: https://hackerone.com/reports/267570
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-09-11T16:42:06.454Z
- **Disclosed**: 2020-04-04T14:56:46.377Z

## Reporter
- **Username**: boredengineer21
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
The following URL
https://kitcrm.com/users/122686/connections
displays us options to connect our several social networking accounts to kitcrm.
Once i connect my facebook account, the facebook section in above link will list out all my facebook page and will give me an option to select a business page. 
One of my facebook page name is "><img src=x onerror=alert(9)>
F220032: Screenshot from 2017-09-11 22-23-23.png 54.6KB 

Now when i click on that drop-down option an alert will pop-up.
F220033: Screenshot from 2017-09-11 22-25-20.png





## Attachments
- Screenshot_from_2017-09-11_22-23-23.png
- Screenshot_from_2017-09-11_22-25-20.png
