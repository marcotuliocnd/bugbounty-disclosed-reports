# Improper validation of Email 

## Report Details
- **Report ID**: 226334
- **URL**: https://hackerone.com/reports/226334
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-05-05T13:32:49.376Z
- **Disclosed**: 2017-05-07T06:08:41.464Z

## Reporter
- **Username**: test_this
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
1.goto https://bridge.cspr.ng/my/account
here no rate limit present for email and display name,real name
i just entered 1000 character length email in email field and it accepted

also for the display name ,real name

another 
there is no regular expression to check valid email 
if u give email as "aaaaaa", "a++++++++", "vdadva*$'/@4%$123", "sdfsjghg@something" all will be accepted as valid email
Also 500+ character email also valid according to your code
here is the specification for email address
https://en.wikipedia.org/wiki/Email_address
and email id must be <254 character 

as email id strored in mysql as VARCHAR(128), 
so all the trailing character in mysql db will be truncted
if your email like abc@gmail.com and you entered as abc+aaaaaaaaaaaaaaaaaa......@gmail.com,then still you receave email in abc@gmail.com
MITIGATION:
 you must use filter_var($email, FILTER_VALIDATE_EMAIL) to validate email
or use Regex like /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/

## Attachments
- Screenshot_-_May_5__2017_7.09_PM.png
