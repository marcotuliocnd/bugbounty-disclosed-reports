# sql injection vulnerablity found

## Report Details
- **Report ID**: 211988
- **URL**: https://hackerone.com/reports/211988
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-03-09T14:44:54.357Z
- **Disclosed**: 2017-10-13T18:46:52.692Z

## Reporter
- **Username**: bd_01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: legalrobot

## Vulnerability Information
a Blind Text Injection Differential vulnerablity was found on your site in the url :https://www.legalrobot.com/assets/icons 

a GET request made on GET /assets/icons/?v=9wr1emhXD568%3B'%20UNION%20SELECT%208%2C%20table_name%2C%20'vega'%20FROM%20information_schema.tables%20WHERE%20table_name%20like'%25 result up in vulnerablity


## Attachments
- Screenshot_at_2017-03-09_20-12-15.png
