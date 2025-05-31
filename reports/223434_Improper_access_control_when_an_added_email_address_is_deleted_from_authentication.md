# Improper access control when an added email address is deleted from authentication

## Report Details
- **Report ID**: 223434
- **URL**: https://hackerone.com/reports/223434
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-24T12:58:41.254Z
- **Disclosed**: 2017-05-17T14:07:28.760Z

## Reporter
- **Username**: h1bountyoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi team,

There is improper access control kind of vulnerability present in your web application.


Steps to reproduce:

1. Create an account.
2.You will recevie a link on email about confrimation.
2. Login into it and add another email address in authentication tab and You will recevie a link on the new email about confrimation.
3.Remove the the any email address from it authentication tab. (Suppose your old email address got lost or hacked).

Now suppose I removed old email address from authentication tab because i doubt the my old email id got hacked.

Logically when user click on the link recived in the step 2 the user should not be allowed to enter in the application because we have removed the email from authentication tab.

When attacker click on the old link recieved in the step 2 will be able to login into the application and the old email id will be automatically added to authentication tab in that account even the we have alredy removed that email address from our account.


Please let me know if anything more is required .!



## Attachments
No attachments
