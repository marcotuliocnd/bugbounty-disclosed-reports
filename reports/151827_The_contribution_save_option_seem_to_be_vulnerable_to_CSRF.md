# The contribution save option seem to be vulnerable to CSRF

## Report Details
- **Report ID**: 151827
- **URL**: https://hackerone.com/reports/151827
- **State**: Closed
- **Severity**: none
- **Submitted**: 2016-07-16T21:57:46.306Z
- **Disclosed**: 2016-07-17T15:14:38.881Z

## Reporter
- **Username**: roshanpty
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
The application is vulnerable to Cross Site Request Forgery
====================

Description
---------------------
The option in the application to save weekly contribution for a project is vulnerable to Cross Site Request forgery. 
**Note:** I am unable to perform the action itself normally. But it is obvious that the application uses no protection against CSRF and the token named **csrf_token** is being passed in the cookie instead of a post parameter or HTTP header. 

Detailed Steps:
---------------------
**Step 1:** Open a project and modify the weekly contribution for the same. 
{F105367}
**Step 2:** Send the request to save the modified value.
{F105368}
**Step 3:** It can be observed that no kind of CSRF protection is employed and the request can be recreated in the following URL format. If anyone clicks on the link in a browser where they are already logged in to gratipay, the amount will be automatically updated.
https://gratipay.com/<project>/payment-instruction.json?amount=<amount>

## Attachments
- 2016-07-16_17_50_20-Passwork_-_Gratipay.png
- 2016-07-16_17_51_39-Program_Manager.png
