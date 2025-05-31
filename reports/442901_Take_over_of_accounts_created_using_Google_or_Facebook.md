# Take over of accounts created using Google or Facebook

## Report Details
- **Report ID**: 442901
- **URL**: https://hackerone.com/reports/442901
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-11-16T20:54:56.443Z
- **Disclosed**: 2019-05-17T03:36:27.301Z

## Reporter
- **Username**: tomoh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
When a user creates an account using Google or Facebook and does not set an additional password, it is possible to set their passwords via CSRF.
Since the account is created using a social media account, no existing password check is needed and the CSRF check on the endpoint is broken. 
To reproduce, create an account with Google or Facebook and make account load the attached HTML file. You should now be able to login to the account with password=ATTACKER_PASS.

## Impact

An attacker can take over of accounts created using Google or Facebook.

## Attachments
- khan_password.html
