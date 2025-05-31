# Stored xss 

## Report Details
- **Report ID**: 149154
- **URL**: https://hackerone.com/reports/149154
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-04T09:19:09.496Z
- **Disclosed**: 2016-08-03T14:55:35.760Z

## Reporter
- **Username**: sysecure
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Hi ,i have found an xss issue here : https://www.algolia.com/explorer#?index=test&tab=ranking
Steps to reproduce :
1-Go to : https://www.algolia.com/explorer#?index=test&tab=ranking
2-At the Attributes to index add this script  :`"><img src=x onerror=prompt('XSS');> ` and press enter .
3-Click save 
You will see that the xss has been fired .
You can go to https://www.algolia.com/explorer#?index=test&tab=ranking again you will see that xss is fired again .

Thanks ,
Saleh

## Attachments
- Screenshot_(107).png
- Screenshot_(108).png
- Screenshot_(109).png
