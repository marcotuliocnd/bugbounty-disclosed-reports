# Two email addresses can access the same account

## Report Details
- **Report ID**: 245305
- **URL**: https://hackerone.com/reports/245305
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-07-02T10:48:40.090Z
- **Disclosed**: 2017-07-03T06:55:29.972Z

## Reporter
- **Username**: streaak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Hello Team,

When I was testing your web application I found that we can change the email address to a new email address.  I tested that feature and noticed that after changing the email to a new email and then back to the old email, I can still access the account using both the email addresses.  
Doing so doesn't allow the email holder of the second email address to create an account on Wakatime using the same email address, as the error shows that the email address has already been taken. I presume that this can be done for a number of emails as I haven't tested that yet. 
One account clearly shouldn't be accessible by 2 email address and is a violation of secure design principles.

Let me know if you need anything else. 

Best Regards,
Streaak2

## Attachments
No attachments
