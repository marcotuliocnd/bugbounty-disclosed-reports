# Sensitive Information Disclosure https://cards-dev.twitter.com

## Report Details
- **Report ID**: 268888
- **URL**: https://hackerone.com/reports/268888
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-16T13:43:53.639Z
- **Disclosed**: 2017-09-29T23:07:06.666Z

## Reporter
- **Username**: hassham
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Dear Twitter Team, 

While researching through one of your domain cards-dev.twitter.com i discovered that the host is disclosing sensitive information when a user browses to a specific directory  
https://cards-dev.twitter.com:443/keys/.

The application downloads a file json.json which discloses the following information
`"customer_key":"████"` 
`"customer_secret":"█████████"`
`"jira_password":"██████"`

I am checking that can this information be used to further escalate any vulnerability. 

Regards, 


## Attachments
- keys.png
