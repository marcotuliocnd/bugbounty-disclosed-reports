# No filteration of null characters in name field

## Report Details
- **Report ID**: 242945
- **URL**: https://hackerone.com/reports/242945
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-06-24T22:20:00.883Z
- **Disclosed**: 2017-07-27T11:51:03.039Z

## Reporter
- **Username**: blake12356
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hello,

##Description:
The account settings page, https://demo.weblate.org/accounts/profile/#account, allows a user to set their username as a null character! A user intercepts the request using a proxy and changes the user name field to %00. 

##Mitigation:
I recommend you have filtering of null characters on your account settings page.

Thanks!




## Attachments
No attachments
