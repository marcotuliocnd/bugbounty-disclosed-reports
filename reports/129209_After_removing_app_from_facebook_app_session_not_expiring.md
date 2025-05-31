# After removing app from facebook app session not expiring.

## Report Details
- **Report ID**: 129209
- **URL**: https://hackerone.com/reports/129209
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-08T09:52:59.847Z
- **Disclosed**: 2017-08-21T13:33:08.401Z

## Reporter
- **Username**: lilly
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
When a user login with facebook 0Auth and then he removes the app from facebook app setting the session is not expiring.
Poc:-

Step1: Go to gratipay login page.
Step2: Click on login with facebook 0 auth and login with facebook.
Step3: Go to facebook then app setting.
Step4: Now remove the gratipay app from here and go back to gratipay site.
Step5: You will see that you are still logged in.

Hence session is not expiring so it is vulnerable.

Thanks
Sushil Saini (Cyber Security Researcher)

## Attachments
No attachments
